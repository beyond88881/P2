# import MySQLdb
from django.shortcuts import HttpResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from static.static.py_public.DBmySQLop import OPMysql

# from example.SQLexecute import queryMySQLTableRecord
from static.static.py_public.publicMethod1 import CJsonEncoder


@csrf_exempt
def categoryTreeList(request):
    a = getCategoryTreeList()  # "main_category_tier"
    treeList = a.transferToTreeList()
    # del a
    # easyList = json.dumps(treeList , cls=CJsonEncoder)
    # easyList = [treeList]
    # return treeList
    treeListData = json.dumps(treeList, cls=CJsonEncoder)
    return HttpResponse(treeListData, content_type="application/json; charset=utf-8")


class getCategoryTreeList(object):  # (request, id=0):

    def __init__(self):
        # self.tableName = tableName
        self.resultsRoot = []
        self.results = []
        self.eaList = []
        self.eaTreeList = []
        self.n = 0
        self.total_n = 0  # 总的顺序
        # main_category_tier

    def __del__(self):
        return

    def _getTierInfoResult(self):
        db = OPMysql()  # 打开数据库连接
        sql = "SELECT main_category_tier.ID_main_category_tier,main_category_tier.ID_main_category," \
              "main_category_tier.ID_main_category_sub,main_category_tier.main," \
              "main_category.description " \
              "FROM main_category_tier INNER JOIN main_category ON main_category.ID = " \
              "main_category_tier.ID_main_category_sub " \
              "WHERE main_category_tier.ID_main_category = main_category_tier.ID_main_category_sub ORDER BY " \
              "main_category_tier.ID_main_category ASC "
        # print(db.op_select(sql))
        self.resultsRoot = db.op_select(sql)
        sql = "SELECT main_category_tier.ID_main_category_tier,main_category_tier.ID_main_category," \
              "main_category_tier.ID_main_category_sub,main_category_tier.main," \
              "main_category.description " \
              "FROM main_category_tier INNER JOIN main_category ON main_category.ID = " \
              "main_category_tier.ID_main_category_sub " \
              "WHERE main_category_tier.ID_main_category <> main_category_tier.ID_main_category_sub ORDER BY " \
              "main_category_tier.ID_main_category ASC "
        self.results = db.op_select(sql)
        for rowRoot in self.resultsRoot:
            start_value = rowRoot["ID_main_category_sub"]
            self.n = self.n + 1
            checkInList = self._checkJasonInListBySorting(self.results, "ID_main_category", start_value)
            levelNo = str(self.n)
            rowRoot["levelNo"] = levelNo
            if str(rowRoot["ID_main_category_sub"]) == str(
                    rowRoot["ID_main_category"]) and checkInList is True:  # 如果有再下一级的展开
                rowRoot["myNode"] = True
            else:
                rowRoot["myNode"] = False
            self.eaList.append(rowRoot)
            self._getTierInfo(start_value, levelNo, 0)
        del db
        return self.eaList

    def _getTierInfo(self, sub_value, upperLevelNo, level):
        # json_sub={}
        # results1=_getJasonInListBySorting(results,"main","<>0")
        m = 0
        for row in self.results:
            nextStart_value = row["ID_main_category"]
            if nextStart_value == sub_value:  # 如果行中的
                m = m + 1
                self.total_n = self.total_n + 1
                nextSub_value = str(row["ID_main_category_sub"])
                levelNo = str(upperLevelNo) + "x" + str(m)
                row["levelNo"] = levelNo
                # if nextSub_value in self.results:  # 如果有再下一级的展开
                checkInList = self._checkJasonInListBySorting(self.results, "ID_main_category", nextSub_value)
                if checkInList is True:  # 如果有再下一级的展开
                    # 循环获取
                    row["myNode"] = True
                    self.eaList.append(row)
                    self._getTierInfo(nextSub_value, levelNo, level + 1)
                else:
                    row["myNode"] = False
                    self.eaList.append(row)
                    # return  # eaList

    def transferToTreeList(self):
        # self.__getTierInfoResult()
        tierList = self._getTierInfoResult()
        tierList.reverse()
        treeList = []
        rowX = {}
        childList = []
        for row in tierList:  # 从尾部向上加入到list
            if row["myNode"] is True:
                rowX["id"] = row["ID_main_category_sub"]
                rowX["text"] = row["description"]
                rowX["state"] = "closed"
                rowX["children"] = childList
                treeList.append(rowX)
                rowX = {}
                childList = []
            else:  # 如果不是节点
                rowX["id"] = row["ID_main_category_sub"]
                rowX["text"] = row["description"]
                childList.append(rowX)
                rowX = {}
        print(treeList)
        return treeList
        # self.eaTreeList.append(rowX)

    def _getJasonInListBySorting(self, orgList, fieldName, fieldValue1):
        # fieldValue如果有多个请使用';'隔开
        # fieldName如果有多个请使用';'隔开
        myList = []
        for subJason in orgList:
            fieldNameList = fieldName.split(";")
            valueJoint = ""
            for x in fieldNameList:
                valueJoint = valueJoint + ";" + subJason[x]
                if valueJoint == fieldValue1:
                    myList.append(subJason)
        return myList

    def _checkJasonInListBySorting(self, orgList, fieldName, fieldValue):
        # fieldValue如果有多个请使用';'隔开
        # fieldName如果有多个请使用';'隔开
        myList = []
        myList = orgList
        for subJason in myList:
            fieldNameList = fieldName.split(";")
            valueJoint = ""
            for x in fieldNameList:
                valueJoint = valueJoint + ";" + str(subJason[x])
                fieldValue1 = ";" + str(fieldValue)
            if str(valueJoint) == str(fieldValue1):
                return True
        return False


def queryTableRecord(tableName="", fetchNumber=0):
    db = OPMysql()  # 打开数据库连接
    # db = MySQLdb.connect("localhost", "root", "", "project", charset='utf8')
    if tableName == "":
        return
    if fetchNumber == 0:
        num = 1
    else:
        num = fetchNumber

    sql = "SELECT * FROM " + tableName + " WHERE projectID < %s" % (str(num))
    try:
        # 获取所有记录列表
        results = db.op_select(sql)
        for row in results:
            str1 = ""
            for key in row:
                str1 = str1 + ";" + str(row[key])
            print(str1)  # # 打印结果
        return results
        # print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
        #       (fname, lname, age, sex, income))
    except:
        print("Error: unable to fecth data")
    # 关闭数据库连接
    # db.dispose()
    del db


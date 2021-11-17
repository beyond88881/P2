# 如果数据里面有时间的话，使用json.dumps（）会出错。下面这个函数就是处理这个问题
import datetime
import json


class MyException(Exception):
    pass


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                # return obj.struct_time('%Y-%m-%d %H:%M:%S')
                da = str(obj.strftime('%Y-%m-%d %H:%M:%S'))
                return da
            elif isinstance(obj, datetime.date):
                da = str(obj.strftime('%Y-%m-%d'))
                return da
            else:
                return json.JSONEncoder.default(self, obj)
        # except Exception(e):
        except MyException:
            if str(obj) == "b'\\x01'":
                return True
            elif str(obj) == "b'\\x00'":
                return False
            else:
                return str(obj, "utf-8")
        # except BaseException):
        #     return str(obj)
        except TypeError:
            return str(obj)
        except ZeroDivisionError:
            return str(obj)
        except NameError:
            print("error")
        # except Exception(BaseException) as e:

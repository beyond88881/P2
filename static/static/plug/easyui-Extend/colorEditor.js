// https://www.cnblogs.com/zhaobl/archive/2013/02/20/2919166.html
$.extend($.fn.datagrid.defaults.editors, {
    colorpicker: {//colorpicker就是你要自定义editor的名称
        init: function (container, options) {
            // var input = $('<input class="easyuidatetimebox">').appendTo(container);
            var input = $('<input>').appendTo(container);

            input.ColorPicker({
                color: '#0000ff',
                onShow: function (colpkr) {
                    $(colpkr).fadeIn(500);
                    return false;
                },
                onHide: function (colpkr) {
                    $(colpkr).fadeOut(500);
                    return false;
                },
                onChange: function (hsb, hex, rgb) {
                    //                    $('#colorSelector div').css('backgroundColor', '#' + hex);
                    input.css('backgroundColor', '#' + hex);
                    input.val('#' + hex);
                }
            });
            return input;
        },
        getValue: function (target) {
            return $(target).val();
        },
        setValue: function (target, value) {
            $(target).val(value);
            $(target).css('backgroundColor', value);
            $(target).ColorPickerSetColor(value);
        },
        resize: function (target, width) {
            var input = $(target);
            if ($.boxModel == true) {
                input.width(width - (input.outerWidth() - input.width()));
            } else {
                input.width(width);
            }
        }
    }
});
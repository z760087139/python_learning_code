// jquery 里面，ajax 使用callback 的异步形式执行回调函数
// 想要并行执行ajax时候，可以通过$.when().done().fail()
// $.when 接收 Deffered()对象   $.ajax 返回的也是 Deffered对象，可以直接嵌套在$.when里面

// 比如页面二级联动时候
$(document).ready(function () {
    function inner(){
        // 定义 Deffered()
        var k = $.Deffered()
        // 提取页面信息，准备发送数据
        var num = $('#button').val
        $.when(
            $.ajax(
                {
                    url:'..',
                    data:num,
                    success: functiono(get_data){
                        // execution
                    }
                }
            )
        )
        // ajax完成时候 返回完成状态的deffered
        .done(function(){
            return  k.resolve()
        })
        // 因为when 并不会进行等待，因此需要先返回未完成状态的deffed
        return k
    }
    $.when(inner())
    .done(
        // another execution
    )
});

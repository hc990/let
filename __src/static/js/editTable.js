//需要首先通过Javascript来解决内容部分奇偶行的背景色不同
//$(document).ready(function(){
//	
//});
//简化的ready写法


$(function(){
	//找到表格的内容区域中所有的奇数行
	//使用even是为了把通过tbody tr返回的所有tr元素中，在数组里面下标是偶数的元素返回，因为这些元素，实际上才是我们期望的tbody里面的奇数行
	$("tbody tr:even").css("background-color","#ECE9D8");

	//我们需要找到所有的学号单元格
	var numTd = $("tbody td:2");
	//给这些单元格注册鼠标点击的事件
	numTd.click(function() {	
		//找到当前鼠标点击的td,this对应的就是响应了click的那个td
		var tdObj = $(this);
		if (tdObj.children("input").length > 0) {
			//当前td中input，不执行click处理
			return false;
		}
		var text = tdObj.html(); 
		//清空td中的内容
		tdObj.html("");
		//创建一个文本框
		//去掉文本框的边框
		//设置文本框中的文字字体大小是16px
		//使文本框的宽度和td的宽度相同
		//设置文本框的背景色
		//需要将当前td中的内容放到文本框中
		//将文本框插入到td中
		var inputObj = $("<input type='text'>").css("border-width","0")
			.css("font-size","16px").width(tdObj.width())
			.css("background-color",tdObj.css("background-color"))
			.val(text).appendTo(tdObj);
		//是文本框插入之后就被选中
		inputObj.trigger("focus").trigger("select");
		inputObj.click(function() {
			return false;
		});
		//处理文本框上回车和esc按键的操作
		inputObj.keyup(function(event){
			//获取当前按下键盘的键值
			var keycode = event.which;
			//处理回车的情况
			if (keycode == 13) {
				//获取当当前文本框中的内容
				var inputtext = $(this).val();
				//将td的内容修改成文本框中的内容
				tdObj.html(inputtext);
			}
			//处理esc的情况
			if (keycode == 27) {
				//将td中的内容还原成text
				tdObj.html(text);
			}
		});
	});
});

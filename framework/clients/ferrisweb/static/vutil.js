function hide(el){document.getElementById(el).style.display = 'none'}

function show(el){document.getElementById(el).style.display = 'block'}

function swap(a,b){hide(a);show(b);}

$(document).ready(function(){
     
    $(".switcher li").bind("click",function(){		
		
		var act = $(this);
		
		$(act).parent().children('li').removeClass("active").end();
		$(act).addClass("active");
		
    });
	
});

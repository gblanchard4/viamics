function refresh_analyses(timer)
{

    //finished = call the server, get status:
    resp = $.getJSON(   "api/get_analyses",
                {},
            function(analyses, status, xhr) 
            {
                mesa = document.getElementsByTagName('table')[0];
                //debuglists = mesa.getElementsByTagName('ul');
                //spans = mesa.getElementsByClassName('analysis_id');

		rows = mesa.getElementsByTagName('tr');
		rowMap = {};
		for(i = 0; i<rows.length; i++)//create a map from analysis_id -> tr,
		{//so the script can update analyses in the browser regardless of the
		 //order the server sends them
		    rowMap[rows[i].getElementsByClassName('analysis_id')[0].innerHTML] =
			rows[i];
		}
    
                //alert("shut: " + data[0]);
                //analyses = data;//the result of the HTTP request
                len = analyses.length;//the number of analyses on the server
                if(len == 0) {timer.stop(); return; }
                finished = (analyses[0].state == "done" );
                for (i = 0; i< len; i++)
                {
                    currentLog = analyses[i].log;
                    debuglist = rowMap[analyses[i].id].getElementsByTagName('ul')[0];
                    for (j = 0; j< currentLog.length; j++)
                    {
                        debuglist.children[j].innerHTML = currentLog[j];
                    }
                    if(analyses[i].state == "done")
                    {
                        state = document.getElementById('analysis_state_'+(i+1));
                        state.src = "/static/done.gif";
                        var link = document.createElement('a');
			link.setAttribute('href', './info/'+analyses[i].id);
                        link.innerHTML = "»";
                        var td = debuglist.parentNode.parentNode;
                        var title = td.getElementsByClassName('smallheadindex')[0];
                        if(title.getElementsByTagName('a')[0])
                        {  
                                c = title.getElementsByTagName('a')[0];
                            	title.removeChild(c);
                        }
                        title.appendChild(link);
                    } else finished = false;
                    
        
        
                }
                if (finished) timer.stop();
            }
        );
    
}




/*
 *
 *    jQuery Timer plugin v0.1
 *        Matt Schmidt [http://www.mattptr.net]
 *
 *    Licensed under the BSD License:
 *        http://mattptr.net/license/license.txt
 *
 */
 
 jQuery.timer = function (interval, callback)
 {
 /**
  *
  * timer() provides a cleaner way to handle intervals  
  *
  *    @usage
  * $.timer(interval, callback);
  *
  *
  * @example
  * $.timer(1000, function (timer) {
  *     alert("hello");
  *     timer.stop();
  * });
  * @desc Show an alert box after 1 second and stop
  * 
  * @example
  * var second = false;
  *    $.timer(1000, function (timer) {
  *        if (!second) {
  *            alert('First time!');
  *            second = true;
  *            timer.reset(3000);
  *        }
  *        else {
  *            alert('Second time');
  *            timer.stop();
  *        }
  *    });
  * @desc Show an alert box after 1 second and show another after 3 seconds
  *
  * 
  */

    var interval = interval || 100;

    if (!callback)
        return false;
    
    _timer = function (interval, callback) {
        this.stop = function () {
            clearInterval(self.id);
        };
        
        this.internalCallback = function () {
            callback(self);
        };
        
        this.reset = function (val) {
            if (self.id)
                clearInterval(self.id);
            
            var val = val || 100;
            this.id = setInterval(this.internalCallback, val);
        };
        
        this.interval = interval;
        this.id = setInterval(this.internalCallback, this.interval);
        
        var self = this;
    };
    
    return new _timer(interval, callback);
 };
 
 $.timer(2000, refresh_analyses);

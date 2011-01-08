function refresh_analyses(timer)
{

    //finished = call the server, get status:
    resp = $.getJSON(   "api/get_analyses",
                {},
            function(data, status, xhr) 
            {
                mesa = document.getElementsByTagName('table')[0];
                debuglists = mesa.getElementsByTagName('ul');
                spans = mesa.getElementsByClassName('analysis_id');
    
                //alert("shut: " + data[0]);
                analyses = data;
                len = analyses.length;
                if(len == 0) return;
                finished = (analyses[0].state == "done");
                for (i = 0; i< len; i++)
                {
                    currentLog = analyses[i].log;
                    debuglist = debuglists[i];
                    for (j = 0; j< currentLog.length; j++)
                    {
                        debuglist.children[j].innerHTML = currentLog[j];
                    }
                    if(analyses[i].state == "done")
                    {
                        state = document.getElementById('analysis_state_'+(i+1));
                        state.src = "/static/done.gif";
                        var link = document.createElement('a');
                        link.setAttribute('href', './info/'+analyses[0].id);
                        link.innerHTML = "»";
                        var td = debuglist.parentNode.parentNode;
                        var title = td.getElementsByClassName('smallheadindex')[0];
                        if(title.getElementsByTagName('a')[0])
                        {  
                            //try
                            //{ 
                                c = title.getElementsByTagName('a')[0];
                            	title.removeChild(c);
                            //}
                            //catch (err)
                            //{
                            //	alert(td.innerHTML + err);
                            //	throw err;
                            //}
                        }
                        title.appendChild(link);
                        finished = (finished && true);
                    } else finished = (finished && false);
                    
        
        
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

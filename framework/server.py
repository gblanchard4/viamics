
    

  

<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>framework/server.py at master from meren's viamics - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    <link href="https://assets0.github.com/stylesheets/bundle_common.css?7ebd928ca3f97afefa144c3d65ae70b92f1248df" media="screen" rel="stylesheet" type="text/css" />
<link href="https://assets3.github.com/stylesheets/bundle_github.css?7ebd928ca3f97afefa144c3d65ae70b92f1248df" media="screen" rel="stylesheet" type="text/css" />

    <script type="text/javascript">
      if (typeof console == "undefined" || typeof console.log == "undefined")
        console = { log: function() {} }
    </script>
    <script type="text/javascript" charset="utf-8">
      var GitHub = {}
      var github_user = 'mazubieta'
      
    </script>
    <script src="https://assets1.github.com/javascripts/jquery/jquery-1.4.2.min.js?7ebd928ca3f97afefa144c3d65ae70b92f1248df" type="text/javascript"></script>
    <script src="https://assets2.github.com/javascripts/bundle_common.js?7ebd928ca3f97afefa144c3d65ae70b92f1248df" type="text/javascript"></script>
<script src="https://assets2.github.com/javascripts/bundle_github.js?7ebd928ca3f97afefa144c3d65ae70b92f1248df" type="text/javascript"></script>


        <script type="text/javascript" charset="utf-8">
      GitHub.spy({
        repo: "meren/viamics"
      })
    </script>

    
  
    
  

  <link href="https://github.com/meren/viamics/commits/master.atom" rel="alternate" title="Recent Commits to viamics:master" type="application/atom+xml" />

        <meta name="description" content="Visual and statistical analysis framework for microbial communities, and more" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "meren/viamics";
      GitHub.currentRef = 'master';
      GitHub.commitSHA = "e5f6689d3a19abd624175641544e4ee43c76a5db";
      GitHub.currentPath = 'framework/server.py';
      GitHub.masterBranch = "master";

      
    </script>
  

            <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

          <script type="text/javascript">
      var mpq = [];
      mpq.push(["init", "65fde2abd433eae3b32b38b7ebd2f37e"]);
      (function() {
      var mp = document.createElement("script"); mp.type = "text/javascript"; mp.async = true;
      mp.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + "//api.mixpanel.com/site_media/js/api/mixpanel.js";
      var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(mp, s);
      })();
      </script>

  </head>

  

  <body class="logged_in page-blob">
    

    

    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="true">
        
          <a class="logo boring" href="https://github.com">
            <img src="/images/modules/header/logov3.png?changed" class="default" alt="github" />
            <![if !IE]>
            <img src="/images/modules/header/logov3-hover.png" class="hover" alt="github" />
            <![endif]>
          </a>
        
        
          





  
    <div class="userbox">
      <div class="avatarname">
        <a href="https://github.com/mazubieta"><img src="https://secure.gravatar.com/avatar/5590032593192382075692ffe5d20dce?s=140&d=https://github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20"  /></a>
        <a href="https://github.com/mazubieta" class="name">mazubieta</a>

        
        
          <a href="https://github.com/inbox/notifications" class="unread_count notifications_count new tooltipped downwards js-notification-count" title="Unread Notifications">1</a>
        
      </div>
      <ul class="usernav">
        <li><a href="https://github.com">Dashboard</a></li>
        <li>
          
          <a href="https://github.com/inbox">Inbox</a>
          <a href="https://github.com/inbox" class="unread_count ">0</a>
        </li>
        <li><a href="https://github.com/account">Account Settings</a></li>
                        <li><a href="/logout">Log Out</a></li>
      </ul>
    </div><!-- /.userbox -->
  


        
        <div class="topsearch">
  
    <form action="/search" id="top_search_form" method="get">
      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <input type="search" class="search my_repos_autocompleter" name="q" results="5" placeholder="Search&hellip;" /> <input type="submit" value="Search" class="button" />
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
    </form>
    <ul class="nav">
      <li><a href="/explore">Explore GitHub</a></li>
      <li><a href="https://gist.github.com">Gist</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
  
</div>

      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public   ">

      

      <div class="title-actions-bar">
        <h1>
          <a href="/meren">meren</a> / <strong><a href="https://github.com/meren/viamics">viamics</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        <li class="for-owner" style="display:none"><a href="https://github.com/meren/viamics/admin" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/meren/viamics/toggle_watch" class="minibutton btn-watch " id="watch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'ec8a50cb21afebeada2aeb4b474176ca58045c86'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/meren/viamics/toggle_watch" class="minibutton btn-watch " id="unwatch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'ec8a50cb21afebeada2aeb4b474176ca58045c86'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          
            <li class="for-notforked" style="display:none"><a href="/meren/viamics/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'ec8a50cb21afebeada2aeb4b474176ca58045c86'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
            <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          

          <li id='pull_request_item' class='nspr' style='display:none'><a href="/meren/viamics/pull/new/master" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a></li>
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/meren/viamics/watchers" title="Watchers" class="tooltipped downwards">3</a></li>
          <li class="forks"><a href="/meren/viamics/network" title="Forks" class="tooltipped downwards">1</a></li>
        </ul>
      </li>
    </ul>

      </div>

        
  <ul class="tabs">
    <li><a href="https://github.com/meren/viamics" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="https://github.com/meren/viamics/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/meren/viamics/network" highlight="repo_network">Network</a></li>
    <li><a href="/meren/viamics/pulls" highlight="repo_pulls">Pull Requests (0)</a></li>

    
      <li><a href="/meren/viamics/forkqueue" highlight="repo_fork_queue">Fork Queue</a></li>
    

    
      
      <li><a href="/meren/viamics/issues" highlight="issues">Issues (0)</a></li>
    

                <li><a href="/meren/viamics/wiki" highlight="repo_wiki">Wiki (2)</a></li>
        
    <li><a href="/meren/viamics/graphs" highlight="repo_graphs">Graphs</a></li>

    <li class="contextswitch nochoices">
      <span class="toggle leftwards" >
        <em>Branch:</em>
        <code>master</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      <a href="#" class="dropdown">Switch Branches (2)</a>
      <ul>
        
          
            <li><strong>master &#x2713;</strong></li>
            
          
          
            <li><a href="/meren/viamics/blob/wait-for-dict/framework/server.py" action="show">wait-for-dict</a></li>
          
        
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/meren/viamics/branches" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div class="frame frame-center tree-finder" style="display: none">
      <div class="breadcrumb">
        <b><a href="/meren/viamics">viamics</a></b> /
        <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
      </div>

      
        <div class="octotip">
          <p>
            <a href="/meren/viamics/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
            <strong>Octotip:</strong> You've activated the <em>file finder</em> by pressing <span class="kbd">t</span>
            Start typing to filter the file list. Use <span class="kbd badmono">↑</span> and <span class="kbd badmono">↓</span> to navigate,
            <span class="kbd">enter</span> to view files.
          </p>
        </div>
      

      <table class="tree-browser" cellpadding="0" cellspacing="0">
        <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
        <tr class="js-no-results no-results" style="display: none">
          <th colspan="2">No matching files</th>
        </tr>
        <tbody class="js-results-list">
        </tbody>
      </table>
    </div>

    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

        <a href="/meren/viamics/downloads" class="download-source" id="download_button" title="Download source, tagged packages and binaries."><span class="icon"></span>Downloads</a>

      <div id="repository_desc_wrapper">
      <div id="repository_description" rel="repository_description_edit">
        
          <p>Visual and statistical analysis framework for microbial communities, and more
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>

      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/meren/viamics/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="ec8a50cb21afebeada2aeb4b474176ca58045c86" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="Visual and statistical analysis framework for microbial communities, and more">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://meren.org/framework/" rel="nofollow">http://meren.org/framework/</a></p>
      </div>

      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/meren/viamics/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="ec8a50cb21afebeada2aeb4b474176ca58045c86" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="http://meren.org/framework/">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>
      </div>
      <div class="rule "></div>
            <div id="url_box" class="url-box">
        <ul class="clone-urls">
          
            
              <li id="private_clone_url"><a href="git@github.com:meren/viamics.git" data-permissions="Read+Write">SSH</a></li>
            
            <li id="http_clone_url"><a href="https://mazubieta@github.com/meren/viamics.git" data-permissions="Read+Write">HTTP</a></li>
            <li id="public_clone_url"><a href="git://github.com/meren/viamics.git" data-permissions="Read-Only">Git Read-Only</a></li>
          
          
        </ul>
        <input type="text" spellcheck="false" id="url_field" class="url-field" />
              <span style="display:none" id="url_box_clippy"></span>
      <span id="clippy_tooltip_url_box_clippy" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://assets1.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=url_box_clippy&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://assets1.github.com/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=url_box_clippy&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

        <p id="url_description">This URL has <strong>Read+Write</strong> access</p>
      </div>
    </div>


        

      </div><!-- /.pagehead -->

      





<script type="text/javascript">
  GitHub.downloadRepo = '/meren/viamics/archives/master'
  GitHub.revType = "master"

  GitHub.controllerName = "blob"
  GitHub.actionName     = "show"
  GitHub.currentAction  = "blob#show"

  
    GitHub.hasWriteAccess = true
    GitHub.hasAdminAccess = false
    GitHub.watchingRepo = true
    GitHub.ignoredRepo = false
    GitHub.hasForkOfRepo = ""
    GitHub.hasForked = false
  

  
</script>






<div class="flash-messages"></div>


  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/meren/viamics/commit/e5f6689d3a19abd624175641544e4ee43c76a5db">docstring for server.ProcessRequest.__init__</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img src="https://secure.gravatar.com/avatar/03a46e127aa1bcdf1ae5674e783e06a7?s=140&d=https://github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="30" height="30"  />
        </div>
        <div class="name">Johnny Brown <span>(author)</span></div>
        <div class="date">
          <abbr class="relatize" title="2011-02-08 20:04:19">Tue Feb 08 20:04:19 -0800 2011</abbr>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/meren/viamics/commit/e5f6689d3a19abd624175641544e4ee43c76a5db" hotkey="c">e5f6689d3a19abd62417</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/meren/viamics/tree/e5f6689d3a19abd624175641544e4ee43c76a5db" hotkey="t">90535c18e0db7fd714f6</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/meren/viamics/tree/a130e8da153c654768e25febbff84eca0fc0f947" hotkey="p">a130e8da153c654768e2</a>
      

    </div>
  </div>

    </div>
  </div>



  <div id="slider">

  

    <div class="breadcrumb" data-path="framework/server.py/">
      <b><a href="/meren/viamics/tree/e5f6689d3a19abd624175641544e4ee43c76a5db">viamics</a></b> / <a href="/meren/viamics/tree/e5f6689d3a19abd624175641544e4ee43c76a5db/framework">framework</a> / server.py       <span style="display:none" id="clippy_4289">framework/server.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://assets1.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_4289&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://assets1.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_4289&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="framework/server.py/">
        
          <ul class="big-actions">
            
            <li><a class="file-edit-link minibutton" href="/meren/viamics/file-edit/__current_ref__/framework/server.py"><span>Edit this file</span></a></li>
          </ul>
        

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://assets2.github.com/images/icons/txt.png?7ebd928ca3f97afefa144c3d65ae70b92f1248df" width="16" /></span>
                <span class="mode" title="File Mode">100644</span>
                
                  <span>823 lines (621 sloc)</span>
                
                <span>35.477 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/meren/viamics/raw/master/framework/server.py" id="raw-url">raw</a></li>
                
                  <li><a href="/meren/viamics/blame/master/framework/server.py">blame</a></li>
                
                <li><a href="/meren/viamics/commits/master/framework/server.py">history</a></li>
              </ul>
            </div>
            
  <div class="data type-python">
    
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>
<span id="L625" rel="#L625">625</span>
<span id="L626" rel="#L626">626</span>
<span id="L627" rel="#L627">627</span>
<span id="L628" rel="#L628">628</span>
<span id="L629" rel="#L629">629</span>
<span id="L630" rel="#L630">630</span>
<span id="L631" rel="#L631">631</span>
<span id="L632" rel="#L632">632</span>
<span id="L633" rel="#L633">633</span>
<span id="L634" rel="#L634">634</span>
<span id="L635" rel="#L635">635</span>
<span id="L636" rel="#L636">636</span>
<span id="L637" rel="#L637">637</span>
<span id="L638" rel="#L638">638</span>
<span id="L639" rel="#L639">639</span>
<span id="L640" rel="#L640">640</span>
<span id="L641" rel="#L641">641</span>
<span id="L642" rel="#L642">642</span>
<span id="L643" rel="#L643">643</span>
<span id="L644" rel="#L644">644</span>
<span id="L645" rel="#L645">645</span>
<span id="L646" rel="#L646">646</span>
<span id="L647" rel="#L647">647</span>
<span id="L648" rel="#L648">648</span>
<span id="L649" rel="#L649">649</span>
<span id="L650" rel="#L650">650</span>
<span id="L651" rel="#L651">651</span>
<span id="L652" rel="#L652">652</span>
<span id="L653" rel="#L653">653</span>
<span id="L654" rel="#L654">654</span>
<span id="L655" rel="#L655">655</span>
<span id="L656" rel="#L656">656</span>
<span id="L657" rel="#L657">657</span>
<span id="L658" rel="#L658">658</span>
<span id="L659" rel="#L659">659</span>
<span id="L660" rel="#L660">660</span>
<span id="L661" rel="#L661">661</span>
<span id="L662" rel="#L662">662</span>
<span id="L663" rel="#L663">663</span>
<span id="L664" rel="#L664">664</span>
<span id="L665" rel="#L665">665</span>
<span id="L666" rel="#L666">666</span>
<span id="L667" rel="#L667">667</span>
<span id="L668" rel="#L668">668</span>
<span id="L669" rel="#L669">669</span>
<span id="L670" rel="#L670">670</span>
<span id="L671" rel="#L671">671</span>
<span id="L672" rel="#L672">672</span>
<span id="L673" rel="#L673">673</span>
<span id="L674" rel="#L674">674</span>
<span id="L675" rel="#L675">675</span>
<span id="L676" rel="#L676">676</span>
<span id="L677" rel="#L677">677</span>
<span id="L678" rel="#L678">678</span>
<span id="L679" rel="#L679">679</span>
<span id="L680" rel="#L680">680</span>
<span id="L681" rel="#L681">681</span>
<span id="L682" rel="#L682">682</span>
<span id="L683" rel="#L683">683</span>
<span id="L684" rel="#L684">684</span>
<span id="L685" rel="#L685">685</span>
<span id="L686" rel="#L686">686</span>
<span id="L687" rel="#L687">687</span>
<span id="L688" rel="#L688">688</span>
<span id="L689" rel="#L689">689</span>
<span id="L690" rel="#L690">690</span>
<span id="L691" rel="#L691">691</span>
<span id="L692" rel="#L692">692</span>
<span id="L693" rel="#L693">693</span>
<span id="L694" rel="#L694">694</span>
<span id="L695" rel="#L695">695</span>
<span id="L696" rel="#L696">696</span>
<span id="L697" rel="#L697">697</span>
<span id="L698" rel="#L698">698</span>
<span id="L699" rel="#L699">699</span>
<span id="L700" rel="#L700">700</span>
<span id="L701" rel="#L701">701</span>
<span id="L702" rel="#L702">702</span>
<span id="L703" rel="#L703">703</span>
<span id="L704" rel="#L704">704</span>
<span id="L705" rel="#L705">705</span>
<span id="L706" rel="#L706">706</span>
<span id="L707" rel="#L707">707</span>
<span id="L708" rel="#L708">708</span>
<span id="L709" rel="#L709">709</span>
<span id="L710" rel="#L710">710</span>
<span id="L711" rel="#L711">711</span>
<span id="L712" rel="#L712">712</span>
<span id="L713" rel="#L713">713</span>
<span id="L714" rel="#L714">714</span>
<span id="L715" rel="#L715">715</span>
<span id="L716" rel="#L716">716</span>
<span id="L717" rel="#L717">717</span>
<span id="L718" rel="#L718">718</span>
<span id="L719" rel="#L719">719</span>
<span id="L720" rel="#L720">720</span>
<span id="L721" rel="#L721">721</span>
<span id="L722" rel="#L722">722</span>
<span id="L723" rel="#L723">723</span>
<span id="L724" rel="#L724">724</span>
<span id="L725" rel="#L725">725</span>
<span id="L726" rel="#L726">726</span>
<span id="L727" rel="#L727">727</span>
<span id="L728" rel="#L728">728</span>
<span id="L729" rel="#L729">729</span>
<span id="L730" rel="#L730">730</span>
<span id="L731" rel="#L731">731</span>
<span id="L732" rel="#L732">732</span>
<span id="L733" rel="#L733">733</span>
<span id="L734" rel="#L734">734</span>
<span id="L735" rel="#L735">735</span>
<span id="L736" rel="#L736">736</span>
<span id="L737" rel="#L737">737</span>
<span id="L738" rel="#L738">738</span>
<span id="L739" rel="#L739">739</span>
<span id="L740" rel="#L740">740</span>
<span id="L741" rel="#L741">741</span>
<span id="L742" rel="#L742">742</span>
<span id="L743" rel="#L743">743</span>
<span id="L744" rel="#L744">744</span>
<span id="L745" rel="#L745">745</span>
<span id="L746" rel="#L746">746</span>
<span id="L747" rel="#L747">747</span>
<span id="L748" rel="#L748">748</span>
<span id="L749" rel="#L749">749</span>
<span id="L750" rel="#L750">750</span>
<span id="L751" rel="#L751">751</span>
<span id="L752" rel="#L752">752</span>
<span id="L753" rel="#L753">753</span>
<span id="L754" rel="#L754">754</span>
<span id="L755" rel="#L755">755</span>
<span id="L756" rel="#L756">756</span>
<span id="L757" rel="#L757">757</span>
<span id="L758" rel="#L758">758</span>
<span id="L759" rel="#L759">759</span>
<span id="L760" rel="#L760">760</span>
<span id="L761" rel="#L761">761</span>
<span id="L762" rel="#L762">762</span>
<span id="L763" rel="#L763">763</span>
<span id="L764" rel="#L764">764</span>
<span id="L765" rel="#L765">765</span>
<span id="L766" rel="#L766">766</span>
<span id="L767" rel="#L767">767</span>
<span id="L768" rel="#L768">768</span>
<span id="L769" rel="#L769">769</span>
<span id="L770" rel="#L770">770</span>
<span id="L771" rel="#L771">771</span>
<span id="L772" rel="#L772">772</span>
<span id="L773" rel="#L773">773</span>
<span id="L774" rel="#L774">774</span>
<span id="L775" rel="#L775">775</span>
<span id="L776" rel="#L776">776</span>
<span id="L777" rel="#L777">777</span>
<span id="L778" rel="#L778">778</span>
<span id="L779" rel="#L779">779</span>
<span id="L780" rel="#L780">780</span>
<span id="L781" rel="#L781">781</span>
<span id="L782" rel="#L782">782</span>
<span id="L783" rel="#L783">783</span>
<span id="L784" rel="#L784">784</span>
<span id="L785" rel="#L785">785</span>
<span id="L786" rel="#L786">786</span>
<span id="L787" rel="#L787">787</span>
<span id="L788" rel="#L788">788</span>
<span id="L789" rel="#L789">789</span>
<span id="L790" rel="#L790">790</span>
<span id="L791" rel="#L791">791</span>
<span id="L792" rel="#L792">792</span>
<span id="L793" rel="#L793">793</span>
<span id="L794" rel="#L794">794</span>
<span id="L795" rel="#L795">795</span>
<span id="L796" rel="#L796">796</span>
<span id="L797" rel="#L797">797</span>
<span id="L798" rel="#L798">798</span>
<span id="L799" rel="#L799">799</span>
<span id="L800" rel="#L800">800</span>
<span id="L801" rel="#L801">801</span>
<span id="L802" rel="#L802">802</span>
<span id="L803" rel="#L803">803</span>
<span id="L804" rel="#L804">804</span>
<span id="L805" rel="#L805">805</span>
<span id="L806" rel="#L806">806</span>
<span id="L807" rel="#L807">807</span>
<span id="L808" rel="#L808">808</span>
<span id="L809" rel="#L809">809</span>
<span id="L810" rel="#L810">810</span>
<span id="L811" rel="#L811">811</span>
<span id="L812" rel="#L812">812</span>
<span id="L813" rel="#L813">813</span>
<span id="L814" rel="#L814">814</span>
<span id="L815" rel="#L815">815</span>
<span id="L816" rel="#L816">816</span>
<span id="L817" rel="#L817">817</span>
<span id="L818" rel="#L818">818</span>
<span id="L819" rel="#L819">819</span>
<span id="L820" rel="#L820">820</span>
<span id="L821" rel="#L821">821</span>
<span id="L822" rel="#L822">822</span>
<span id="L823" rel="#L823">823</span>
</pre>
          </td>
          <td width="100%">
            
              
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><span class="c"># -*- coding: utf-8 -*-</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="c"># Copyright (C) 2010 - 2011, University of New Orleans</span></div><div class='line' id='LC5'><span class="c">#</span></div><div class='line' id='LC6'><span class="c"># This program is free software; you can redistribute it and/or modify it under</span></div><div class='line' id='LC7'><span class="c"># the terms of the GNU General Public License as published by the Free</span></div><div class='line' id='LC8'><span class="c"># Software Foundation; either version 2 of the License, or (at your option)</span></div><div class='line' id='LC9'><span class="c"># any later version.</span></div><div class='line' id='LC10'><span class="c">#</span></div><div class='line' id='LC11'><span class="c"># Please read the COPYING file.</span></div><div class='line' id='LC12'><span class="c">#</span></div><div class='line' id='LC13'><span class="c"># --</span></div><div class='line' id='LC14'><span class="c">#</span></div><div class='line' id='LC15'><span class="c"># Server core. This program runs the server and starts listening the domain</span></div><div class='line' id='LC16'><span class="c"># socket for requests. Handles and respondes to incoming requests.</span></div><div class='line' id='LC17'><span class="c">#</span></div><div class='line' id='LC18'><span class="c"># executers dictionary in ProcessRequest class contains the available</span></div><div class='line' id='LC19'><span class="c"># requests.</span></div><div class='line' id='LC20'><span class="c">#</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="c"># standard python modules</span></div><div class='line' id='LC23'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC24'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC25'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC26'><span class="kn">import</span> <span class="nn">copy</span></div><div class='line' id='LC27'><span class="kn">import</span> <span class="nn">zlib</span></div><div class='line' id='LC28'><span class="kn">import</span> <span class="nn">shutil</span></div><div class='line' id='LC29'><span class="kn">import</span> <span class="nn">socket</span></div><div class='line' id='LC30'><span class="kn">import</span> <span class="nn">base64</span></div><div class='line' id='LC31'><span class="kn">import</span> <span class="nn">cPickle</span></div><div class='line' id='LC32'><span class="kn">import</span> <span class="nn">threading</span></div><div class='line' id='LC33'><span class="kn">import</span> <span class="nn">traceback</span></div><div class='line' id='LC34'><span class="kn">import</span> <span class="nn">matplotlib.cm</span> <span class="kn">as</span> <span class="nn">cm</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'><span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&quot;../&quot;</span><span class="p">)</span></div><div class='line' id='LC37'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">framework.constants</span> <span class="kn">as</span> <span class="nn">c</span></div><div class='line' id='LC39'><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Please create and edit a constants.py from the template file provided&quot;</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'><span class="kn">import</span> <span class="nn">framework.sanity_check</span></div><div class='line' id='LC44'><span class="n">framework</span><span class="o">.</span><span class="n">sanity_check</span><span class="o">.</span><span class="n">all</span><span class="p">()</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><span class="kn">from</span> <span class="nn">framework.modules.modules</span> <span class="kn">import</span> <span class="n">server_modules_dict</span></div><div class='line' id='LC48'><span class="kn">from</span> <span class="nn">framework</span> <span class="kn">import</span> <span class="n">helper_functions</span></div><div class='line' id='LC49'><span class="kn">from</span> <span class="nn">framework.helper_functions</span> <span class="kn">import</span> <span class="n">HeatmapOptions</span><span class="p">,</span> <span class="n">SerializeToFile</span><span class="p">,</span> <span class="n">DeserializeFromFile</span><span class="p">,</span> <span class="n">GetCopy</span><span class="p">,</span> <span class="n">RelativePath</span></div><div class='line' id='LC50'><span class="kn">from</span> <span class="nn">framework.tools.logger</span> <span class="kn">import</span> <span class="n">debug</span></div><div class='line' id='LC51'><br/></div><div class='line' id='LC52'><span class="kn">import</span> <span class="nn">framework.tools.rdp</span></div><div class='line' id='LC53'><span class="kn">import</span> <span class="nn">framework.tools.env</span></div><div class='line' id='LC54'><span class="kn">import</span> <span class="nn">framework.tools.qpcr</span></div><div class='line' id='LC55'><span class="kn">import</span> <span class="nn">framework.tools.heatmap</span></div><div class='line' id='LC56'><span class="kn">import</span> <span class="nn">framework.tools.bar</span></div><div class='line' id='LC57'><span class="kn">import</span> <span class="nn">framework.tools.piechart</span></div><div class='line' id='LC58'><span class="kn">import</span> <span class="nn">framework.tools.diversityindex</span></div><div class='line' id='LC59'><span class="kn">import</span> <span class="nn">framework.tools.rarefaction</span></div><div class='line' id='LC60'><span class="kn">import</span> <span class="nn">framework.tools.taxons</span></div><div class='line' id='LC61'><span class="kn">import</span> <span class="nn">framework.tools.hcluster</span></div><div class='line' id='LC62'><br/></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'><span class="k">def</span> <span class="nf">formatExceptionInfo</span><span class="p">(</span><span class="n">maxTBlevel</span><span class="o">=</span><span class="mi">5</span><span class="p">):</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cla</span><span class="p">,</span> <span class="n">exc</span><span class="p">,</span> <span class="n">trbk</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">excName</span> <span class="o">=</span> <span class="n">cla</span><span class="o">.</span><span class="n">__name__</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">excArgs</span> <span class="o">=</span> <span class="n">exc</span><span class="o">.</span><span class="n">__dict__</span><span class="p">[</span><span class="s">&quot;args&quot;</span><span class="p">]</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">excArgs</span> <span class="o">=</span> <span class="s">&quot;&lt;no args&gt;&quot;</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">excTb</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">format_tb</span><span class="p">(</span><span class="n">trbk</span><span class="p">,</span> <span class="n">maxTBlevel</span><span class="p">)</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">text</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">text</span> <span class="o">+=</span> <span class="n">excName</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">text</span> <span class="o">+=</span> <span class="n">excArgs</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">excTb</span><span class="p">:</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">text</span> <span class="o">+=</span> <span class="n">line</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">text</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'><br/></div><div class='line' id='LC80'><span class="k">class</span> <span class="nc">ServerState</span><span class="p">:</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">running_analyses</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">done_analyses</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">dir</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">analyses_dir</span><span class="p">):</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">dir</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">):</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">done_analyses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">dir</span><span class="p">)</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'><span class="k">class</span> <span class="nc">Server</span><span class="p">:</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">socket_name</span><span class="p">):</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serversocket</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_UNIX</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">)</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serversocket</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">socket_name</span><span class="p">)</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serversocket</span><span class="o">.</span><span class="n">listen</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serverstate</span> <span class="o">=</span> <span class="n">ServerState</span><span class="p">()</span></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">* Server is up and running :)</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC99'><br/></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">last_thread</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">clientsocket</span><span class="p">,</span> <span class="n">address</span><span class="p">)</span> <span class="o">=</span> <span class="n">serversocket</span><span class="o">.</span><span class="n">accept</span><span class="p">()</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;interrupted.. closing socket&quot;</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serversocket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">socket_name</span><span class="p">)</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">threadid</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">())</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">thread</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">ProcessRequest</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="n">clientsocket</span><span class="p">,</span> <span class="n">serverstate</span><span class="p">,</span> <span class="n">threadid</span><span class="p">))</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">thread</span><span class="o">.</span><span class="n">setName</span><span class="p">(</span><span class="n">threadid</span><span class="p">)</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'><span class="k">class</span> <span class="nc">ProcessRequest</span><span class="p">:</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC120'><span class="sd">    takes a request through a UNIX domain socket `clientsocket`, and writes the </span></div><div class='line' id='LC121'><span class="sd">server response to the socket. The socket should provide a python dict, </span></div><div class='line' id='LC122'><span class="sd">for example the one passed into helper_functions.server. one of the functions </span></div><div class='line' id='LC123'><span class="sd">in `executors` will be called based on `dict[&quot;request&quot;]`</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">clientsocket</span><span class="p">,</span> <span class="n">serverstate</span><span class="p">,</span> <span class="n">threadid</span><span class="p">):</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC130'><span class="sd">        reads one line of text from the clientsocket, passes the text through</span></div><div class='line' id='LC131'><span class="sd">        cPickle, then calls one of the functions in executors.</span></div><div class='line' id='LC132'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">threadid</span> <span class="o">=</span> <span class="n">threadid</span><span class="c">#never used?</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">clientsocket</span> <span class="o">=</span> <span class="n">clientsocket</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">socket_is_alive</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span> <span class="o">=</span> <span class="n">serverstate</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">encode_response</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">base64</span><span class="o">.</span><span class="n">encodestring</span><span class="p">(</span><span class="n">zlib</span><span class="o">.</span><span class="n">compress</span><span class="p">(</span><span class="n">cPickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">x</span><span class="p">),</span> <span class="mi">9</span><span class="p">))</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">decode_request</span>  <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">zlib</span><span class="o">.</span><span class="n">decompress</span><span class="p">(</span><span class="n">base64</span><span class="o">.</span><span class="n">decodestring</span><span class="p">(</span><span class="n">x</span><span class="p">)))</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_socket</span><span class="p">()</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;</span><span class="se">\n\n</span><span class="s">* Incoming Data: &quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">executers</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;exec_analysis&#39;</span>                <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">exec_analysis</span><span class="p">,</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;remove_analysis&#39;</span>              <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_analysis</span><span class="p">,</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;status&#39;</span>                       <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">status_request</span><span class="p">,</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_analyses&#39;</span>                 <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_analyses</span><span class="p">,</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_analysis_name&#39;</span>            <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_analysis_name</span><span class="p">,</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_type_of_analysis&#39;</span>         <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_type_of_analysis</span><span class="p">,</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_analysis_ranks&#39;</span>           <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_analysis_ranks</span><span class="p">,</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_sample_map_name&#39;</span>          <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_sample_map_name</span><span class="p">,</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_sample_maps&#39;</span>              <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_sample_maps</span><span class="p">,</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_sample_map_instances&#39;</span>     <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_sample_map_instances</span><span class="p">,</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_samples_dict_path&#39;</span>        <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_samples_dict_path</span><span class="p">,</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_relative_taxon_charts_dir&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_relative_taxon_charts_dir</span><span class="p">,</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_relative_type_specific_data_dir&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_relative_type_specific_data_dir</span><span class="p">,</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_otu_confidence_tuples&#39;</span>    <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_otu_confidence_tuples</span><span class="p">,</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_otu_t_p_tuples&#39;</span>           <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_otu_t_p_tuples</span><span class="p">,</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;get_samples_in_an_analysis&#39;</span>   <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_samples_in_an_analysis</span><span class="p">,</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;append_samples_to_analysis&#39;</span>   <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_samples_to_analysis</span><span class="p">,</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;info&#39;</span>                         <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_analysis_info</span><span class="p">,</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;refresh_analysis_files&#39;</span>       <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">refresh_analysis_files</span><span class="p">,</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;heatmap_options&#39;</span>              <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">heatmap_options</span><span class="p">,</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;refresh_heatmap&#39;</span>              <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">refresh_heatmap</span><span class="p">,</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;refresh_sample_map&#39;</span>           <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_or_refresh_sample_map</span><span class="p">,</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;new_sample_map&#39;</span>               <span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">generate_or_refresh_sample_map</span><span class="p">}</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">executers</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;request&#39;</span><span class="p">]):</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="s">&#39;content&#39;</span><span class="p">:</span> <span class="s">&#39;unknown request&#39;</span><span class="p">})</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;time_stamp&#39;</span><span class="p">):</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># time_stamp should be generated by &quot;time&quot; function in time module.</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="s">&#39;content&#39;</span><span class="p">:</span> <span class="s">&#39;request dict has to have a &quot;time_stamp&quot; variable&#39;</span><span class="p">})</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">request_handler</span> <span class="o">=</span> <span class="n">executers</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;request&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">__name__</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time_stamp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;time_stamp&#39;</span><span class="p">]</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;* Calling request handler: &quot;</span><span class="p">,</span> <span class="n">request_handler</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">executers</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;request&#39;</span><span class="p">])()</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">error_log</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">error_logs_dir</span><span class="p">,</span> <span class="n">time_stamp</span><span class="o">.</span><span class="n">__str__</span><span class="p">())</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">traceback</span><span class="o">.</span><span class="n">print_exc</span><span class="p">(</span><span class="nb">file</span><span class="o">=</span><span class="nb">open</span><span class="p">(</span><span class="n">error_log</span><span class="p">,</span> <span class="s">&quot;w&quot;</span><span class="p">))</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_is_alive</span><span class="p">:</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">exception_info</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">error_log</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="s">&#39;time_stamp&#39;</span><span class="p">:</span> <span class="n">time_stamp</span><span class="o">.</span><span class="n">__str__</span><span class="p">(),</span> <span class="s">&#39;exception&#39;</span><span class="p">:</span> <span class="n">exception_info</span><span class="p">})</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">write_socket</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">response_dict</span><span class="p">):</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">r</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">encode_response</span><span class="p">(</span><span class="n">response_dict</span><span class="p">)</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;* Outgoing Data (</span><span class="si">%d</span><span class="s"> bytes): &quot;</span> <span class="o">%</span> <span class="nb">len</span><span class="p">(</span><span class="n">r</span><span class="p">),</span> <span class="n">response_dict</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">total_sent</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">clientsocket</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">r</span><span class="p">)</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">socket_is_alive</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">total_sent</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'><br/></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">read_socket</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC199'><span class="sd">        loops over self.clientsocket in 512-byte chunks until a chunk ends with \n.</span></div><div class='line' id='LC200'><span class="sd">returns self.decode_request of the data recieved.</span></div><div class='line' id='LC201'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="bp">True</span><span class="p">:</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">clientsocket</span><span class="o">.</span><span class="n">recv</span><span class="p">(</span><span class="mi">512</span><span class="p">)</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">+=</span> <span class="n">chunk</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">chunk</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">:</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">decode_request</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">remove_analysis</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span>             <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">analysis_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="p">:</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">analysis_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="p">:</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">)</span></div><div class='line' id='LC221'><br/></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'><br/></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">exec_analysis</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span>             <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;data_file_sha1sum&#39;</span><span class="p">]</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data_file_temp_path</span>     <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;data_file_path&#39;</span><span class="p">]</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">job_description</span>         <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;job_description&#39;</span><span class="p">]</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_type</span>           <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_type&#39;</span><span class="p">]</span></div><div class='line' id='LC230'><br/></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">late_response_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;return_when_done&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;return_when_done&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="bp">True</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">analysis_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">server_modules_dict</span><span class="p">:</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="s">&#39;content&#39;</span><span class="p">:</span> <span class="s">&#39;Wrong type of analysis.&#39;</span><span class="p">})</span></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Server state is being updated, running processes.APPEND(this)&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Copying data file&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">data_file_temp_path</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">data_file_name</span><span class="p">))</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Filling job description: &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="n">job_description</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">job_description</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC246'><br/></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">late_response_request</span> <span class="ow">is</span> <span class="bp">False</span><span class="p">:</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Response is being sent&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;process_id&#39;</span><span class="p">:</span> <span class="n">analysis_id</span><span class="p">})</span></div><div class='line' id='LC250'><br/></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">################################################################</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># call sever modules..</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">################################################################</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># analysis specific stuff.</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">server_modules_dict</span><span class="p">[</span><span class="n">analysis_type</span><span class="p">]</span><span class="o">.</span><span class="n">_exec</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># common analysis routines..</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">server_modules_dict</span><span class="p">[</span><span class="s">&#39;commons&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">_exec</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">################################################################</span></div><div class='line' id='LC260'><br/></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># update server state so the info page is browsable.</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Server state is being updated, running analyses.REMOVE(this), done analyses.APPEND(this)&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Info page is ready for this study.&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC266'><br/></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">late_response_request</span> <span class="ow">is</span> <span class="bp">True</span><span class="p">:</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Response is being sent&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;process_id&#39;</span><span class="p">:</span> <span class="n">analysis_id</span><span class="p">})</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_samples_dict_path</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC273'><br/></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC275'><br/></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;samples_dict_path&#39;</span><span class="p">:</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">samples_serialized_file_path</span><span class="p">})</span></div><div class='line' id='LC277'><br/></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">refresh_heatmap</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span>    <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">]</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span>     <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;options&#39;</span><span class="p">]</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rank</span>        <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;rank&#39;</span><span class="p">]</span></div><div class='line' id='LC283'><br/></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC285'><br/></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC287'><br/></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="o">.</span><span class="n">abundance_file</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="nb">vars</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">)[</span><span class="n">c</span><span class="o">.</span><span class="n">percent_abundance_file_prefix</span> <span class="o">+</span> <span class="n">rank</span> <span class="o">+</span> <span class="s">&#39;_file_path&#39;</span><span class="p">])</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="o">.</span><span class="n">output_file</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="nb">vars</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">)[</span><span class="n">c</span><span class="o">.</span><span class="n">abundance_heatmap_file_prefix</span> <span class="o">+</span> <span class="n">rank</span> <span class="o">+</span> <span class="s">&#39;_file_path&#39;</span><span class="p">])</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">SerializeToFile</span><span class="p">(</span><span class="n">options</span><span class="p">,</span> <span class="nb">vars</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">)[</span><span class="n">c</span><span class="o">.</span><span class="n">heatmap_options_file_prefix</span> <span class="o">+</span> <span class="n">rank</span> <span class="o">+</span> <span class="s">&#39;_file_path&#39;</span><span class="p">])</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">framework</span><span class="o">.</span><span class="n">tools</span><span class="o">.</span><span class="n">heatmap</span><span class="o">.</span><span class="n">main</span><span class="p">(</span><span class="n">options</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">analyses_dir</span><span class="p">)</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="s">&#39;content&#39;</span><span class="p">:</span> <span class="n">formatExceptionInfo</span><span class="p">()})</span></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC296'><br/></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;options&#39;</span><span class="p">:</span> <span class="n">options</span><span class="p">})</span></div><div class='line' id='LC298'><br/></div><div class='line' id='LC299'><br/></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">heatmap_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span>    <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">]</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rank</span>        <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;rank&#39;</span><span class="p">]</span></div><div class='line' id='LC304'><br/></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC308'><br/></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;options&#39;</span><span class="p">:</span> <span class="n">DeserializeFromFile</span><span class="p">(</span><span class="nb">vars</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">)[</span><span class="n">c</span><span class="o">.</span><span class="n">heatmap_options_file_prefix</span> <span class="o">+</span> <span class="n">rank</span> <span class="o">+</span> <span class="s">&#39;_file_path&#39;</span><span class="p">])})</span></div><div class='line' id='LC310'><br/></div><div class='line' id='LC311'><br/></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">generate_or_refresh_sample_map</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC314'><br/></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># update server state</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Server state is being updated, running analyses.APPEND(this)&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC321'><br/></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># read the original sampels dict and otu library</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">samples_dict</span> <span class="o">=</span> <span class="n">DeserializeFromFile</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">samples_serialized_file_path</span><span class="p">)</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">otu_library</span>  <span class="o">=</span> <span class="n">DeserializeFromFile</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">otu_library_file_path</span><span class="p">)</span></div><div class='line' id='LC325'><br/></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># if request dict has &#39;instance&#39;, sample map exists and needs to be refreshed</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;instance&#39;</span><span class="p">):</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">]</span></div><div class='line' id='LC329'><br/></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># if late response wasn&#39;t requested send response immediately</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;return_when_done&#39;</span><span class="p">):</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC333'><br/></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC335'><br/></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filtered_samples_dict</span> <span class="o">=</span> <span class="n">DeserializeFromFile</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_filtered_samples_dict_file_path</span><span class="p">)</span></div><div class='line' id='LC337'><br/></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># else, this is a new sample map request.</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;sample_map_dict&#39;</span><span class="p">][</span><span class="s">&#39;sample_map_name&#39;</span><span class="p">]</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;sample_map_dict&#39;</span><span class="p">][</span><span class="s">&#39;sample_map_list&#39;</span><span class="p">]</span></div><div class='line' id='LC342'><br/></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC344'><br/></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># get a new instance id for the analysis and create sample map directories</span></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Creating new sample map directory for &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="n">sample_map_name</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">create_new_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">)</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Current sample map directory is &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC349'><br/></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># store sample map name</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_name_file_path</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">sample_map_name</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Sample map name has been stored&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC353'><br/></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># store sample map</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_file_path</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">sample</span> <span class="ow">in</span> <span class="n">sample_map_list</span><span class="p">:</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%(sample)s</span><span class="se">\t</span><span class="si">%(group)s</span><span class="se">\t</span><span class="si">%(color)s</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">sample</span><span class="p">)</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Sample map has been stored&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC360'><br/></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># get filtered samples dict and store it for sample map</span></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Filtered samples dict are being generated and stored&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filtered_samples_dict</span> <span class="o">=</span> <span class="n">framework</span><span class="o">.</span><span class="n">helper_functions</span><span class="o">.</span><span class="n">filter_dict</span><span class="p">(</span><span class="n">samples_dict</span><span class="p">,</span> <span class="n">keep_only</span> <span class="o">=</span> <span class="p">[</span><span class="n">s</span><span class="p">[</span><span class="s">&#39;sample&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">sample_map_list</span><span class="p">])</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">SerializeToFile</span><span class="p">(</span><span class="n">filtered_samples_dict</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_filtered_samples_dict_file_path</span><span class="p">)</span></div><div class='line' id='LC365'><br/></div><div class='line' id='LC366'><br/></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_functions_common_dict</span> <span class="o">=</span> <span class="n">server_modules_dict</span><span class="p">[</span><span class="s">&#39;commons&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">_sample_map_functions</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">common_function_ids</span> <span class="o">=</span> <span class="n">sample_map_functions_common_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></div><div class='line' id='LC369'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">common_function_ids</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">common_function_ids</span><span class="p">:</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_functions_common_dict</span><span class="p">[</span><span class="nb">id</span><span class="p">][</span><span class="s">&#39;func&#39;</span><span class="p">](</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC372'><br/></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_functions_module_dict</span> <span class="o">=</span> <span class="n">server_modules_dict</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">]</span><span class="o">.</span><span class="n">_sample_map_functions</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">module_function_ids</span> <span class="o">=</span> <span class="n">sample_map_functions_module_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">module_function_ids</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">module_function_ids</span><span class="p">:</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_functions_module_dict</span><span class="p">[</span><span class="nb">id</span><span class="p">][</span><span class="s">&#39;func&#39;</span><span class="p">](</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC378'><br/></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># update server state</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Server state is being updated, running analyses.REMOVE(this), done analyses.APPEND(this)&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC384'><br/></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;All files for sample map has been generated&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC386'><br/></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># if late response was requested, send it now</span></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;return_when_done&#39;</span><span class="p">):</span></div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC390'><br/></div><div class='line' id='LC391'><br/></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_analyses</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analyses</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;returns analyses that are running on the server or were finished&quot;&quot;&quot;</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">analysis_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="p">:</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analyses</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s">&#39;id&#39;</span><span class="p">:</span> <span class="n">analysis_id</span><span class="p">,</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="n">name</span><span class="p">,</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;type&#39;</span><span class="p">:</span> <span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">,</span></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;state&#39;</span><span class="p">:</span> <span class="s">&#39;running&#39;</span><span class="p">,</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;log&#39;</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span><span class="o">.</span><span class="n">readlines</span><span class="p">()[</span><span class="o">-</span><span class="mi">5</span><span class="p">:]})</span></div><div class='line' id='LC403'><br/></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">analysis_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="p">:</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analyses</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s">&#39;id&#39;</span><span class="p">:</span> <span class="n">analysis_id</span><span class="p">,</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="n">name</span><span class="p">,</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;type&#39;</span><span class="p">:</span> <span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">,</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;state&#39;</span><span class="p">:</span> <span class="s">&#39;done&#39;</span><span class="p">,</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;log&#39;</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span><span class="o">.</span><span class="n">readlines</span><span class="p">()[</span><span class="o">-</span><span class="mi">5</span><span class="p">:]})</span></div><div class='line' id='LC412'><br/></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;analyses&#39;</span><span class="p">:</span> <span class="n">analyses</span><span class="p">})</span></div><div class='line' id='LC414'><br/></div><div class='line' id='LC415'><br/></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_sample_map_name</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">]</span></div><div class='line' id='LC419'><br/></div><div class='line' id='LC420'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC421'><br/></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC423'><br/></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_name_file_path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()})</span></div><div class='line' id='LC425'><br/></div><div class='line' id='LC426'><br/></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_analysis_ranks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC429'><br/></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC431'><br/></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;analysis_ranks&#39;</span><span class="p">:</span> <span class="n">c</span><span class="o">.</span><span class="n">ranks</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">]})</span></div><div class='line' id='LC433'><br/></div><div class='line' id='LC434'><br/></div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_analysis_name</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC437'><br/></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC439'><br/></div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()})</span></div><div class='line' id='LC441'><br/></div><div class='line' id='LC442'><br/></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_type_of_analysis</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC444'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC445'><br/></div><div class='line' id='LC446'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC447'><br/></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;type_of_analysis&#39;</span><span class="p">:</span> <span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">})</span></div><div class='line' id='LC449'><br/></div><div class='line' id='LC450'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">append_samples_to_analysis</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span>         <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data_file_temp_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;data_file_path&#39;</span><span class="p">]</span></div><div class='line' id='LC453'><br/></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC455'><br/></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">additional_data_file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="s">&quot;additional_data_file&quot;</span><span class="p">)</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Copying additional data file&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">data_file_temp_path</span><span class="p">,</span> <span class="n">additional_data_file_path</span><span class="p">)</span></div><div class='line' id='LC459'><br/></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;additional_data_file_path&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">additional_data_file_path</span></div><div class='line' id='LC461'><br/></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC463'><br/></div><div class='line' id='LC464'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">################################################################</span></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># call server modules for append..</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">################################################################</span></div><div class='line' id='LC467'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># analysis specific stuff.</span></div><div class='line' id='LC468'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">server_modules_dict</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">]</span><span class="o">.</span><span class="n">_append</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC469'><br/></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># common analysis routines..</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">server_modules_dict</span><span class="p">[</span><span class="s">&#39;commons&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">_append</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">################################################################</span></div><div class='line' id='LC473'><br/></div><div class='line' id='LC474'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">additional_data_file_path</span><span class="p">)</span></div><div class='line' id='LC475'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Done.&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC476'><br/></div><div class='line' id='LC477'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">refresh_analysis_files</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC479'><br/></div><div class='line' id='LC480'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC481'><br/></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_module_dict</span> <span class="o">=</span> <span class="n">server_modules_dict</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">]</span><span class="o">.</span><span class="n">_module_functions</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC483'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_common_dict</span> <span class="o">=</span> <span class="n">server_modules_dict</span><span class="p">[</span><span class="s">&#39;commons&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">_module_functions</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">)</span></div><div class='line' id='LC484'><br/></div><div class='line' id='LC485'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;get_refresh_options&#39;</span><span class="p">):</span></div><div class='line' id='LC486'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">refresh_options_module</span> <span class="o">=</span> <span class="n">functions_module_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">refresh_options_common</span> <span class="o">=</span> <span class="n">functions_common_dict</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></div><div class='line' id='LC488'><br/></div><div class='line' id='LC489'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">refresh_options_module</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></div><div class='line' id='LC490'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">refresh_options_common</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></div><div class='line' id='LC491'><br/></div><div class='line' id='LC492'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">refresh_options</span> <span class="o">=</span> <span class="n">refresh_options_module</span> <span class="o">+</span> <span class="n">refresh_options_common</span></div><div class='line' id='LC493'><br/></div><div class='line' id='LC494'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">refresh_options</span></div><div class='line' id='LC495'><br/></div><div class='line' id='LC496'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_dict</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC497'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_dict</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">functions_module_dict</span><span class="p">)</span></div><div class='line' id='LC498'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_dict</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">functions_common_dict</span><span class="p">)</span></div><div class='line' id='LC499'><br/></div><div class='line' id='LC500'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># this is important. functions_dict contains function names,</span></div><div class='line' id='LC501'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># descriptions, as well as actual memory references to functions</span></div><div class='line' id='LC502'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># exported by protocol specific and common module provide.</span></div><div class='line' id='LC503'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC504'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># memory references are meaningful in the context of the server</span></div><div class='line' id='LC505'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># and they shouldn&#39;t be sent to clients (since clients can not</span></div><div class='line' id='LC506'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># do anything with them).</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC508'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># here, I am solving the problem by stripping those references</span></div><div class='line' id='LC509'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># from the data structure with my dirty loop before writing sending</span></div><div class='line' id='LC510'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># response data back to the client. a better solution could replace</span></div><div class='line' id='LC511'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># this anytime.</span></div><div class='line' id='LC512'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">module_item</span> <span class="ow">in</span> <span class="n">functions_dict</span><span class="p">:</span></div><div class='line' id='LC513'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_dict</span><span class="p">[</span><span class="n">module_item</span><span class="p">][</span><span class="s">&#39;func&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC514'><br/></div><div class='line' id='LC515'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;refresh_options&#39;</span><span class="p">:</span> <span class="n">refresh_options</span><span class="p">,</span> <span class="s">&#39;functions_dict&#39;</span><span class="p">:</span> <span class="n">functions_dict</span><span class="p">})</span></div><div class='line' id='LC516'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC517'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">refresh_requests</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;refresh_requests&#39;</span><span class="p">]</span></div><div class='line' id='LC518'><br/></div><div class='line' id='LC519'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># if late response wasn&#39;t requested send response immediately</span></div><div class='line' id='LC520'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;return_when_done&#39;</span><span class="p">):</span></div><div class='line' id='LC521'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC522'><br/></div><div class='line' id='LC523'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># trixy part:</span></div><div class='line' id='LC524'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">request</span> <span class="ow">in</span> <span class="n">refresh_requests</span><span class="p">:</span></div><div class='line' id='LC525'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">request</span> <span class="ow">in</span> <span class="n">functions_module_dict</span><span class="p">:</span></div><div class='line' id='LC526'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_module_dict</span><span class="p">[</span><span class="n">request</span><span class="p">][</span><span class="s">&#39;func&#39;</span><span class="p">](</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC527'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">request</span> <span class="ow">in</span> <span class="n">functions_common_dict</span><span class="p">:</span></div><div class='line' id='LC528'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">functions_common_dict</span><span class="p">[</span><span class="n">request</span><span class="p">][</span><span class="s">&#39;func&#39;</span><span class="p">](</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC529'><br/></div><div class='line' id='LC530'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># send the late response if it was requested</span></div><div class='line' id='LC531'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;return_when_done&#39;</span><span class="p">):</span></div><div class='line' id='LC532'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">})</span></div><div class='line' id='LC533'><br/></div><div class='line' id='LC534'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="p">(</span><span class="s">&quot;Done with refresh tasks.&quot;</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">log_file</span><span class="p">)</span></div><div class='line' id='LC535'><br/></div><div class='line' id='LC536'><br/></div><div class='line' id='LC537'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_sample_map_instances</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC538'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC539'><br/></div><div class='line' id='LC540'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC541'><br/></div><div class='line' id='LC542'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instances</span> <span class="o">=</span> <span class="n">framework</span><span class="o">.</span><span class="n">helper_functions</span><span class="o">.</span><span class="n">sorted_copy</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">get_sample_map_instances</span><span class="p">())</span></div><div class='line' id='LC543'><br/></div><div class='line' id='LC544'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">meta</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC545'><br/></div><div class='line' id='LC546'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">instance</span> <span class="ow">in</span> <span class="n">instances</span><span class="p">:</span></div><div class='line' id='LC547'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC548'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_name_file_path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC549'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_groups</span><span class="p">,</span> <span class="n">group_colors</span> <span class="o">=</span> <span class="n">helper_functions</span><span class="o">.</span><span class="n">get_groups_colors_from_sample_map_file</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_file_path</span><span class="p">)</span></div><div class='line' id='LC550'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">meta</span><span class="p">[</span><span class="n">instance</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="n">name</span> <span class="ow">or</span> <span class="s">&quot;Noname&quot;</span><span class="p">,</span></div><div class='line' id='LC551'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;sample_groups&#39;</span><span class="p">:</span> <span class="n">sample_groups</span><span class="p">,</span></div><div class='line' id='LC552'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;group_colors&#39;</span><span class="p">:</span> <span class="n">group_colors</span><span class="p">}</span></div><div class='line' id='LC553'><br/></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;instances&#39;</span><span class="p">:</span> <span class="n">instances</span><span class="p">,</span> <span class="s">&#39;meta&#39;</span><span class="p">:</span> <span class="n">meta</span> <span class="p">})</span></div><div class='line' id='LC555'><br/></div><div class='line' id='LC556'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_otu_confidence_tuples</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC557'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC558'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rank</span> <span class="o">=</span>  <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;rank&#39;</span><span class="p">]</span></div><div class='line' id='LC559'><br/></div><div class='line' id='LC560'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC561'><br/></div><div class='line' id='LC562'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">otu_confidence_tuples</span> <span class="o">=</span> <span class="n">DeserializeFromFile</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">type_specific_data_dir</span><span class="p">,</span> <span class="n">rank</span> <span class="o">+</span> <span class="s">&#39;_rdp_confidence_ordering_info&#39;</span><span class="p">))</span></div><div class='line' id='LC563'><br/></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;otu_confidence_tuples&#39;</span><span class="p">:</span> <span class="n">otu_confidence_tuples</span><span class="p">})</span></div><div class='line' id='LC565'><br/></div><div class='line' id='LC566'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_relative_type_specific_data_dir</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC567'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC568'><br/></div><div class='line' id='LC569'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC570'><br/></div><div class='line' id='LC571'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">relative_type_specific_data_dir</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">type_specific_data_dir</span><span class="p">)</span></div><div class='line' id='LC572'><br/></div><div class='line' id='LC573'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;relative_type_specific_data_dir&#39;</span><span class="p">:</span> <span class="n">relative_type_specific_data_dir</span><span class="p">})</span></div><div class='line' id='LC574'><br/></div><div class='line' id='LC575'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_relative_taxon_charts_dir</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC576'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC577'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span>    <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">]</span></div><div class='line' id='LC578'><br/></div><div class='line' id='LC579'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC580'><br/></div><div class='line' id='LC581'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC582'><br/></div><div class='line' id='LC583'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">relative_taxon_charts_dir</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span><span class="p">)</span></div><div class='line' id='LC584'><br/></div><div class='line' id='LC585'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;taxon_charts_dir&#39;</span><span class="p">:</span> <span class="n">relative_taxon_charts_dir</span><span class="p">})</span></div><div class='line' id='LC586'><br/></div><div class='line' id='LC587'><br/></div><div class='line' id='LC588'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_otu_t_p_tuples</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC589'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC590'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span>    <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">]</span></div><div class='line' id='LC591'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;rank&#39;</span><span class="p">):</span></div><div class='line' id='LC592'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rank</span>        <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;rank&#39;</span><span class="p">]</span></div><div class='line' id='LC593'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC594'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rank</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC595'><br/></div><div class='line' id='LC596'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC597'><br/></div><div class='line' id='LC598'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC599'><br/></div><div class='line' id='LC600'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_groups</span><span class="p">,</span> <span class="n">group_colors</span> <span class="o">=</span> <span class="n">helper_functions</span><span class="o">.</span><span class="n">get_groups_colors_from_sample_map_file</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_file_path</span><span class="p">)</span></div><div class='line' id='LC601'><br/></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">otu_t_p_tuple_dict</span> <span class="o">=</span> <span class="n">DeserializeFromFile</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_file_path</span><span class="p">)</span></div><div class='line' id='LC603'><br/></div><div class='line' id='LC604'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">rank</span><span class="p">:</span></div><div class='line' id='LC605'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;otu_t_p_tuple_list&#39;</span><span class="p">:</span> <span class="n">otu_t_p_tuple_dict</span><span class="p">[</span><span class="n">rank</span><span class="p">]</span> <span class="p">})</span></div><div class='line' id='LC606'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC607'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;otu_t_p_tuple_dict&#39;</span><span class="p">:</span> <span class="n">otu_t_p_tuple_dict</span> <span class="p">})</span></div><div class='line' id='LC608'><br/></div><div class='line' id='LC609'><br/></div><div class='line' id='LC610'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_sample_maps</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC611'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC612'><br/></div><div class='line' id='LC613'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC614'><br/></div><div class='line' id='LC615'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maps</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC616'><br/></div><div class='line' id='LC617'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># if instance specified, return only that, otherwise return all sample maps.</span></div><div class='line' id='LC618'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_instances</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC619'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&#39;instance&#39;</span><span class="p">):</span></div><div class='line' id='LC620'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_instances</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;instance&#39;</span><span class="p">])</span></div><div class='line' id='LC621'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC622'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sample_map_instances</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">get_sample_map_instances</span><span class="p">()</span></div><div class='line' id='LC623'><br/></div><div class='line' id='LC624'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">instance</span> <span class="ow">in</span> <span class="n">sample_map_instances</span><span class="p">:</span></div><div class='line' id='LC625'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">change_current_sample_map_instance</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC626'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maps</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">helper_functions</span><span class="o">.</span><span class="n">get_sample_map_dict</span><span class="p">(</span><span class="n">p</span><span class="p">))</span></div><div class='line' id='LC627'><br/></div><div class='line' id='LC628'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;sample_maps&#39;</span><span class="p">:</span> <span class="n">maps</span><span class="p">})</span></div><div class='line' id='LC629'><br/></div><div class='line' id='LC630'><br/></div><div class='line' id='LC631'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_analysis_info</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC632'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC633'><br/></div><div class='line' id='LC634'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC635'><br/></div><div class='line' id='LC636'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">info_dict</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;id&#39;</span><span class="p">:</span> <span class="n">analysis_id</span><span class="p">,</span></div><div class='line' id='LC637'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span></div><div class='line' id='LC638'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;type&#39;</span><span class="p">:</span> <span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">,</span></div><div class='line' id='LC639'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;ranks&#39;</span><span class="p">:</span> <span class="n">c</span><span class="o">.</span><span class="n">ranks</span><span class="p">[</span><span class="n">p</span><span class="o">.</span><span class="n">type</span><span class="p">],</span></div><div class='line' id='LC640'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rdp_output_file_exists&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">rdp_output_file_path</span><span class="p">),</span></div><div class='line' id='LC641'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rdp_output_file_path&#39;</span>  <span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">rdp_output_file_name</span><span class="p">),</span></div><div class='line' id='LC642'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;all_unique_samples_list&#39;</span><span class="p">:</span> <span class="n">framework</span><span class="o">.</span><span class="n">helper_functions</span><span class="o">.</span><span class="n">sorted_copy</span><span class="p">([</span><span class="n">sample</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">sample</span> <span class="ow">in</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">all_unique_samples_file_path</span><span class="p">)</span><span class="o">.</span><span class="n">readlines</span><span class="p">()]),</span></div><div class='line' id='LC643'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;samples_sequences_bar&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">samples_sequences_bar_name</span><span class="p">),</span></div><div class='line' id='LC644'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;pie_charts_dir&#39;</span> <span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">pie_charts_dir_name</span><span class="p">),</span></div><div class='line' id='LC645'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rarefaction_all_samples_exists&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">rarefaction_curves_all_samples_file_path</span><span class="p">),</span></div><div class='line' id='LC646'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rarefaction_all_samples&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">rarefaction_curves_all_samples_file_name</span><span class="p">),</span></div><div class='line' id='LC647'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rarefaction_curves_dir&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">rarefaction_curves_dir_name</span><span class="p">),</span></div><div class='line' id='LC648'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rarefaction_prefix&#39;</span><span class="p">:</span> <span class="n">c</span><span class="o">.</span><span class="n">rarefaction_curve_file_prefix</span><span class="p">,</span></div><div class='line' id='LC649'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;rarefaction_postfix&#39;</span><span class="p">:</span> <span class="n">c</span><span class="o">.</span><span class="n">rarefaction_curve_file_postfix</span><span class="p">,</span></div><div class='line' id='LC650'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;shannon_diversity_index_img&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">shannon_diversity_index_img_name</span><span class="p">),</span></div><div class='line' id='LC651'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;simpsons_diversity_index_img&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">simpsons_diversity_index_img_name</span><span class="p">),</span></div><div class='line' id='LC652'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;shannon_diversity_index_data&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">shannon_diversity_index_data_name</span><span class="p">),</span></div><div class='line' id='LC653'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;simpsons_diversity_index_data&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">simpsons_diversity_index_data_name</span><span class="p">)}</span></div><div class='line' id='LC654'><br/></div><div class='line' id='LC655'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;info&#39;</span><span class="p">:</span> <span class="n">info_dict</span><span class="p">})</span></div><div class='line' id='LC656'><br/></div><div class='line' id='LC657'><br/></div><div class='line' id='LC658'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_samples_in_an_analysis</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC659'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">analysis_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_dict</span><span class="p">[</span><span class="s">&#39;analysis_id&#39;</span><span class="p">]</span></div><div class='line' id='LC660'><br/></div><div class='line' id='LC661'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">Meta</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC662'><br/></div><div class='line' id='LC663'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">samples</span> <span class="o">=</span> <span class="n">framework</span><span class="o">.</span><span class="n">helper_functions</span><span class="o">.</span><span class="n">sorted_copy</span><span class="p">([</span><span class="n">sample</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">sample</span> <span class="ow">in</span> <span class="nb">open</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">all_unique_samples_file_path</span><span class="p">)</span><span class="o">.</span><span class="n">readlines</span><span class="p">()])</span></div><div class='line' id='LC664'><br/></div><div class='line' id='LC665'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;samples&#39;</span><span class="p">:</span> <span class="n">samples</span><span class="p">})</span></div><div class='line' id='LC666'><br/></div><div class='line' id='LC667'><br/></div><div class='line' id='LC668'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">status_request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC669'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">write_socket</span><span class="p">({</span><span class="s">&#39;response&#39;</span><span class="p">:</span> <span class="s">&#39;OK&#39;</span><span class="p">,</span> <span class="s">&#39;running_analyses&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">running_analyses</span><span class="p">,</span> <span class="s">&#39;done_analyses&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">serverstate</span><span class="o">.</span><span class="n">done_analyses</span><span class="p">})</span></div><div class='line' id='LC670'><br/></div><div class='line' id='LC671'><br/></div><div class='line' id='LC672'><span class="k">class</span> <span class="nc">Dirs</span><span class="p">:</span></div><div class='line' id='LC673'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">analysis_id</span><span class="p">):</span></div><div class='line' id='LC674'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">analyses_dir</span><span class="p">,</span> <span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC675'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC676'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC677'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC678'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC679'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC680'><br/></div><div class='line' id='LC681'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">):</span></div><div class='line' id='LC682'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">)</span></div><div class='line' id='LC683'><br/></div><div class='line' id='LC684'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_maps_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_maps_dir_name</span><span class="p">)</span></div><div class='line' id='LC685'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_maps_dir</span><span class="p">):</span></div><div class='line' id='LC686'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_maps_dir</span><span class="p">)</span></div><div class='line' id='LC687'><br/></div><div class='line' id='LC688'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">pie_charts_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">pie_charts_dir_name</span><span class="p">)</span></div><div class='line' id='LC689'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pie_charts_dir</span><span class="p">):</span></div><div class='line' id='LC690'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pie_charts_dir</span><span class="p">)</span></div><div class='line' id='LC691'><br/></div><div class='line' id='LC692'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rarefaction_curves_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">rarefaction_curves_dir_name</span><span class="p">)</span></div><div class='line' id='LC693'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rarefaction_curves_dir</span><span class="p">):</span></div><div class='line' id='LC694'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rarefaction_curves_dir</span><span class="p">)</span></div><div class='line' id='LC695'><br/></div><div class='line' id='LC696'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">type_specific_data_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">type_specific_figures_dir_name</span><span class="p">)</span></div><div class='line' id='LC697'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_specific_data_dir</span><span class="p">):</span></div><div class='line' id='LC698'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_specific_data_dir</span><span class="p">)</span></div><div class='line' id='LC699'><br/></div><div class='line' id='LC700'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_sample_map_instances</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC701'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="nb">dir</span> <span class="k">for</span> <span class="nb">dir</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_maps_dir</span><span class="p">)</span> <span class="k">if</span> <span class="ow">not</span> <span class="nb">dir</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)]</span></div><div class='line' id='LC702'><br/></div><div class='line' id='LC703'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">create_new_sample_map_instance</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">files</span><span class="p">):</span></div><div class='line' id='LC704'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_maps_dir</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_sample_map_instances</span><span class="p">())</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span></div><div class='line' id='LC705'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">)</span></div><div class='line' id='LC706'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir_name</span><span class="p">)</span></div><div class='line' id='LC707'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span><span class="p">)</span></div><div class='line' id='LC708'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir_name</span><span class="p">)</span></div><div class='line' id='LC709'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir</span><span class="p">)</span></div><div class='line' id='LC710'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir_name</span><span class="p">)</span></div><div class='line' id='LC711'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir</span><span class="p">)</span></div><div class='line' id='LC712'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="o">.</span><span class="n">update_sample_map_files_info</span><span class="p">()</span></div><div class='line' id='LC713'><br/></div><div class='line' id='LC714'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">change_current_sample_map_instance</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">files</span><span class="p">,</span> <span class="n">instance</span><span class="p">):</span></div><div class='line' id='LC715'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance</span> <span class="o">=</span> <span class="n">instance</span></div><div class='line' id='LC716'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_maps_dir</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">instance</span><span class="p">))</span></div><div class='line' id='LC717'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir_name</span><span class="p">)</span></div><div class='line' id='LC718'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir_name</span><span class="p">)</span></div><div class='line' id='LC719'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir_name</span><span class="p">)</span></div><div class='line' id='LC720'><br/></div><div class='line' id='LC721'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#make sure these directories exist:</span></div><div class='line' id='LC722'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span><span class="p">):</span></div><div class='line' id='LC723'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_taxon_charts_dir</span><span class="p">)</span></div><div class='line' id='LC724'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir</span><span class="p">):</span></div><div class='line' id='LC725'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir</span><span class="p">)</span></div><div class='line' id='LC726'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir</span><span class="p">):</span></div><div class='line' id='LC727'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sample_map_dendrograms_dir</span><span class="p">)</span></div><div class='line' id='LC728'><br/></div><div class='line' id='LC729'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">files</span><span class="o">.</span><span class="n">update_sample_map_files_info</span><span class="p">()</span></div><div class='line' id='LC730'><br/></div><div class='line' id='LC731'><br/></div><div class='line' id='LC732'><span class="k">class</span> <span class="nc">Images</span><span class="p">:</span></div><div class='line' id='LC733'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dirs</span><span class="p">):</span></div><div class='line' id='LC734'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">samples_sequences_bar_path</span>         <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">samples_sequences_bar_name</span><span class="p">)</span></div><div class='line' id='LC735'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simpsons_diversity_index_img_path</span>  <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">simpsons_diversity_index_img_name</span><span class="p">)</span></div><div class='line' id='LC736'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">shannon_diversity_index_img_path</span>   <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">shannon_diversity_index_img_name</span><span class="p">)</span></div><div class='line' id='LC737'><br/></div><div class='line' id='LC738'><span class="k">class</span> <span class="nc">Files</span><span class="p">:</span></div><div class='line' id='LC739'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dirs</span><span class="p">):</span></div><div class='line' id='LC740'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">dirs</span>                         <span class="o">=</span> <span class="n">dirs</span></div><div class='line' id='LC741'><br/></div><div class='line' id='LC742'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">J</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span></div><div class='line' id='LC743'><br/></div><div class='line' id='LC744'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">data_file_path</span>                        <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">data_file_name</span><span class="p">)</span></div><div class='line' id='LC745'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rdp_output_file_path</span>                  <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">rdp_output_file_name</span><span class="p">)</span></div><div class='line' id='LC746'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">all_unique_samples_file_path</span>          <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">all_unique_samples_file_name</span><span class="p">)</span></div><div class='line' id='LC747'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">otu_library_file_path</span>                 <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">otu_library_file_name</span><span class="p">)</span></div><div class='line' id='LC748'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rdp_error_log_file_path</span>               <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">rdp_error_log_file_name</span><span class="p">)</span></div><div class='line' id='LC749'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">seperator_file_path</span>                   <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">seperator_file_name</span><span class="p">)</span></div><div class='line' id='LC750'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">log_file</span>                              <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">log_file_name</span><span class="p">)</span></div><div class='line' id='LC751'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">job_file</span>                              <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">job_name_file_name</span><span class="p">)</span></div><div class='line' id='LC752'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">type_of_analysis_file_path</span>            <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">type_of_analysis_file_name</span><span class="p">)</span></div><div class='line' id='LC753'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">samples_serialized_file_path</span>          <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">samples_serialized_file_name</span><span class="p">)</span></div><div class='line' id='LC754'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rarefaction_dict_serialized_file_path</span> <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">rarefaction_dict_serialized_file_name</span><span class="p">)</span></div><div class='line' id='LC755'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rarefaction_curves_all_samples_file_path</span> <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">rarefaction_curves_all_samples_file_name</span><span class="p">)</span></div><div class='line' id='LC756'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simpsons_diversity_index_data_path</span>  <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">simpsons_diversity_index_data_name</span><span class="p">)</span></div><div class='line' id='LC757'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">shannon_diversity_index_data_path</span>   <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dirs</span><span class="o">.</span><span class="n">analysis_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">shannon_diversity_index_data_name</span><span class="p">)</span></div><div class='line' id='LC758'><br/></div><div class='line' id='LC759'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_name_file_path</span>                     <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC760'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_file_path</span>                          <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC761'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_file_path</span>      <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC762'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_real_file_path</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC763'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_filtered_samples_dict_file_path</span>    <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC764'><br/></div><div class='line' id='LC765'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">taxa_color_dict_file_path</span>         <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">taxa_color_dict_file_name</span><span class="p">)</span></div><div class='line' id='LC766'><br/></div><div class='line' id='LC767'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">update_sample_map_files_info</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC768'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">J</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span></div><div class='line' id='LC769'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">H</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dirs</span><span class="o">.</span><span class="n">sample_map_instance_dir</span><span class="p">,</span> <span class="n">c</span><span class="o">.</span><span class="n">sample_map_heatmaps_dir_name</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span></div><div class='line' id='LC770'><br/></div><div class='line' id='LC771'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_name_file_path</span>                     <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">sample_map_name_file_name</span><span class="p">)</span></div><div class='line' id='LC772'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_file_path</span>                          <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">sample_map_file_name</span><span class="p">)</span></div><div class='line' id='LC773'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_file_path</span>      <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_file_name</span><span class="p">)</span></div><div class='line' id='LC774'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_real_file_path</span> <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">sample_map_otu_t_p_tuples_dict_real_file_name</span><span class="p">)</span></div><div class='line' id='LC775'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sample_map_filtered_samples_dict_file_path</span>    <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">sample_map_filtered_samples_dict_file_name</span><span class="p">)</span></div><div class='line' id='LC776'><br/></div><div class='line' id='LC777'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">levels_list</span> <span class="ow">in</span> <span class="n">c</span><span class="o">.</span><span class="n">ranks</span><span class="o">.</span><span class="n">values</span><span class="p">():</span></div><div class='line' id='LC778'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">level</span> <span class="ow">in</span> <span class="n">levels_list</span><span class="p">:</span></div><div class='line' id='LC779'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">percent_abundance_file_prefix</span></div><div class='line' id='LC780'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">vars</span><span class="p">(</span><span class="bp">self</span><span class="p">)[</span><span class="s">&#39;</span><span class="si">%s%s</span><span class="s">_file_path&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">level</span><span class="p">)]</span> <span class="o">=</span> <span class="n">J</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">level</span><span class="p">))</span></div><div class='line' id='LC781'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">abundance_heatmap_file_prefix</span></div><div class='line' id='LC782'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">vars</span><span class="p">(</span><span class="bp">self</span><span class="p">)[</span><span class="s">&#39;</span><span class="si">%s%s</span><span class="s">_file_path&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">level</span><span class="p">)]</span> <span class="o">=</span> <span class="n">H</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s%s</span><span class="s">.png&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">level</span><span class="p">))</span></div><div class='line' id='LC783'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">heatmap_options_file_prefix</span></div><div class='line' id='LC784'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">vars</span><span class="p">(</span><span class="bp">self</span><span class="p">)[</span><span class="s">&#39;</span><span class="si">%s%s</span><span class="s">_file_path&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">level</span><span class="p">)]</span> <span class="o">=</span> <span class="n">H</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">level</span><span class="p">))</span></div><div class='line' id='LC785'><br/></div><div class='line' id='LC786'><br/></div><div class='line' id='LC787'><span class="k">class</span> <span class="nc">Meta</span><span class="p">:</span></div><div class='line' id='LC788'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC789'><span class="sd">    Meta-info for a particular analysis. contains - </span></div><div class='line' id='LC790'><span class="sd">dirs - Dirs object</span></div><div class='line' id='LC791'><span class="sd">files - Files object</span></div><div class='line' id='LC792'><span class="sd">images - Images object</span></div><div class='line' id='LC793'><span class="sd">type - str</span></div><div class='line' id='LC794'><span class="sd">desc - str</span></div><div class='line' id='LC795'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC796'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">analysis_id</span><span class="p">):</span></div><div class='line' id='LC797'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">dirs</span> <span class="o">=</span> <span class="n">Dirs</span><span class="p">(</span><span class="n">analysis_id</span><span class="p">)</span></div><div class='line' id='LC798'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">files</span> <span class="o">=</span> <span class="n">Files</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dirs</span><span class="p">)</span></div><div class='line' id='LC799'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">images</span> <span class="o">=</span> <span class="n">Images</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dirs</span><span class="p">)</span></div><div class='line' id='LC800'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">type</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_analysis_type</span><span class="p">()</span></div><div class='line' id='LC801'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">desc</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_analysis_desc</span><span class="p">()</span></div><div class='line' id='LC802'><br/></div><div class='line' id='LC803'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">set_analysis_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span></div><div class='line' id='LC804'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span> <span class="ow">in</span> <span class="n">c</span><span class="o">.</span><span class="n">ranks</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span></div><div class='line' id='LC805'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">type</span> <span class="o">=</span> <span class="nb">type</span></div><div class='line' id='LC806'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">type_of_analysis_file_path</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">type</span><span class="p">)</span></div><div class='line' id='LC807'><br/></div><div class='line' id='LC808'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_analysis_type</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC809'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">type_of_analysis_file_path</span><span class="p">):</span></div><div class='line' id='LC810'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">type_of_analysis_file_path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC811'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC812'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span></div><div class='line' id='LC813'><br/></div><div class='line' id='LC814'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_analysis_desc</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC815'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">):</span></div><div class='line' id='LC816'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">job_file</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC817'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC818'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span></div><div class='line' id='LC819'><br/></div><div class='line' id='LC820'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC821'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Initializes the Server with the socket specified in config.py&quot;&quot;&quot;</span></div><div class='line' id='LC822'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Server</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">socket_name</span><span class="p">)</span></div><div class='line' id='LC823'><br/></div></pre></div>
              
            
          </td>
        </tr>
      </table>
    
  </div>


          </div>
        </div>
      </div>
    </div>
  

  </div>


<div class="frame frame-loading" style="display:none;">
  <img src="/images/modules/ajax/big_spinner_336699.gif">
</div>

    </div>
  
      
    </div>

    <div id="footer" class="clearfix">
      <div class="site">
        <div class="sponsor">
          <a href="http://www.rackspace.com" class="logo">
            <img alt="Dedicated Server" src="https://assets3.github.com/images/modules/footer/rackspace_logo.png?v2?7ebd928ca3f97afefa144c3d65ae70b92f1248df" />
          </a>
          Powered by the <a href="http://www.rackspace.com ">Dedicated
          Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
          Computing</a> of Rackspace Hosting<span>&reg;</span>
        </div>

        <ul class="links">
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
          <li><a href="http://support.github.com?sso=_-D9qfwBNALVWtVhGCwVCzX3G3akBoO36XQ8M-kMER3mItaw2V5DpBTBMMTZiae4c7sk3aoLm4cvtB6DYc0pVsgLav6ndYTVLOyVwnKJbF9WmETJaETbZCHGtBLyEK96-tRgyEQ6cI3VeQbfppxpJx92OQtvSjK8RaGe2WFSnmDlzk-6ce-WkFB6LvrM9jCF6fP4zmO4d_bZMJOwHGQdz7W6VI7rb8YC80wZHkYh80A">Support</a></li>
          <li><a href="https://github.com/training">Training</a></li>
          <li><a href="http://jobs.github.com">Job Board</a></li>
          <li><a href="http://shop.github.com">Shop</a></li>
          <li><a href="https://github.com/contact">Contact</a></li>
          <li><a href="http://develop.github.com">API</a></li>
          <li><a href="http://status.github.com">Status</a></li>
        </ul>
        <ul class="sosueme">
          <li class="main">&copy; 2011 <span id="_rrt" title="0.62095s from fe6.rs.github.com">GitHub</span> Inc. All rights reserved.</li>
          <li><a href="/site/terms">Terms of Service</a></li>
          <li><a href="/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
        </ul>
      </div>
    </div><!-- /#footer -->

    
      
      
        <!-- current locale:  -->
        <div class="locales">
          <div class="site">

            <ul class="choices clearfix limited-locales">
              <li><span class="current">English</span></li>
              
                  <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
              
                  <li><a rel="nofollow" href="?locale=fr">Français</a></li>
              
                  <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
              
                  <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
              
                  <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
              
                  <li><a rel="nofollow" href="?locale=zh">中文</a></li>
              
              <li class="all"><a href="#" class="minibutton btn-forward js-all-locales"><span><span class="icon"></span>See all available languages</span></a></li>
            </ul>

            <div class="all-locales clearfix">
              <h3>Your current locale selection: <strong>English</strong>. Choose another?</h3>
              
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=en">English</a></li>
                  
                      <li><a rel="nofollow" href="?locale=af">Afrikaans</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ca">Català</a></li>
                  
                      <li><a rel="nofollow" href="?locale=cs">Čeština</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
                  
                      <li><a rel="nofollow" href="?locale=es">Español</a></li>
                  
                      <li><a rel="nofollow" href="?locale=fr">Français</a></li>
                  
                      <li><a rel="nofollow" href="?locale=hr">Hrvatski</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=id">Indonesia</a></li>
                  
                      <li><a rel="nofollow" href="?locale=it">Italiano</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
                  
                      <li><a rel="nofollow" href="?locale=nl">Nederlands</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=no">Norsk</a></li>
                  
                      <li><a rel="nofollow" href="?locale=pl">Polski</a></li>
                  
                      <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=sr">Српски</a></li>
                  
                      <li><a rel="nofollow" href="?locale=sv">Svenska</a></li>
                  
                      <li><a rel="nofollow" href="?locale=zh">中文</a></li>
                  
                </ul>
              
            </div>

          </div>
          <div class="fade"></div>
        </div>
      
    

    <script>window._auth_token = "ec8a50cb21afebeada2aeb4b474176ca58045c86"</script>
    <div id="keyboard_shortcuts_pane" style="display:none">
  <h2>Keyboard Shortcuts</h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column middle">
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Open tree</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>p</dt>
        <dd>Open parent</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column last">
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->
  </div><!-- /.columns.equacols -->

  <div class="rule"></div>

  <h3>Issues</h3>

  <div class="columns threecols">
    <div class="column first">
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>x</dt>
        <dd>Toggle select target</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column middle">
      <dl class="keyboard-mappings">
        <dt>I</dt>
        <dd>Mark selected as read</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>U</dt>
        <dd>Mark selected as unread</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>e</dt>
        <dd>Close selected</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Remove selected from view</dd>
      </dl>
    </div><!-- /.column.middle -->
    <div class="column last">
      <dl class="keyboard-mappings">
        <dt>c</dt>
        <dd>Create issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>l</dt>
        <dd>Create label</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>i</dt>
        <dd>Back to inbox</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>u</dt>
        <dd>Back to issues</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>/</dt>
        <dd>Focus issues search</dd>
      </dl>
    </div>
  </div>

  <div class="rule"></div>

  <h3>Network Graph</h3>
  <div class="columns equacols">
    <div class="column first">
      <dl class="keyboard-mappings">
        <dt>← <em>or</em> h</dt>
        <dd>Scroll left</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>→ <em>or</em> l</dt>
        <dd>Scroll right</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>↑ <em>or</em> k</dt>
        <dd>Scroll up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>↓ <em>or</em> j</dt>
        <dd>Scroll down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Toggle visibility of head labels</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column last">
      <dl class="keyboard-mappings">
        <dt>shift ← <em>or</em> shift h</dt>
        <dd>Scroll all the way left</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>shift → <em>or</em> shift l</dt>
        <dd>Scroll all the way right</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>shift ↑ <em>or</em> shift k</dt>
        <dd>Scroll all the way up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>shift ↓ <em>or</em> shift j</dt>
        <dd>Scroll all the way down</dd>
      </dl>
    </div><!-- /.column.last -->
  </div>

</div>
    

    <!--[if IE 8]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie8")
    </script>
    <![endif]-->

    <!--[if IE 7]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie7")
    </script>
    <![endif]-->

    
    <script type='text/javascript'>mpq.push(['identify', 'mazubieta']);</script>
    
  </body>
</html>


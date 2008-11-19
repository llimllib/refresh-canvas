<%def name="head(codebox_height=200)">
<html>
 <head>
  <style type="text/css">
body, html {margin:0;
            padding:0;
            background:white;
            color:#000;
}
body { min-width: 750px; }
#wrap { margin:0 auto; width:100%; }
#canvascontainer { margin-left: 5px;
				   margin-top: 5px;
                   width: 320px;
                   float: left;
				   position: fixed;
}
<%
    codebox_width = 700
%>
#codebox {border: 1px solid LightGray;
          width:${codebox_width+4}px;
          height:${codebox_height}px;
          margin-top: 10px;
}
#libraryContainer {border: 1px solid LightGray;
          width:${codebox_width+4}px;
          height:${codebox_height}px;
          margin-top: 10px;
}
#textcontainer {font: 14px;
    margin-left: 320px;
    margin-right: 10px;
	margin-top:   10px;
}
#footer {clear:both;}

#canvas { border: 1px solid DarkGray; }
  </style>
  <script type="text/javascript" src="jquery-1.2.6.js"></script>
  <script type="text/javascript" src="codemirror/codemirror.js"></script>
  <title>Canvas Tutorial</title>
  <script type="application/x-javascript">
var editor = undefined;
var libEditor = undefined;
var intervalID = undefined;

function runCode() {
	if (intervalID != undefined)
	    clearInterval(intervalID);
    //TODO: handle exceptions somehow
    $("#canvas")[0].getContext("2d").clearRect(0,0,
	  $("#canvas")[0].width,
	  $("#canvas")[0].height);
	//if there's a library defined, eval it
	eval($("#library").val());
    intervalID = eval(editor.getCode());
}

var libraryOpen = false;

$(document).ready(function(){

$("#libraryContainer").hide();

editor = CodeMirror.fromTextArea("code", {
  parserfile: ["tokenizejavascript.js", "parsejavascript.js"],
  path: "codemirror/",
  stylesheet: "codemirror/jscolors.css",
  width: "${codebox_width}px",
  height: "${codebox_height}px",
});

libEditor = CodeMirror.fromTextArea("library", {
  parserfile: ["tokenizejavascript.js", "parsejavascript.js"],
  path: "codemirror/",
  stylesheet: "codemirror/jscolors.css",
  width: "${codebox_width}px",
  height: "${codebox_height}px",
});

$("#showlib").click(function() {
	$("#explain").toggle();
	$("#libraryContainer").toggle();
	var text = libraryOpen ? "Show Library" : "Show Code";
	$("#showlib").text(text);
});

});
  </script>
 </head>
 <body>
 <div id="wrap">
   <!-- <div id="header">
   <h2>Breakout Tutorial</h2>
    </div>-->

   <div id="canvascontainer">
       <canvas id="canvas" width="300" height="300"></canvas>
       <div style="text-align:center">
       <input type="submit" value="run code" onclick="runCode()"/>
       </div>
	   <a href="#" id="showlib">Show Library</a><br>
	   <a href="#" id="prevLink">prev</a> <a href="#" id="nextLink" style="text-align: right;">next</a>
   </div>
   <div id="textcontainer">

</%def>

<%def name="link(p, f)">
    <div id="footer">
	   % if p:
		   <a href="${p}.html">&lt; &lt; previous</a>
	   % endif
       <a href="${f}.html">next &gt;&gt;</a>
    </div>
    </div>
 </body>
</html>
</%def>

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
}
<%
    codebox_width = 450
%>
#codebox {border: 1px solid LightGray;
          width:${codebox_width+4}px;
          height:${codebox_height}px;
          margin-top: 10px;
}
#textcontainer {font: 14px;
    margin-left: 320px;
    margin-right: 10px;
}
#footer {clear:both;}

#canvas { border: 1px solid DarkGray; }
  </style>
  <script type="text/javascript" src="jquery-1.2.6.js"></script>
  <script type="text/javascript" src="codemirror/codemirror.js"></script>
  <title>Canvas Tutorial</title>
  <script type="application/x-javascript">
var editor = undefined;
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

$(document).ready(function(){

editor = CodeMirror.fromTextArea("code", {
  parserfile: ["tokenizejavascript.js", "parsejavascript.js"],
  path: "codemirror/",
  stylesheet: "codemirror/jscolors.css",
  width: "${codebox_width}px",
  height: "${codebox_height}px",
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
   </div>
   <div id="textcontainer">

</%def>

<%def name="next(f)">
    <div id="footer">
       <a href="${f}">next &gt;&gt;</a>
    </div>
    </div>
 </body>
</html>
</%def>

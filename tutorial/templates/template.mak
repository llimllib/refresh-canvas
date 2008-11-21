<html>
 <head>
  <style type="text/css">
body, html {margin:0;
            padding:0;
            background:white;
            color:#000;
}
body { min-width: 750px; 
	   font-size: 62.5%;}
#wrap { margin:0 auto; width:100%; }
#canvascontainer { margin-left: 5px;
                   margin-top: 5px;
                   width: 320px;
                   float: left;
                   position: fixed;
}
<%
    codebox_height = 26 + code.count("\n") * 15
    codebox_width = 700
%>
#codebox {border: 1px solid LightGray;
          width:${codebox_width+4}px;
          height:${codebox_height}px;
          margin-top: 10px;
          nothing: ${code};
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
#libraryBox { border: 1px solid DarkGray; }
    </style>
    <script type="text/javascript" src="jquery-1.2.6.js"></script>
    <script type="text/javascript" src="jquery-ui-1.6rc2.js"></script>
    <link rel="stylesheet" href="theme/ui-theme.css" type="text/css" media="screen">
    <script type="text/javascript" src="codemirror/codemirror.js"></script>
    <title>Canvas Tutorial</title>
<script type="text/javascript">
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

    $("#textcontainer ul").tabs();
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

         % if prev:
             <a href="${prev}.html" id="prevLink">prev</a>
         % endif
         % if next:
             <a href="${next}.html" id="nextLink">next</a>
         % endif
    </div>

    <div id="textcontainer">
        <ul><li class="ui-tabs-nav-item"><a href="#explain"><span>Code</span></a></li>
            <li class="ui-tabs-nav-item"><a href="#libraryContainer"><span>Library</span></a></li>
        </ul>
        <div id="explain">${explain_before}
            % if code:
                 <div id="codebox">
                 <textarea id="code" rows=${code.count("\n")+1} cols=100>${code}</textarea>
                 </div>
                 <p>${explain_after}
            % endif
        </div>
     
        <div id="libraryContainer">
        % if library:
            <div id="libraryBox">
                <textarea id="library" rows=${library.count("\n")+1}
                          cols=100>${library}</textarea>
            </div>
        % endif
        </div>
    </div>
 </body>
</html>

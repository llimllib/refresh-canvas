<%def name="head(script='')">
<html>
 <head>
  <style type="text/css">
#canvas { border: 1px solid;
		  width:        300px;
		  height:       300px;
		  float:        left;
		  margin-right: 15px;
}
div#explain { font:  14px;
              width: 800px;
}
a#next { /*TODO get right aligned*/ }
  </style>
  <script type="text/javascript" src="jquery-1.2.6.js"></script>
  <script type="text/javascript" src="codemirror/codemirror.js"></script>
  <title>Canvas Tutorial</title>
  <script type="application/x-javascript">
var editor = undefined;

function runCode() {
    //TODO: handle exceptions somehow
    eval(editor.getCode());
}

$(document).ready(function(){

editor = CodeMirror.fromTextArea("code", {
  parserfile: ["tokenizejavascript.js", "parsejavascript.js"],
  path: "codemirror/",
  stylesheet: "codemirror/jscolors.css",
  width: "100%",
  height: "200px",
});

});
  </script>
 </head>
 <body>
   <h2>Breakout Tutorial</h2>

   <canvas id="canvas" width="300" height="300"></canvas>

</%def>

<%def name="next(f)">
   <a id="next" href="${f}">next &gt;&gt;</a>
 </body>
</html>
</%def>

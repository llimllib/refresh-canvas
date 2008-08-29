<%namespace name="head" file="head.mak" />
${head.head()}

   <div id="explain">Now that we've got a canvas to draw on, let's do so:
   <textarea id="code" rows=10 cols=50>//get a reference to the canvas
var ctx = $('#canvas').getContext("2d");

//draw a circle
ctx.arc(75,75,10,0,Math.PI*2,true); 
ctx.fill();</textarea><br />
	<input type="submit" value="run code" onclick="runCode()"/>
   </div>

${head.next('square.html')}

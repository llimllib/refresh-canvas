<%namespace name="head" file="head.mak" />
${head.head()}

   <div id="explain">Now that we've got a canvas to draw on, let's do so:
   <div style="border: 1px solid; margin-left:320px;">
   <textarea id="code" rows=10 cols=50>//get a reference to the canvas
var ctx = $('#canvas')[0].getContext("2d");

//draw a circle
ctx.arc(75,75,10,0,Math.PI*2,true); 
ctx.fill();</textarea></div>
	<input type="submit" value="run code" onclick="runCode()"/>
   </div>

${head.next('square.html')}

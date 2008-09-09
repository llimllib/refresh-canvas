<%namespace name="head" file="head.mak" />
${head.head()}

	<div id="explain">Now that we've got a canvas to draw on, let's do so:
	   <div id="codebox">
		   <textarea id="code" rows=10 cols=50>//get a reference to the canvas
var ctx = $('#canvas')[0].getContext("2d");

//draw a circle
ctx.beginPath();
ctx.arc(75, 75, 10, 0, Math.PI*2, true); 
ctx.closePath();
ctx.fill();</textarea></div>
			<input type="submit" value="run code" onclick="runCode()"/><br>
		<p>
		You may want to comment out the <code>arc(...)</code> call and try
		<code>ctx.rect(x, y, width, height)</code>.
		<p>Make sure you keep the arc and rect calls in between calls to
		<code>beginPath()</code> and <code>closePath()</code> just like the
		sample call above. You may also try substituting <code>stroke()</code>
		for <code>fill()</code>.
    </div>
${head.next('color.html')}

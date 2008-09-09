<%namespace name="head" file="head.mak" />
${head.head(310)}
	<div id="explain">We can also turn our ball different colors. Changing the value of
	ctx.fillStyle will change the canvas' current color; we can set its value to a hex
	string of the format <code>'#rrggbb'</code> or to a string 
	<code>'rgba(r, g, b, a)'</code> where a is a value
	between 0 and 1 representing the transparency of the color.
	   <div id="codebox">
		   <textarea id="code" rows=10 cols=50>var ctx = $('#canvas')[0].getContext("2d");

ctx.fillStyle = "#CCA68F";
ctx.beginPath();
ctx.arc(220, 220, 50, 0, Math.PI*2, true);
ctx.closePath();
ctx.fill();

ctx.fillStyle = "#60BF60";
ctx.beginPath();
ctx.arc(100, 100, 100, 0, Math.PI*2, true);
ctx.closePath();
ctx.fill();

//the rectangle is half transparent
ctx.fillStyle = "rgba(128, 104, 89, .5)"
ctx.beginPath();
ctx.rect(15, 150, 120, 120);
ctx.closePath();
ctx.fill();</textarea></div>
			<input type="submit" value="run code" onclick="runCode()"/><br>
			<p>
			Play around a bit with the colors and the rectangle's alpha value and see
			how the objects respond.
    </div>
${head.next('move.html')}

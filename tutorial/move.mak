<%namespace name="head" file="head.mak" />
${head.head(340)}
	<div id="explain">
	   <div id="codebox">
		   <textarea id="code" rows=10 cols=50>var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;

function init() {
    ctx = $('#canvas')[0].getContext("2d");
    return setInterval(draw, 10);
}

function draw() {
    ctx.clearRect(0,0,300,300);
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI*2, true); 
    ctx.closePath();
    ctx.fill();
    x += dx;
    y += dy;
}

init();</textarea>
		</div>
		<input type="submit" value="run code" onclick="runCode()"/><br>
		<p>
		Words!
	</div>

${head.next('square.html')}

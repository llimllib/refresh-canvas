<%namespace name="head" file="head.mak" />
${head.head(400)}
	<div id="explain">
	   <div id="codebox">
		   <textarea id="code" rows=10 cols=50>var x = 150;
var y = 150;
var dx = 0;
var dy = 0;
var intervalID = 0;
var ctx;

function init() {
    ctx = $('#canvas')[0].getContext("2d");
    dx = 2; 
    dy = 5;
    x = 150;
    y = 150;
    draw();
}

function startdraw() {
    init();
    clearInterval(intervalID);
    intervalID = setInterval(draw, 10);
}

function abort() {
    clearInterval(intervalID);
    ctx.clearRect(0,0,300,300);
    init();
}

function draw() {
    ctx.clearRect(0,0,300,300);
    ctx.beginPath();
    ctx.arc(x,y,10,0,Math.PI*2,true); 
    ctx.closePath();
    ctx.fill();
    x += dx;
    y += dy;
}

startdraw();</textarea>
		</div>
		<input type="submit" value="run code" onclick="runCode()"/><br>
		<p>
		Words!
	</div>

${head.next('square.html')}

<%namespace name="head" file="head.mak" />
${head.head(340)}
	<div id="explain">Our ball can fly! But it runs away too quickly; let's
	contain it in our box by rebounding off the walls.
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
 
  if (x + dx > $('#canvas').width() || x + dx < 0)
    dx = .5 * -dx;
  if (y + dy > $('#canvas').height() || y + dy < 0)
    dy = -dy;
 
  x += dx;
  y += dy;
}

init();</textarea>
		</div>
		<input type="submit" value="run code" onclick="runCode()"/><br>
		<p>
        Try to change the draw() function so that the ball accelerates or decelerates
        every time it hits a wall.
	</div>

${head.next('bounce.html')}

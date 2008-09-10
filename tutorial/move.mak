<%namespace name="head" file="head.mak" />
${head.head(340)}
	<div id="explain">Now that we've got a ball, let's make it move.
	   In order to do so, we'll create a <code>draw()</code> function
	   which wipes the screen, draws the ball, then updates its current
	   position. We'll use a call to 
	   <code>setInterval(function, timeout)</code> in the <code>init()</code>
	   function to tell the browser to run our draw function every 10
	   milliseconds, creating the illusion of movement.
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
        Try changing the dx and dy values to change the direction of the ball,
        or change the x and y variables to change where the ball will start.
		Make sure to try negative values for dx and dy.
	</div>

${head.next('library.html')}

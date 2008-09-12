<%namespace name="head" file="head.mak" />
${head.head(390)}
	<div id="explain">Now we can start to think about making our game
  a bit like an actual game. Let's add a paddle, and only allow the
  ball to bounce off the bottom when it hits it.
  <div id="codebox">
       <textarea id="code" rows=10 cols=50>paddlex = WIDTH / 2;
paddleh = 10;
paddlew = 75;

function draw() {
  clear();
  circle(x, y, 10);
  rect(paddlex, HEIGHT-paddleh, paddlew, paddleh);
 
  if (x + dx > WIDTH || x + dx < 0)
	  dx = -dx;

  if (y + dy < 0)
	  dy = -dy;
  else if (y + dy > HEIGHT) {
    if (x > paddlex && x < paddlex + paddlew)
      dy = -dy;
    else
      clearInterval(intervalId);
  }
 
  x += dx;
  y += dy;
}

init();</textarea>
		</div>
		<input type="submit" value="run code" onclick="runCode()"/><br>
		<p>
    You probably want to be able to move the paddle - we'll cover that in
    the next page.
    <p>
    The constants paddlex, paddleh, and paddlew will be hidden in the library
    from now on.
	</div>

	   <textarea id="library" style="display: none">
var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH = $("canvas").width()
var HEIGHT = $("canvas").height()
var intervalId = 0;

function circle(x,y,r) {
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI*2, true);
  ctx.closePath();
  ctx.fill();
}

function rect(x,y,w,h) {
  ctx.beginPath();
  ctx.rect(x,y,w,h);
  ctx.closePath();
  ctx.fill();
}

function clear() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
}

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  intervalId = setInterval(draw, 10);
	return intervalId;
}
       </textarea>
${head.next('keyboard.html')}

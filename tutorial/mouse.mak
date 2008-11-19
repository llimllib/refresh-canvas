<%namespace name="head" file="head.mak" />
${head.head(570)}
	<div id="explain">Adding mouse support to our game is even simpler;
    all we have to do is send the mousemove event to an onMouseMove
    function, see if the mouse is within the borders of the game,
    and move the paddle if it is.
    <div id="codebox">
       <textarea id="code" rows=10 cols=50>var canvasMinX = $("#canvas").offset().left;
var canvasMaxX = canvasMinX + $("#canvas").width();

function onMouseMove(evt) {
  if (evt.pageX &gt; canvasMinX
   &amp;&amp; evt.pageX &lt; canvasMaxX) {
    paddlex = evt.pageX - canvasMinX;
  }
}

$(document).mousemove(onMouseMove);
	   
function draw() {
  clear();
  circle(x, y, 10);

  if (rightDown) paddlex += 5;
  else if (leftDown) paddlex -= 5;
  rect(paddlex, HEIGHT-paddleh, paddlew, paddleh);
 
  if (x + dx &gt; WIDTH || x + dx &lt; 0)
	  dx = -dx;

  if (y + dy &lt; 0)
    dy = -dy;
  else if (y + dy &gt; HEIGHT) {
    if (x &gt; paddlex &amp;&amp; x &lt; paddlex + paddlew)
      dy = -dy;
    else
      clearInterval(intervalId);
  }
 
  x += dx;
  y += dy;
}

init();</textarea>
		</div>
    <p>Try changing the draw function so that the middle of the paddle is
		located directly above the mouse pointer instead of the left side.
		<p>Now that the keyboard and mouse work, all that's left to do is put in
    the bricks and add some design and code polish. As usual, we'll stuff all
    the code not in the draw() function into the library on all future pages.
	</div>

<div id="libraryContainer">
<textarea id="library" style="display: none">var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH = $("canvas").width()
var HEIGHT = $("canvas").height()
var paddlex = WIDTH / 2;
var paddleh = 10;
var paddlew = 75;
var rightDown = false;
var leftDown = false;
var canvasMinX = 0;
var canvasMaxX = 0;
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

function onKeyDown(evt) {
  if (evt.keyCode == 39) rightDown = true;
  else if (evt.keyCode == 37) leftDown = true;
}

function onKeyUp(evt) {
  if (evt.keyCode == 39) rightDown = false;
  else if (evt.keyCode == 37) leftDown = false;
}

$(document).keydown(onKeyDown);
$(document).keyup(onKeyUp);

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + $("#canvas").width();
  intervalId = setInterval(draw, 10);
  return intervalId;
}
       </textarea></div>

${head.link('keyboard', 'bricks')}

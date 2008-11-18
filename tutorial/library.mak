<%namespace name="head" file="head.mak" />
${head.head(660)}
     <textarea id="library" style="display: none">
       </textarea>
  <div id="explain">Now that we're getting somewhere, our code's getting a bit
	too big for a single screen, so we'll start sticking some of it into a library
	of functions to make our lives easier. In future pages, expect the library code
	to be sitting hidden on the page so that we can focus on our draw() function.
	<p>Simply hit the "show library" button to review it at any time.
  <div id="codebox">
       <textarea id="code" rows=10 cols=50>//BEGIN LIBRARY CODE
var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH = $("canvas").width()
var HEIGHT = $("canvas").height()

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  return setInterval(draw, 10);
}

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

//END LIBRARY CODE

function draw() {
  clear();
  circle(x, y, 10);
 
  x += dx;
  y += dy;
}

init();</textarea>
		</div>
		<p>
		See how much simpler the draw() function is now? Functionally,
    everything should still work the same.
	</div>

${head.next('bounce.html')}

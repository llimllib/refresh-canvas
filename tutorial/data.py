[{"name": "index",
"title": "Introduction",
"explain_before": """Welcome! In this tutorial, we're going to create a breakout
clone that you can play in your browser, using javascript and the &lt;canvas&gt; element.
<p>In order to use this tutorial, you'll need to have a relatively recent version
of <a href="http://mozilla.com/firefox">Firefox</a>, <a
href="http://apple.com/safari">Safari</a>, or <a href="http://opera.com">Opera</a>.
You cannot use Internet Explorer, because Microsoft hss decided not to implement the
&lt;canvas&gt; element in it.
<p>Before you read any further, click on the "run code" button on the left to
play the game that we'll end up creating.
<p>On every page, you'll be able to click the "run code" button to run the code
we've developed so far. Every page besides this one has an editor in it containing
the javascript code that will be run in the same box as the game as soon as you
click the button. You can make changes to the code, and see the results
instantly by clicking the "run code" button.
<p>In order to make our lives easier, I've included the <a
href="http://jquery.com">jQuery</a> framework in every page, which extends
javascript in your browser with some useful methods.
<p>If you have any comments or questions, feel free to leave a comment on the
"comments" tab.
""",
"hidden_code": """var x = 25;
var y = 250;
var dx = 1.5;
var dy = -4;
var ctx;
var WIDTH;
var HEIGHT;
var paddlex;
var paddleh = 10;
var paddlew = 75;
var rightDown = false;
var leftDown = false;
var canvasMinX = 0;
var canvasMaxX = 0;
var intervalId = 0;
var bricks;
var NROWS = 5;
var NCOLS = 5;
var BRICKWIDTH;
var BRICKHEIGHT = 15;
var PADDING = 1;

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  WIDTH = $("#canvas").width();
  HEIGHT = $("#canvas").height();
  BRICKWIDTH = (WIDTH/NCOLS) - 1;
  paddlex = WIDTH / 2;
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + WIDTH;
  intervalId = setInterval(draw, 10);
  return intervalId;
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
  rect(0,0,WIDTH,HEIGHT);
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

function onMouseMove(evt) {
  if (evt.pageX &gt; canvasMinX &amp;&amp; evt.pageX &lt; canvasMaxX) {
    paddlex = Math.max(evt.pageX - canvasMinX - (paddlew/2), 0);
    paddlex = Math.min(WIDTH - paddlew, paddlex);
  }
}

$(document).mousemove(onMouseMove);

function initbricks() {
    bricks = new Array(NROWS);
    for (i=0; i &lt; NROWS; i++) {
        bricks[i] = new Array(NCOLS);
        for (j=0; j &lt; NCOLS; j++) {
            bricks[i][j] = 1;
        }
    }
}

function drawbricks() {
  for (i=0; i &lt; NROWS; i++) {
    ctx.fillStyle = rowcolors[i];
    for (j=0; j &lt; NCOLS; j++) {
      if (bricks[i][j] == 1) {
        rect((j * (BRICKWIDTH + PADDING)) + PADDING, 
             (i * (BRICKHEIGHT + PADDING)) + PADDING,
             BRICKWIDTH, BRICKHEIGHT);
      }
    }
  }
}

var ballr = 10;
var rowcolors = ["#FF1C0A", "#FFFD0A", "#00A308", "#0008DB", "#EB0093"];
var paddlecolor = "#FFFFFF";
var ballcolor = "#FFFFFF";
var backcolor = "#000000";

function draw() {
  ctx.fillStyle = backcolor;
  clear();
  ctx.fillStyle = ballcolor;
  circle(x, y, ballr);

  if (rightDown) paddlex += 5;
  else if (leftDown) paddlex -= 5;
  ctx.fillStyle = paddlecolor;
  rect(paddlex, HEIGHT-paddleh, paddlew, paddleh);

  drawbricks();

  //want to learn about real collision detection? go read
  // http://www.harveycartel.org/metanet/tutorials/tutorialA.html
  rowheight = BRICKHEIGHT + PADDING;
  colwidth = BRICKWIDTH + PADDING;
  row = Math.floor(y/rowheight);
  col = Math.floor(x/colwidth);
  //reverse the ball and mark the brick as broken
  if (y &lt; NROWS * rowheight &amp;&amp; row &gt;= 0 &amp;&amp; col &gt;= 0 &amp;&amp; bricks[row][col] == 1) {
    dy = -dy;
    bricks[row][col] = 0;
  }
 
  if (x + dx + ballr &gt; WIDTH || x + dx - ballr &lt; 0)
    dx = -dx;

  if (y + dy - ballr &lt; 0)
    dy = -dy;
  else if (y + dy + ballr &gt; HEIGHT - paddleh) {
    if (x &gt; paddlex &amp;&amp; x &lt; paddlex + paddlew) {
      //move the ball differently based on where it hit the paddle
      dx = 8 * ((x-(paddlex+paddlew/2))/paddlew);
      dy = -dy;
    }
    else if (y + dy + ballr &gt; HEIGHT)
      clearInterval(intervalId);
  }
 
  x += dx;
  y += dy;
}

init();
initbricks();"""
},
 {"name": "ball",
"title": "Draw a Circle",
"explain_before": """The first thing we need to do is create an instance of the &lt;canvas&gt; element so that
   we can start to draw on it. If you look in the source for this page, you'll see a 
   declaration that looks like this:<br />
   <pre>&lt;canvas id="canvas" width="300" height="300"&gt;&lt;/canvas&gt;</pre>
   This declaration creates the canvas on which we'll draw in the rest of the tutorial.
   <p>Now that we've got a canvas to draw on, let's do so:""",
"code": """//get a reference to the canvas
var ctx = $('#canvas')[0].getContext("2d");

//draw a circle
ctx.beginPath();
ctx.arc(75, 75, 10, 0, Math.PI*2, true); 
ctx.closePath();
ctx.fill();""",
"explain_after": """You may want to comment out the <code>arc(...)</code> call and try
    <code>ctx.rect(x, y, width, height)</code>.
    <p>Make sure you keep the arc and rect calls in between calls to
    <code>beginPath()</code> and <code>closePath()</code> just like the
    sample call above. You may also try substituting <code>stroke()</code>
    for <code>fill()</code>."""
},
{"name": "color",
"title": "Add Some Color",
"explain_before": """We can also turn our ball different colors. Changing the value of
  ctx.fillStyle will change the canvas' current color; we can set its value to a hex
  string of the format <code>'#rrggbb'</code> or to a string 
  <code>'rgba(r, g, b, a)'</code> where a is a value
  between 0 and 1 representing the transparency of the color.
""",
"code": """var ctx = $('#canvas')[0].getContext("2d");

ctx.fillStyle = "#00A308";
ctx.beginPath();
ctx.arc(220, 220, 50, 0, Math.PI*2, true);
ctx.closePath();
ctx.fill();

ctx.fillStyle = "#FF1C0A";
ctx.beginPath();
ctx.arc(100, 100, 100, 0, Math.PI*2, true);
ctx.closePath();
ctx.fill();

//the rectangle is half transparent
ctx.fillStyle = "rgba(255, 255, 0, .5)"
ctx.beginPath();
ctx.rect(15, 150, 120, 120);
ctx.closePath();
ctx.fill();""",
"explain_after": """Play around a bit with the colors and the rectangle's alpha value and see
    how the objects respond.
"""
},
{"name": "move",
"title": "Action",
"explain_before": """We've already made a <a href="ball.html">ball</a>,
       now let's make it move.
     In order to do so, we'll create a <code>draw()</code> function
     which wipes the screen, draws the ball, then updates its current
     position. We'll use a call to 
     <code>setInterval(function, timeout)</code> in the <code>init()</code>
     function to tell the browser to run our draw function every 10
     milliseconds, creating the illusion of movement.""",
"code": """var x = 150;
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

init();""",
"explain_after": """Try changing the dx and dy values to change the direction of the ball,
        or change the x and y variables to change where the ball will start.
    Make sure to try negative values for dx and dy.
"""
},
{"name": "library",
"title": "Library: an Interlude",
"explain_before": """Now that we're getting somewhere, our code's getting a bit
  too big for a single screen, so we'll start sticking some of it into a library
  of functions to make our lives easier. In future pages, expect the library code
  to be sitting hidden on the page so that we can focus on our draw() function.
  <p>Just click on the library tab to review it at any time.""",
"code": """//BEGIN LIBRARY CODE
var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var WIDTH;
var HEIGHT;
var ctx;

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  WIDTH = $("#canvas").width();
  HEIGHT = $("#canvas").height();
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

init();
""",
"explain_after": """See how much simpler the draw() function is now?
<p>If you edit the library, the changes will be reflected when you hit
"run code", just like they are with the code box right now.""",
"library": "//Nothing here just yet! Check back on the next page."
},
{"name": "bounce",
"title": "Bounce",
"explain_before": """Our ball can fly, but it runs away too quickly; let's
  contain it in our box by rebounding off the walls.""",
"code": """function draw() {
  clear();
  circle(x, y, 10);
 
  if (x + dx &gt; WIDTH || x + dx &lt; 0)
    dx = -dx;
  if (y + dy &gt; HEIGHT || y + dy &lt; 0)
    dy = -dy;
 
  x += dx;
  y += dy;
}

init();""",
"explain_after": """Try to change the draw() function so that the ball accelerates or decelerates
        every time it hits a wall.""",
"library": """var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH; 
var HEIGHT;

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
  WIDTH = $("#canvas").width()
  HEIGHT = $("#canvas").height()
  return setInterval(draw, 10);
}"""
},
{"name": "paddle",
"title": "Add a Paddle",
"explain_before": """Now we can start to think about making our game
  a bit like an actual game. Let's add a paddle, and only allow the
  ball to bounce off the bottom when it hits it.""",
"code": """var paddlex;
var paddleh;
var paddlew;

function init_paddle() {
  paddlex = WIDTH / 2;
  paddleh = 10;
  paddlew = 75;
}

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
      //game over, so stop the animation
      clearInterval(intervalId);
  }
 
  x += dx;
  y += dy;
}

init();
init_paddle();""",
"explain_after": """You probably want to be able to move the paddle - we'll cover that in
    the next page.
    <p>
    The constants paddlex, paddleh, and paddlew will be moved to the regular init()
    function from now on.""",
"library": """var x = 140;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH;
var HEIGHT;
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
  WIDTH = $("#canvas").width()
  HEIGHT = $("#canvas").height()
  intervalId = setInterval(draw, 10);
  return intervalId;
}"""
},
{"name": "keyboard",
"title": "The Keyboard",
"explain_before": """To add keyboard input to control our paddle, we need
  to do two things: find out when the left and right arrows have been
  pressed and move the paddle when they have.
  <p>In order to receive key events, we'll create one function called
  onKeyUp and another called onKeyDown, then use a bit of jQuery magic
  to bind them to the appropriate events.
  <p>Then, on our way through the draw function, we'll check to see if
  either arrow is pressed down, and move the paddle accordingly.
""",
"code": """rightDown = false;
leftDown = false;

//set rightDown or leftDown if the right or left keys are down
function onKeyDown(evt) {
  if (evt.keyCode == 39) rightDown = true;
  else if (evt.keyCode == 37) leftDown = true;
}

//and unset them when the right or left key is released
function onKeyUp(evt) {
  if (evt.keyCode == 39) rightDown = false;
  else if (evt.keyCode == 37) leftDown = false;
}

$(document).keydown(onKeyDown);
$(document).keyup(onKeyUp);
       
function draw() {
  clear();
  circle(x, y, 10);

  //move the paddle if left or right is currently pressed
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

init();""",
"explain_after": """Now that we've got a working paddle, animation, and a bouncing ball,
        we've got something close to a game coming together.
    <p>On the next page, we'll move support for the keyboard into the
    library and add support for the mouse in a very similar manner.""",
"library": """var x = 150;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH;
var HEIGHT;
var paddlex;
var paddleh = 10;
var paddlew = 75;
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
  WIDTH = $("#canvas").width()
  HEIGHT = $("#canvas").height()
  paddlex = WIDTH / 2;
  intervalId = setInterval(draw, 10);
  return intervalId;
}"""
},
{"name": "mouse",
"title": "The Mouse",
"explain_before": """Adding mouse support to our game is even simpler;
    all we have to do is send the mousemove event to an onMouseMove
    function, see if the mouse is within the borders of the game,
    and move the paddle if it is.""",
"code": """var canvasMinX;
var canvasMaxX;

function init_mouse() {
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + WIDTH;
}

function onMouseMove(evt) {
  if (evt.pageX &gt; canvasMinX &amp;&amp; evt.pageX &lt; canvasMaxX) {
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

init();
init_mouse();""",
"explain_after": """Try changing the draw function so that the middle of the paddle is
    located directly above the mouse pointer instead of the left side.
    <p>Now that the keyboard and mouse work, all that's left to do is put in
    the bricks and add some design and code polish. As usual, we'll stuff all
    the code not in the draw() function into the library on all future pages.
""",
"library": """var x = 130;
var y = 150;
var dx = 2;
var dy = 4;
var ctx;
var WIDTH;
var HEIGHT;
var paddlex;
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
  WIDTH = $("#canvas").width()
  HEIGHT = $("#canvas").height()
  paddlex = WIDTH / 2;
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + WIDTH;
  intervalId = setInterval(draw, 10);
  return intervalId;
}"""
},
{"name": "bricks",
"title": "The Bricks",
"explain_before": """Now we'll create a <a
  href="http://www.webreference.com/programming/javascript/diaries/12/">2-dimensional
  array</a> to hold bricks, use a couple loops to draw the ones that haven't
  been broken, and make sure to remove bricks when they've been hit.

""",
"code": """var bricks;
var NROWS;
var NCOLS;
var BRICKWIDTH;
var BRICKHEIGHT;
var PADDING;

function initbricks() {
  NROWS = 5;
  NCOLS = 5;
  BRICKWIDTH = (WIDTH/NCOLS) - 1;
  BRICKHEIGHT = 15;
  PADDING = 1;

  bricks = new Array(NROWS);
  for (i=0; i &lt; NROWS; i++) {
    bricks[i] = new Array(NCOLS);
    for (j=0; j &lt; NCOLS; j++) {
      bricks[i][j] = 1;
    }
  }
}
       
function draw() {
  clear();
  circle(x, y, 10);

  if (rightDown) paddlex += 5;
  else if (leftDown) paddlex -= 5;
  rect(paddlex, HEIGHT-paddleh, paddlew, paddleh);

  //draw bricks
  for (i=0; i &lt; NROWS; i++) {
    for (j=0; j &lt; NCOLS; j++) {
      if (bricks[i][j] == 1) {
        rect((j * (BRICKWIDTH + PADDING)) + PADDING, 
             (i * (BRICKHEIGHT + PADDING)) + PADDING,
             BRICKWIDTH, BRICKHEIGHT);
      }
    }
  }

  //have we hit a brick?
  rowheight = BRICKHEIGHT + PADDING;
  colwidth = BRICKWIDTH + PADDING;
  row = Math.floor(y/rowheight);
  col = Math.floor(x/colwidth);
  //if so, reverse the ball and mark the brick as broken
  if (y &lt; NROWS * rowheight &amp;&amp; row &gt;= 0 &amp;&amp; col &gt;= 0 &amp;&amp; bricks[row][col] == 1) {
    dy = -dy;
    bricks[row][col] = 0;
  }
 
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

init();
initbricks();""",
"explain_after": """Try adding code to make the ball bounce in different directions
    based on where it hits the paddle.
    <p>It seems at every step as if what we have is getting closer to
    being a real game, but that it's never quite there. One thing that's
    for sure is that this version of the game is ugly; on the next page
    we'll jazz it up a bit.""",
"library": """var x = 25;
var y = 250;
var dx = 1.5;
var dy = -4;
var ctx;
var WIDTH;
var HEIGHT;
var paddlex;
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

function onMouseMove(evt) {
  if (evt.pageX &gt; canvasMinX &amp;&amp; evt.pageX &lt; canvasMaxX) {
    paddlex = evt.pageX - canvasMinX - (paddlew/2);
  }
}

$(document).mousemove(onMouseMove);

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  WIDTH = $("#canvas").width()
  HEIGHT = $("#canvas").height()
  paddlex = WIDTH / 2;
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + WIDTH;
  intervalId = setInterval(draw, 10);
  return intervalId;
}"""
},
{"name": "finish",
"title": "Finishing Touches",
"explain_before": """Now we'll add a few finishing touches to our game,
like colors, and a more fun paddle collision equation. There's an
infinite amount of improvements you could make, so go ahead and try them
out.""",
"code": """var ballr = 10;
var rowcolors = ["#FF1C0A", "#FFFD0A", "#00A308", "#0008DB", "#EB0093"];
var paddlecolor = "#FFFFFF";
var ballcolor = "#FFFFFF";
var backcolor = "#000000";

function draw() {
  ctx.fillStyle = backcolor;
  clear();
  ctx.fillStyle = ballcolor;
  circle(x, y, ballr);

  if (rightDown) paddlex += 5;
  else if (leftDown) paddlex -= 5;
  ctx.fillStyle = paddlecolor;
  rect(paddlex, HEIGHT-paddleh, paddlew, paddleh);

  drawbricks();

  //want to learn about real collision detection? go read
  // http://www.harveycartel.org/metanet/tutorials/tutorialA.html
  rowheight = BRICKHEIGHT + PADDING;
  colwidth = BRICKWIDTH + PADDING;
  row = Math.floor(y/rowheight);
  col = Math.floor(x/colwidth);
  //reverse the ball and mark the brick as broken
  if (y &lt; NROWS * rowheight &amp;&amp; row &gt;= 0 &amp;&amp; col &gt;= 0 &amp;&amp; bricks[row][col] == 1) {
    dy = -dy;
    bricks[row][col] = 0;
  }
 
  if (x + dx + ballr &gt; WIDTH || x + dx - ballr &lt; 0)
    dx = -dx;

  if (y + dy - ballr &lt; 0)
    dy = -dy;
  else if (y + dy + ballr &gt; HEIGHT - paddleh) {
    if (x &gt; paddlex &amp;&amp; x &lt; paddlex + paddlew) {
      //move the ball differently based on where it hit the paddle
      dx = 8 * ((x-(paddlex+paddlew/2))/paddlew);
      dy = -dy;
    }
    else if (y + dy + ballr &gt; HEIGHT)
      clearInterval(intervalId);
  }
 
  x += dx;
  y += dy;
}

init();
initbricks();""",
"explain_after": """""",
"library": """var x = 25;
var y = 250;
var dx = 1.5;
var dy = -4;
var ctx;
var WIDTH;
var HEIGHT;
var paddlex;
var paddleh = 10;
var paddlew = 75;
var rightDown = false;
var leftDown = false;
var canvasMinX = 0;
var canvasMaxX = 0;
var intervalId = 0;
var bricks;
var NROWS = 5;
var NCOLS = 5;
var BRICKWIDTH;
var BRICKHEIGHT = 15;
var PADDING = 1;

function init() {
  ctx = $('#canvas')[0].getContext("2d");
  WIDTH = $("#canvas").width();
  HEIGHT = $("#canvas").height();
  paddlex = WIDTH / 2;
  BRICKWIDTH = (WIDTH/NCOLS) - 1;
  canvasMinX = $("#canvas").offset().left;
  canvasMaxX = canvasMinX + WIDTH;
  intervalId = setInterval(draw, 10);
  return intervalId;
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
  rect(0,0,WIDTH,HEIGHT);
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

function onMouseMove(evt) {
  if (evt.pageX &gt; canvasMinX &amp;&amp; evt.pageX &lt; canvasMaxX) {
    paddlex = Math.max(evt.pageX - canvasMinX - (paddlew/2), 0);
    paddlex = Math.min(WIDTH - paddlew, paddlex);
  }
}

$(document).mousemove(onMouseMove);

function initbricks() {
    bricks = new Array(NROWS);
    for (i=0; i &lt; NROWS; i++) {
        bricks[i] = new Array(NCOLS);
        for (j=0; j &lt; NCOLS; j++) {
            bricks[i][j] = 1;
        }
    }
}

function drawbricks() {
  for (i=0; i &lt; NROWS; i++) {
    ctx.fillStyle = rowcolors[i];
    for (j=0; j &lt; NCOLS; j++) {
      if (bricks[i][j] == 1) {
        rect((j * (BRICKWIDTH + PADDING)) + PADDING, 
             (i * (BRICKHEIGHT + PADDING)) + PADDING,
             BRICKWIDTH, BRICKHEIGHT);
      }
    }
  }
}
"""
},
{"name":"coda",
"title":"Coda",
"explain_before": """That's it, Thanks for reading this far! The code presented
here is cribbed mostly from a <a
href="http://billmill.org/static/refresh-canvas/presentation/index-osf.html">presentation</a>
I gave to <a href="http://refreshbmore.org/">Refresh Baltimore</a> in August, 2008.

Some resources you may find helpful if you study canvas more:
<ul><li>Mozilla's <a href="https://developer.mozilla.org/en/Drawing_Graphics_with_Canvas">
canvas tutorial</a> is excellent, and much more comprehensive than this one.
<li><a href="http://www.whatwg.org/specs/web-apps/current-work/multipage/the-canvas-element.html#the-canvas-element">The
Spec</a>. Since it's currently in development, these features may or may not be
available in current browsers.
<li><a href="http://getfirebug.com/">Firebug</a> is an essential tool for any javascript
developer.
</ul>

<p>Innumerable thanks to <a 
href="http://marijn.haverbeke.nl/codemirror/">codemirror</a> for the awesome 
text editor in use all over this tutorial, and to <a 
href="http://jquery.com/">jQuery</a> and <a href="http://ui.jquery.com/">jQuery 
UI</a> for making my life much easier.

<p>You can find the code used to generate this tutorial (using the excellent <a
href="http://www.makotemplates.org/">mako</a> template library) on <a
href="http://github.com/llimllib/refresh-canvas/tree/master/tutorial">github</a>.

<p>Feel free to <a href="mailto:bill.mill@gmail.com">drop me a line</a> if you have
any comments or questions, or <a href="http://billmill.org">visit my blog</a>."""
}
]

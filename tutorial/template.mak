<%namespace name="head" file="head.mak" />
${head.head()}

   <div id="explain">What we're going to do in this tutorial is use the new 
   &lt;canvas&gt; element to create a simplified clone of the old Atari game
   <a href="http://billmill.org/static/refresh-canvas/presentation/pix/breakout_cover.jpg">Breakout</a>.
   The first thing we need to do is create an instance of the &lt;canvas&gt; element so that
   we can start to draw on it. If you look in the source for this page, you'll see a 
   declaration that looks like this:<br />
   <pre>&lt;canvas id="canvas" width="300" height="300"&gt;&lt;/canvas&gt;</pre>
   This declaration creates the canvas on which we'll draw in the rest of the tutorial.</div>

${head.link(None, "ball")}

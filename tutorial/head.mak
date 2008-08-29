<%def name="head(script='')">
<html>
 <head>
  <style type="text/css">
#canvas { border: 1px solid;
		  width:        300px;
		  height:       300px;
		  float:        left;
		  margin-right: 15px;
}
div#explain { font:  14px;
              width: 800px;
}
a#next { /*TODO get right aligned*/ }
  </style>
  <title>Canvas Tutorial</title>
  <script type="application/x-javascript">
${script}
  </script>
 </head>
 <body>
</%def>

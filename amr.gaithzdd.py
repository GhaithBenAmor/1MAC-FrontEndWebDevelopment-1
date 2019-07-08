import webbrowser
#====================================================1MAC - UDACITY =======================================================

#=========================================== A workshop done by amr.gaithzdd ==============================================

#===================================================== html_file ==========================================================

html_file = open("amr.gaithzdd.html","w+")

html = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    	<title>Ghaith Ben Amor</title>
	<link rel="stylesheet" type="text/css" href="qq.css">
	<link href="https://fonts.googleapis.com/css?family=DM+Serif+Display&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Acme|Lobster|Overpass|Righteous|Roboto+Condensed&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link href="https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
  </head>
  <body>
  	<header>
		<div class="title">
			<h1>Full-Stack Web Developement</h1>
			<h4 class="sponsors">Udacity - One Million Arab Coders</h4> 
 		</div>
 		
 		<div class="button">
 			<button type="button" class="btn btn-primary"><a href="https://www.udacity.com" class="link" target="_blank">Udacity</a></button>
			<button type="button" class="btn btn-secondary"><a href="http://www.arabcoders.ae" class="link" target="_blank">Arab Coders</a></button>
			<button type="button" class="btn btn-warning"><a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fghaith-ben-amor-6a8003108%3Ffbclid%3DIwAR0E5BjNNQ5DPXhb906ESAaUaotg1F-LkVC253WHL6YS914cWRttKhorhBs&h=AT3hN_06w7TsCfr79onEbXDv-PYoehNbAi6zea5Z1QyMGjNZ6uupyFevdX2xYvl6JmJ41y61ljJYO-EMYR2PTamYenbyOjOD20efy6hsoY8hZWIaqwNkwxuJrZrjFODnIm-_" class="link" target="_blank">My Linkedin</a></button>
			<button type="button" class="btn btn-success">amr.gaithzdd</button>
			<button type="button" class="btn btn-danger"><a href="https://www.facebook.com/gaith.amr.18"></a>My Facebook</button>
			<button type="button" class="btn btn-info">Info</button>
			
		</div>
	</header>
	<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
		  <ol class="carousel-indicators">
		    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
		    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
		    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
		  </ol>
		  <div class="carousel-inner">
		    <div class="carousel-item active">
		      <img src="images/3.png" class="d-block w-100" alt="...">
		    </div>
		    <div class="carousel-item">
		      <img src="images/2.jpg" class="d-block w-100" alt="...">
		    </div>
		    <div class="carousel-item">
		      <img src="images/1.jpg" class="d-block w-100" alt="...">
		    </div>
		  </div>
		  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
		    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
		    <span class="sr-only">Previous</span>
		  </a>
		  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
		    <span class="carousel-control-next-icon" aria-hidden="true"></span>
		    <span class="sr-only">Next</span>
		  </a>
	</div>
	<div id="container">
		<div class="client">
			<h3>Front-End : Client Side</h3>
			<div class="box">
				<div><img src="images/html.png" class="html"></div>
				<iframe id="ytplayer" type="text/html" width="390" height="200"
  				src="https://www.youtube.com/embed/IsXEVQRaTX8"
 				frameborder="0"></iframe>
			</div>
			
			<div class="box">
				<div><img src="images/css.png" class="css"></div>
			    <iframe id="ytplayer" type="text/html" width="390" height="200"
  				src="https://www.youtube.com/embed/6d_4sd_l7rQ"
 				frameborder="0">		
 			    </iframe>
 			</div>
 			<div class="box">
				<div><img src="images/js.png" class="js"></div>
				<iframe id="ytplayer" type="text/html" width="390" height="200"
  				src="https://www.youtube.com/embed/upDLs1sn7g4"
 				frameborder="0">
 				</iframe>
 			</div>


		</div>
		<div class="serveur">
			<h3>Back-End  : Serveur Side</h3>
			<i class="fas fa-server" style="color:white;font-size: 20px"></i>
			<div class="box">
				<div><img src="images/11.png" class="nodejs"></div>
				<iframe id="ytplayer" type="text/html" width="390" height="200"
  				src="https://www.youtube.com/embed/uVwtVBpw7RQ"
 				frameborder="0"></iframe>
			</div>
			
			<div class="box">
				<div><img src="images/22.jpg" class="postgresql"></div>
			    <iframe id="ytplayer" type="text/html" width="390" height="200"
  				src="https://www.youtube.com/embed/GI3eO14Fy90"
 				frameborder="0">		
 			    </iframe>
 			</div>
 			<div class="box">
				<div><img src="images/33.png" class="monogodb"></div>
				<iframe id="ytplayer" type="text/html" width="390" height="200"
  				src="https://www.youtube.com/embed/CvIr-2lMLsk"
 				frameborder="0">
 				</iframe>
 			</div>

		</div>
	</div>
    <footer>
    	<p>&copy; 2019 amr.gaithzdd (Ghaith Ben Amor) http://www.arabcoders.ae/ <p>
    </footer>


"""

html +="""
 </body>
</html>"""

html +="""
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
"""

html_file.write(html)
html_file.close()
#================================= css_file ======================================

css_file = open('amr.gaithzdd.css','w+')
css = """
header{
	background-image: url(images/image.jpg);
	background-repeat: no-repeat;
	background-size: cover;
    border-bottom: 8px solid black;
}
.link:hover{
	color: white;
}
.btn btn-primary{
	padding:0px 100px 0px 100px;
}
.sponsors{
	font-family: 'Montserrat', sans-serif;
}

.title{

	padding: 50px;
	text-align: center;
	font-size: 50px;
    font-family: 'DM Serif Display', serif;
}
.button{
	text-align: center;
	padding-top: -10px;
	padding-bottom: 10px;
}
.link{
	color: white;
}
.client{
	background-image: url(images/front.jpg);
	background-size: cover;
	padding: 15px;
	width: 683px;
	border-right: 8px solid #A9A9A9;

}
.client h3{
	font-size: 30px;
    font-family: 'Overpass', sans-serif;
    font-weight: bold;
}
.serveur{
	background-image: url(images/back.jpg);
	background-size: cover;
	padding: 15px;
	width: 683px;
	padding-bottom: 300px;
}
.serveur h3{
	font-size: 30px;
	color: white;
    font-family: 'Overpass', sans-serif;
    font-weight: bold;
}
.html{
	width: 80px;
	height: 80px;
	margin-top: 50px;
	margin-right: 10px;
}
.css{
	width: 60px;
	height: 80px;
	margin-top: 50px;
	margin-left: 10px;
	margin-right: 10px;
	margin-right: 20px;
}
.js{
	width: 60px;
	height: 60px;
	margin-top: 50px;
	margin-left: 10px;
	margin-right: 10px;
    margin-right: 20px;
}
.nodejs{
	width: 140px;
	height: 50px;
	margin-top: 50px;
	margin-right: 20px;
}
.postgresql{
	width: 90px;
	height: 100px;
	margin-top: 50px;
	margin-left: 20px;
	margin-right: 50px;
}
.monogodb{
	width: 90px;
	height: 70px;
	margin-top: 50px;
	margin-left: 20px;
	margin-right: 50px;

}
.box{
	display: flex;
}
footer p{
	background-color: black;
	text-align: center;
	color: white;
	margin: 0px;
	padding:5px;
	padding-top: 10px;
	font-family: 'Roboto Mono', monospace;

}
#container{
	display: flex;
	height: 800px;
	border-bottom: 5px solid #A9A9A9;
}
#ytplayer{
	margin-top: 5px;
}
#carouselExampleIndicators{
	border-bottom: 8px solid #A9A9A9;
}
"""
css_file.write(css)
css_file.close()
#===========================open in the browser=================================
webbrowser.open_new_tab('amr.gaithzdd.html')

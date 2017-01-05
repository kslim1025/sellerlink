
<?php get_header(); ?>

{% block title %}Vacation Rental Marketplace | {{ super() }}{% endblock %}

<style>
.jumbotron { min-height:300px; }
.media-boxes { min-height:250px; }

ul.carousel-selectors {
list-style:none;
margin:0; padding:0;
}
ul.carousel-selectors li { border-bottom:2px solid #071a71; display:block; height:55px; vertical-align:middle; margin:0; padding-top:30px; }
ul.carousel-selectors li.last { border-bottom:none; }

.carousel { background-color:#7484d9;
            color:white; padding:5px; border:2px solid #071a71;
          }

div.carousel-selectors {
	border:2px solid #071a71;border-left:none; 
	background-color:#7484d9; color:white; 
	height:364px; 
	padding:0; margin-left:0px
}

div.carousel-selectors ul {
	list-style-type:none;
	margin:0;padding:0;
	font-weight:bold; font-size:16px;
	letter-spacing:2px;
}
div.carousel-selectors ul li {
	display:block; 
	height:70px; padding-top:30px;
	border-bottom:2px solid #071a71;
}
div.carousel-selectors ul li.last {
	border-bottom:none;
}
div.carousel-selectors ul li.active {
	background-color:#071a71;
	color:white;
}
div.carousel-selectors ul li:hover {
	background-color:#071a71;
}

.media-boxes div h4 { color:white; }
.media-boxes > div { border:2px solid #071a71;
                   background-image:url('<?php echo static_url('/wp-content/themes/sellerlink/images/media_bg.png'); ?>');
		   text-align:center; height:200px;
                   color:black;
}
</style>

<div class="jumbotron">

<div class="container">
<div id="carousel" class="col-lg-12 carousel slide" style="margin-left:0">
	
	<div class="carousel-inner" style="height:350px">
		<div class="item">Test
		<div class="carousel-caption">
		<h4>Slide 1</h4>
		<p>test</p>
		</div>
		</div>
		<div class="item">Test
		<div class="carousel-caption">
		<h4>Slide 2</h4>
		<p>test</p>
		</div>
		</div>
	</div>

</div>

</div>
</div>

<div class="text-center">
Search by Map
</div>
<br>

<div class="row media-boxes">
<div class="col-lg-4">

<h4 class="text-center">Twitter</h4>
<br><br>

<div class="input-group">

	<input type=text class="form-control" name="twitter-post" placeholder="Interact with our bot!" />

	<span class="btn input-group-addon"><i class="glyphicon glyphicon-retweet"></i></span>

</div>

</div>

<div class="col-lg-4">
<h4 class="text-center">Latest Activity</h4>
<br>

new Listing, Resort, Hotel, City, User, Post/Comment, Inquiry
vacation club/group
...edit all pages with markdown
...view on map

</div>
<div style="float:left;width:360px">
<h4 class="text-center">Blog</h4>
<br>

New Post

</div>
</div>

<div class="text-center">
FB LIKES

</div>
<br>


<?php get_footer(); ?>


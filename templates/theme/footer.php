
    </div>

    <footer>

	<div class="container">

	<div class="row">
	<div class="col-lg-4">
	<h2>Vacation Resources</h2>
	<a href="<?php echo url_for('timeshare_news') ?>">Timeshare News</a><br>
	<a href="<?php echo url_for('timeshare_search') ?>">Timeshare Search</a><br>
	<a href="<?php echo url_for('timeshare_top') ?>">Top Timeshare Destinations (...)</a> | <a href="<?php echo url_for('timeshare_map') ?>">Map</a><br>
	<a href="<?php echo url_for('timeshare_forum') ?>">Timeshare Forum</a><br>
	<a href="<?php echo url_for('timeshare_resources') ?>">Timeshare Resources</a><br>
	<a href="<?php echo url_for('timeshare_newsletter')?>">Timeshare Newsletter</a><br>
	<a href="<?php echo url_for('developer_index') ?>">Developer Information</a><br>

	<br>
	<h4><a href="<?php echo url_for('listing_new') ?>">Add A Free Listing</a></h4>

	</div>
	<div class="col-lg-4">
	<h2>Company Information</h2>
	<a href="<?php echo url_for('company_news') ?>">News</a> | <a href="<?php echo url_for('company_blog') ?>">Blog</a> | <a href="/">Shop</a> <br>
	<a href="<?php echo  url_for('about_us') ?>">About Us</a><br>
	<a href="<?php echo  url_for('contact_us') ?>">Contact Us</a><br>
	<a href="<?php echo  url_for('company_pricing') ?>">Pricing</a> | <a href="<?php echo url_for('company_marketing') ?>">Marketing</a><br>
	<a href="<?php echo  url_for('company_terms') ?>">Terms Of Service</a><br>
	<a href="<?php echo url_for('company_privacy') ?>">Privacy Policy</a><br>
	<a href="<?php echo url_for('company_advertising') ?>">Advertising Services</a><br>
	<a href="">DMCA Notice</a><br>

	<br>
	<h4><a href="tel:8777273718">Need Help? Call Us! 877-727-3718</a></h4>
	</div>
	<div class="col-lg-4">	
	<br><br><br>
	<br>

	Join Us On<br>
	<a target="_new" href="http://facebook.com/vacationsellerlink"><i class="fa fa-facebook-square fa-2x"></i></a>
	<a target="_new" href="http://twitter.com/sellerlink"><i class="fa fa-twitter-square fa-2x"></i></a>
	<a target="_new" href="http://plus.google.com/"><i class="fa fa-google-plus-square fa-2x"></i></a>
	<a target="_new" href="http://youtube.com/user/sellerlink"><i class="fa fa-youtube-square fa-2x"></i></a>
        <a target="_new" href="http://youtube.com/user/sellerlink"><i class="fa fa-pinterest-square fa-2x"></i></a>
        <a target="_new" href="http://youtube.com/user/sellerlink"><i class="fa fa-instagram fa-2x"></i></a>
        <a target="_new" href="http://youtube.com/user/sellerlink"><i class="fa fa-flickr fa-2x"></i></a>

        <h4>&copy; Total Travel Marketing, Inc.</h4>

	</div>
	</div>

	<br>
	ADSENSE

	</div>
	<br>

    </footer>


<?php // XXX wp_enqueue ?>

    <link rel=stylesheet href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" />
    <link rel=stylesheet href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" />
    <link rel=stylesheet href="<?php echo static_url('/wp-content/themes/sellerlink/css/sellerlink-screen.css'); ?>" />

    <!-- Bootstrap core JavaScript -->
    <script src="<?php echo static_url('/wp-content/themes/sellerlink/js/jquery.min.js'); ?>"></script>
    <script src="<?php echo static_url('/wp-content/themes/sellerlink/js/bootstrap.min.js'); ?>"></script>
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>

    <script>
	$(document).ready( function() {
//		$("#auto-top").typeahead({source:, highlighter:});
//		$("#auto-top").autocomplete({source:['a','b','c']});


		$('#nav').affix({ offset: { top: $('header').height() } });

	} );
    </script>


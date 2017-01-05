<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- <link rel="icon" href="../../favicon.ico"> -->

    <title>SellerLink</title>


    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <header>
    <nav class="navbar navbar-fixed-top">
      <div class="navbar-header">
        <a class="navbar-brand" href="/"><img alt="SellerLink" src="/static/img/sellerlink-logo-trans.png"/></a>
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
      </div>
      <div class="navbar-collapse collapse">

      <form role="form" class="col-lg-6">
	    <div class="input-group form-group">
          <input type="text" id="auto-top" name="search" data-provide="typeahead" autocomplete="off" placeholder="Search for hotels and resorts..." name="search" class="form-control autocomplete">
	        <span class="btn input-group-addon"><i class="glyphicon glyphicon-search"></i></span>
	    </div>
      </form>
        
        <div class="navbar-header navbar-right">
          <a href='{{ url_for('login') }}'>Log in</a>
	        <a href='{{ url_for('register') }}'>Sign up FREE</a>

    	    <button class="btn btn-success" onclick="location.href='{{ url_for('listing_new') }}">List Property</button>
	        
      	</div>
      </div>
    </nav>

    </header>

    <div class="content container">



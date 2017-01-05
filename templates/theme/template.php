<?php

function sellerlink_preprocess_html(&$vars) {
	drupal_add_css("//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css", array('type' => 'external'));
        drupal_add_css("//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css", array('type' => 'external'));
	// XXX jqueryui

	drupal_add_js("//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js");
}


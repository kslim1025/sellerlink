<?php
function get_title($title) {

}
function static_url($file) {
	return get_site_url() . $file;
}

function url_for($slug) {

	return "/";

}


if ( function_exists( 'register_nav_menus' ) ) {
	register_nav_menus(
		array(
		  'primary' => 'Primary Header Nav',
		)
	);
}


function initialize_admin () {

	//set Your icon URL here
    $icon = '';

    //adding page object -> http://codex.wordpress.org/Function_Reference/add_object_page
    add_object_page('Other Items', 'Other Items', 'manage_options', 'other-items', 'display_other_page', $icon);

    //in order to not duplicate top menu - first child menu have the same slug as parent
    //http://codex.wordpress.org/Function_Reference/add_submenu_page

    add_submenu_page('other-items', 'Actions', 'Actions', 'manage_options', 'slk-actions', 'display_actions_page');

    add_submenu_page('other-items', 'Geoshapes', 'Geoshapes', 'manage_options', 'slk-geoshape', 'display_geoshape_page');

    add_submenu_page('other-items', 'Locations', 'Locations', 'manage_options', 'slk-locations', 'display_locations_page');

    add_submenu_page('other-items', 'Open Hours', 'Open Hours', 'manage_options', 'slk-openhours', 'display_openhours_page');

    add_submenu_page('other-items', 'People', 'People', 'manage_options', 'slk-people', 'display_people_page');

    add_submenu_page('other-items', 'Media Objects', 'Media Objects', 'manage_options', 'slk-media', 'display_media_page');

    add_submenu_page('other-items', 'Image Objects', 'Image Objects', 'manage_options', 'slk-image', 'display_image_page');

    add_submenu_page('other-items', 'Video Objects', 'Video Objects', 'manage_options', 'slk-video', 'display_video_page');

}

function display_other_page() {
	echo "<h2>Other Items</h2>";

}

function display_actions_page() { display_pod_page("action"); }
function display_geoshape_page() { display_pod_page("geoshape"); }
function display_people_page() { display_pod_page("person"); }
function display_openhours_page() { display_pod_page("openhourspecificatio"); }
function display_locations_page() { display_pod_page("location"); }
function display_media_page() { display_pod_page("mediaobject"); }
function display_image_page() { display_pod_page("imageobject"); }
function display_video_page() { display_pod_page("videoobject"); }

function display_pod_page($pod_name) {
    //initialize pods
    $object = pods($pod_name);

    //for this pod type we will also use all available fields
    $fields = array();
    foreach($object->fields as $field => $data) {
        $fields[$field] = array('label' => $data['label']);
    }       

    //adding few basic parameters
    $object->ui = array(
/*        'item'   => 'author',
        'items'  => 'authors',
*/
        'fields' => array(
            'add'       => $fields,
            'edit'      => $fields,
            'duplicate' => $fields,
            'manage'    => $fields,
        ),
    );         

    //pass parameters
    pods_ui($object);
}

add_action('admin_menu','initialize_admin');


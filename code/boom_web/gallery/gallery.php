<?php

$rootpath = '../img_capture';
// $fileinfos = new RecursiveIteratorIterator(
//     new RecursiveDirectoryIterator($rootpath)
// );

$photos = array();

if ($handle = opendir($rootpath)) {
    while (false !== ($entry = readdir($handle))) {
        if ($entry != "." && $entry != "..") {
                $entry = $rootpath.'/'.$entry;
                $img_date = date("F d Y H:i:s", filemtime($entry));
                $title = $img_date;
            	$ext = pathinfo($entry, PATHINFO_EXTENSION);
            	if (strcmp($ext, 'jpg') == 0) 
    				$photos[] = array('baseurl' => "$entry", 'title' => "$title");
        }
    }
    closedir($handle);
}

echo json_encode($photos, JSON_UNESCAPED_SLASHES);



?>
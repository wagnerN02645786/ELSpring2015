<?php 
exec("python ./img_capture/take_pic.py 2>&1", $output); //runs python script that deactivates camera server and takes picture
print_r($output); //if you allow the browser to visit this file, this echos the output of the python file take_pic.py
?>

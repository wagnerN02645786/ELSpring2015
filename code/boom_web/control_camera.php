<?php

// $teste = fopen("newfile.txt", "w") or die("Unable to open file!");
// $txt = "John Doe\n";
// fwrite($teste, $txt);
// fclose($teste);

 $motor1 = '0';
 $motor2 = '0';
 $motor3 = '0';

$motor_script_location = "./Adafruit_PWM_Servo_Driver/test_WriteFile.py";

$handle = fopen("./Adafruit_PWM_Servo_Driver/Location_Motor", "r") or die("Unable to open file!");
if ($handle)
{
 $motor1 = fgets($handle);
 $motor2 = fgets($handle);
 $motor3 = fgets($handle);	
}
fclose($handle);

$direction = $_POST['direction'];

 $m1 = intval($motor1);
 $m2 = intval($motor2);
 $m3 = intval($motor3);	

$angle = 5;

if (strcmp($direction, 'xup') == 0)
{
	$m1 = $m1 + $angle;
}
else if (strcmp($direction, 'xdown') == 0)
{
	$m1 = $m1 - $angle;
}
else if (strcmp($direction, 'yup') == 0)
{
	$m2 = $m2 + $angle;
}
else if (strcmp($direction, 'ydown') == 0)
{
	$m2  = $m2 - $angle;
}
else if (strcmp($direction, 'zup') == 0)
{
	$m3 = $m3 + $angle;
}
else if (strcmp($direction, 'zdown') == 0)
{
	$m3 = $m3 - $angle;
}
else 
{
	//error
	$m1 = 0;
	$m2 = 0;
	$m3 = 0;
}

$cmd = "sudo python ".$motor_script_location." ".$m1." ".$m2." ".$m3;
$output = array();
exec($cmd, $output);

?>
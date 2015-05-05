<?php

$m1 = $_POST['motor1'];
$m2 = $_POST['motor2'];
$m3 = $_POST['motor3'];

$motor_script_location = "./Adafruit_PWM_Servo_Driver/test_WriteFile.py";
$cmd = "sudo python ".$motor_script_location." ".$m1." ".$m2." ".$m3;

$output = array();
exec($cmd, $output);

?>

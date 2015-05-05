<?php
exec("sudo python ./Adafruit_PWM_Servo_Driver/test_WriteFile.py 120 120 120 2>&1", $output);
print_r($output);
?>


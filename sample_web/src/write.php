<?php
$password = filter_input(INPUT_POST, 'password', FILTER_VALIDATE_REGEXP, array('options' => array('regexp' => '/^\w+$/D'))) or die('password?');
$content = filter_input(INPUT_POST, 'content', FILTER_VALIDATE_REGEXP, array('options' => array('regexp' => '/^\w+$/D'))) or die('content?');


# This is your (only!) writeable directory. Store flags here.
$mydir = '/opt/ctf/sample_web/rw/';

# In this example, we create a new (randomly-named) file for each flag.
$somerand = openssl_random_pseudo_bytes(8) or die("random");
$note_id = bin2hex($somerand);

$f = fopen($mydir.$note_id, 'x') or die("fopen");
fputcsv($f, array($content, password_hash($password, PASSWORD_DEFAULT))) or die("fputcsv");
fclose($f) or die("fclose");
?>

<!DOCTYPE html>
<html>
<body>
    <p>Your note is safe with us! You can retrieve it with your password and this note ID: <?= $note_id; ?>
</body>
</html>

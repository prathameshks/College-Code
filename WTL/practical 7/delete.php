<?php

$conn = mysqli_connect("localhost:3306", '', '', 'student_db');

if (!isset($_GET['id'])) {
    header("location: index.php");
    die;
}else{
    $stu_id = $_GET['id'];
    $qry = "DELETE FROM students WHERE `id` = $stu_id ";
    $res = mysqli_query($conn, $qry);
    if (!$res) {
        header("location:index.php?s=Failed+To+Delete&type=danger");
    } else {
        header("location:index.php?s=Deleted+Record&type=success");
    }
}

?>

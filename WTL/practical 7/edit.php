<?php

$conn = mysqli_connect("localhost:3306", '', '', 'student_db');

if (!isset($_GET['id']) && !isset($_POST['id'])) {
    header("location: index.php");
    die;
}


if (isset($_POST['submit'])) {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $class = $_POST['class'];
    $division = $_POST['division'];
    $address = $_POST['address'];

    $sql = "UPDATE `students`
    SET `name` = '$name',
    `class`='$class',
    `division`='$division',
    `address`='$address'
    WHERE `id` = $id";
echo $sql;
    $res = mysqli_query($conn, $sql);
    if (!$res) {
        header("location:edit.php?s=Failed+To+Edit&type=danger");
    } else {
        header("location:index.php?s=Edited+Record&type=success");
    }
    die;
}

$stu_id = $_GET['id'];
$qry = "SELECT * FROM students WHERE `id` = $stu_id ";
$res = mysqli_query($conn, $qry);
$fail = false;
if (!$res || mysqli_num_rows($res) < 1) {
    $fail = true;
} else {
    $data = mysqli_fetch_row($res);
}
// var_dump($data);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practical 7</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>

<body class="h-100 bg-light">
    <div class="container py-5">
        <h1 class="mb-5">Student Information System</h1>
        <h2 class="mb-4">Edit Record</h2>
        <?php
        if ($fail) {
        ?>
            <p>No Such Record Found</p>
        <?php
        } else {
        ?>
            <form method="post">
                <input type="text" name="id" value="<?= $data[0] ?>" hidden>
                <div class="mb-3">
                    <input type="text" name="name" placeholder="Enter Name" value="<?= $data[1] ?>" class="form-control">
                </div>
                <div class="mb-3">
                    <select name="class" class="form-select">
                        <option value="Comp" <?= $data[2] == 'Comp' ? 'selected' : '' ?>>Comp</option>
                        <option value="Mech" <?= $data[2] == 'Mech' ? 'selected' : '' ?>>Mech</option>
                        <option value="EnTC" <?= $data[2] == 'EnTC' ? 'selected' : '' ?>>EnTC</option>
                        <option value="AnR" <?= $data[2] == 'AnR' ? 'selected' : '' ?>>AnR</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="">Division</label><br>
                    <div class="form-check form-check-inline">
                        <input type="radio" name="division" id="div1" value="1" <?= $data[3] == '1' ? 'checked' : '' ?> class="form-check-input">
                        <label for="div1" class="form-check-label">1</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input type="radio" name="division" id="div2" value="2" <?= $data[3] == '2' ? 'checked' : '' ?> class="form-check-input">
                        <label for="div2" class="form-check-label">2</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input type="radio" name="division" id="div3" value="3" <?= $data[3] == '3' ? 'checked' : '' ?> class="form-check-input">
                        <label for="div3" class="form-check-label">3</label>
                    </div>
                </div>
                <div class="mb-3">
                    <textarea name="address" id="" placeholder="Enter Address" cols="30" rows="5" class="form-control"><?= $data[4] ?></textarea>
                </div>
                <div class="mb-3">
                    <input type="submit" name="submit" id="submit" class="btn btn-primary">
                    <input type="reset" value="Reset" class="btn btn-secondary">
                </div>
            </form>
        <?php
        }
        ?>
    </div>
    <footer class="footer mt-auto py-3 bg-light">
        <div class="container">
            <span class="text-muted">Created in PHP and MySQL by Prathamesh Sable.</span>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>

</html>
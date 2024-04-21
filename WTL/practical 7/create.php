<?php
$conn = mysqli_connect("localhost:3306", '', '', 'student_db');
if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $class = $_POST['class'];
    $division = $_POST['division'];
    $address = $_POST['address'];
    $sql = "INSERT INTO `students`(`name`, `class`, `division`, `address`) VALUES ('$name','$class','$division','$address')";
    $res = mysqli_query($conn, $sql);
    if (!$res) {
        header("location:index.php?s=Failed+To+Create&type=danger");
    } else {
        header("location:index.php?s=Created+Record&type=success");
    }
}
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

    <?php include "navbar.php" ?>
    <div class="container py-5">

        <h2 class="mb-4">Add Record</h2>
        <form method="post">
            <div class="mb-3">
                <input type="text" name="name" placeholder="Enter Name" class="form-control">
            </div>
            <div class="mb-3">
                <select name="class" class="form-select">
                    <option value="" selected disabled hidden>Select Class</option>
                    <option value="Comp">Comp</option>
                    <option value="Mech">Mech</option>
                    <option value="EnTC">EnTC</option>
                    <option value="AnR">AnR</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="">Division</label><br>
                <div class="form-check form-check-inline">
                    <input type="radio" name="division" id="div1" value="1" class="form-check-input">
                    <label for="div1" class="form-check-label">1</label>
                </div>
                <div class="form-check form-check-inline">
                    <input type="radio" name="division" id="div2" value="2" class="form-check-input">
                    <label for="div2" class="form-check-label">2</label>
                </div>
                <div class="form-check form-check-inline">
                    <input type="radio" name="division" id="div3" value="3" class="form-check-input">
                    <label for="div3" class="form-check-label">3</label>
                </div>
            </div>
            <div class="mb-3">
                <textarea name="address" id="" placeholder="Enter Address" cols="30" rows="5" class="form-control"></textarea>
            </div>
            <div class="mb-3">
                <input type="submit" name="submit" id="submit" class="btn btn-primary">
                <input type="reset" value="Reset" class="btn btn-secondary">
            </div>
        </form>
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
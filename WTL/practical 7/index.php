<?php
$conn = mysqli_connect("localhost:3306", '', '', 'student_db');
$sql = "SELECT * FROM `students`;";
$res = mysqli_query($conn, $sql);
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
        <h1 class="mb-5">Student Records</h1>
        <?php
        if (isset($_GET['s'])) {
        ?>
            <div class="alert alert-<?= isset($_GET['type']) ? $_GET['type'] : 'primary' ?> alert-dismissible fade show" role="alert">
                <strong><?=$_GET['s']?> </strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        <?php
        }
        ?>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Class</th>
                    <th>Division</th>
                    <th>Address</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                while ($row = mysqli_fetch_row($res)) {
                ?>
                    <tr>
                        <td><?= $row['0'] ?></td>
                        <td><?= $row['1'] ?></td>
                        <td><?= $row['2'] ?></td>
                        <td><?= $row['3'] ?></td>
                        <td><?= $row['4'] ?></td>
                        <td>
                            <a href="edit.php?id=<?= $row['0'] ?>" class="btn btn-primary">
                                Edit
                            </a>
                        </td>
                        <td>
                            <a href="delete.php?id=<?= $row['0'] ?>" class="btn btn-danger">
                                Delete
                            </a>
                        </td>
                    </tr>
                <?php
                }
                ?>
            </tbody>
        </table>
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

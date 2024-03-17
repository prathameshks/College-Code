<%@ page import="java.sql.*" %>
<%@ page import="jakarta.servlet.http.*" %>

<%! Connection connection = null; %>

<%
    try {
        Class.forName("com.mysql.jdbc.Driver");
        
        connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/student_db", "", "");

        // Prepare and execute SELECT query
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT * FROM students_info");
%>

<!DOCTYPE html>
<html>
<head>
    <title>Student Information System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    
</head>
<body>
	<div class="container">
		<h1>Student Information</h1>
		
		<div class="m-2">
			
			<form action="insert_student.jsp" method="post">
				<div class="mb-0">
					<label for="name" class="form-label">Student Name:</label>
					<input type="text" name="name" id="name" required class="form-control">
				</div>
				<div class="mb-0">
					<label for="class" class="form-label">Class:</label>
					<input type="text" name="class" id="class" required class="form-control">
				</div>
				<div class="mb-0">
					<label for="division" class="form-label">Division:</label>
					<input type="text" name="division" id="division" required class="form-control">
				</div>
				<div class="mb-0">
					<label for="city" class="form-label">City:</label>
					<input type="text" name="city" id="city" required class="form-control">
				</div>

				<button type="submit" class="btn btn-primary">Add Student</button>
			</form>

			<%
				if (resultSet != null) {
			%>

			<table class="table table-striped">
				<thead>
					<tr>
						<th scope="col">Student ID</th>
						<th scope="col">Student Name</th>
						<th scope="col">Class</th>
						<th scope="col">Division</th>
						<th scope="col">City</th>
					</tr>
				</thead>
				<% while (resultSet.next()) { %>
				<tr>
					<td><%= resultSet.getInt("roll_no") %></td>
					<td><%= resultSet.getString("name") %></td>
					<td><%= resultSet.getString("class") %></td>
					<td><%= resultSet.getString("division") %></td>
					<td><%= resultSet.getString("city") %></td>
				</tr>
				<% } %>
			</table>

			<%
				}
			} catch (ClassNotFoundException e) {
				e.printStackTrace();
			} catch (SQLException e) {
				e.printStackTrace();
			} finally {
				if (connection != null) {
					try {
						connection.close();
					} catch (SQLException e) {
						e.printStackTrace();
					}
				}
			}
			%>

		</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</body>
</html>

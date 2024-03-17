<%@ page import="java.sql.*" %>
<%@ page import="jakarta.servlet.http.*" %>

<%! Connection connection = null; %>

<%
try {
    // Get form data
    String stud_name = request.getParameter("name");
    String class_val = request.getParameter("class");
    String division = request.getParameter("division");
    String city = request.getParameter("city");

    Class.forName("com.mysql.jdbc.Driver");
    connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/student_db", "", "");

    // Prepare and execute INSERT query
    PreparedStatement statement = connection.prepareStatement("INSERT INTO students_info (name, class, division, city) VALUES (?, ?, ?, ?)");
    statement.setString(1, stud_name);
    statement.setString(2, class_val);
    statement.setString(3, division);
    statement.setString(4, city);
    statement.executeUpdate();

    // Redirect back to index.jsp to display updated data (optional)
    response.sendRedirect("/Assignment6/");

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

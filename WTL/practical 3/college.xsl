<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h1 align="center">Teaching Staff</h1>
                <table border="2" align="center">
                    <tr bgcolor="">
                        <th>id</th>
                        <th>name</th>
                        <th>department</th>
                    </tr>
                        <xsl:for-each select="college/teaching">
                    <tr>
                            <td><xsl:value-of select="id"/></td>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="department"/></td>
                    </tr>
                        </xsl:for-each>
                </table>
                <br/>
                <h1 align="center">Non-Teaching Staff</h1>
                <table border="2" align="center">
                    <tr>
                        <th>id</th>
                        <th>name</th>
                    </tr>
                        <xsl:for-each select="college/non-teaching">
                    <tr>
                            <td><xsl:value-of select="id"/></td>
                            <td><xsl:value-of select="name"/></td>
                    </tr>
                        </xsl:for-each>
                </table>
                <br/>
                <h1 align="center">Students</h1>
                <table border="2" align="center">
                    <tr>
                        <th>id</th>
                        <th>name</th>
                        <th>department</th>
                        <th>section</th>
                        <th>year</th>
                    </tr>
                        <xsl:for-each select="college/student">
                    <tr>
                            <td><xsl:value-of select="id"/></td>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="department"/></td>
                            <td><xsl:value-of select="section"/></td>
                            <td><xsl:value-of select="year"/></td>
                    </tr>
                        </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>

#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="doctor_info")
cur=db.cursor()

name1=form.getvalue("name1")
mail1=form.getvalue("email1")
password1=form.getvalue("password1")

sql = "SELECT * FROM doc_login WHERE name=%s  AND  mail=%s AND password=%s"
val = [name1,mail1,password1]
cur.execute(sql, val)
result = cur.fetchone()
x=name1.lower()
if result:
    print("<h1 style='color:#008CBA;'><center>Welcome Dr.",name1, " please fill the details</center></h1><br><br><br>")
    print("""
<style>
th,td{
        border:1px solid black;
        border-collapse:collapse;
        background-color:white;
        border-radius:10px;
        border-style:ridge;
        border-color:black;
        padding:15px;
        border-spacing:50px;
}
tr:nth-child(even){
        background-color:blue;
}
</style>
<body>
<table style="width:100%">
        <head>
        <caption><h1></h1></caption>
        </head>
        <tr style="height:100px">
                <th style="width:15%">Name of the patient</th>
                <th>Patient's Phone no</th>
                <th>Patient's mail-id</th>
                
        </tr>
        """)
    cur.execute("select * from {}".format(x))
    for i in cur:
        print("<tr>")
        print("<td>",i[0],"</td>")
        print("<td>",i[1],"</td>")
        print("<td>",i[2],"</td>")
    print("</tr>")
    print("</table>")
    print("</body>")

    
else:
    print( """
    <h1><center>Invalid username or password</center></h1>
    <style>
	body{
		background-image:url('app.jpg');
		background-repeat:no-repeat;
		background-size:cover;
    }
    </style>
    """)



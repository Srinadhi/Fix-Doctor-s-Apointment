#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="patients_details")
cur=db.cursor()

name1=form.getvalue("name1")
mail1=form.getvalue("email1")
password1=form.getvalue("password1")

sql = "SELECT * FROM pat_details WHERE name=%s  AND  mail=%s AND password=%s"
val = [name1,mail1,password1]
cur.execute(sql, val)
result = cur.fetchone()
if result:
    print("<h1 style='color:#008CBA;'><center>Welcome",name1, " please fill the details</center></h1><br><br><br>")
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
        <caption><h1>Doctor's details</h1></caption>
        </head>
        <tr style="height:100px">
                <th style="width:15%">Doctor Name</th>
                <th>Doctor's specialization</th>
                <th>Morning Slot</th>
                <th>Afternoon Slot</th>
                <th>Night Slot</th>
        </tr>
        """)
    cur.execute("select * from doctor_details ")
    for i in cur:
        print("<tr>")
        print("<td>",i[0],"</td>")
        print("<td>",i[1],"</td>")
        print("<td>",i[2],"</td>")
        print("<td>",i[3],"</td>")
        print("<td>",i[4],"</td>")
    print("</tr>")
    print("</table>")
    print("</body>")

    print("<h1><center>Our Casuality Doctors are avaliable for 24X7 so you can directly come to hospital at any time.</center></h1>")
    print('''
    
  <head>
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
    <link rel="stylesheet" href="style2.css">
  </head>
    <form action="mail.py" id="ft-form" method="POST" accept-charset="UTF-8">
  <fieldset>
    <legend>For person</legend>
    <label>
      Name
      <input type="text" name="name" required>
    </label>
    <div class="two-cols">
      <label>
        Email address
        <input type="email" name="email" required>
      </label>
      <label>
        Phone number
        <input type="tel" name="phone">
      </label>
    </div>
  </fieldset>
  <fieldset>
    <legend>Appointment request</legend>
    <div class="two-cols">
      <label>
        Doctor Name
        <input type="text" name="doc_name" required>
      </label><br>
      <label>
        Datum
        <input type="date" name="doc_date" required>
      </label>
      <label>
        Time
        <input type="text" name="time" required>
      </label>
    </div>
  </fieldset>
  <h1><center>Confirmation will be done through email</center></h1>

  <div class="btns">
    <input type="text" name="_gotcha" value="" style="display:none;">
    <input type="submit" value="Submit request">
  </div>
</form>
<style>
''')
    
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



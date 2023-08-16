#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="doctor_info")
cur=db.cursor()

name=form.getvalue("name")
number=form.getvalue("Phone-No")
mail=form.getvalue("email")
password=form.getvalue("password")
dob=form.getvalue("dob") 
age=form.getvalue("age")
aad=form.getvalue("aad")



print("<h1 style='color:white;'><center>Welcome to Patient's Login Page</center></h1>")

print("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Login & Signup Page</title>
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
    <link rel="stylesheet" href="style1.css">
  </head>
  <body>
    <div class="container">
      <div class="form-wrap">
        <h1 class="form-heading">Login</h1>
        <form class="form" method="post" action="appointment.py">
          <div class="input-group">
            <input type="text" name="name1" id="name1" required>
            <label for="name1">Name</label>
          </div>
          <div class="input-group">
            <input type="email" name="email1" id="email" required>
            <label for="email">Email</label>
          </div>
          <div class="input-group">
            <input type="password" name="password1" id="password1" required>
            <label for="password1">Password</label>
          </div>
          <button type="submit" style="background-color: #008CBA; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">LogIn</button>
        </form>

      </div>
      <div class="form-wrap">
        <h1 class="form-heading">Signup</h1>
        <form class="form" method="post" >
          <div class="input-group">
            <input type="text" name="name" id="name" required>
            <label for="name">Name</label>
          </div>
          <div class="input-group">
            <input type="text" name="Phone-No" id="Phone-No" required>
            <label for="Phone-No">Phone-No</label>
          </div>
          <div class="input-group">
            <input type="email" name="email" id="email" required>
            <label for="email">Email</label>
          </div>
          <div class="input-group">
            <input type="password" name="password" id="password" required>
            <label for="password">Password</label>
          </div>
          <div class="input-group">
            <input type="text" name="dob" id="dob" required>
            <label for="dob">Date of Birth</label>
          </div>
          <div class="input-group">
            <input type="number" name="age" id="age" required>
            <label for="age">Age</label>
          </div>
          <div class="input-group">
            <input type="text" name="aad" id="aad" required>
            <label for="aad">Aadhar Number</label>
          </div>
          <button type="submit" style="background-color: #008CBA; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer;">SignUp</button>
        </form>
        <h4 style='color:#008CBA;'><center>If you are already SignUp you can directly logIn</center></h4>

      </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="app.js"></script>
  </body>
  <style>
	body{
		background-image:url('pat.jpeg');
		background-repeat:no-repeat;
		background-size:cover;
}
</style>
</html>
""")

cur.execute("SELECT * FROM  pat_details WHERE aad=%s",(aad))

result = cur.fetchone()
if result:
    print("<h1 style='color:#008CBA;'><center>You are already Signup  </center></h1>")
else:
    query="insert into pat_details values(%s,%s,%s,%s,%s,%s,%s)"  
    val=[name,number,mail,password,dob,age,aad]
    cur.execute(query,val)
    db.commit()
    print("<h1 style='color:#008CBA;</center>SignUp successfully</center></h1>")


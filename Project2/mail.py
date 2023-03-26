#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="doctor_info")
cur=db.cursor()


name=form.getvalue('name')
email=form.getvalue('email')
phone=form.getvalue('phone')
doc_name=form.getvalue('doc_name')
doc_date=form.getvalue('doc_date')
time=form.getvalue('time')

query= "insert into appointment values(%s,%s,%s,%s,%s,%s)"
val =[name,email,phone,doc_name,doc_date,time]

cur.execute(query,val)
db.commit()


print( """
    <h1 style='color:#008CBA;'><center>Your appointment fixed sucessfully</center></h1>
    <style>
	body{
		background-image:url('app.jpg');
		background-repeat:no-repeat;
		background-size:cover;
    }
    </style>
    """)

msg = MIMEMultipart()

sender = "sridummypro@gmail.com"
recipient = email

message = 'This the mail from Hami Hospital.Your appointment confirmed with '+doc_name+' on '+doc_date+' at '+time+'.'

msg.attach(MIMEText(message, 'plain'))

msg['Subject'] = 'Appointment Conformation'

smtp_server = 'smtp.gmail.com'
smtp_port = 587

smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
smtp_obj.starttls()
smtp_obj.login(sender, 'qcqlggmmdlnqynxw')

smtp_obj.sendmail(sender, recipient, msg.as_string())

smtp_obj.quit()
print('''
<h2><center>&#128512Your appointment sent to your mail<center></h2>
''')

x=doc_name.lower()
que="insert into "+x+" values(%s,%s,%s)"
value=[name,phone,time]
cur.execute(que,value)
db.commit()
print('ok')

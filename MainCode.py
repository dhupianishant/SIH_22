#Importing the Modules
import mysql.connector as m
from django.utils.crypto import get_random_string
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image, ImageDraw, ImageFont
from twilio.rest import Client
import smtplib
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username=input("Enter username: ")
pwd=input("Enter password: ")

#Login
if username=='nishant' and pwd=='qwerty':
               print("Login Succesfull.")
               
               #Connection to MySQL Databse
               mydb=m.connect(host="localhost", user="root", passwd="student", database="monuments_data")

               #Checking the connection
               if mydb.is_connected:
                              print("Succesfully Connected to MySQL Database.")

               #Defining the Cursor
               cursor=mydb.cursor()

               #Selection of monuments
               print("Select the monumnet for which you want to book the ticket.")        
               print("1. Taj Mahal, Agra\n2. Hawa Mahal, Jaipur\n3. Statue of Unity, Gujarat")
               mon_choice=int(input("Choose a Monument "))
               
               #Taj Mahal, Agra
               if mon_choice==1:
                              print("You have selected TAJ MAHAL, AGRA.")
                              
                              #Taking input from users
                              srno = get_random_string(5)
                              dt = input("Please enter date for booking (YYYY-MM-DD): ")
                              name = input("Please enter your Name: ")
                              mob_num = input("Please enter your Mobile Number: ")
                              age = int(input("Please enter your Age: "))
                              gender = input("Please enter your Gender(M/F): ")
                              mail = input("Please enter your email id: ")
                              
                              #Enetring data into Database
                              s = "INSERT INTO taj_visitors (srno, name, mob_num, gender, dt, age, mail) VALUES ('{}', '{}', '{}', '{}', '{}', {}, '{}')".format(srno, name, mob_num, gender, dt, age, mail)
                              cursor.execute(s)
                              mydb.commit()

                              #Sending SMS
                              client = Client("ACc551339c4ebfe9e1d0aefc10599abc03", "d63dc43dac85adec50f70d95d1e9d8df")
                              b='Your Registration has been succesfull with the following Reg No.: ' + srno
                              client.messages.create(to=mob_num, from_="+16105491075", body=b)

                              #Generating the QR Code
                              url=pyqrcode.create(srno)
                              url.png('taj.png', scale=7)

                              #Pasting the QRCode on white image
                              img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\bgimage.png")
                              img2= Image.open(r"C:\Users\nisha\Documents\SIH' 22\taj.png")
                              img.paste(img2, (1500, 445))
                              img.save("tajticket.png")

                              #Writing text on Image
                              img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\tajticket.png")
                              d1= ImageDraw.Draw(img)
                              fnt=ImageFont.truetype('C:\Windows\Fonts\LFAXDI.TTF', 20)
                              d1.text((200,445), 'Taj Mahal, Agra', font=fnt, fill=(0, 0, 0))
                              d1.text((200,470), srno, font=fnt, fill=(0, 0, 0))
                              d1.text((200,495), dt, font=fnt, fill=(0, 0, 0))
                              d1.text((200,520), name, font=fnt, fill=(0, 0, 0))
                              d1.text((200,545), str(age), font=fnt, fill=(0, 0, 0))
                              d1.text((200,570), gender, font=fnt, fill=(0, 0, 0))
                              img.save("FinalTajTicket.png")
                              img.show()

                              #Sending the Mail
                              subject = "You eTicket for Taj Mahal Visit"
                              body = "Hello visitor, kindly find attached your eTicket for you visit to Taj Mahal."
                              sender_email = "nishantdhupia.cse25@jecrc.ac.in"
                              receiver_email = mail
                              password = "requestotp123"

                              # Create a multipart message and set headers
                              message = MIMEMultipart()
                              message["From"] = sender_email
                              message["To"] = receiver_email
                              message["Subject"] = subject

                              # Add body to email
                              message.attach(MIMEText(body, "plain"))

                              filename = "FinalTajTicket.png" 

                              # Open PDF file in binary mode
                              with open(filename, "rb") as attachment:
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attachment.read())

                              # Encode file in ASCII characters to send by email    
                              encoders.encode_base64(part)

                              # Add header as key/value pair to attachment part
                              part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

                              # Add attachment to message and convert message to string
                              message.attach(part)
                              text = message.as_string()

                              # Log in to server using secure context and send email
                              context = ssl.create_default_context()
                              with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                server.login(sender_email, password)
                                server.sendmail(sender_email, receiver_email, text)

               #Hawa Mahal, Jaipur
               elif mon_choice==2:
                              print("You have selected HAWA MAHAL, JAIPUR.")
                              
                              #Taking input from user
                              srno = get_random_string(5)
                              dt = input("Please enter date for booking (YYYY-MM-DD): ")
                              name = input("Please enter your Name: ")
                              mob_num = input("Please enter your Mobile Number: ")
                              age = int(input("Please enter your Age: "))
                              gender = input("Please enter your Gender(M/F): ")
                              mail = input("Please enter your mail: ") 
                              
                              #Enetring data into Database
                              s = "INSERT INTO hawa_visitors (srno, name, mob_num, gender, dt, age, mail) VALUES ('{}', '{}', '{}', '{}', '{}', {}, '{}')".format(srno, name, mob_num, gender, dt, age, mail)
                              cursor.execute(s)
                              mydb.commit()

                              #Sending SMS
                              client = Client("ACc551339c4ebfe9e1d0aefc10599abc03", "d63dc43dac85adec50f70d95d1e9d8df")
                              b='Your Registration has been succesfull with the following Reg No.: ' + srno
                              client.messages.create(to=mob_num, from_="+16105491075", body=b)

                              #Generating the QR Code
                              url=pyqrcode.create(srno)
                              url.png('hawa.png', scale=7)

                              #Pasting the QRCode on white image
                              img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\bgimage.png")
                              img2= Image.open(r"C:\Users\nisha\Documents\SIH' 22\hawa.png")
                              img.paste(img2, (1500, 445))
                              img.save("hawaticket.png")

                              #Writing text on Image
                              img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\hawaticket.png")
                              d1= ImageDraw.Draw(img)
                              fnt=ImageFont.truetype('C:\Windows\Fonts\LFAXDI.TTF', 20)
                              d1.text((200,445), 'Hawa Mahal, Jaipur', font=fnt, fill=(0, 0, 0))
                              d1.text((200,470), srno, font=fnt, fill=(0, 0, 0))
                              d1.text((200,495), dt, font=fnt, fill=(0, 0, 0))
                              d1.text((200,520), name, font=fnt, fill=(0, 0, 0))
                              d1.text((200,545), str(age), font=fnt, fill=(0, 0, 0))
                              d1.text((200,570), gender, font=fnt, fill=(0, 0, 0))
                              img.save("FinalHawaTicket.png")
                              img.show()
                              
                              #Sending the Mail
                              subject = "You eTicket for Hawa Mahal Visit"
                              body = "Hello visitor, kindly find attached your eTicket for you visit to Hawa Mahal."
                              sender_email = "nishantdhupia.cse25@jecrc.ac.in"
                              receiver_email = mail
                              password = "requestotp123"

                              # Create a multipart message and set headers
                              message = MIMEMultipart()
                              message["From"] = sender_email
                              message["To"] = receiver_email
                              message["Subject"] = subject

                              # Add body to email
                              message.attach(MIMEText(body, "plain"))

                              filename = "FinalHawaTicket.png" 

                              # Open PDF file in binary mode
                              with open(filename, "rb") as attachment:
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attachment.read())

                              # Encode file in ASCII characters to send by email    
                              encoders.encode_base64(part)

                              # Add header as key/value pair to attachment part
                              part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

                              # Add attachment to message and convert message to string
                              message.attach(part)
                              text = message.as_string()

                              # Log in to server using secure context and send email
                              context = ssl.create_default_context()
                              with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                server.login(sender_email, password)
                                server.sendmail(sender_email, receiver_email, text)

               
               #Statue of Unity, Gujarat
               elif mon_choice==3:
                              print("You have selected STATUE OF UNITY, GUJARAT.")
                              
                              #taking input from user
                              srno = get_random_string(5)
                              dt = input("Please enter date for booking (YYYY-MM-DD): ")
                              name = input("Please enter your Name: ")
                              mob_num = input("Please enter your Mobile Number: ")
                              age = int(input("Please enter your Age: "))
                              gender = input("Please enter your Gender(M/F): ") 
                              mail = input("Please enter your mail id: ")          
                              
                              #Enetring data into Database
                              s = "INSERT INTO unity_visitors (srno, name, mob_num, gender, dt, age, mail) VALUES ('{}', '{}', '{}', '{}', '{}', {}, '{}')".format(srno, name, mob_num, gender, dt, age, mail)
                              cursor.execute(s)
                              mydb.commit()

                              #Generating the QR Code
                              url=pyqrcode.create(srno)
                              url.png('unity.png', scale=7)

                              #Sending SMS
                              client = Client("ACc551339c4ebfe9e1d0aefc10599abc03", "d63dc43dac85adec50f70d95d1e9d8df")
                              b='Your Registration has been succesfull with the following Reg No.: ' + srno
                              client.messages.create(to=mob_num, from_="+16105491075", body=b)

                              #Pasting the QRCode on white image
                              img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\bgimage.png")
                              img2= Image.open(r"C:\Users\nisha\Documents\SIH' 22\unity.png")
                              img.paste(img2, (1500, 445))
                              img.save("unityticket.png")

                              #Writing text on Image
                              img = Image.open(r"C:\Users\nisha\Documents\SIH' 22\unityticket.png")
                              d1= ImageDraw.Draw(img)
                              fnt=ImageFont.truetype('C:\Windows\Fonts\LFAXDI.TTF', 20)
                              d1.text((200,445), 'Statue of Unity, Gujarat', font=fnt, fill=(0, 0, 0))
                              d1.text((200,470), srno, font=fnt, fill=(0, 0, 0))
                              d1.text((200,495), dt, font=fnt, fill=(0, 0, 0))
                              d1.text((200,520), name, font=fnt, fill=(0, 0, 0))
                              d1.text((200,545), str(age), font=fnt, fill=(0, 0, 0))
                              d1.text((200,570), gender, font=fnt, fill=(0, 0, 0))
                              img.save("FinalUnityTicket.png")
                              img.show()

                              #Sending the Mail
                              subject = "You eTicket for Staue of Unity visit."
                              body = "Hello visitor, kindly find attached your eTicket for you visit to Statue of Unity."
                              sender_email = "nishantdhupia.cse25@jecrc.ac.in"
                              receiver_email = mail
                              password = "requestotp123"

                              # Create a multipart message and set headers
                              message = MIMEMultipart()
                              message["From"] = sender_email
                              message["To"] = receiver_email
                              message["Subject"] = subject

                              # Add body to email
                              message.attach(MIMEText(body, "plain"))

                              filename = "FinalUnityTicket.png" 

                              # Open PDF file in binary mode
                              with open(filename, "rb") as attachment:
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attachment.read())

                              # Encode file in ASCII characters to send by email    
                              encoders.encode_base64(part)

                              # Add header as key/value pair to attachment part
                              part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

                              # Add attachment to message and convert message to string
                              message.attach(part)
                              text = message.as_string()

                              # Log in to server using secure context and send email
                              context = ssl.create_default_context()
                              with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                server.login(sender_email, password)
                                server.sendmail(sender_email, receiver_email, text)
               
               #Invalid Choice
               else:
                              print("Enter a valid choice.")


else:
               print("Please enter Valid credentials.")
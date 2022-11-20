import random
import smtplib
from email_validator import validate_email

# smptlib Gmail PORT
PORT = 587

# Importing my Email and Password
file = open("confidential.txt", "r")
myEmail = ""
myPass = ""
for data in file:
    value = data.split(",")
    myEmail = value[0]
    myPass = value[1]

# Input of User Email Id
userEmail = input("Enter you Email id : ")

# Text message to be send
message = "Otp to login to your account is: "

try:
    # Validating the Email
    validated_email = validate_email(userEmail)
except:
    print("Invalid Email");


# Function for sending email to user
def sendEmailtoUser():
    server.sendmail(myEmail , userEmail , message + str(otp) )

    # Quiting the server after sending email
    server.quit();

try:
    server = smtplib.SMTP('smtp.gmail.com', PORT)
    server.starttls()
    server.login(myEmail,myPass)
    otp = random.randrange(100000,1000000)
    
    # sending Email to User
    sendEmailtoUser()

    #Input from user to validate OTP
    isCorrectOtp = int(input(("Enter your Otp : ")))

    # Validating entered Otp
    if(isCorrectOtp == otp):
        print("Logged in Successfully!")
    else:
        print("Invalid Otp!")
except:
    print("An Exception occured!")
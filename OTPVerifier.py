#Programmer -python_scripts (Puneet)
#Python GUI to generate OTP , send it to user input email-id & validate it using smtplib & email modules

#Simple Mail Transfer Protocol (SMTP) is a protocol, which handels sending e-mail and routing 
#email between mail servers. The smptlib modules defines an SMTP client session object that 
#can be used to send mail to any Internet machine with an SMTP or ESMTP listener.
#
#The email module is a library for managing email messages. It is specifically not designed to
#do any sending of email messages to SMTP, NNTP , or other servers; those are functions of 
#modules such as smtplib and nntplib. The package attempts to be as RFC-compliant as possible

#Importing Necessary Packages
import random
import smtplib
import tkinter as tk
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidget():
    emailLabel=Label(root,text="ENTER YOUR EMAIL-ID : ",bg="deepskyblue3")
    emailLabel.grid(row=0,column=1,padx=5,pady=5)

    emailEntry=Entry(root,textvariable=emailid,width=30)
    emailEntry.grid(row=0,column=2,padx=5,pady=5)

    sendOTPbutton=Button(root,text="Send OPT",command=sendOTP,width=20)
    sendOTPbutton.grid(row=0,column=3,padx=5,pady=5)

    root.msgLabel=Label(root,bg="deepskyblue3")
    root.msgLabel.grid(row=1,column=1,padx=5,pady=5,columnspan=3)

    otpLabel=Label(root,text="Enter the OPT : ",bg="deepskyblue3")
    otpLabel.grid(row=2,column=1,padx=5,pady=5)

    root.otpEntry=Entry(root,textvariable=otp,width=30,show="*")
    root.otpEntry.grid(row=2,column=2,padx=5,pady=5)

    validateOTP=Button(root,text="Validate OTP",command=validate,width=20)
    validateOTP.grid(row=2,column=3,padx=5,pady=5)

    root.otpLabel=Label(root,bg="deepskyblue3")
    root.otpLabel.grid(row=3,column=1,padx=5,pady=5,columnspan=3)


# Defining sendOTP() to generate and send OTP to user-input email-id
def sendOTP():
    # Storing digits from 0 to 9 as String in numbers variables & declaring empty string
    #variable named root.genOTP
    numbers="0123456789"
    root.genOTP=""
    #Fetching and storing user-input mail id in receiverEmail variable
    receiverEmail=emailid.get()

    #Generating 6-digits OTP
    for i in range(6):

        root.genOTP+=numbers[int(random.random()*10)]
        # Concatenating and Storing generated OTP with messages to be sent in otpMSG
        otpMSG="YOUR OTP IS : "+root.genOTP

        #Creating instance of class MIMEMultipart()
        message=MIMEMultipart()
        #Storing the email details in respective fields
        message['FROM']="OTP VALIDATOR (python_scripts)"
        message['TO']=receiverEmail
        message['Subject']="OTP VALIDATION"
        #Attaching the otpMSG with MIME instance
        message.attach(MIMEText(otpMSG))
        #creating a smtp session 
        smtp=smtplib.SMTP('smtp.gmail.com',587)
        # Starting TLS for security 
        smtp.starttls()
        #Authenticating the sender using the login() method
        smtp.login("sender's email address","sender's email password")
        #Sending the email with Multipart message converted into string
        smtp.sendmail("sender's email address",receiverEmail,message.as_string())
        #Terminating the session
        smtp.quit()
        #Formatting receiveEmail to replace(hide) mail id with *
        receiverEmail='{}********{}'.format(receiverEmail[0:2],receiverEmail[-10:])
        #Displaying the success message 
        root.msgLabel.config(text="OTP HAS BEEN SENT TO"+receiverEmail)

# Defining validOTP() to validate user-input OTP mail with script generated OTP 
def validate():
    #Storing user-input OTP
    userInputOTP=otp.get()
    #Storing system generated OTP
    systemOTP=root.genOTP

    #Validating OTP
    if userInputOTP==systemOTP:

        root.otpLabel.config(text="OPT VALIDATED SUCCESSFULLY")
    else:
        root.otpLabel.config(text="INVALID OTP")

#Creating object of class tk
root=tk.Tk()

#Setting the title, background color and disabling the resizing property
root.title("EmailOTP")
root.resizable(False,False)
root.config(background="deepskyblue3")

#Creating tkinter variables
emailid=StringVar()
otp=StringVar()

#Calling the CreateWidget() function with argument bgColor
CreateWidget()

#Defining infinite loop to run application
root.mainloop()
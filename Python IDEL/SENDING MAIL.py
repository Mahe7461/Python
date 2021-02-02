#send amail using python
#syntax
import smtplib
sender='mahe7461@gmail.com'
receivers=['karajohn906@gmail.com']
message='hello'
try:
    smtpObj=smtplib.SMTP('smtp.gmail.com',465)
    smtpObj.sendmail(sender ,receivers,message)
    print ('mail send successfully')
except SMTPException:
    print ('Error: unable to send email')





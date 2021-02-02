

import smtplib
# it create smtp session
s=smtplib.SMTP(host='smtp.gmail.com',port=587)
#start TLS for security
s.nehlo()
s.starttls()
#Authentication
s.login('mahea956@gmail.com','Imissu@123')
#message
message=' hello '
#to send the message
s.sendmail('mahea956@gmail.com','mahe7461@gmail.com',message)
#terminating session
s.quit()    

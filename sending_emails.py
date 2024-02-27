import getpass, smtplib

# Connect to Gmail
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())
print(smtp_object.starttls())

# User authentication
email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')
smtp_object.login(email, password)

# Email payload
from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Enter the message: ")
msg = "Subject " + subject + "\n" + message

# Send email
smtp_object.sendmail(from_address, to_address, msg)

# Close session
smtp_object.quit()









import email, getpass, imaplib

# Connect to Gmail
M = imaplib.IMAP4_SSL('imap.gmail.com')

# User authentication
e_mail = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')
M.login(e_mail, password)

# Select folder to extract data from
M.select('Inbox')

# Search for email using subject
typ, data = M.search(None, 'SUBJECT "NEW TEST"')
print(typ) # Should print 'OK' if no error
print(data) # Email IDs

# Unique Email ID
email_id = data[0]

result, email_data = M.fetch((email_id, '(RFC822)'))

# Clean up results
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():

    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)









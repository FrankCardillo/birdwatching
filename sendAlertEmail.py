import smtplib, ssl, json

def sendAlertEmail(licensePlate):
    port = 465  # For SSL
    password = ''

    with open('./config/env.json') as configFile:
        data = json.load(configFile)
        password = data['emailPassword']
        
    # Create a secure SSL context
    context = ssl.create_default_context()

    senderEmail = "metalbirdwatching@gmail.com"
    receiverEmail = "frankiecardillo2@yahoo.com"
    message = 'Subject: A blacklisted license plate has appeared \n This license plate is in your hood: {}.'.format(licensePlate)

    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context)
    server.login(senderEmail, password)
    server.sendmail(senderEmail, receiverEmail, message)
    server.quit()

sendAlertEmail('8CB651')
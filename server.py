from Adafruit_IO import *
import csv
while True: 
    aio = Client('giollers','aio_EQnq51ltfn5sEhP7N3chUJ31IyE9')
    value = aio.receive('data').value
    values=[]
    with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';') 
        for row in reader:
	    values.append(row[0])
    values.append(temp) #we add the latest data
    values.pop(0) #we erase the oldest data
    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')

        for i in range(len(values)):
            writer.writerow([values[i]])

    mail=aio.receive('control')
    plant = "ficus"
    threshold = 0
    last_values=[]
    with open('threshold.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:                    
	    if row[0]==plant:
		    threshold=row[1]
	
    with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            last_values.append(row[0])
        if int(last_values[-1])<int(threshold):
	aio.send('control', 1)   
        else:
	    aio.send('control', 0)


    if mail==0 and aio.receive('control')==1:
        import smtplib
        sender_email = "theo.sigaud@gmail.com"
        rec_email = "theo.sigaud@gmail.com"
        password = "cindy77120"
        message = "Your plantcare is activated."
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)

    if mail==1 and aio.receive('control')==0:
        import smtplib
        sender_email = "theo.sigaud@gmail.com" 
        rec_email = "theo.sigaud@gmail.com"
        password = "cindy77120"
        message = "Plant caring done.”
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)

import pandas
import datetime as dt
import random
import smtplib

your_name = "Your_Name"
# Getting today's month and day
now = dt.datetime.now()
today_day = now.day
today_month = now.month

# Reading CSV file and creating a dataframe
data = pandas.read_csv('birthdays.csv')

# Converting dataframe into a dictionary in which key is a tuple
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

# checking if today's month and day matches with any key in the birthdays_dict
if (today_month, today_day) in birthdays_dict:

    # Holding a value of the key that matches today's month and day
    birthday_person = birthdays_dict[(today_month, today_day)]

    # selecting a random letter from folder letter_templates
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # Opening the selected letter
    with open(file_path) as r_file:

        # Reding contents of the selected letter
        content = r_file.read()

        # Replacing [NAME] with the person name in selected letter
        letter = content.replace("[NAME]", birthday_person["name"]).replace("[Your Name]", your_name)

    # Setting up the SMTP server
    # Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    with smtplib.SMTP('smtp.gmail.com') as connection:  # SMTP server of your email service provider
        # your email
        my_email = "you_email@abc.com"

        # password of your email account
        my_password = "password"

        # Recipient email address from the csv file
        recipient_email = birthday_person["email"]

        # Applying TLS and sending mail
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"Subject:Birthday wish\n\n{letter}")

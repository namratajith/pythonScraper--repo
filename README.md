
Amazon Price Checker
This Python script allows you to track the price of a specific Amazon product and sends an email notification when the price drops below a certain threshold.

Features
Price Monitoring: Monitors the price of a specified Amazon product.
Email Notification: Sends an email notification if the price drops below a set value.
How to Use
Setup:

Ensure you have Python installed.
Install the required libraries by running pip install requests and pip install beautifulsoup4 in your terminal or command prompt.
Configuration:

Modify the URL variable in the script to the Amazon product URL you want to track.
Set your desired price threshold in the check_price() function (if (converted_price < 1700):).
Run the Script:

Execute the script in your Python environment.
Email Configuration:

Update the send_mail() function:
Set up a Gmail account for sending emails.
Replace 'ed.magician@gmail.com' with your Gmail address.
Update 'mjutimzlroarivxo' with your Gmail account's App Password (if you have 2-factor authentication enabled).
Change the receiver email address 'simo.edwin@yahoo.com' to the email where you want to receive notifications.
Exiting:

The script will continuously monitor the price and send an email when it meets the specified conditions. To stop the script, interrupt the program in your Python environment.
Security Note
Email Credentials: Ensure your email credentials (username and password) are kept secure and not shared.
Gmail Access: If you're using a Gmail account, consider enabling less secure app access or using App Passwords for better security.

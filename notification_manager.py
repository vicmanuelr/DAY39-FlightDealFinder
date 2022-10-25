import smtplib
import os
from flight_data import FlightData


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message: FlightData, email_to):
        MY_EMAIL = os.environ.get("EMAIL")
        MY_PASSWORD = os.environ.get("EMAIL_PW")
        composed_message = f"Low price alert! Only ${message.price} to fly to {message.destination_city}, from {message.out_date}, to {message.return_date}.\n{message.book_link}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as msg:
            msg.starttls()
            msg.login(user=MY_EMAIL, password=MY_PASSWORD)
            msg.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email_to,
                msg=f"Subject:Flight Alert from Victor Flight Club!\n\n{composed_message}",
            )

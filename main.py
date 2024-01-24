from bs4 import BeautifulSoup
import requests
import smtplib

# Your email credentials
MY_EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
RECEIVER_EMAIL = "ENTER RECEIVER MAIL ADRESS"

# Amazon product URL to track (I choose this product.if you want other products you can change the url.)
URL = "https://www.amazon.com.tr/dp/B0813RJRYC?ref_=cm_sw_r_cp_ud_dp_FF4CK9B11M4QAQHJXT3S"

# Headers to mimic a user request
headers = {
    "User-Agent": "ENTER YOUR OWN INFORMATIONS FROM https://myhttpheader.com/",
    "Accept-Language": "ENTER YOUR OWN INFORMATIONS FROM https://myhttpheader.com/",
}

# Send a request to the Amazon page
response = requests.get(URL, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, "lxml")

# Extract the product price
price = soup.find(name="span", class_="a-offscreen").get_text()

# Process the price to convert it to a float
price_without_currency = price.split("TL")[0]
remove_dot = price_without_currency.replace(".", "")
string_to_float = remove_dot.replace(",", ".")
float_price = float(string_to_float)

# Check if the price is below a threshold
if float_price < 10000:
    # Setup the email connection 
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)

    # Send an email alert
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECEIVER_EMAIL,
        msg="Subject: Cheap LEGO\n\n Cheap LEGO alert"
    )

    # Close the email connection
    connection.close()

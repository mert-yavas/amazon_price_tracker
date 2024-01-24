# Amazon Price Tracker
## Overview
Hello, I'm Mert, and today marks Day 47 of my "100 Days of Python" challenge. In this project, I've developed a Python script named 'main.py' that serves as an Amazon price tracker. The script monitors the price of a specific product on Amazon and sends an email alert if the price drops below a set threshold.

## Project Description
The script uses web scraping with BeautifulSoup to extract the price of a product from its Amazon page. It then converts the price to a float for comparison. If the price is below a specified threshold, the script sends an email alert using the smtplib library. The goal is to automate the process of tracking Amazon product prices.

## How to Run
To use the Amazon Price Tracker script, follow these steps:

* Open the Python script: main.py
```bash
   python main.py
```
* Fill in your email credentials, the receiver's email address, and the Amazon product URL.
* Customize the User-Agent and Accept-Language headers in the script based on your browser's information.
* Run the script to monitor the product's price on Amazon.
* Make sure you have the required libraries installed (requests, beautifulsoup4).
## Project Files
* main.py: The main Python script for tracking Amazon product prices and sending email alerts.
## Customization
Feel free to customize the script by modifying the headers, email credentials, and the product URL according to your needs. You can also adjust the price threshold for triggering email alerts.

## Dependencies
The project relies on the following Python libraries:

* requests: For making HTTP requests to scrape Amazon product information.
* BeautifulSoup: For parsing HTML and extracting the product price.
* smtplib: For sending email alerts.
## Educational Insights
Through this project, you can gain insights into the following:

* Web Scraping: Learn the basics of web scraping using BeautifulSoup.
* Price Tracking: Understand how to monitor and track product prices on e-commerce websites.
* Email Alerts: Implement email alerts based on specific conditions.
* Header Customization: Explore how to use headers to mimic user requests and avoid blocking.
## Conclusion
I hope you find the Amazon Price Tracker script useful for keeping an eye on product prices. Feel free to explore, modify, and adapt the script to suit your specific needs. Happy coding!

Note: Be respectful when scraping websites and always check the website's terms of service.

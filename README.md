# Price_tracker
This Python script serves as an automated price tracking and email alert system for a specific Amazon product. It continuously monitors the price of a designated product listed on Amazon India. Here's an introduction for the code:

"**Automated Amazon Price Tracker and Email Notifier**

This Python script is designed to monitor the price of a particular product listed on Amazon India. Using web scraping techniques, it extracts the current price of the product and checks whether it has fallen below a specified threshold (in this case, 11,000 INR). When the price drops below this threshold, the script sends an email notification to alert the user about the price drop.

The script employs the following key components:
- Web scraping with the 'requests' and 'BeautifulSoup' libraries to extract product information from Amazon's website.
- Continuous monitoring enabled by an infinite loop ('while True') to periodically check the product's price.
- Email notifications powered by the 'smtplib' library, allowing the script to send alerts via Gmail.

This code provides a practical example of how to automate price tracking for online shopping, ensuring users are promptly informed when a product's price meets their desired criteria. It can be customized for various products and price thresholds, making it a valuable tool for savvy online shoppers."

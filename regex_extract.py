import re

# Sample input text
text = """
Contact: user@example.com, firstname.lastname@company.co.uk
Website: https://www.example.com, https://sub.example.org/page
Phone: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Hashtags: #example #ThisIsAHashtag
Meeting at 14:30 tomorrow.
Reminder set for 2:30 PM.
Wake-up time is 07:00.
Event starts at 12:15 am.
"""

# Regular Expressions
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'(\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4})'
credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
hashtag_pattern = r'#\w+'
time_24hr_pattern = r'\b([01]?\d|2[0-3]):[0-5]\d\b'
time_12hr_pattern = r'\b(1[0-2]|0?[1-9]):[0-5]\d\s?(AM|PM|am|pm)\b'

# Finding matches
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)
credit_cards = re.findall(credit_card_pattern, text)
hashtags = re.findall(hashtag_pattern, text)
times_24hr = re.findall(time_24hr_pattern, text)
times_12hr = re.findall(time_12hr_pattern, text)

# Output
print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("Credit Card Numbers:", credit_cards)
print("Hashtags:", hashtags)
print("24-Hour Times:", [match for match in times_24hr if match])  # filter non-empty
print("12-Hour Times:", ['{} {}'.format(hour, meridiem) for hour, meridiem in times_12hr])

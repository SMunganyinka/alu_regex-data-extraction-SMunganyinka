# 🔍 ALU Regex Data Extraction - Shakira

This project showcases how to extract structured data using **Regular Expressions** in Python from raw text.



## 📌 Features

This project extracts the following data patterns from a large text string:

- ✅ **Email addresses** (e.g., `user@example.com`)
- ✅ **URLs** (e.g., `https://example.com`)
- ✅ **Phone numbers** in multiple formats (e.g., `(123) 456-7890`, `123-456-7890`)
- ✅ **Credit card numbers** (e.g., `1234 5678 9012 3456`)
- ✅ **Hashtags** (e.g., `#ExampleHashtag`)
- ✅ **Time formats** (24-hour and 12-hour like `14:30`, `2:30 PM`)

---

## 🛠️ Technologies Used

- Python 3.13.2
- Regular Expressions (`re` module)

---

## 📁 Project Structure


alu_regex-data-extraction-SMunganyinka/
├── regex_extract.py  # Main Python script
└── README.md         # Project documentation
🚀 How to Run
Clone the repository:


git clone https://github.com/SMunganyinka/alu_regex-data-extraction-SMunganyinka.git
cd alu_regex-data-extraction-SMunganyinka
Run the script:


python3 regex_extract.py
View the output:
The extracted data will be printed in the terminal under relevant categories.

---

🧪 Example Output

Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'https://sub.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit Card Numbers: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Hashtags: ['#example', '#ThisIsAHashtag']
24-Hour Times: ['14:30', '07:00']
12-Hour Times: ['2:30 PM', '12:15 am']

---

✅ Regex Patterns Used
Type	Regex Pattern
Email	\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}\b
URL	https?://[^\s]+
Phone Number	\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}
Credit Card	\b(?:\d{4}[- ]?){3}\d{4}\b
Hashtag	#\w+
Time (24-hour)	`\b(?:[01]?\d
Time (12-hour)	`\b(1[0-2]

---

📬 Contact
Shakira
📧 Email: s.munganyin@alustudent.com
🔗 GitHub: github.com/SMunganyinka
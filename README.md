# 🕷️ Freelancer Job Scraper
This is a Python script that uses Selenium to scrape freelance job listings from Freelancer.com. You can specify a keyword (e.g., python, react, scraping) and the number of pages to scrape. It will return a list of job titles, descriptions, and direct links to the job posts.

## 🚀 Features
- Headless browser scraping using Selenium and Chrome
- Automatically installs the correct ChromeDriver
- Customizable keyword and pagination
- Extracts:
  - Job Title
  - Job Description
  - Job Link

## 🧰 Technologies Used
- Python 3
- Selenium
- webdriver-manager
- ChromeDriver

## 📦 Installation
1. Clone the repository:
    git clone https://github.com/yourusername/freelancer-job-scraper.git
    cd freelancer-job-scraper
2. Create a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
    pip install -r requirements.txt

    requirements.txt content:
      selenium
      webdriver-manager
   
## 🧪 Usage
Run the script in your terminal:
  python freelancer_scraper.py
Then enter a keyword when prompted, for example:
  Enter keyword (e.g. python, react, scraping): python
The script will then scrape and print job listings for the first 2 pages.

## 📝 Example Output
🔹 Python Script for Data Extraction
Extract data from a website using Python and BeautifulSoup.
https://www.freelancer.com/projects/python/Python-Script-for-Data-Extraction
------------------------------------------------------------

## ⚠️ Disclaimer
This script is intended for educational purposes only. Scraping websites may violate their terms of service. Always ensure you have permission before running automated scripts on any site.

## 📄 License
MIT License

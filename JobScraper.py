from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_freelancer_jobs(keyword="python", pages=2):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    all_jobs = []
    base_url = "https://www.freelancer.com/jobs/"

    for page in range(1, pages + 1):
        url = f"{base_url}{keyword}/?pg={page}"
        print(f"Scraping page {page}: {url}")
        driver.get(url)
        time.sleep(3)  # wait for JavaScript content to load

        job_cards = driver.find_elements(By.CLASS_NAME, "JobSearchCard-item")

        for card in job_cards:
            try:
                title_elem = card.find_element(By.CLASS_NAME, "JobSearchCard-primary-heading-link")
                desc_elem = card.find_element(By.CLASS_NAME, "JobSearchCard-primary-description")

                job = {
                    "title": title_elem.text.strip(),
                    "description": desc_elem.text.strip(),
                    "link": title_elem.get_attribute("href")
                }
                all_jobs.append(job)

            except Exception as e:
                print("Skipping a job card due to error:", e)
                continue

    driver.quit()
    return all_jobs

# Example usage
if __name__ == "__main__":
    keyword = input("Enter keyword (e.g. python, react, scraping): ").strip().lower()
    scraped_jobs = scrape_freelancer_jobs(keyword=keyword, pages=2)

    for job in scraped_jobs:
        print(f"\n🔹 {job['title']}")
        print(f"{job['description']}")
        print(f"{job['link']}")
        print("-" * 60)

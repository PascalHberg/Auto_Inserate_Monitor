import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import MIN_PS, MAX_KM, MAX_PRICE


class OtoMotoScraper:
    def __init__(self, logger):
        self.logger = logger

    def scrape(self):
        chromedriver_autoinstaller.install()

        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=options)

        results = []

        try:
            url = (
                "https://www.otomoto.pl/osobowe/"
                f"?search%5Bfilter_float_engine_power%3Afrom%5D={MIN_PS}&"
                f"search%5Bfilter_float_mileage%3Ato%5D={MAX_KM}&"
                f"search%5Bfilter_float_price%3Ato%5D={MAX_PRICE}&"
                "search%5Bfilter_enum_gearbox%5D=automatic"
            )

            driver.get(url)

            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article")))

            items = driver.find_elements(By.CSS_SELECTOR, "article")

            for item in items:
                try:
                    title = item.find_element(By.CSS_SELECTOR, "h1, h2, h3").text
                    link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

                    if not link:
                        continue

                    results.append({
                        "title": title,
                        "link": link
                    })

                except:
                    continue

        except Exception as e:
            self.logger.error(f"Scraper Fehler: {e}")

        finally:
            driver.quit()

        return results

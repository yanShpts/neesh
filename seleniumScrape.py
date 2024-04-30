from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Extension ID for Glimpse (from the Chrome Web Store link)
extension_id = "ocmojhiloccgbpjnkeiooioedaklapap"

# Add the extension to Chrome using its ID
options.add_extension('Unconfirmed 513673.crdownload')

# Create the Chrome driver instance with the extension installed
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
url = "https://trends.google.com/trends/explore?date=today%205-y&q=youtube"  # Replace with the actual URL
driver.get(url)

#wait for the page to load 
wait = WebDriverWait(driver, 30)
wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

# Find the span element with the class "font-bold"
span_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.font-bold")))

# Extract the text content from the span element
text_content = span_element.text
print(text_content)

# Close the browser
driver.quit()
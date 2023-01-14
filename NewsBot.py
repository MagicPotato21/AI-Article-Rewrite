from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess


# Initialize webdriver
driver = Firefox()

# Navigate to CNN Business Tech page
driver.get("https://edition.cnn.com/business/tech")

# Wait for the first article to be loaded
wait = WebDriverWait(driver, 10)
container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container__text.container_lead-plus-headlines-with-images__text")))

# Click on the first article
container.click()

# Wait for the article title to be loaded
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".headline__wrapper")))

# Copy the article title
title = driver.find_element(By.ID, "maincontent").text

# Copy the article content
content_elements = driver.find_elements(By.CSS_SELECTOR, "div.article__content p.paragraph.inline-placeholder")
content = [element.text for element in content_elements]

# Save the title and content to a text file
with open("article.txt", "w", encoding="utf-8") as f:
    f.write(title + "\n\n" + "\n\n".join(content))

# Close the webdriver
driver.quit()

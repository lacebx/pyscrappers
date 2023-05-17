import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the webdriver and load the page
driver = webdriver.Chrome()
driver.get('siteURL') 

# Wait for the yourthing links to be loaded
yourthing_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.container of what you want to scrape')))

# Create a list to hold the yourthing names
yourthing_names = []

# Iterate through each yourthing link and extract the yourthing name
for yourthing_link in yourthing_links:
    driver.execute_script("arguments[0].scrollIntoView(true);", yourthing_link)
    yourthing_name_elems = yourthing_link.find_elements(By.CSS_SELECTOR, 'actual text/thing you want to scrape')
    for yourthing_name_elem in yourthing_name_elems:
        yourthing_name = yourthing_name_elem.get_attribute('innerText').strip()
        if yourthing_name:
            yourthing_names.append(yourthing_name)  

# Write the yourthing names to a CSV file
with open('yourthings.csv', 'w', newline='') as csvfile:
    fieldnames = ['yourthings']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for yourthing_name in yourthing_names:
        writer.writerow({'yourthings': yourthing_name})

# Quit the webdriver
driver.quit()

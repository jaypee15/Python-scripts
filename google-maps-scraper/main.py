from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import csv
import re



def get_business(city, business):
    driver = webdriver.Chrome()

    search_query = f'{business}+in+{city}'
    url = f'https://www.google.com/maps/search/{search_query}/'
    driver.get(url)

    results=[]


    ActionChains(driver)\
        .scroll_by_amount(0, 1000)\
        .perform()
    
    time.sleep(3)  
    elements = driver.find_elements(By.CSS_SELECTOR, 'div.Nv2PK')
    for element in elements:

     
        element.click()
        time.sleep(5)  

        website_href=""
        phone_number=""
        business_name=""
        address=""
        try:
            # Explicitly wait for the element to be visible and extract the href attribute
            website_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-item-id="authority"]'))
            )
            website_href = website_element.get_attribute('href')
            print("Website Href:", website_href)
        except Exception as e:
            print("Error:", e)

        
        try:
            # Find the button element with the data-item-id attribute
            button_element = driver.find_element(By.XPATH,'//button[contains(@data-item-id, "address")]')
            aria_label = button_element.get_attribute('aria-label')
            
            # Use regex to extract the address from the aria-label attribute
            address_match = re.search(r'Address: (.+)$', aria_label)
            if address_match:
                address = address_match.group(1)
                print("Address:", address)
            else:
                print("Address not found.")
        except Exception as e:
            print("Error:", e)

        try:
            # Find business name
            h1_elements = driver.find_elements(By.TAG_NAME, 'h1')
            if len(h1_elements) >= 2:
                h1_element = h1_elements[1] 
            else:
                h1_element = h1_elements[0]

            business_name = h1_element.text
            print("Business Name:", business_name)
        except Exception as e:
            print("Error:", e)

       
        try:
            # Find the button element with the data-item-id attribute
            button_element = driver.find_element(By.XPATH, '//button[contains(@data-item-id, "phone:tel:")]')
            data_item_id = button_element.get_attribute('data-item-id')
            
            # Use regex to extract the phone number from data-item-id
            phone_match = re.search(r'\+(?:\d+\s*)+', data_item_id)
            if phone_match:
                phone_number = phone_match.group(0)
                print("Phone Number:", phone_number)
            else:
                print("Phone number not found.")
        except Exception as e:
            print("Error:", e)

        results.append({'Business Name': business_name, 'Website': website_href, 'Address': address, 'Phone Number': phone_number})
            
    driver.close()
    return results



def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Business Name', 'Website', 'Address', 'Phone Number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    city = 'New York'  # Replace with the desired city
    business = 'cafe'
    companies = get_business(city, business)
    filename = f'{business}_in_{city}.csv'
    save_to_csv(companies, filename)
    print(f'Data saved to {filename}')

if __name__ == '__main__':
    main()

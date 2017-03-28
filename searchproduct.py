import time
from selenium import webdriver

# Create new Session
driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application homepage
driver.get("http://demo.magentocommerce.com/")

# Click on Search Button
search_button = driver.find_element_by_class_name("search")
search_button.click()

# Get the search textbox
search_field = driver.find_element_by_name("keys")
search_field.clear()

# Enter search keyword and Submit
search_field.send_keys("phones")
search_field.submit()

# Get Products Link
products_link = driver.find_element_by_link_text("products")
products_link.click()

# Wait until page reloads javascript || jQuery
time.sleep(5)

# Get all the anchor elements which have product names displayed currently on result page using
# xpath method
products = driver.find_elements_by_xpath("//div[@class='result-title']/a")

# Get the number of anchor elements found
print("Found %s products: " % str(len(products)))

# Iterate through each anchor element and print the text that is name of the product
for product in products:
    print(product.text)

# Close the browser window
driver.quit()

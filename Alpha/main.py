from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Firefox options for automated downloads
options = Options()
options.headless = False  # Set to True for headless mode

# Set up the WebDriver
driver = webdriver.Firefox(options=options)

try:
    # Navigate to the login page
    driver.get("https://app.runwayml.com/video-tools/teams/abcdef101198/dashboard")

    # Wait for the page to load
    time.sleep(5)  # Adjust this sleep time as needed for your page

    # Locate the "Username or Email" input field and enter the email
    email_field = driver.find_element(By.NAME, 'usernameOrEmail')
    email_field.send_keys('OCTOPUS777888')

    # Locate the "Password" input field and enter the password
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('K1betkilel')

    # Locate the "Log in" button and click it
    login_button = driver.find_element(By.XPATH, '//button[@type="submit" and .//span[text()="Log in"]]')
    login_button.click()

    # Wait for the login process to complete
    time.sleep(5)  # Adjust based on expected login time

    # Scroll until the "Text/Image to Video" button is visible and click it
    button_xpath = '//button[@type="button" and .//span[text()="Text/Image to Video"]]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
    button = driver.find_element(By.XPATH, button_xpath)
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

    # Click the "Select from Assets" button
    select_button_xpath = '//button[@class="ImageOrVideoPromptEmpty__Button-sc-17itqex-1 eFIKAk"]'
    select_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, select_button_xpath))
    )
    select_button.click()

    # Sleep for 10 seconds
    time.sleep(10)

    # Click the next specified element
    drag_drop_xpath = '//div[@class="Base__Box-sc-thne2y-0 eWuROf"]'
    drag_drop_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, drag_drop_xpath))
    )
    drag_drop_element.click()

    # Wait for the file input element to be present
    file_input_xpath = '//input[@type="file"]'
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, file_input_xpath))
    )
    
    # Path to the .jpg file
    file_path = os.path.expanduser("~/Documents/step.jpg")

    # Send the file path to the file input element
    file_input.send_keys(file_path)

    # Sleep for 10 seconds
    time.sleep(10)

    # Click the "Generate 4s" button
    generate_button_xpath = '//div[@data-state="closed"]//button[contains(@class, "GenerateButtonForNonUnlimitedPlans__Button-sc-uwwfm9-0")]'
    generate_button = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, generate_button_xpath))
    )
    time.sleep(5)
    generate_button.click()

    # Wait for 240 seconds (4 minutes) to ensure video generation is complete
    time.sleep(240)

    # Click the "Download video" button
    download_button_css = 'button[aria-label="Download video"]'
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, download_button_css))
    )
    download_button.click()
    print("Download started.")

    # Sleep for 20 seconds to allow the download to complete
    time.sleep(20)

finally:
    # Close the browser
    driver.quit()

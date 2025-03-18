import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

Website_link = "http://10.10.99.18:8002/login"
driver.get(Website_link)

time.sleep(3)

try:
    print("🔍 Searching for username field...")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    print("✅ Username field found!")

    time.sleep(1)

    print("🔍 Searching for password field...")
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    print("✅ Password field found!")

    time.sleep(1)

    username_field.send_keys("superadmin@gmail.com")
    password_field.send_keys("Dost@123")

    print(f"🔍 Username entered: {username_field.get_attribute('value')}")
    print(f"🔍 Password entered: {password_field.get_attribute('value')}")

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login"))
        )
        print("✅ Login button found!")

        driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
        time.sleep(2)

        if login_button.is_displayed() and login_button.is_enabled():
            try:
                login_button.click()
                print("✅ Login button clicked!")
            except:
                print("⚠️ Normal click failed, using JavaScript click...")
                driver.execute_script("arguments[0].click();", login_button)

            WebDrivtime.sleep(3)
erWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("✅ Page Loaded Successfully!")

            time.sleep(15)

            expected_url = "http://10.10.99.18:8002/dashboard"
            WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
            print("✅ Redirected to Dashboard Successfully!")

            assert "Dashboard" in driver.page_source, "❌ Error: 'Dashboard' text not found!"
            print("✅ Assert Passed: 'Dashboard' text is present on the page!")


            invalid_texts = ["00 Jan 0000", "00 Dec 0000"]
            for text in invalid_texts:
                if text in driver.page_source:
                    print(f"❌ FAILED: Invalid text detected - '{text}'")
                    driver.quit()
                    exit()

            print("✅ All texts are valid!")

        else:
            print("⚠️ Login button is not clickable!")

    except TimeoutException:
        print("❌ Login Failed! Error: TimeoutException (Login button not found)")
        driver.quit()
        exit()

except (NoSuchElementException, TimeoutException, Exception) as e:
    print(f"❌ Login Failed! Error: {repr(e)}")
    driver.quit()
    exit()

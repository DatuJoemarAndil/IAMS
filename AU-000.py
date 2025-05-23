from LOGIN import AuditLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

login_bot = AuditLogin()
login_bot.login()
login_bot.go_to_audit_page()

driver = login_bot.driver
wait = login_bot.wait

try:
    add_icon_colored = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fas fa-plus text-white-100']")))
    add_icon_colored.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='aud_title']")))

    audit_title_field = wait.until(EC.element_to_be_clickable((By.ID, "aud_title")))
    audit_title_field.clear()
    audit_title_field.send_keys("Annual Compliance Audit")

    audit_type_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'select2-selection')]"))
    )
    audit_type_dropdown.click()

    audit_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Environmental')]")))
    audit_option.click()

    aud_period_from_dropdown = wait.until(EC.presence_of_element_located((By.ID, "aud_period_from")))
    select_period_from = Select(aud_period_from_dropdown)
    select_period_from.select_by_value("2020")

    aud_period_to_dropdown = wait.until(EC.presence_of_element_located((By.ID, "aud_period_to")))
    select_period_to = Select(aud_period_to_dropdown)
    select_period_to.select_by_value("2025")

    audit_code_field = wait.until(EC.presence_of_element_located((By.ID, "aud_code")))
    audit_code_field.clear()
    audit_code_field.send_keys("AUTO-2025-001")

    audit_desc_field = wait.until(EC.presence_of_element_located((By.ID, "aud_desc")))
    audit_desc_field.clear()
    audit_desc_field.send_keys("Automated description for this audit entry.")

    remarks_field = wait.until(EC.presence_of_element_located((By.ID, "aud_remarks")))
    remarks_field.clear()
    remarks_field.send_keys("Automated remarks entry by Selenium.")

    field_to_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#audit-form > div:nth-child(4) > div > span > span.selection > span")))
    field_to_input.click()
    field_to_input.send_keys("SAMPLE")
    field_to_input.send_keys(Keys.RETURN)

    save_button = wait.until(EC.element_to_be_clickable((By.ID, "addAudit")))
    save_button.click()

    time.sleep(2)

finally:
    login_bot.quit()

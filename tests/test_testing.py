from selenium import webdriver
from selenium.webdriver.common.by import By


def test_bob():
    print("Starting on the earth")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.icloud.com/")

    driver.find_element(By.CSS_SELECTOR, ".sign-in-button").click()
    frame_index = 0
    driver._switch_to.frame(frame_index)
    driver.find_element(
        By.XPATH, "//div[@id='sign_in_form']/div/div/div/div/div/input").click()
    driver.find_element(
        By.XPATH, "//div[@id='sign_in_form']/div/div/div/div/div/input").send_keys("vishnuvardhanuv36@gmail.com")
    driver.find_element(By.XPATH, "//button[@id='sign-in']/i").click()
    driver.find_element(
        By.XPATH, "//div[@id='sign_in_form']/div/div/div[2]/div/div/input").send_keys("Chandra@12")
    driver.find_element(By.XPATH, "//button[@id='sign-in']/i").click()
    print("ended")

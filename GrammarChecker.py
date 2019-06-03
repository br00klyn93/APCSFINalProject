# Written by Nikhil Alapati
# Licence: Open Source
# This program logs in grammarly and checks the document for errors


# imports selenium API for controlling website
from selenium import webdriver
# imports keys fromm slenium
from selenium.webdriver.common.keys import Keys
# imports time for getting the program to sleep while the grammarly does its work
import time
# uses the chrome driver to navigate grammarly
import pickle


# function for logging in requires username and password


def login(driver, username, password):

    driver.find_element_by_class_name(
        "_2IV5P-_-_-client-guidelines-input_field--input_field-input").send_keys(username)  # Finds the username text box and sends the username
    time.sleep(0.5)
    driver.find_element_by_class_name(
        "_2IV5P-_-_-client-guidelines-input_field--input_field-input").send_keys(Keys.TAB, password, Keys.RETURN)  # types the password

# checks the document


def CheckDocument(driver, document):
    driver.find_element_by_class_name(
        "_758e07ad-document_item-add").click()  # finds the add new doc button
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id=\"page\"]/div/div/div/div/div[2]/div[1]/div[8]/div[3]/div[1]/div[1]/div/div/div[1]/input").send_keys(Keys.TAB, document)  # finds the text box to paste the text form the document
    time.sleep(6.5)
    driver.find_element_by_xpath(
        "//*[@id=\"page\"]/div/div/div/div/div[2]/div[1]/div[8]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]").click()  # finds the view all alerts button to close the "get premium tab"


def PostUrlCookies(driver):
    cookie = str(driver.get_cookies())
    print(cookie)
    print(driver.current_url)

# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("https://saucelabs.com/")
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul[2]/li/a").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul[2]/li[2]/a").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul[2]/li[3]/a").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul[2]/li[3]/a[2]").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul/li/a").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul/li[3]/a").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul/li[5]/a").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul/li[2]/a").click()
        driver.find_element_by_css_selector("img.sauce-logo-img").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul/li[4]/a").click()
        driver.find_element_by_link_text("Sauce Labs").click()
        driver.find_element_by_css_selector("a.hamburger").click()
        driver.find_element_by_xpath("//nav[@id='global']/div/section/ul/li[6]/a").click()
        driver.get(self.base_url + "/")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

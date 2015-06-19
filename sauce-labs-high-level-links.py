# -*- coding: utf-8 -*-
# CS82A - Automation Project - Ibrahima Sow
# Version 2
# https://github.com/ibrsow/cs82a/blob/master/sauce-labs-high-level-links.py
# http://www.screencast.com/t/hwLRb4Xq3
#
# This module Create a Selenium test to automate the checking of the high-level links behind
# the three-horizontal-bar glyph in the header of the Sauce Labs home page: RESOURCES, PRICING,
# FEATURES, DOCS, SIGN UP, COMPANY, ENTERPRISE, LOGIN, COMMUNITY, and SOLUTIONS.

from selenium import webdriver
import unittest

links_landing_pages = {
    "RESOURCES"  : "//a[contains(text(),'Resources')]",        # <a href="https://saucelabs.com/resources" title="Resources">
    "PRICING"    : "//a[contains(text(),'Pricing')])[3]",      # <a title="Pricing" href="/pricing">
    "FEATURES"   : "//a[contains(text(),'Features')])[3]",     # <a href="/features">
    "DOCS"       : "//a[contains(text(),'Docs')])[3]",         # <a href="https://docs.saucelabs.com/?_ga=1.138110450.398500475.1434607228" title="Docs">
    "SIGN UP"    : "//a[contains(text(),'Sign up')]",          # <a href="https://saucelabs.com/signup/trial" title="Sign up">
    "COMPANY"    : "//a[contains(text(),'Company')])[2]",      # <a href="https://saucelabs.com/our-values">
    "ENTERPRISE" : "//a[contains(text(),'Enterprise')])[3]",   # <a href="https://saucelabs.com/enterprise" title="Enterprise">
    "LOGIN"      : "//a[contains(text(),'Login')]",            # <a href="https://saucelabs.com/login" title="Log in">
    "COMMUNITY"  : "//a[contains(text(),'Community')]",        # <a href="https://saucelabs.com/opensauce" title="Community">
    "SOLUTIONS"  : "//a[contains(text(),'Solutions')]",        # <a href="https://saucelabs.com/selenium" title="Solutions">
    }

class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"

    def test_sauce_labs_headers(self):
        driver = self.driver
        glyph  = "//a[contains(@href, '#')]"

        for link in links_landing_pages:
            driver.get(self.base_url)
            driver.find_element_by_xpath(glyph).click()
            driver.find_element_by_link_text(link).click()

    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

'''
# -*- coding: utf-8 -*-
# CS82A - Automation Project - Ibrahima Sow
# Version 1

class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        glyph         = "//a[contains(@href, '#')]"

    def test_sauce_labs_headers(self):
        driver = self.driver

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("//a[contains(text(),'Resources')]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("(//a[contains(text(),'Pricing')])[3]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("(//a[contains(text(),'Features')])[3]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("(//a[contains(text(),'Docs')])[3]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("//a[contains(text(),'Sign up')]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("(//a[contains(text(),'Company')])[2]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("(//a[contains(text(),'Enterprise')])[3]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("//a[contains(text(),'Community')]").click()

        driver.get(self.base_url)
        driver.find_element_by_xpath(glyph).click()
        driver.find_element_by_xpath("//a[contains(text(),'Solutions')]").click()

    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
'''

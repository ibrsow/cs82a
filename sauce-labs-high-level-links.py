# -*- coding: utf-8 -*-
# CS82A - Automation Project - Ibrahima Sow
#
# This module Create a Selenium test to automate the checking of the high-level links behind
# the three-horizontal-bar glyph in the header of the Sauce Labs home page: RESOURCES, PRICING,
# FEATURES, DOCS, SIGN UP, COMPANY, ENTERPRISE, LOGIN, COMMUNITY, and SOLUTIONS.


from selenium import webdriver
import unittest

links_landing_titles = {
    "RESOURCES"  : r'Resources',
    "PRICING"    : r'Pricing',
    "FEATURES"   : r'Features',
    "DOCS"       : r'Docs',
    "SIGN UP"    : r'SignXXXX',
    "COMPANY"    : r'Company',
    "ENTERPRISE" : r'Enterprise',
    "LOGIN"      : r'Login',
    "COMMUNITY"  : r'Community',
    "SOLUTIONS"  : r'Solutions',
    }


class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
    
    def test_sauce_labs_headers(self):
        driver = self.driver

        for link in links_landing_titles:
            driver.get(self.base_url)
            driver.find_element_by_link_text(link).click()
            expected_title = links_landing_titles[link]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


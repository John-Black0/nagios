import sys
import time
import unittest
import warnings

from errno import ENETRESET
from unittest import TestCase
from selenium import webdriver
from genericpath import exists
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NagiosBelea(TestCase):

    def setUp(self):

        if not sys.warnoptions:
            warnings.simplefilter('ignore', ResourceWarning)

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('disable-gps')
        self.options.add_argument('ignore-certificate-errors')
        self.options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=self.options)

    def tearDown(self):
        self.driver.quit()

    def test_nagios_auto(self):
        #login
        self.driver.get('http://negru:test@monitor.jcs.jo/nagios1/check_mk/')
        time.sleep(1)
        url = 'view-source:http://monitor.jcs.jo/nagios1/check_mk/view.py?view_name=svcproblems'

        self.driver.get(url)
        get_source = self.driver.page_source
        search_text = 'Perflib Oracle11'
        if search_text in get_source:
            self.driver.get('http://monitor.jcs.jo/nagios1/check_mk/logwatch.py?host=fiberproject&file=Application')
            accept_button = self.driver.find_element(By.XPATH, '//a[text()="Clear Log"]')
            accept_button.click()
            accept_button = self.driver.find_element(By.NAME, '_do_confirm')
            accept_button.click()
        
        time.sleep(1)
        self.driver.get(url)
        get_source = self.driver.page_source
        search_text = 'Schannel'
        if search_text in get_source:
            self.driver.get('http://monitor.jcs.jo/nagios1/check_mk/logwatch.py?host=fiberweb&file=System')
            accept_button = self.driver.find_element(By.XPATH, '//a[text()="Clear Log"]')
            accept_button.click()
            accept_button = self.driver.find_element(By.NAME, '_do_confirm')
            accept_button.click()

        time.sleep(1)
        self.driver.get(url)
        get_source = self.driver.page_source
        search_text = 'Software_Protection_Platform_Service'
        fiberweb = 'fiberweb'
        fiberproject = 'fiberproject'
        if search_text and fiberweb in get_source:
            self.driver.get('http://monitor.jcs.jo/nagios1/check_mk/logwatch.py?host=fiberweb&file=Application')
            accept_button = self.driver.find_element(By.XPATH, '//a[text()="Clear Log"]')
            accept_button.click()
            accept_button = self.driver.find_element(By.NAME, '_do_confirm')
            accept_button.click()
        elif search_text and fiberproject in get_source:
            self.driver.get('http://monitor.jcs.jo/nagios1/check_mk/logwatch.py?host=fiberproject&file=Application')
            accept_button = self.driver.find_element(By.XPATH, '//a[text()="Clear Log"]')
            accept_button.click()
            accept_button = self.driver.find_element(By.NAME, '_do_confirm')
            accept_button.click()
            
        time.sleep(1)
        self.driver.get(url)
        get_source = self.driver.page_source
        search_text = 'AutoEnrollment'
        if search_text in get_source:
            self.driver.get('http://monitor.jcs.jo/nagios1/check_mk/logwatch.py?host=fiberweb&file=Application')
            accept_button = self.driver.find_element(By.XPATH, '//a[text()="Clear Log"]')
            accept_button.click()
            accept_button = self.driver.find_element(By.NAME, '_do_confirm')
            accept_button.click()

if __name__ == '__main__':
    unittest.main()
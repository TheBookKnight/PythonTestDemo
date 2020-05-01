from selenium import webdriver
from SampleProject.POMDemo.Pages.GoogleMethods import GoogleMethods
import time
import unittest
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))


class GooglePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/cadavezj/PycharmProjects/PythonTestDemo/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_valid(self):
        driver = self.driver
        driver.get("https://google.com")
        googlemethods = GoogleMethods(driver)
        googlemethods.search("selenium python")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="C:/Users/cadavezj/PycharmProjects/PythonTestDemo/reports"))
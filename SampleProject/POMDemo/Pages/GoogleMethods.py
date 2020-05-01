from SampleProject.POMDemo.Locators.Google import Google


class GoogleMethods():

    def __init__(self, driver):
        self.driver = driver
        self.searchbar_name         = Google.searchbar_name
        self.googlesearch_btn_name  = Google.googlesearch_btn_name

    def search(self, query):
        self.driver.find_element_by_name(self.searchbar_name).clear()
        self.driver.find_element_by_name(self.searchbar_name).send_keys(query)
        self.driver.find_element_by_name(self.googlesearch_btn_name).click()
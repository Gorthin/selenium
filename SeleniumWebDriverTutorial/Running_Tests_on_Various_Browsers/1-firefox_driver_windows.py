from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService

class RunFFTests():

    def test(self):
        ffservice = FFService(executable_path="C:\webdriver\geckodriver.exe")
        # Instantiate Browser
        driver = webdriver.Firefox(service=ffservice)
        # Open the provided URL
        driver.get("https://www.letskodeit.com")

ff = RunFFTests()
ff.test()
import os
from selenium import webdriver

drivers_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'drivers'))

firefox_driver = webdriver.Firefox(executable_path='%s\%s' % (drivers_folder, 'geckodriver.exe'))
# ie_driver = webdriver.Ie(executable_path='%s\%s' % (drivers_folder, 'iedriverserver.exe'))
# chrome_driver = webdriver.Chrome(executable_path='%s\%s' % (drivers_folder, 'chromedriver.exe'))

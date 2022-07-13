# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMensajeinvitado():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mensajeinvitado(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1440, 774)
    self.driver.find_element(By.CSS_SELECTOR, "h5:nth-child(2)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(5)").text == "Inicia sesión o regístrate para obtener beneficios"
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand > span").click()
  

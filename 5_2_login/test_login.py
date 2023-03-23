from config.driver_config import DriverConfig

from time import sleep

driver = DriverConfig().driver_config()
driver.get("http://www.tcpjwtester.top")
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/div/input").send_keys("周杰伦")
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div/form/div[4]/div/div/input").send_keys("123456")
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div/form/button").click()
sleep(3)
driver.quit()

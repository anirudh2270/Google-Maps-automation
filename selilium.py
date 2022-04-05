from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'D:\python projects\chromedriver.exe')
driver.get('https://www.google.com/maps/@20.9880135,82.7525294,5z')
sleep(2)

def search_place():
    place = driver.find_element_by_class_name("tactile-searchbox-input")
    place.send_keys("Ambala")
    submit = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()

search_place()


def directions():
    sleep(10)
    directions = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button")
    directions.click()


directions()


def where_to_go():
    sleep(6)
    where_to_go = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    where_to_go.send_keys("Bengaluru, Karnataka")
    sleep(4)
    search = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()


where_to_go()

#shows total kilometers
def kilometers():
    sleep(6)
    Totalkilometers = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div")
    print("Total Kilometers:", Totalkilometers.text)


kilometers()


def Route():
    Route = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/h1[1]/span")
    print("Route available:", Route.text)

Route()




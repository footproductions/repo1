from selenium import webdriver
import yaml #import yaml module
yaml.warnings({'YAMLLoadWarning': False}) #bypasses Python Loader error on next line
from yaml.loader import Loader
import time #to include pause before closing out browser

#conf = yaml.load(open(loginDetails.yml))
conf = yaml.load(open('c:\\codemonkey\\loginDetails.yml'))
myLogin = conf['docker_user']['user']
myPassword = conf['docker_user']['passwordd']
url = 'https://id.docker.com/login/?next=%2Fid%2Foauth%2Fauthorize%2F%3Fclient_id%3D43f17c5f-9ba4-4f13-853d-9d0074e349a7%26next%3D%252F%253Fref%253Dlogin%26nonce%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI0M2YxN2M1Zi05YmE0LTRmMTMtODUzZC05ZDAwNzRlMzQ5YTciLCJleHAiOiIyMDIxLTA1LTI4VDE2OjI1OjUzLjc0MTIzNjI1MloiLCJpYXQiOiIyMDIxLTA1LTI4VDE2OjIwOjUzLjc0MTIzNjgwNFoiLCJyZnAiOiJ3S3YzQ2tNQVNMOGkwSFdVM0dLMVRRPT0iLCJ0YXJnZXRfbGlua191cmkiOiIvP3JlZj1sb2dpbiJ9.dtHZnBPqy_qzu2YNWe5eE2isBxHNRuJBSyHXceiMfbE%26redirect_uri%3Dhttps%253A%252F%252Fhub.docker.com%252Fsso%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%26state%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI0M2YxN2M1Zi05YmE0LTRmMTMtODUzZC05ZDAwNzRlMzQ5YTciLCJleHAiOiIyMDIxLTA1LTI4VDE2OjI1OjUzLjc0MTIzNjI1MloiLCJpYXQiOiIyMDIxLTA1LTI4VDE2OjIwOjUzLjc0MTIzNjgwNFoiLCJyZnAiOiJ3S3YzQ2tNQVNMOGkwSFdVM0dLMVRRPT0iLCJ0YXJnZXRfbGlua191cmkiOiIvP3JlZj1sb2dpbiJ9.dtHZnBPqy_qzu2YNWe5eE2isBxHNRuJBSyHXceiMfbE'

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='c:\\codemonkey\\chromedriver.exe')
#usernameId = 'nw_username'
#passwordId = 'nw_password'
#submit_buttonId = 'nw_submit'

def login(url ,usernameID, username, passwordID, password, submit_buttonID):
        driver.get(url)
        driver.find_element_by_id('nw_username').send_keys(myLogin)
        driver.find_element_by_id('nw_password').send_keys(myPassword)
        driver.find_element_by_id('nw_submit').click()

login(url, "nw_username", "myLogin", "nw_password", "myPassword", "nw_submit")

time.sleep (10) #pause to allow any broswer latency to finish.
#clean logoff clicks
driver.find_element_by_class_name('styles__username___oMG_s').click()
time.sleep (2)
driver.find_element_by_class_name('styles__ssoLogout___3S3jd').click()
time.sleep (3)
driver.close() #force close browser..no clean logoff







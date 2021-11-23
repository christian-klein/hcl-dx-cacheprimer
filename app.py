# CACHEPRIMER
# -----------
# This utility will check if the server is up and responding with a code lower than 
# 400 and then use Selenium to hit each page
# Usage: Create or edit .env in same directory or set environment variables
# -----------
# .env Structure:
# RETRIES=5
# WAIT=2
# PROTOCOL="http"
# URL="localhost:10039"
# PREFIX="/wps/portal"
# PAGES="/woodburnstudio/home", "/woodburnstudio/our-exhibitions","/woodburnstudio/our-products"
# Created using Python 3.8.10

# from os import curdir
import sys
import requests
import time

from decouple import Csv, config 
from selenium import webdriver

NOSTOP = False
retriesTotal = 0

RETRIES = int(config('RETRIES')) # 0 if indefinitely
WAITTIME = float(config('WAIT'))
PROTOCOL = config('PROTOCOL')
URL =config('URL')
PREFIX = config('PREFIX')
PAGES = config('PAGES', cast=Csv())

URL_PREFIX = '{}://{}{}'.format(PROTOCOL,URL,PREFIX)

if not RETRIES: NOSTOP = True

# Check if URL responds
success = False

print('*************** Cache Primer ***************')
print(' Target Server: {}'.format(URL_PREFIX))
if NOSTOP:
    print(' Retries: unlimited')
else:
    print(' Retries: {} Every: {}s'.format(RETRIES,WAITTIME))
print('--------------------------------------------')
print

while not success:
    retriesTotal += 1
    try:
        response = requests.get(URL_PREFIX)
    except requests.exceptions.ConnectionError:
        print('[{}] Could not connect to site {}'.format(retriesTotal, URL_PREFIX))
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
    else:
        if response.status_code < 400:
            success = True
        else:
            print('[{}] Could not connect to site {}. HTTP Code {}'.format(retriesTotal, URL_PREFIX, response.status_code))
    if retriesTotal >= RETRIES and not NOSTOP:
        print('--------------------------------------------')
        sys.exit('Tried {} times every {} seconds. No reply.'.format(RETRIES, WAITTIME))
    if not success: time.sleep(WAITTIME)

browser = webdriver.Remote(
    command_executor="http://chrome:4444",
    options=webdriver.ChromeOptions()
)

for page in PAGES:
    cur_page = URL_PREFIX+page
    print('Page: {}'.format(cur_page))
    browser.get(cur_page)
    print(browser.current_url)

browser.quit()
 
print('Finished', flush=True)

# CACHEPRIMER
# -----------
# This utility will check if the server is up and responding with a code lower than 
# 400 and then use Selenium to hit each page
# Usage: Create or edit config.json in same directory
# -----------
# Structure:
# {
#     "retries": "5",            <--- How often to try. Set to 0 to go forever
#     "wait": "2",               <--- in seconds
#     "protocol": "http",        <--- Protocol
#     "url": "localhost:10039",  <--- URL, including port if needed
#     "path": "/wps/portal",     <--- Path to portal
#     "pages": [
#         "/woodburnstudio/home",
#         ...
#     ]
# }
# Created using Python 3.8.10

import json, sys
import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from xvfbwrapper import Xvfb

noStop = False
retriesTotal = 0

# load configuration
with open('config.json') as json_config:
    config = json.load(json_config)

url_prefix = '{}://{}{}'.format(config['protocol'],config['url'],config['path'])
retries = int(config['retries']) # 0 if indeffinitely
if not retries: noStop = True
waitTime = float(config['wait'])

# Check if URL responds
success = False

print('*************** Cache Primer ***************')
print(' Target Server: {}'.format(url_prefix))
if noStop:
    print(' Retries: unlimited')
else:
    print(' Retries: {} Every: {}s'.format(retries,waitTime))
print('--------------------------------------------')
print

while not success:
    retriesTotal += 1
    try:
        response = requests.get(url_prefix)
    except requests.exceptions.ConnectionError:
        print('[{}] Could not connect to site {}'.format(retriesTotal, url_prefix))
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
    else:
        if response.status_code < 400:
            success = True
        else:
            print('[{}] Could not connect to site {}. HTTP Code {}'.format(retriesTotal, url_prefix, response.status_code))
    if retriesTotal >= retries and not noStop:
        print('--------------------------------------------')
        sys.exit('Tried {} times every {} seconds. No reply.'.format(retries, waitTime))
    if not success: time.sleep(waitTime)

with Xvfb() as xvfb:
    ser = Service("./chromedriver")
    op = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=ser, options=op)

    for page in config['pages']:
        browser.get('{}{}'.format(url_prefix,page))
        print(browser.current_url)

    browser.quit()

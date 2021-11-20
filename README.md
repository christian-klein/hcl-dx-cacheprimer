# CACHEPRIMER
This utility will check if the server is up and responding with a code lower than 400 and then use Selenium to hit each page.

This approach can also be used as a baseline for Selenium based testing.

## Usage: 
Create or edit config.json in same directory
Structure:
```
 {
     "retries": "5",            <--- How often to try. Set to 0 to go forever
     "wait": "2",               <--- in seconds
     "protocol": "http",        <--- Protocol
     "url": "localhost:10039",  <--- URL, including port if needed
     "path": "/wps/portal",     <--- Path to portal
     "pages": [
         "/woodburnstudio/home",
         ...
     ]
 }
 ```


## Installation:
This tool was written with Python 3.8.10 and the instructions assume a Linux machine, though it should work similarly on Mac and PC. 

### Install Python
Install Python3 and apt install python3.x-venv and create a virtual environment named venv
```
python3 -m venv venv 
```
then
```
source venv/bin/activate 
```
You should now be see the virtual environment in front of your prompt.
```
(venv) ~/hcl-dx-cacheprimer$ python --version
Python 3.8.10
(venv) ~/hcl-dx-cacheprimer$
```
### Install Chrome.

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo apt install ./google-chrome-stable_current_amd64.deb
```

### Install Chromedriver
Next, download and extract the appropriate chromedriver from https://chromedriver.chromium.org/ to this directory.
```
(venv) ~/GitHub/hcl-dx-cacheprimer$ ll
total 20504
drwxr-xr-x  5 cdk2128 cdk2128     4096 Nov 19 20:14 ./
drwxr-xr-x 20 cdk2128 cdk2128     4096 Nov 16 20:37 ../
drwxr-xr-x  7 cdk2128 cdk2128     4096 Nov 16 20:38 .git/
-rw-r--r--  1 cdk2128 cdk2128      153 Nov 19 20:05 .gitignore
drwxr-xr-x  2 cdk2128 cdk2128     4096 Nov 17 16:28 .vscode/
-rw-r--r--  1 cdk2128 cdk2128     1696 Nov 19 20:13 README.md
-rw-r--r--  1 cdk2128 cdk2128     2585 Nov 19 20:01 app.py
-rwxr-xr-x  1 cdk2128 cdk2128 20952448 Nov 10 17:40 chromedriver*
-rw-r--r--  1 cdk2128 cdk2128      947 Nov 19 19:55 config.json
-rw-r--r--  1 cdk2128 cdk2128       29 Nov 18 14:40 requirements.txt
drwxr-xr-x  6 cdk2128 cdk2128     4096 Nov 16 20:52 venv/
(venv) ~/GitHub/hcl-dx-cacheprimer$ 
```

Install `xvfb libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1` if `chromedriver --version` throws errors.

``` 
~/GitHub/hcl-dx-cacheprimer$ chromedriver --version 
ChromeDriver 96.0.4664.45 (76e4c1bb2ab4671b8beba3444e61c0f17584b2fc-refs/branch-heads/4664@{#947})
```

If this does not resolve the issue, run `chromedriver --version` to see missing dependencies and install them using apt-cache search.

Install Python requirements using 
```
pip install -r ./requirements.txt
```

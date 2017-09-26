import json
from selenium import webdriver
import argparse

# parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s', metavar='save',
                    help='Save as csv to the specified filename.',
                    nargs=1, required=False)
parser.add_argument('-un', metavar='username', help='A myfitnesspal username.',
                    nargs=1, type=str, required=True)
parser.add_argument('-pw', metavar='password', help='A myfitnesspal password.',
                    nargs=1, type=str, required=True)
args = vars(parser.parse_args())
un = args['un'][0]
pw = args['pw'][0]

# set up our web driver
driver = webdriver.PhantomJS()
url = 'https://www.myfitnesspal.com/account/login'

# log in and get a session
driver.get(url)
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.send_keys(un)
password.send_keys(pw)
password.submit()

# get the json file we want and transform it
driver.get('http://www.myfitnesspal.com/reports/results/'
           'progress/1/365.json?report_name=Weight&')
data = json.loads(driver.find_element_by_tag_name('body').text)

# if we want, write it to a csv using -s filename.csv, otherwise print it
if args['s'] and 'data' in data:
    import pandas as pd
    pd.DataFrame(data['data']).to_csv(args['s'][0], sep=',',
                                      index=False, header=True)
    print('I fulfilled my purpose and wrote {}!'.format(args['s']))
else:
    print(data)

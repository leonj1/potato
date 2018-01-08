import requests
import argparse
import json

login_url = 'https://put.io/login'
# next should be empty
login_data = {
    'username': '',
    'password': '',
    'next': '',
}

parser = argparse.ArgumentParser()
parser.add_argument("--user", help="put.io username")
parser.add_argument("--password", help="put.io password")
parser.add_argument("--file", help="file to upload")
args = parser.parse_args()

credentials  = login_data
credentials ['username'] = args.user
credentials ['password'] = args.password

files = {'upload_file': open(args.file,'rb')}
s = requests.Session()
r = requests.post(login_url, files=files, data=credentials)


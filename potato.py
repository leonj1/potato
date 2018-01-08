import requests
import argparse

login_url = 'https://put.io/login'
# next should be empty
login_data = {
    'username': '',
    'password': '',
    'next': '',
}

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file to push")
args = parser.parse_args()

files = {'upload_file': open(args.file,'rb')}
s = requests.Session()
r = requests.post(login_url, files=files, data=login_data)


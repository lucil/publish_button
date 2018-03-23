fname = 'configuration_staging.txt'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
contents = [x.strip() for x in content] 

staging_url = contents[0]
auth_token = contents[1]

import requests

url = staging_url

querystring = {"executeAllStages":"true","os_authType":"basic"}

headers = { 'authorization': auth_token}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
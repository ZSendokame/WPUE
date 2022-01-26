import requests
import sys

# Error
if len(sys.argv) <= 1:
    print('[-] Can\'t find any argument')
    exit()

get = requests.get(sys.argv[1] + '/wp-json/')

if get.status_code >= 400:
    print(f'[-] The site "{sys.argv[1]}" does not have "/wp-json/" directory or it\'s not indexable.')
    exit(1)

# Main
userCount = 0

while True:
    userCount += 1
    get = requests.get(f'{sys.argv[1]}/wp-json/wp/v2/users/{userCount}')
    json = get.json()

    if get.status_code >= 400:
        pass

    else:
        print(f'[+] Username: {json["name"]}')
        print(f'- User ID             : ' + str(json["id"]))
        print(f'- Expanded Url        : {sys.argv[1]}/wp-json/wp/v2/users/{userCount}')
        print(f'- Super Admin         : ' + str(json["is_super_admin"]))

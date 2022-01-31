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
get = requests.get(f'{sys.argv[1]}/wp-json/wp/v2/users/')
json = get.json()

print('_______')
for part in json:
    print('[+] Username  : ' + part["name"])
    print('- User Slug   : ' + part["slug"])
    print('- User ID     : ' + str(part["id"]))
    print(f'- Expanded URL: {sys.argv[1]}/wp-json/wp/v2/users/{part["id"]}')
    print('- Super Admin : ' + str(part['is_super_admin']))
print('-------')

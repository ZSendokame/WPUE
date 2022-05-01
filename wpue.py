import requests
import sys

sys.argv = sys.argv[1:]

# Error
if not len(sys.argv):
    print('[-] Can\'t find any argument'); exit(1)

get = requests.get(sys.argv[0] + '/wp-json/wp/v2/users')

if get.status_code >= 400:
    print(f'[-] The site "{sys.argv[0]}" does not have "/wp-json/wp/v2/users" directory or it\'s not indexable.'); exit(1)

# Main
print('_______')
for part in get.json():
    print('[+] Username  : ' + part["name"])
    print('- User Slug   : ' + part["slug"])
    print('- User ID     : ' + str(part["id"]))
    print(f'- Expanded URL: {sys.argv[0]}/wp-json/wp/v2/users/{part["id"]}')
    print(f'- Super Admin : {part["is_super_admin"]}\n')
print('-------')

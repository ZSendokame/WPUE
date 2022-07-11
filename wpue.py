import requests
import arguing

url = arguing.set('--url', mandatory=True, help_message='URL to check.')

# Error
if not len(arguing.argv):
    print('[-] Can\'t find any argument')
    exit(1)

get = requests.get(url + '/wp-json/wp/v2/users')

if get.status_code >= 400:
    print(f'[-] "{url}" does not have /wp-json/ or it\'s not indexable.')
    exit(1)

# Main
print('_______')
for user in get.json():
    print('[+] Username  : ' + user["name"])
    print('- User Slug   : ' + user["slug"])
    print('- User ID     : ' + str(user["id"]))
    print(f'- Expanded URL: {url}/wp-json/wp/v2/users/{user["id"]}\n')
print('-------')

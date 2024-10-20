import requests
import json
import os

# gets the random vnc id
r = requests.get('https://computernewb.com/vncresolver-next/api/v1/random')
data = r.json()
id_value = data.get('id')
print(id_value)

# gets the image
img = requests.get(f'https://computernewb.com/vncresolver-next/api/v1/screenshot/{id_value}')
os.makedirs('result', exist_ok=True)
os.makedirs(f'result/{id_value}', exist_ok=True)

# saves the image
with open(f'result/{id_value}/vnc_{id_value}.png', 'wb') as f:
    f.write(img.content)

# saves the data to a json file with the same name as the image
with open(f'result/{id_value}/vnc_{id_value}.json', 'w') as f:
    json.dump(data, f, indent=4)

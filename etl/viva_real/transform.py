import pandas as pd
import json
import re

def get_price_condo(text):
    match = re.search('[0-9].*[0-9]', text)
    if match:
        return int(match.group().replace('.', ''))
    return None

with open('extracted.json', 'r') as f:
    records = json.load(f)

df = pd.DataFrame.from_records(records['records'])

df.fillna("", inplace=True)

base_href_viva = "https://www.vivareal.com.br"
df['url'] = df['url'].apply(lambda x:base_href_viva+x)

df['room'] = df['room'].replace(to_replace='Quartos?',value='',regex=True)
df['room'] = df['room'].replace(to_replace='-+',value='0',regex=True)
df['room'] = df['room'].replace(to_replace='\s+',value='',regex=True).astype(int)

df['area'] = df['area'].replace(to_replace='m.*', value='', regex=True)
df['area'] = df['area'].replace(to_replace='\s+', value='', regex=True).astype(int)

df['address'] = df['address'].replace(to_replace='\s\s+',value='',regex=True)
df['address'] = df['address'].apply(lambda x:x.replace('ver mapa', '').strip())

df['title'] = df['title'].replace(to_replace='\s\s+',value='',regex=True)
df['title'] = df['title'].apply(lambda x:x.strip())

df['amenities'] = df['amenities'].apply(lambda x: [item.strip() for item in x])

df['garage'] = df['garage'].replace(to_replace='-+',value='0',regex=True)
df['garage'] = df['garage'].replace(to_replace='[vV]agas?', value='', regex=True).astype(int)

df['bathroom'] = df['bathroom'].replace(to_replace='-+',value='0',regex=True)
df['bathroom'] = df['bathroom'].replace(to_replace='[bB]anheiros?', value='', regex=True).astype(int)

df['price'] = df['price'].apply(lambda x:re.search('[0-9].*[0-9]', x).group().replace('.', '')).astype(int)
df['condo'] = df['condo'].apply(get_price_condo)


df.to_json('transformed.json', orient='records', index=False, indent=4)
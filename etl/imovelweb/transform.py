import pandas as pd
import re

def get_price_condo(text):
    match = re.search('[0-9].*[0-9]', text)
    if match:
        return int(match.group().replace('.', ''))
    return None

def get_bath(text):
    match = re.search('\d ban', text)
    if match:
        return int(re.search('\d ban', text).group().split()[0])
    return None

def get_room(text):
    match = re.search('\d quartos?', text)
    if match:
        return int(re.search('\d quartos?', text).group().split()[0])
    return None

def get_garage(text):
    match = re.search('\d vagas?', text)
    if match:
        return int(re.search('\d vagas?', text).group().split()[0])
    return None

df = pd.read_json('extracted.json')
df.fillna('', inplace=True)

df['price'] = df['price'].apply(lambda x:re.search('[0-9].*[0-9]', x).group().replace('.', '')).astype(int)
df['condo'] = df['condo'].apply(get_price_condo)

df['areas'] = df['features'].apply(lambda x:re.findall('\d+ m.', x))
df[['area total', 'area util']] = df['areas'].to_list()
df['area util'] = df['area util'].replace(to_replace='m.+', value='', regex=True).astype(int)
df['area total'] = df['area total'].replace(to_replace='m.+', value='', regex=True).astype(int)

df.drop(columns=['areas'], inplace=True)

df['room'] = df['features'].apply(get_room)
df['garage'] = df['features'].apply(get_garage)
df['bathroom'] = df['features'].apply(get_bath)

df['url'] = df['url'].apply(lambda x:'https://www.imovelweb.com.br'+x)

df.to_json('transformed.json', orient='records', indent=4, index=False)
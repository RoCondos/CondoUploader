import random
import secrets
from lxml import etree

file_name = 'file.rbxlx'

try:
    doc = etree.parse(file_name)
except Exception as e:
    print(f"Error occurred while parsing the file: {e}")
    exit(1)

def update_unique_id():
    print('UNBLACKLISTER > Updating UniqueId...')
    for element in doc.xpath("//UniqueId[@name='UniqueId']"):
        element.text = f'ILlmaijji{secrets.token_hex(110)}'
    doc.write(file_name)

def update_referent():
    print('UNBLACKLISTER > Updating Referent...')
    for element in doc.xpath("//Item[@referent]"):
        random_string = ''.join(random.choice('oijj') for _ in range(70))
        element.attrib['referent'] = f'Strijg{random_string}'
    doc.write(file_name)

def update_asset_id():
    print('UNBLACKLISTER > Updating AssetId...')
    for element in doc.xpath("//SourceAssetId[@name='SourceAssetId']"):
        element.text = f'-{secrets.token_hex(20)}'
    doc.write(file_name)

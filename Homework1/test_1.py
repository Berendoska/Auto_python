import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


def test_post_create(user_login, get_description):
    result = S.post(url=data['address_post'], headers={'X-Auth-Token': user_login},
                    data={'title': data['tlt'], 'description': data['desc'], 'content': data['text']})
    assert str(result) == '<Response [200]>', 'post_create FAIL'


def test_check_post(user_login, get_description):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}).json()['data']
    list_description = [i['description'] for i in result]
    assert get_description in list_description, 'check_post FAIL'
from vk_api.vk_api import VkApi
import facebook
from instagram.client import InstagramAPI
import requests
name = input('введите название соц. сети: ')
user_id = input('введите id пользователя: ')
if name == 'vk':
    vk = VkApi(app_id=7646807, token='1bfbce991bfbce991bfbce99991b8f60ce11bfb1bfbce9944664b4da26b585a50448b66').get_api()
    data = vk.users.get(user_ids=user_id, fields=['city', 'country', 'education', 'interests','about'])[0]
    print('профиль закрыт' if data['is_closed'] else 'профиль открыт')
    print(data['city']['title'] if 'city' in data else 'город не указан')
    print(data['country']['title'] if 'country' in data else 'страна не указан')
    print(data['education'] if 'education' in data else 'Образование не указано')
    print(data['interests'] if 'interests' in data else 'Нет интересов')
elif name == 'inst':
    replay = requests.get('https://graph.instagram.com/'+user_id+'?fields=id,username&access_token='+'IGQVJVbndKX19uTDZAkT0pLeHpjejloR2p5eWdZAQkRtZA0xLWDdrZAmRmVVE2bURSa01jb2NMdmZAIYVFXRWlOamUyWUFCZAUp1SWZAvcEhrTV9uSGtnU043bWJ2MkpOaGV3aTFWbTF5N0czRDZA4NW00RnJaaQZDZD')
    print(replay.text)
elif name == 'facebook':
    graph = facebook.GraphAPI(access_token='EAAJ0cmAkx5MBABcfic57UmHwaBqguHE1FhhgQRU6ExlaEaz3uiN62hc62gNPE7HLHVCzolDEInWZALuEwpYrlZAZALA93xGhlZBZCJ30dLP0P6GZCj99K1BH6pkn5tBwV7redbXaZBYw2ZAZAEru3g3ZAlB2Nivu572RKl3NHAoZCCZBov9dK2ZCcSBBTrupEMoLZBctExJgEjoM6ZC9gZDZD')
    user_fields = graph.get_object(user_id, fields='location{location{city,country}}')
    location = user_fields.get('location',{}).get('location',{})
    print(location['city'] if 'city' in location else 'город не указан')
    print(location['country'] if 'country' in location else 'страна не указана')
else:
    print('нихрена ты умный, свали с такими высказываниями отсюда')


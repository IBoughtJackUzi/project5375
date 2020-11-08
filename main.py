from vk_api.vk_api import VkApi
import facebook
from instagram.client import InstagramAPI
import requests
name = input('введите название соц. сети: ')
user_id = input('введите id пользователя: ')
if name == 'vk':
    vk = VkApi(app_id=7646807, token='1bfbce991bfbce991bfbce99991b8f60ce11bfb1bfbce9944664b4da26b585a50448b66').get_api()
    data = vk.users.get(user_ids=user_id, fields=['city', 'country', 'education'])[0]
    print('профиль закрыт' if data['is_closed'] else 'профиль открыт')
    print(data['city']['title'] if 'city' in data else 'город не указан')
    print(data['country']['title'] if 'country' in data else 'страна не указан')
    print(data['education'] if 'education' in data else 'Образование не указано')
elif name == 'inst':
    replay = requests.get('https://graph.instagram.com/'+user_id+'?fields=id,username&access_token='+'IGQVJVbndKX19uTDZAkT0pLeHpjejloR2p5eWdZAQkRtZA0xLWDdrZAmRmVVE2bURSa01jb2NMdmZAIYVFXRWlOamUyWUFCZAUp1SWZAvcEhrTV9uSGtnU043bWJ2MkpOaGV3aTFWbTF5N0czRDZA4NW00RnJaaQZDZD')
    print(replay.text)
elif name == 'facebook':
    graph = facebook.GraphAPI(access_token='EAAJ0cmAkx5MBALoCmBD38c7aTyKfdzsfu3etVapILw2mXsqiGsyrxtMyJQEddEbD6rqPYcd0is1WILeiyybOrt7HnSREVgx8ej96ZBZCwMHfMh6Jujfcq3Np3DOTYUgeky9goZBZCuKtl2vczF8yfcCIeY1W9Ffaznaf5h5mkxbY4Lg5TGyJCPHPsz6ZARNxiRREcamMYg0a6ta54sNj2wxuoZAZC74u2ZA2JXir0sZBRoYKvkm2vvj2bUCE2awsLC9cZD')
    user_fields = graph.get_object(user_id, fields='location{location{city,country}}')
    location = user_fields.get('location',{}).get('location',{})
    print(location['city'] if 'city' in location else 'город не указан')
    print(location['country'] if 'country' in location else 'страна не указана')
else:
    print('нихрена ты умный, свали с такими высказываниями отсюда')


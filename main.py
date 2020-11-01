from vk_api.vk_api import VkApi
name = input('введите название соц. сети: ')
user_id = input('введите id пользователя: ')
if name == 'vk':
    vk = VkApi(app_id=7646807, token='1bfbce991bfbce991bfbce99991b8f60ce11bfb1bfbce9944664b4da26b585a50448b66').get_api()
    data = vk.users.get(user_ids=user_id, fields=['city', 'country'])[0]
    print('профиль закрыт' if data['is_closed'] else 'профиль открыт')
    print(data['city']['title'] if 'city' in data else 'город не указан')
    print(data['country']['title'] if 'country' in data else 'страна не указан')
elif name == 'inst':
    pass
elif name == 'facebook':
    pass
else:
    print('нихрена ты умный, свали с такими высказываниями отсюда')


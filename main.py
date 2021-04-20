import os
import pandas as pd
from vk_api.vk_api import VkApi
import facebook
from instagram.client import InstagramAPI
import requests
from tkinter import *
from PIL import Image
from urllib.request import urlopen, urlretrieve
APP_ID = 7646807
TOKEN = '1bfbce991bfbce991bfbce99991b8f60ce11bfb1bfbce9944664b4da26b585a50448b66'
POST_COUNT = 50
PHOTO_COUNT = 100


def save_posts_to_file(vk, user_id, count):
    data = vk.wall.get(owner_id=user_id, count=count)
    table: dict = {
        "id": [],
        "text": [],
        "copy_text": []
    }

    for x in data['items']:
        id = '--'
        text = '--'
        cp_text = '--'

        if x['text']:
            text = x['text']
        try:
            if x['copy_history']:
                id = x['copy_history'][0]['from_id']
                if x['copy_history'][0]['text']:
                    cp_text = x['copy_history'][0]['text']
        except KeyError:
            pass

        table['id'].append(id)
        table['text'].append(text)
        table['copy_text'].append(cp_text)

    pd.DataFrame.from_dict(table).to_excel('posts.xlsx')


def get_info():
    social = var.get()
    user_id = ent.get()
    if social == 0:
        vk = VkApi(app_id=APP_ID, token=TOKEN).get_api()
        data = vk.users.get(user_ids=user_id, fields=['city', 'country', 'education', 'interests', 'about', 'photo_max_orig'])[0]
        image = Image.open(urlopen(data['photo_max_orig']))
        image.show()
        output = ''
        output += ('профиль закрыт' if data['is_closed'] else 'профиль открыт') + '\n'
        output += (data['city']['title'] if 'city' in data else 'город не указан') + '\n'
        output += (data['country']['title'] if 'country' in data else 'страна не указан') + '\n'
        output += (data['education'] if 'education' in data else 'Образование не указано') + '\n'
        output += (data['interests'] if 'interests' in data else 'Нет интересов') + '\n'
        lab2['text'] = output

        save_posts_to_file(vk, data['id'], POST_COUNT)

        photo_ids = []
        owner_id = data['id']
        for elem in vk.photos.get(owner_id=owner_id, album_id='profile', count=PHOTO_COUNT)['items']:
            photo_id = elem['id']
            photo_ids.append(f'{owner_id}_{photo_id}')
        for elem in vk.photos.get(owner_id=owner_id, album_id='wall', count=PHOTO_COUNT)['items']:
            photo_id = elem['id']
            photo_ids.append(f'{owner_id}_{photo_id}')

        if len(photo_ids) == 0:
            return
        if not os.path.exists(os.path.join('photos', str(owner_id))):
            os.makedirs(os.path.join('photos', str(owner_id)))

        for photo in vk.photos.getById(photos=photo_ids, extended=0, photo_sizes=1):
            max_height = -1
            max_index = 0
            for i in range(len(photo['sizes'])):
                if photo['sizes'][i]['height'] > max_height:
                    max_height = photo['sizes'][i]['height']
                    max_index = i
            url = photo['sizes'][max_index]['url']
            photo_id = photo['id']
            urlretrieve(url, os.path.join('photos', str(owner_id), f'{photo_id}.jpg'))
    elif social == 1:
        output2 = ''
        replay = requests.get(
            'https://graph.instagram.com/' + user_id + '?fields=id,username&access_token=' + 'IGQVJVbndKX19uTDZAkT0pLeHpjejloR2p5eWdZAQkRtZA0xLWDdrZAmRmVVE2bURSa01jb2NMdmZAIYVFXRWlOamUyWUFCZAUp1SWZAvcEhrTV9uSGtnU043bWJ2MkpOaGV3aTFWbTF5N0czRDZA4NW00RnJaaQZDZD')
        output2 += (replay.text) + '\n'
        lab2['text'] = output2
    elif social == 2:
        output3 = ''
        graph = facebook.GraphAPI(
            access_token='EAAJ0cmAkx5MBAJsBcNj84Gq6Jxbp5kC03GzVNuKPVN6cFNKfWnIkaN4pIuDYC5L0U44YQyy4s4ImUnIwmwZB6GgXKLcA3QPksEmYTR1FhyxoqZAPHyZB1nsI9jLoxeNEOTfcfhqxkBLJxZABmZCXZCxNJ7iSvEOo7sdTK4hB522hvsaindAyexWHI91rR0EYLw1Mqdajl2Rag6sZBx22xTnGv2y5rDBqSUVnyzexZAlHWJoZB9RsNxgtJBm4qMWx36IAZD')
        user_fields = graph.get_object(user_id, fields='location{location{city,country}}')
        location = user_fields.get('location', {}).get('location', {})
        output3 += (location['city'] if 'city' in location else 'город не указан') + '\n'
        output3 += (location['country'] if 'country' in location else 'страна не указана') + '\n'
        lab2['text'] = output3


root = Tk()
root.geometry("600x600")

var = IntVar()
lab = Label(text='Choose social')
rb1 = Radiobutton(text='VK', variable=var, value=0, font=("Courier", 18))
rb2 = Radiobutton(text='Instagram', variable=var, value=1, font=("Courier", 18))
rb3 = Radiobutton(text='Facebook', variable=var, value=2, font=("Courier", 18))
lab1 = Label(text='Enter ID:')
ent = Entry()
btn = Button(text='Confirm', command=get_info)
lab2 = Label()

lab.pack()
rb1.pack()
rb2.pack()
rb3.pack()
lab1.pack()
ent.pack()
btn.pack()
lab2.pack()
root.mainloop()
from vk_api.vk_api import VkApi
import facebook
from instagram.client import InstagramAPI
import requests
from tkinter import *
def func():
    social = var.get()
    user_id = ent.get()
    if social == 0:
        vk = VkApi(app_id=7646807, token='1bfbce991bfbce991bfbce99991b8f60ce11bfb1bfbce9944664b4da26b585a50448b66').get_api()
        data = vk.users.get(user_ids=user_id, fields=['city', 'country', 'education', 'interests','about'])[0]
        output = ''
        output += ('профиль закрыт' if data['is_closed'] else 'профиль открыт') + '\n'
        output += (data['city']['title'] if 'city' in data else 'город не указан') + '\n'
        output += (data['country']['title'] if 'country' in data else 'страна не указан') + '\n'
        output += (data['education'] if 'education' in data else 'Образование не указано') + '\n'
        output += (data['interests'] if 'interests' in data else 'Нет интересов') + '\n'
        lab2['text'] = output
    elif social == 1:
        output2 = ''
        replay = requests.get('https://graph.instagram.com/'+user_id+'?fields=id,username&access_token='+'IGQVJVbndKX19uTDZAkT0pLeHpjejloR2p5eWdZAQkRtZA0xLWDdrZAmRmVVE2bURSa01jb2NMdmZAIYVFXRWlOamUyWUFCZAUp1SWZAvcEhrTV9uSGtnU043bWJ2MkpOaGV3aTFWbTF5N0czRDZA4NW00RnJaaQZDZD')
        output2 += (replay.text) + '\n'
        lab2['text'] = output2
    elif social == 2:
        output3 = ''
        graph = facebook.GraphAPI(access_token='EAAJ0cmAkx5MBAJsBcNj84Gq6Jxbp5kC03GzVNuKPVN6cFNKfWnIkaN4pIuDYC5L0U44YQyy4s4ImUnIwmwZB6GgXKLcA3QPksEmYTR1FhyxoqZAPHyZB1nsI9jLoxeNEOTfcfhqxkBLJxZABmZCXZCxNJ7iSvEOo7sdTK4hB522hvsaindAyexWHI91rR0EYLw1Mqdajl2Rag6sZBx22xTnGv2y5rDBqSUVnyzexZAlHWJoZB9RsNxgtJBm4qMWx36IAZD')
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
btn = Button(text='Confirum', command=func)
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

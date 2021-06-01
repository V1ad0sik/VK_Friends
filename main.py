from vk_api import vk_api

user_id = 1 # ID человека
token = ''  # Токе

vk_session = vk_api.VkApi(app_id = 2274003, token = token) # Авторизация
vk = vk_session.get_api()

info = vk.users.get(user_id =  user_id, fields = "counters, friends") # Количество друзей

num = int(info[0]['counters']['friends']) # Количество друзей в цифрах
user_friends = list(vk.friends.get(user_id = user_id, order='hints')['items']) # ID всех друзей

array_city = [] # Список городов

for i in range(0, num):
	info = list(vk.users.get(user_id =  int(user_friends[i]), fields = "city")) # Смотрим город друга
	
	try:
		print(' ' + info[0]['city']['title'])
		array_city.append(info[0]['city']['title'])
	except:
		print(' Город не определен')
		pass

array_d = {}.fromkeys(array_city, 0) # Сортировка 
for a in array_city:
    array_d[a] += 1

array_result = list(array_d.items()) # Количество друзей в городах

print(f'---\n {array_result}' )
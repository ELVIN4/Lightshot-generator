import requests, random
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from datetime import datetime

photo = int(input('Введите количество валидных фото: '))

template = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

    <title>AREL | Lightshot</title>
  </head>
  <body class="p-3 mb-2 bg-dark text-green">
  </body>
</html>

<nav class="navbar fixed-top navbar-light bg-primary">
  <div class="container-fluid">
    <a class="navbar-brand" href="https://areldev.ru">AREL</a>
    <a class="navbar-brand" href="https://t.me/ARELDEV_CHANNEL">Telegram Group</a>
    <a class="navbar-brand" href="https://t.me/AREL_CHAT">Telegram Chat</a>
  </div>
</nav>
'''

filename = str(datetime.strftime(datetime.now(), "%d.%m.%y-%H.%M.%S"))
temp = open(f'{filename}.html', 'a+')
temp.write(template)
temp.close()

print('[+] The script is running ')

while photo > 0:
	text = 'abcdefghijklnopqrstuvwxyzACDEHIJKMPQRSTUXYZ1234567890'
	url = ''

	for i in range(6):
		url += random.choice(text)

	html = requests.get(f'https://prnt.sc/{url}', headers={'User-agent':generate_user_agent(device_type='desktop', os=('linux'))}).text
	soup = bs(html, 'lxml')
	img = soup.find(class_='no-click screenshot-image')

	try:
		if img.get('src') != '//st.prntscr.com/2021/02/09/0221/img/0_173a7b_211be8ff.png':
			photo -= 1
			with open(f'{filename}.html', 'a+') as file:
				file.write(f'\n{img}')
			link = img.get('src')
			print(f'[+] URL {link} SAVED')

	except:
		pass


print(f'[+] Complete, photos saved in file {filename}.html')
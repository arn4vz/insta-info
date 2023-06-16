######CODED BY ARNAV########

import os,requests,telebot

from telebot import TeleBot

from cfonts import render, say

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

F = '\033[2;32m' #اخضر

C = "\033[1;97m" #ابيض

B = '\033[1;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح.

C = "\033[1;97m" #ابيض

output = render('ACC INFO', colors=['white', 'black'], align='center')

print(output)

print(F)

print('                   by @hackerworld69')

print(F+'-'*67)

tok=input(Y+'BotToken : ')

if tok:

	print('send /start to your bot to start')bot=telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])

def message(message):

  	bot.send_message(message.chat.id,'<strong> - BY : @HACKERWORLD69</strong>',parse_mode='html')

@bot.message_handler(func=lambda message:True)

def sta(message):

  		user=message.text

  		head={'x-ig-app-id':'936619743392459'}

  		url=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

  		req=requests.get(url,headers=head).json()['data']['user']

  

  		i=req['id']

  		p=req['profile_pic_url']

  		fo=req['edge_followed_by']['count']

  		fw=req['edge_follow']['count']

  		b=req['biography']

  		m=req['edge_owner_to_timeline_media']['count']

  		fid=req['fbid']

  		ib=req['is_business_account']

  		date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]

  		bot.send_photo(message.chat.id,p,f'<strong>- Followers : {fo}\n- Following : {fw}\n- ID :<code> {i}</code>\n- Date : {date}\n- Posts : {m}\n- FB-ID : {fid}\n- Is-Business : {ib}\n- Bio : {b}</strong>',parse_mode='html')

bot.polling(True)

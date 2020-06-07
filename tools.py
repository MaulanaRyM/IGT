#python3
#codec by rym

from banner import ban1, ban2, ban3, ban
import requests as r
import json, wget, time, os, sys

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
run = True
print(b+ban)
def stalk():
    os.system('clear')
    print(b+ban1)
    user = input(c+'username : ')
    req = r.get('https://instagram.com/'+user+'/?__a=1')
    name = req.json()['graphql']['user']['full_name']
    bio = req.json()['graphql']['user']['biography']
    url = req.json()['graphql']['user']['external_url']
    post = req.json()['graphql']['user']['edge_owner_to_timeline_media']['count']
    folwd = req.json()['graphql']['user']['edge_followed_by']['count']
    folw = req.json()['graphql']['user']['edge_follow']['count']
    print(b+'')
    print('++++++++Results++++++++')
    time.sleep(1)
    print ('[+] username :' +user)
    print ('[+] Full Name :', name)
    time.sleep(0.2)
    print ('[+] Bio :', bio)
    time.sleep(0.2)
    print ('[+] Website :', url)
    time.sleep(0.2)
    print ('[+] Total Post :', post)
    time.sleep(0.2)
    print ('[+] Follower :', folwd)
    time.sleep(0.2)
    print ('[+] Following :', folw)

def vid():
    os.system('clear')
    print(b+ban2)
    inp = input(c+'Enter Post ID : ')
    name = input('Set Name As : ')
    req = r.get('https://instagram.com/p/'+inp+'/?__a=1')
    url = req.json()['graphql']['shortcode_media']['video_url']
    time.sleep(1)
    print(b+'Downloading....')
    wget.download(url, 'output/video/'+name+'.mp4')
    print('')
    print(a+'Berhasil Menyimpan di output/video/'+name+'.mp4')

def img():
    os.system('clear')
    print(b+ban3)
    inp = input(c+'Enter Post ID : ')
    name = input('Set Name As : ')
    req = r.get('https://instagram.com/p/'+inp+'/?__a=1')
    url = req.json()['graphql']['shortcode_media']['display_url']
    time.sleep(1)
    print(b+'Downloading....')
    wget.download(url, 'output/image/'+name+'.jpg')
    print('')
    print(a+'Berhasil Menyimpan di output/image/'+name+'.jpg')

while run:
    inp = input(c+"Pilih Tools : ")
    if inp == '1':
        stalk()
        run = False

    if inp == '2':
        vid()
        run = False

    if inp == '3':
        img()
        run = False

    if inp == '4':
       print('Exiting...')
       run = False

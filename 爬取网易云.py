import  requests
url='https://m804.music.126.net/20250217203710/4bbea31bf6e33aad355a59810c4c6cf5/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/56350492591/ca60/0020/5a0a/1caa00564dad70eb1fc1d1296dcb62a9.m4a?vuutv=wjy95ll4Zk85Fdu7iXEl7dkb54JATIT/8HtxWv1l7n46hlcPg62m2muRn90bgaKAkrhan3eT3/Bi1P6d4FL6P5F3SIFiZNVvzA6ox01DWKc=&authSecret=0000019513d2b1ae11b20a743a690007'
res2=requests.get(url)
print(res2.content)

with open('Lord Konws.mp3','wb') as f:
    f.write(res2.content)
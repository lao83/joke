import random
user=int(input("用户请输入你要出的是什么：1（石头）2（剪刀）3（布）:"))
computer=random.randint(1,3)
if user == computer:
    print('平局')
elif (user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1):
    print('恭喜你获得胜利')
else:
    print('真可惜下次再来')
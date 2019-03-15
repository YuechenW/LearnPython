import random
secret = random.randint(0,10)
print('-----------版权所有，翻版必究----------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:(0~10)")
guess = int(temp)
num = 0
while guess != secret:
    num += 1
    if guess > secret:
            print("哥，大了大了~~")
    else:
            print("嘿,小了！小了！！")
    if num == 3:
        break
    temp = input("哎呀，猜错了，请重新输入吧:")
    guess = int(temp)
    
if num == 3:
    print("猜错啦，小甲鱼现在心里想的是%d!"%secret)
else:    
    print("卧槽，你是小甲鱼心里的蛔虫吗？!")
    print("哼，猜中了也没有奖励!")
    print("游戏结束，不玩啦")
    

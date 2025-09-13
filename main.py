import random

def roll_dice():
     dice=random.randrange(1,7)

     return dice

def main():
     print('welcome to my ludo game.')
     player=[]
     n=int(input('how many player?:'))
     i=1
     # مشخص کردن رنگ هر بازیکن و مقدار دهی اولیه
     while i <=n:
          if i==1:
               color=input('enter player color[red,yellow,blue,green] : ')
               player1={'color':color,'block':0,'in':0}
               player.append(player1)
          elif i==2:
               color=input('enter player color[red,yellow,blue,green] : ')
               player2={'color':color,'block':0,'in':0}
               player.append(player2)
          elif i==3:
               color=input('enter player color[red,yellow,blue,green] : ')
               player3={'color':color,'block':0,'in':0}
               player.append(player3)
          elif i==4:
               color=input('enter player color[red,yellow,blue,green] : ')
               player4={'color':color,'block':0,'in':0}
               player.append(player4)
          i+=1

     running=True
     while running:
          round=0
          i=round%n
          dice=roll_dice()
          while dice==6:
               if player[i]['in']==1:
                    player[i]['block']+=dice
               dice=roll_dice()

          if dice!=6:
               if player[i]['in']==1:
                    player[i]['block']+=dice



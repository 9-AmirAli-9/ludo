player=[]
n=int(input('how many player?:'))
i=1
while i <=n:
    if i==1:
         color=input('enter player color[red,yellow,blue,green] : ')
         player1={'color':color,'turn':0,'in':0}
         player.append(player1)
    elif i==2:
         color=input('enter player color[red,yellow,blue,green] : ')
         player2={'color':color,'turn':0,'in':0}
         player.append(player2)
    elif i==3:
         color=input('enter player color[red,yellow,blue,green] : ')
         player3={'color':color,'turn':0,'in':0}
         player.append(player3)
    elif i==4:
         color=input('enter player color[red,yellow,blue,green] : ')
         player4={'color':color,'turn':0,'in':0}
         player.append(player4)
    i+=1


def main():
      player=input('how many player?')

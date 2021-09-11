#Tambola Game : A game like Bingo:::
import time
name=input("ENTER YOUR NAME ")
print('WELCOME ',name)
list2=[]
print("1 -> Play Game Know :")
print("2 -> Learn How to play :")
choice=int(input())
while True:
    if(choice==1):
        p=int(input("\n\nENTER NUMBER OF PLAYERS(Enter Atleast 2):\n\n"))
        if(p<2 or p>10):    
            print("invalid Selection")
        else:
            import random
            for i in range (0,p):
                list1=[]
                for j in range (0,10):
                    list1.append(random.choice(range(30)))
                    list2.append(random.choice(range(30)))
                print(list1,"\n ")
            print('Are You Ready (enter Yes or No)')
            y=input()
            if(y=='yes' or y=='Yes' or y=='YES'):
                for i in range (0,len(list2)):
                    print("                   ",list2[i])
                    time.sleep(3)
            else:
                break
            win=input("ENTER WINNER ")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(" CONGRATULATIONS ",win)
            time.sleep(1)
            print(" CONGRATULATIONS ",win) 
            time.sleep(1)
            print(" CONGRATULATIONS ",win) 
            time.sleep(1)
            print(" CONGRATULATIONS ",win) 
            time.sleep(1)
            print(" CONGRATULATIONS ",win) 
            time.sleep(1)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Do You Want TO Play Again :(Enter Yes or No)")
            y=input()
            if(y=='no'or y=='No' or y=='NO'or y!='yes'):
                break
    elif(choice==2):
        print("TAMBOLA GAME (A multiplayer game)")
        print("* You are provided the numbers of list , that count is depends on Players which you are provided to us.")
        time.sleep(3)
        print("* If you enter 2 player then 2 list are shown below for player 1 and player 2 . Decide mutually who is player 1 and who is palyer 2.")
        time.sleep(4)
        print("* Now, the game will start ater you give 'Yes' to System. The game is started now .")
        time.sleep(3)
        print("* The game gives you a number, if the number is present in your list then circle that number and if number is present in your friends list then they will circle that number. ")
        time.sleep(4)
        print("* RESULT : that player having more Circles is the Winner of the game .")
        print("YOU WANT TO PLAY GAME ? (Enter yes)")
        if(input()=='yes'):
            choice=1
        else :
            break

            
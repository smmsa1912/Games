# Starter
import random
import time
import sys

print('\n Kindly Wait The Game Is Loading!... :)')
time.sleep(1)
print(' NOTE: You Need 5 Points To Win The Match')
time.sleep(2)

# Containers
s_com = 0
s_player = 0

opt1 = 'Stone' 
opt2 = 'Paper'
opt3 = 'Scissor'
opt4 = 'stone'
opt5 = 'paper'
opt6 = 'scissor'
opt7 = 'STONE'
opt8 = 'PAPER'
opt9 = 'SCISSOR'
tool = ('Stone' , 'Paper' , 'Scissor')
a1 = '1'
a2 = '2'
a3 = '3'
tool = ('Stone' , 'Paper' , 'Scissor')

# Com Selection

('\n')
bold = '\033[1m'
start = input(' \n Kindly Press Enter To Continue:')
time.sleep(0.5)
if start != '':
    print(' Kindly Press Enter To Continue And Try Again')
    time.sleep(1)
    quit()
name = input(' Enter Your Nickname Here:\n')
name = name.capitalize()
if name == '':
    print(' Sry! Kindly Enter Your Nickname :(')
    time.sleep(1)
    quit()
time.sleep(1)
print('\n Welcome',name+',')
while start == '':
        time.sleep(1.5)
        com = random.choice(tool)
        delay = 0.25 , 0.50 , 0.75 , 1 , 1.25 , 1.50 , 1.75 , 2
        print(' Kindly Wait! :)')
        time.sleep(1.3)
        print(' Computer Is Choosing..!')
        shell = sys.stdout
        time.sleep(0.7)
        shell.write(' Choosing')
        str = '...'
        for letter in str:
            sys.stdout.write(letter)
            time.sleep(random.choice(delay))
        print(' Done!! \n')
        time.sleep(2)
        print(' Now Your Turn,')
        time.sleep(1)
    # Player Choice
        player = input(' Which One Will You Choose \n' + ' ' + '[' +a1+']' + opt1 +' ' 'Or' ' ' + '[' +a2+']' + opt2 + ' ' 'Or' ' ' + '[' +a3+']'+ opt3 + '\n' )
        
        Player = player.capitalize()
        Com = com.capitalize()


        if player == opt1 :
            print(' Ok! You Choosed Stone!..')
        elif player == opt2 :
            print(' Ok! You Choosed Paper!..')
        elif player == opt3 :
            print(' Ok! You Choosed Scissor!..')
        elif player == opt4:
            print(' Ok! You Choosed Stone!..')
        elif player == opt5:
            print(' Ok! You Choosed Paper!..')
        elif player == opt6:
            print(' Ok! You Choosed Scissor!..')
        elif player == opt7:
            print(' Ok! You Choosed Stone!..')
        elif player == opt8:
            print(' Ok! You Choosed Paper!..')
        elif player == opt9 :
            print(' Ok! You Choosed Scissor!..')
        elif player == a1:
            print(' Ok! You Choosed Stone!..')
        elif player == a2:
            print(' Ok! You Choosed Paper!..')
        elif player == a3:
            print(' Ok! You Choosed Scissor!..')
        elif player != opt1 or opt2 or opt3 or opt4 or opt5 or opt6 or opt7 or opt8 or opt9 or a1 or a2 or a3 or '1' or '2' or '3':
            time.sleep(0.7)
            print(' :(')
            time.sleep(0.7)
            print (' Choose And Write From The Given Option Only Or Check The Spelling')
            time.sleep(1)
            input(' Press Enter To Rechoose From The Option')
            player = input(' Which One Will You Choose \n' + ' ' + '[' +a1+']' + opt1 + ' ' 'Or' ' ' + '[' +a2+']' + opt2 + ' ' 'Or' ' ' + '[' +a3+']'+ opt3 + '\n' )
    # 2nd Chance
            if player == opt1 :
                print(' Ok! You Choosed Stone!..')
            elif player == opt2 :
                print(' Ok! You Choosed Paper!..')
            elif player == opt3 :
                print(' Ok! You Choosed Scissor!..')
            elif player == opt4:
                print(' Ok! You Choosed Stone!..')
            elif player == opt5:
                print(' Ok! You Choosed Paper!..')
            elif player == opt6:
                print(' Ok! You Choosed Scissor!..')
            elif player == opt7:
                print(' Ok! You Choosed Stone!..')
            elif player == opt8:
                print(' Ok! You Choosed Paper!..')
            elif player == opt9 :
                print(' Ok! You Choosed Scissor!..')
            elif player == a1:
                print(' Ok! You Choosed Stone!..')
            elif player == a2:
                print(' Ok! You Choosed Paper!..')
            elif player == a3:
                print(' Ok! You Choosed Scissor!..')
            elif player != opt1 or opt2 or opt3 or opt4 or opt5 or opt6 or opt7 or opt8 or opt9 or a1 or a2 or a3 or '1' or '2' or '3':
                time.sleep(0.7)
                print(' :(')
                time.sleep(0.7)
                print (' Choose And Write From The Given Option Only Or Check The Spelling')
                time.sleep(0.7)
                print(' Sry, You Have Last Chance Enter Correctly Or You Will Be Quit!...')
                time.sleep(1)
                input(' Press Enter To Rechoose From The Option')
                player = input(' Which One Will You Choose \n' + ' ' + '[' +a1+']' + opt1 + ' ' 'Or' ' ' + '[' +a2+']' + opt2 + ' ' 'Or' ' ' + '[' +a3+']'+ opt3 + '\n' )
                Player = player.capitalize()
    # 3rd Chance
                if player == opt1 :
                    print(' Ok! You Choosed Stone!..')
                elif player == opt2 :
                    print(' Ok! You Choosed Paper!..')
                elif player == opt3 :
                    print(' Ok! You Choosed Scissor!..')
                elif player == opt4:
                    print(' Ok! You Choosed Stone!..')
                elif player == opt5:
                    print(' Ok! You Choosed Paper!..')
                elif player == opt6:
                    print(' Ok! You Choosed Scissor!..')
                elif player == opt7:
                    print(' Ok! You Choosed Stone!..')
                elif player == opt8:
                    print(' Ok! You Choosed Paper!..')
                elif player == opt9 :
                    print(' Ok! You Choosed Scissor!..')
                elif player == a1:
                    print(' Ok! You Choosed Stone!..')
                elif player == a2:
                    print(' Ok! You Choosed Paper!..')
                elif player == a3:
                    print(' Ok! You Choosed Scissor!..')
                else:
                    time.sleep(0.7)
                    print(' Sry, Try Again! :(')
                    time.sleep(0.7)
                    Help = input(' Do You Need Any Help In Choosing??\n Yes/Y Or No/N \n')
                    Help = Help.capitalize()
                    if Help == 'Yes' or 'Y':
                        print('\n Hello Welcome To The Game!!'),
                        time.sleep(1.5),
                        print(' If You Want To Choose Stone Or Scissor Or Paper'),
                        time.sleep(2.5), 
                        print(' There Are Two Ways,'),
                        time.sleep(1.5),
                        print(' 1. Just Type The Number Of the Options'),
                        time.sleep(2), 
                        print(' For Example: To choose Stone Type "1" / To Choose Paper type "2" / To Choose Scissor Type "3"'),
                        time.sleep(2.5),
                        print(' Another Way Of Choosing:'),
                        time.sleep(1.5),
                        print(' 2. Just Type The Name'),
                        time.sleep(1.5),
                        print(' For Example: To Choose Stone Type "Stone" / To Choose Paper Type "Paper" / To Choose Scissor Type "Scissor"'),
                        time.sleep(2.5),
                        print(' If You Still Face Any Error Or It Shows "Sry" Or "Try Again" Or ":("')
                        time.sleep(1)
                        print(' That Mean You Have Done Any Mistake')
                        time.sleep(1.5)
                        print(' You Should Avoid The Following Mistakes')
                        time.sleep(1.5)
                        print(' You Should Not Leave Any Spaces Before OR After a Word \n For Example:')
                        time.sleep(2)
                        print(' If You Choosed Stone You Should Write "Stone" Or "1" You Should Not Write " Stone" Or "Stone "')
                        time.sleep(2.5)
                        print(' Still Not Solved Kindly Drop Your Problem In Issue Section In Github :)')
                        time.sleep(2)
                        print(' Thats all!! Done!! :D')
                        input(' Press Enter To Quit The Game And Try Again :)')
                        quit()
                    elif Help == 'N':
                        time.sleep(0.7)
                        print('Bye Bye!..')
                        time.sleep(1) 
                        quit()
                    elif Help == 'No':
                        time.sleep(0.7)
                        print('Bye Bye!..')
                        time.sleep(1) 
                        quit()
                    elif Help != 'Yes' or 'Y':
                        time.sleep(0.7)
                        print(' Sry :( Try Again!')
                        time.sleep(1) 
                        quit()
                    else:
                        time.sleep(0.7)
                        print(' Sry :( Try Again!')
                        time.sleep(1) 
                        quit()           

        Player = player.capitalize()            
        #Result

        time.sleep(1.5)
    # Result

        if Player == Com:
            print(' Match Draw')
        elif  Player == 'Stone' and Com == 'Stone':
            print(' Match Draw')
        elif  Player == 'Paper' and Com == 'Paper':
            print(' Match Draw')
        elif  Player == 'Scissor' and Com == 'Scissor':
            print(' Match Draw')
        elif Player == '1' and Com == 'Stone':
            print(' Match Draw')
        elif Player == '2' and Com == 'Paper':
            print(' Match Draw')
        elif Player == '3' and Com == 'Scissor':
            print(' Match Draw')
        elif Player == a1 and Com  == 'Stone':
                print(' Match Draw')
        elif Player == a2 and Com  == 'Paper':
                print(' Match Draw')
        elif Player == a3 and Com  == 'Scissor':
                print(' Match Draw')
        elif Player == 'Stone' and Com == 'Paper':
            print(' You Lose')
        elif Player == 'Stone' and Com == 'Scissor':
            print(' You Won')
        elif Player == 'Paper' and Com == 'Scissor':
            print(' You Lose')
        elif Player == 'Paper' and Com == 'Stone':
            print(' You Won')
        elif Player == 'Scissor' and Com == 'Stone':
            print(' You Lose')
        elif Player == 'Scissor' and Com == 'Paper':
            print(' You Won')
        elif Player == a1 and Com == 'Paper':
            print(' You Lose')
        elif Player == a1 and Com == 'Scissor':
            print(' You Won')
        elif Player == a2 and Com == 'Scissor':
            print(' You Lose')
        elif Player == a2 and Com == 'Stone':
            print(' You Won')
        elif Player == a3 and Com == 'Stone':
            print(' You Lose')
        elif Player == a3 and Com == 'Paper':
            print(' You Won')  
        elif Player == '3' and Com == 'Stone':
            print(' You Lose')
        elif Player == '3' and Com == 'Paper':
            print(' You Won')
        elif Player == '2' and Com == 'Stone':
            print(' You Won')
        elif Player == '2' and Com == 'Scissor':
            print(' You Lose')
        elif Player == '1' and Com == 'Scissor':
            print(' You Won')
        elif Player == '1' and Com == 'Paper':
            print(' You Lose')
        else:
            print(' Sry, Try Again!..')
            time.sleep(1)
            quit()
                
        time.sleep(1)
        
    # Show Com Choosed 
        Player = player.capitalize()
        Com = com.capitalize()

        if Player == Com:
            print(' As Computer Also Choosed', Com)
        elif Player == 'Stone' and Com == 'Stone':
            print(' As Computer Also Choosed', Com)
        elif Player == 'Paper' and Com == 'Paper':
            print(' As Computer Also Choosed', Com)
        elif Player == 'Scissor' and Com == 'Scissor':
            print(' As Computer Also Choosed ', Com)
        elif Player == '1' and Com == 'Stone':
            print(' As Computer Also Choosed',Com)
        elif Player == '2' and Com == 'Paper':
            print(' As Computer Also Choosed',Com)
        elif Player == '3' and Com == 'Scissor':
            print(' As Computer Also Choosed',Com)
        elif Player == 'Stone' and Com == 'Paper':
            print(' As Computer Choosed', Com)
        elif Player == 'Stone' and Com == 'Scissor':
            print(' As Computer Choosed', Com)
        elif Player == 'Paper' and Com == 'Scissor':
            print(' As Computer Choosed', Com)
        elif Player == 'Paper' and Com == 'Stone':
            print( 'As Computer Choosed', Com)
        elif Player == 'Scissor' and Com == 'Stone':
            print(' As Computer Choosed', Com)
        elif Player == 'Scissor' and Com == 'Paper':
            print(' As Computer Choosed', Com)
        elif Player == a1 and Com  == ' Stone':
            print(' As Computer Also Choosed', Com)
        elif Player == a2 and Com  == ' Paper':
            print(' As Computer Also Choosed', Com)
        elif Player == a3 and Com  == ' Scissor':
            print(' As Computer Also Choosed', Com)
        elif Player == a1 and Com == 'Paper':
            print(' As Computer Choosed', Com)
        elif Player == a1 and Com == 'Scissor':
            print( ' As Computer Choosed', Com)
        elif Player == a2 and Com == 'Scissor':
            print(' As Computer Choosed', Com)
        elif Player == a2 and Com == 'Stone':
            print(' As Computer Choosed', Com)
        elif Player == a3 and Com == 'Stone':
            print(' As Computer Choosed', Com)
        elif Player == a3 and Com == 'Paper':
            print(' As Computer Choosed', Com)
        elif Player == '3' and Com == 'Stone':
            print(' As Computer Choosed', Com)
        elif Player == '3' and Com == 'Paper':
            print(' As Computer Choosed', Com)
        elif Player == '2' and Com == 'Stone':
            print(' As Computer Choosed', Com)
        elif Player == '2' and Com == 'Scissor':
            print(' As Computer Choosed', Com)
        elif Player == '1' and Com == 'Scissor':
            print(' As Computer Choosed', Com)
        elif Player == '1' and Com == 'Paper':
            print(' As Computer Choosed', Com)
        else:
            print('Sry! :(')
            time.sleep(1)
            quit()
        time.sleep(1)

        
    #Score 
        while s_com <= 5 or s_player <= 5:
            if Player == 'Stone' and Com == 'Stone' or Player == 'Paper' and Com == 'Paper' or Player == 'Scissor' and Com == 'Scissor' or Player == '1' and Com == 'Stone' or Player == '2' and Com == 'Paper' or Player == '3' and Com == 'Scissor' or Player == Com:
                if s_com == s_player:
                    print(' Your Score And Computer Score Is Still:', s_com)
                    time.sleep(1)
                    break
                elif s_com != s_player:
                    print(' Your Score Is', s_player)
                    time.sleep(1)
                    print(' And Computer Score Is', s_com)
                    break
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                    break
            elif Player == 'Stone' and Com == 'Paper' or Player == '1' and Com == 'Paper':
                s_com += 1
                if s_com == s_player:
                    print(' Your Score And Computer Score Is:', s_com)
                    time.sleep(1)
                elif s_com != s_player:
                    print(' Computer Scored 1 Point')
                    time.sleep(1.5)
                    print(' Computer Score Is:', s_com)
                    time.sleep(2)
                    print(' And Your Score Is:', s_player)
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                break
            elif Player == 'Stone' and Com == 'Scissor' or Player == '1' and Com == 'Scissor':
                s_player += 1
                if s_com == s_player:
                    print(' Your Score And Computer Score Is:', s_com)
                    time.sleep(1)
                elif s_com != s_player:
                    print(' You Scored 1 Point')
                    time.sleep(1.5)
                    print(' Your Score Is:', s_player)
                    time.sleep(2)
                    print(' And Computer Score Is:', s_com)
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                break
            elif Player == 'Paper' and Com == 'Stone' or Player == '2' and Com == 'Stone':
                s_player += 1
                if s_com == s_player:
                    print(' Your Score And Computer Score Is:', s_com)
                    time.sleep(1)
                elif s_com != s_player:
                    print(' You Scored 1 Point')
                    time.sleep(1.5)
                    print(' Your Score Is:', s_player)
                    time.sleep(2)
                    print(' And Computer Score Is:', s_com)
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                break
            elif Player == 'Paper' and Com == 'Scissor' or Player == '2' and Com == 'Scissor':
                s_com += 1
                if s_com == s_player:
                    print(' Your Score And Computer Score Is:', s_com)
                    time.sleep(1)
                elif s_com != s_player:
                    print(' Computer Scored 1 Point') 
                    time.sleep(1.5)
                    print(' Computer Score Is:', s_com)
                    time.sleep(2)
                    print(' And Your Score Is:', s_player)
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                break
            elif Player == 'Scissor' and Com == 'Stone' or Player == '3' and Com == 'Stone':
                s_com += 1
                if s_com == s_player:
                    print(' Your Score And Computer Score Is:', s_com)
                    time.sleep(1)
                elif s_com != s_player:
                    print(' Computer Scored 1 Point') 
                    time.sleep(1.5)
                    print(' Computer Score Is:', s_com)
                    time.sleep(2)
                    print(' And Your Score Is:', s_player)
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                break
            elif Player == 'Scissor' and Com == 'Paper' or Player == '3' and Com == 'Paper':
                s_player += 1
                if s_com == s_player:
                    print(' Your Score And Computer Score Is:', s_com)
                    time.sleep(1)
                elif s_com != s_player:
                    print(' You Scored 1 Point')
                    time.sleep(1.5)
                    print(' Your Score Is:', s_player)
                    time.sleep(2)
                    print(' And Computer Score Is:', s_com)
                else:
                    print(' Sry! Unable To Show Your Score :(')
                    time.sleep(1)
                    print(' Try Again!')
                break
            else:
                print(" Sry :( Can't Display Scoreboard!")
                quit()  
        
        if s_player == 5:
            time.sleep(1.5)

            print('\n You Scored 5 Points Which Means')
            time.sleep(1.5)
            if s_player - s_com > 1:
                print(' You Won This Match By',s_player - s_com,'Points','And Computer Lose This Match')
            elif s_player - s_com <= 1:
                print(' You Won This Match By',s_player - s_com,'Point','And You Computer This Match')
            time.sleep(1.5)
            again = input(' Do You Want To Play Again?\n Y/Yes or N/No \n')
            again = again.capitalize()
            if again == 'Y':
                print(' Ok! :)')
                time.sleep(1)
                s_com = 0
                s_player = 0
                shell = sys.stdout
                shell.write(' Loading!')
                str = '...'
                for letter in str:
                    sys.stdout.write(letter)
                    time.sleep(random.choice(delay))
                print(' Done!!')

            elif again == 'Yes':
                print(' Ok! :)')
                time.time(1)
                s_com = 0
                s_player = 0
                shell = sys.stdout
                shell.write(' Loading!')
                str = '...'
                for letter in str:
                    sys.stdout.write(letter)
                    time.sleep(random.choice(delay))
                print(' Done!!')
                
            elif 'No':
                print(' Ok! :(')
                time.sleep(1)
                print(' Bye Bye!')
                time.sleep(1)
                quit()
            elif 'N':
                print(' Ok! :(')
                time.sleep(1)
                print(' Bye Bye!')
                time.sleep(1)
                quit()
            else:
                print(' Sry :(')
                quit()
        
        elif s_com == 5:
            time.sleep(1.5)
            print('\n Computer Scored 5 Points, Which Means')
            time.sleep(1.5)
            if s_player - s_com > 1:
                print(' Computer Won This Match By',s_player - s_com,'Points','And You Lose This Match')
            elif s_player - s_com <= 1:
                print(' Computer Won This Match By',s_player - s_com,'Point','And You Lose This Match')
            time.sleep(1.5)
            again = input(' Do You Want To Play Again?\n Y/Yes or N/No \n')
            again = again.capitalize()
            if again == 'Y':
                print(' Ok! :)')
                time.sleep(1)
                s_com = 0
                s_player = 0
                shell = sys.stdout
                shell.write(' Loading!')
                str = '...'
                for letter in str:
                    sys.stdout.write(letter)
                    time.sleep(random.choice(delay))
                print(' Done!!')
                
            elif again == 'Yes':
                print(' Ok! :)')
                time.time(1)
                s_com = 0
                s_player = 0
                shell = sys.stdout
                shell.write(' Loading!')
                str = '...'
                for letter in str:
                    sys.stdout.write(letter)
                    time.sleep(random.choice(delay))
                print(' Done!!')
               
            elif 'No':
                print(' Ok! :(')
                time.sleep(1)
                print(' Bye Bye!')
                time.sleep(1)
                quit()
            elif 'N':
                print(' Ok! :(')
                time.sleep(1)
                print(' Bye Bye!')
                time.sleep(1)
                quit()
            else:
                print(' Sry :(')
                quit()       

        elif s_com <= 4 or s_player <= 4:
            time.sleep(1.5)
            again = input(' Do You Want To Continue The Game? :)\n Yes/Y Or No/N ?\n')
            Again = again.capitalize()
            if Again == 'No':
                print(' :(')
                time.sleep(1.5)
                if s_com > s_player:
                    time.sleep(1.5)
                    if s_com - s_player > 1:
                        print(' Ok! You Lose This Match By',s_player - s_com,'Points')
                    elif s_com - s_player <= 1:
                        print(' Ok! You Lose This Match By',s_player - s_com,'Point')
                elif s_player > s_com:
                    time.sleep(1.5)
                    if s_player - s_com > 1:
                        print(' Ok! You Won This Match By',s_player - s_com,'Points')
                    elif s_player - s_com <= 1:
                        print(' Ok! You Won This Match By',s_player - s_com,'Point')
                time.sleep(1)
                quit()
            elif Again == 'N':
                print(' :(')
                time.sleep(1.5)
                if s_com > s_player:
                    time.sleep(1.5)
                    if s_com - s_player > 1:
                        print(' Ok! You Lose This Match By',s_player - s_com,'Points')
                    elif s_com - s_player <= 1:
                        print(' Ok! You Lose This Match By',s_player - s_com,'Point')
                elif s_player > s_com:
                    time.sleep(1.5)
                    if s_player - s_com > 1:
                        print(' Ok! You Won This Match By',s_player - s_com,'Points')
                    elif s_player - s_com <= 1:
                        print(' Ok! You Won This Match By',s_player - s_com,'Point')
                time.sleep(1)
                quit()
            
            elif Again == 'Yes':
                print(' :)')
                time.sleep(1.5)
                shell = sys.stdout
                shell.write(' Loading!')
                str = '...'
                for letter in str:
                    sys.stdout.write(letter)
                    time.sleep(random.choice(delay))
                print(' Done! :)')
                time.sleep(1)
                print('\n Welcome Back',name+',')
            elif Again == 'Y':
                print(' :)')
                time.sleep(1.5)
                shell = sys.stdout
                shell.write(' Loading!')
                str = '...'
                for letter in str:
                    sys.stdout.write(letter)
                    time.sleep(random.choice(delay))
                print(' Done!!')
                time.sleep(1)
                print('\n Welcome Back',name+',')
        else:
            print(' :(')
            time.sleep(1)
            print(' Sry Try Again!')
            time.sleep(1.5)
            quit()
else:
    print(' Sry! Try Again :(')
    time.sleep(1)
    quit() 

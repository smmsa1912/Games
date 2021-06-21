# Starter
import time
print(' Kindly Wait The Game Is Loading!... :)')
time.sleep(1.5)
print(' Game Will Be Load Within 15 Sec')
time.sleep(1.5)
print(' Kindly Be Patient :D')
time.sleep(1)
       
def main():
    import random
    import time
    import sys
    
# Containers

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
# Com Selection
    ('\n')
    bold = '\033[1m'
    input(bold + ' \n Kindly Press Enter To Continue: \n')
    time.sleep(0.5)
    print(' Welcome')
    time.sleep(1)
    name = input(' Enter Your Nickname Here:\n')
    tool = ('Stone' , 'Paper' , 'Scissor')
    com = random.choice(tool)
    Name = name.capitalize()
    delay = 0.25 , 0.50 , 0.75 , 1 , 1.25 , 1.50
    print(' Ok!..')
    time.sleep(1)
    print(' Computer Is Choosing')
    shell = sys.stdout
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
    elif player != opt1 or opt2 or opt3 or opt4 or opt5 or opt6 or opt7 or opt8 or opt9 or a1 or a2 or a3:
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
        elif player != opt1 or opt2 or opt3 or opt4 or opt5 or opt6 or opt7 or opt8 or opt9 or a1 or a2 or a3:
            time.sleep(0.7)
            print(' :(')
            time.sleep(0.7)
            print (' Choose And Write From The Given Option Only Or Check The Spelling')
            time.sleep(0.7)
            print(' Sry, You Have Last Chance Enter Correctly Or You Will Be Quit!...')
            time.sleep(1)
            input(' Press Enter To Rechoose From The Option')
            player = input(' Which One Will You Choose \n' + ' ' + '[' +a1+']' + opt1 + ' ' 'Or' ' ' + '[' +a2+']' + opt2 + ' ' 'Or' ' ' + '[' +a3+']'+ opt3 + '\n' )
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
                Help = input('Do You Need Any Help In Choosing?? Yes/Y Or No/N')
                if Help == 'Yes' or 'yes' or 'YES' or 'Y' or 'y':
                    print(' Hello Welcome To The Game!!'),
                    time.sleep(1.5),
                    print(' If You Want To Choose Stone Or Scissor Or Paper'),
                    time.sleep(2.5), 
                    print(' There Are Two Ways,'),
                    time.sleep(1.5),
                    print(' 1. Just Type The The Number Of the Options'),
                    time.sleep(2), 
                    print(' For Example: To choose Stone Type "1" / To Choose Paper type "2" / To Choose Scissor Type "3"'),
                    time.sleep(2.5),
                    print(' Another Way Of Choosing:'),
                    time.sleep(1.5),
                    print(' 2. Just Type The Name'),
                    time.sleep(1.5),
                    print(' For Example: To Choose Stone Type "Stone" / To Choose Paper Type "Paper" / To Choose Scissor Type "Scissor"'),
                    time.sleep(2.5),
                    print(' If You Still Face Any Error Or It Shows "Sry Again"')
                    time.sleep(1)
                    print(' That Mean You Have Done Any Mistake')
                    time.sleep(1.5)
                    print(' You Should Avoid The Following Mistakes')
                    time.sleep(1.5)
                    print(' You Should Not Leave Any Spaces Before OR After a Word \n For Example:')
                    time.sleep(2)
                    print('If You Choosed Stone You Should Write "Stone" Or "1" You Should Not Write " Stone" Or "Stone "')
                    time.sleep(2.5)
                    print('Still Not Solved Kindly Drop Your Problem In Issue Section In Github :)')
                    time.sleep(2)
                    print(' Thats all !! Done!! :D')
                    main()
                elif Help == 'No' or 'no' or 'NO' or 'N' or 'n':
                    time.sleep(0.7)
                    print('Bye Bye!..')
                    time.sleep(1) 
                    quit()    
                else:
                    time.sleep(0.7)
                    print('Bye Bye!..')
                    time.sleep(1) 
                    quit()           

            
    import time
    #Result

    time.sleep(1.5)
# Result
    if  Player == 'Stone' and Com == 'Stone':
        print(' Match Draw')
    if  Player == 'Paper' and Com == 'Paper':
        print(' Match Draw')
    if  Player == 'Scissor' and Com == 'Scissor':
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
    elif player == a1 and Com  == 'Stone':
        print(' Match Draw')
    elif player == a2 and Com  == 'Paper':
        print(' Match Draw')
    elif player == a3 and Com  == 'Scissor':
        print(' Match Draw')
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
        
    time.sleep(1.5)

# Show Com Choosed 

    if Player == Com:
        print(' As Computer Also Choosed', Com)
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
    elif player == a1 and Com  == ' Stone':
        print(' As Computer Also Choosed', Com)
    elif player == a2 and Com  == ' Paper':
        print(' As Computer Also Choosed', Com)
    elif player == a3 and Com  == ' Scissor':
        print(' As Computer Also Choosed', Com)
    elif Player == a1 and Com == 'Paper':
        print(' As Computer Choosed', Com)
    elif Player == a1 and Com == 'Scissor':
        print( 'As Computer Choosed', Com)
    elif Player == a2 and Com == 'Scissor':
        print(' As Computer Choosed', Com)
    elif Player == a2 and Com == 'Stone':
        print(' As Computer Choosed', Com)
    elif Player == a3 and Com == 'Stone':
        print(' As Computer Choosed', Com)
    elif Player == a3 and Com == 'Paper':
        print(' As Computer Choosed', Com)
    else:
        print('Sry! :(')
    time.sleep(1.5)

    

   #play Again
    
    a = 'yes'
    si = 'no'
    s = 'NO'
    S = 'No'
    ss = 'N'
    SS = 'n'
    Ag = 'Yes'
    ag = 'YES'
    aa = 'Y'
    aaa = 'y'
    time.sleep(1)
    again = input(' Do You Want To Play Again (Yes/Y Or No/N) \n')
    if again == a:
        time.sleep(1)
        print(' Thank You')
        time.sleep(1.5)
        
        main() 
        ('\n')


    elif again == Ag:
        time.sleep(1)
        print(' Thank You')
        time.sleep(1.5)
       
        main()
        ('\n')

    elif again == aaa:
        time.sleep(1)
        print(' Thank You')
        time.sleep(1.5)
        
        main() 
        ('\n')

    elif again == aa:
        time.sleep(1)
        print(' Thank You')
        time.sleep(1.5)
        
        main() 
        ('\n')

    elif again == ag:
        time.sleep(1)
        print(' Thank You')
        time.sleep(1.5)
        main() 
        ('\n')




    elif again == S:
        print('Thank You' + ' ' + Name + ' ' + 'For Playing' )
        time.sleep(1)
        print('Bye Bye')
        time.sleep(1.5)
        quit()
    elif again == SS:
        print('Thank You' + ' ' + Name + ' ' + 'For Playing' )
        time.sleep(1)
        print('Bye Bye')
        time.sleep(1.5)
        quit()
    elif again == ss:
        print('Thank You' + ' ' + Name + ' ' + 'For Playing' )
        time.sleep(1)
        print('Bye Bye')
        time.sleep(1.5)
        quit()
    elif again == s:
        print('Thank You' + ' ' + Name + ' ' + 'For Playing' )
        time.sleep(1)
        print('Bye Bye')
        time.sleep(1.5)
        quit()
    elif again == si:
        print('Thank You' + ' ' + Name + ' ' + 'For Playing' )
        time.sleep(1)
        print('Bye Bye')
        time.sleep(1.5)
        quit()
    else:
        print('Sry, Try Again! :(')
        time.sleep(1)
        quit()
main()
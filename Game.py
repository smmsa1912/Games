#Import
def main():
   
    import random
    import time
    import sys

    
    #Containers

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
    user = 0
    com_ = 0

    #Setting
    ('\n')
    bold = '\033[1m'
    enter = (bold + ' \n Kindly Press Enter To Continue: \n')
    a = input(enter)
    time.sleep(0.5)
    print(' Welcome')
    time.sleep(1)
    name = input(' Enter Your Name Here:\n')
    tool = ('Stone' , 'Paper' , 'Scissor')
    com = random.choice(tool)
    Name = name.capitalize()
    print(' Ok!..')
    time.sleep(1)
    print(' Computer Is Choosing')
    shell = sys.stdout
    shell.write(' Choosing')
    str = '...'
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(random.randint(1,2))
    print(' Done!! \n')
    time.sleep(2)
    print(' Now Your Turn,')
    time.sleep(1)
    player = input(' Which One Will You Choose \n' + ' ' + opt1 + ' ' + opt2 + ' ' 'Or' ' ' + opt3 + '\n' )

    #Player Choice

    if player == opt1:
        print(' Ok! You Choosed Stone!..')
    elif player == opt2:
        print(' Ok! You Choosed Paper!..')
    elif player == opt3:
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
    elif player == opt9:
        print(' Ok! You Choosed Scissor!..')
    else:
        print (' Choose And Write From The Given Option Only Or Check The Spelling')
        time.sleep(1)
        input(' Press Enter To Rechoose From The Option')
        player = input(' Which One Will You Choose \n' + ' ' + opt1 + ' ' + opt2 + ' ' 'Or' ' ' + opt3 + '\n' )
        if player == opt1:
            print(' Ok! You Choosed Stone!..')
        elif player == opt2:
            print(' Ok! You Choosed Paper!..')
        elif player == opt3:
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
        elif player == opt9:
            print(' Ok! You Choosed Scissor!..')
        else:
            print(' Sry, Try Again! :(')
            quit()

    #Result

    Player = player.capitalize()
    Com = com.capitalize()

    time.sleep(1.5)

    if Player == com:
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
    else:
        print(' Sry, Try Again')
        time.sleep(1)
        quit()
    time.sleep(1.5)

    if ' Match Draw' or 'Match Draw':
        print('As Computer Also Choosed' + ' ' + com)
    elif ' You Won':
        print(' As Computer Choosed,' , Com)
    elif ' You Lose':
        print(' As Computer Choosed,' , Com)
    elif (' Match Draw'):   
        print('As Computer Also Choosed' + ' ' + com)
    elif ():
        print('As Computer Also Choosed' + ' ' + com)
    else:
        print('Sry :( Server Problem!...')
        quit()


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

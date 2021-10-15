import random 

def choose():
    words=['rainbow','computer','science','Programming','Mathematics','player','condition','reverse','water','board']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,' Your score is :',p1)
    print(p2n,' Your score is :',p2)
    print("Thanks for Playing")
    print("Have a Nice Day...")


def play():
    p1name = input("player 1, Please Enter your name" )
    p2name = input("player 2, Please Enter your name" )
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task
        picked_word = choose()
        #create question
        qn = jumble(picked_word)
        print(qn)
        # for Player 1
        if turn % 2 ==0 :
            print(p1name," your turn. ")
            ans = input("what is in my Mind ? ")
            if ans == picked_word:
                pp1=pp1+1
                print("your score is : ",pp1)
            else:
                print("Better Luck Next Time . I Thought :",picked_word)
            c = input('Press 1 to continue and 0 to quit :')
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        # for Player 2
        else:
            print(p2name," your turn. ")
            ans = input("what is in my Mind ? ")
            if ans == picked_word:
                pp2=pp2+1
                print("your score is : ",pp2)
            else:
                print("Better Luck Next Time . I Thought :",picked_word)
            c = int(input('Press 1 to continue and 0 to quit :'))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn = turn + 1
        
        
        
play()

import random
def choice():
    words=['air', 'computer', 'science', 'window',
         'python', 'english', 'baseball', 'india',
         'front', 'liquid', 'ball', 'codealpha']
    return random.choice(words)
def game():
    word=choice()
    guesses=''
    print("guess the letter")
    turns=10
    while turns>0:
        failed=0
        print("guess again")
        for i in word:
            if i in guesses:
                print(i,end=' ')
            else:
                print('-',end=' ')
                failed+=1
        if failed==0:
            print("you won the game and guessed the word right")
            print("the word is ",word)
            break
        print()
        guess=input()
        guesses+=guess
        if guess in word:
            print("you guessed char is  ",guess,"  and you guessed it right" )
        if guess not in word:
            turns-=1
            print("you have ",turns,"have more guesses??")
            if turns==0:
                print("you lost")
                print("the word is ",word)
                break
    if turns==0:
        print("your score is 0")
    else:
        print("Your score is",turns*10)
if __name__=="__main__":
    game()
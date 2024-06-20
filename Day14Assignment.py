#                                          SYMBOL QUIZ GAME
#count=10 user will loss the game
#total=15 user will win the game
#total<=-10 user will loss the game
count=0
total=0
# function loss to reduce -1 from score
def loss(n):
    global count
    global total
    total-=1
    count+=1
    if total<=-10 or count==10:
        return "UNLUCKLY you loss the game"
    return "you hit button=",count,"time and your score now=",total 
# function win to increase +1 from score
def win(n):
    global count
    global total
    total+=1
    count+=1
    if total>=15 or count==10:
        return "LUCKLY you win the game"
    return "you hit  button=",count,"time and your score now=",total 
# function win_win to increase +4 from score
def win_win(n):
    global count
    global total
    total+=4
    count+=1
    if total>=15 or count==10:
        return "LUCKLY you win the game"
    return " you hit  button=",count,"time and WOW your score now=",total
# function loss_loss to reduce -4 from score
def loss_loss(n):
    global count
    global total
    total-=4
    count+=1
    if total<=-10 or count==10:
        return "UNLUCKLY you loss the game"
    return "you hit  button=",count,"time and unfortunately your score now=",total
#predefine dict(key_value pairs) 
quiz_dict={
    '#':loss,
    '@':win_win,
    '!':loss,
    '$':loss_loss,
    '%':win,
    '^':loss,
    '&':loss_loss,
    '*':win,
    '(':win_win,
    ')':loss,
    '|':loss,
    '?':win_win,
    ':':loss,
    ';':win,
    '}':win_win,
    '{':win,
    '"':loss,
    '>':win_win,
    '<':win,
    '~':loss_loss,
    '+':win,
    '_':loss,
    '=':win,
    '-':loss_loss,
    '`':win,
    '/':win_win,
    " ":loss
}
#start the game by press correct syntax of play key
initiate=True
while initiate:
    switch=input("Enter the play key ON = ")
    if switch=="ON":
        print("congratulation you unlock the device")
        initiate=False
    else:
        print("please enter the correct key")
        initiate=True
#for loop for showing the symbol which user can use
for symbol in quiz_dict:
    print(symbol)
#while loop to start game
start= True
while True:
    guess_symbol=input("HIT any special character =")
    get_symbol=quiz_dict.get(guess_symbol)
    if get_symbol:
        result=get_symbol(get_symbol)
        print(result)
        if count==10 or (total>=15 or total<=-10) or -10 in result:
            #ask user to play again or not
            again=input("Do you want to play to game again (yes/no)")
            lower_letter=again.lower()
            if lower_letter=="yes":
                start= True
                count=0
                total=0
            else:
                break
    else:
        #tell the user that user hit wrong key
        print("you enter the wrong character")
        start = False
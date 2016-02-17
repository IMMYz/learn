def start():
    print("Here is a long long bright way\nYou go 'right' or 'left'?")
    way = input(">")
    if way == 'left':
       ugly_girl()
    elif way == 'right':
         pretty_girl()
    else :
         print("you can't type?")



def ugly_girl():
    print("In the end of the road,there has a ugly girl")
    print("You can tell her u are 'ugly' or u are 'pretty'")
    question_again = False

    while True:
        next = input(">")
        if next == 'ugly' :
            dead("The ugly girl show her true face,it was very beautiful,but the light make you blind")
        elif next =='pretty' and not question_again:
            print("'I want hear you say the truth,her give you the second chance'")
            question_again = True
        elif next == 'pretty' and question_again:
            print("The girl in fact is very ugly,and she give you a hug,\nasking you to give her a date")
            date()


def pretty_girl():
    print("In the end of road,there has a pretty girl")
    print("You can tell her u are 'ugly' or u are 'pretty'")
    next = input(">")
        
    if next == 'ugly':
       dead("'No one dare said it to me',and the girl break your dick")
    elif next =='pretty':
         print("The girl give you a hug,and have a date with you")
         date()

def date():
    print("You can take girl to the cinema 'watch movie' or you can take her to 'hotal'")
    next = input(">")

    if next == 'watch movie':
       dead("You and the girl watched an boring movie,and the broke up")
    elif next == 'hotal':
        dead("you are a father.")
    else:
        print("nonono")
        

def dead(why):
    print(why,"\nGAME OVER!!")
    exit(0)

start()


from spy_details import spy_name,spy_age,spy_saluatation,spy_rating

print 'Let\'s get started'
question = "Continue  as "+spy_saluatation+" "+spy_name+"(Y/N)"
#print('Hey Jus checking if this ever comes here')
existing = raw_input(question)

def start_chat(spy_name,spy_age,spy_rating):
    menu_choices ="What do u want o do?\n 1:Add a status update\n"
    menu_choices =int (raw_input(menu_choices))
    #Just a comment for the sake of comment
    print("what's up bro?")
    #if(menu_choice==1):
        #print("Yo")
        #add Status Update
    #else:
        #Exit application



if existing.upper()=="Y":
    print "Authentication complete.Welcome"+spy_name+"age:"+str(spy_age)+"and rating:"+str(spy_rating)+"Proud to have you on leader board"

else:
    spy_name= raw_input("Welcome to spy chat, you must tell your spy name first!!!:")
    if len(spy_name)>0:
        spy_saluatation= raw_input("What should we call u(Mr or Ms)?")

        if len(spy_saluatation)>0:
            spy_name=spy_saluatation+" "+spy_name
            spy_age=input("what is your spy age?")
            if spy_age>12 and spy_age<50:
                spy_rating=input("what is your spy rating?")

                if spy_rating>4.5:
                    print "GREAT ACE"
                elif spy_rating>3.5 and spy_rating<=4.5:
                    print "You are one of the good ones"
                elif spy_rating>=2.5 and spy_rating<=3.5:
                    print "you can always do better"
                else:
                    print "we can always use somebody to help in he office"
                spy_is_online = True
                print "Authentication complete.welcome "+spy_name+"age:"+str(spy_age)+"and rating of:"+str(spy_rating)+"Proud to have you on leaderboard"
                start_chat(spy_name,spy_age,spy_rating)
            else:
                print"sorry u r not age to be a spy"

            print"a spy needs to have a valid name.Try again please. "
                    


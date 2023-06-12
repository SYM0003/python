# customizez exception handling
    # exception helps us in denoting that someting went wrong in our program
    # sometime pvm may not have exception according to the requirement of the
    # programer so programer can define his own excepion and can use it inside
    # the program to fullfill his requirements

    # i.e. suppose you are devoleping a matrimonial site where you have instruction
    # that the age of the applicant must be between 18 to 60, so if any user who's age
    # is not in this range than he is not valid applicant for the site so we can use
    # exception handling concept over here
    # we can create to exception here-->
    # TooYoung()
    # TooOld()

    # who to define used defined exception

    # # method 1
    # class ExceptionName(BaseException):
    #     def __init__(self,msg):
    #         self.msg=msg
    
    # # method 2
    # class ExceptionName(Exception):
    #     def __init__(self,msg):
    #         self.msg=msg



class TooOld(BaseException):
    def __init__(self,msg):
        self.msg=msg

class TooYoung(Exception):
    def __init__(self,msg):
        self.msg=msg
    

# how to raise userdefindex exception: since pvm don't to
#  about when should it raise the user defined exceptions 
# so that progrmer is resposible to raise these exception 
# accordig to his requirment

# in our case we shoud raise TooYoung exception if age<18
# and should raise TooOld exception if age>60

age=int(input('Enter your age'))

if age<18 :
    raise TooYoung('you are too young for marriede')
elif age>60 :
    raise TooOld('Now you should rest')
else:
    print('We will mail your details of your match')
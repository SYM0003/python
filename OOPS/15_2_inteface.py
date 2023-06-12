#interface:
# it is the concept of reprsenting the requrement of the software that 
# is is gonna create by the devoleper

# at the intial stage of the devolepment of any software we may not have the
# idead about implimentation of the requirement, so we just write down the 
# requirements in document (SRS), so that a we may have the blueprint of the 
# software
# 
# in Java there is special class which support for SRS which is called
# NOTE interface NOTE but in python we don't have such concept
#
# but we can use the abstraction class concept for the same requirement
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# an abstract class that contais only abstract method can be considered as
# an interface class.
# 
# EXAMPLE: Suppose we have a client and he told us following requirement for 
# his software: he want to automate some process in his organisation
# so he came to you and told these requiremnt
# 
# 1. software should have a feature for updating the salary of employee 
# automatically
# 2. software should have a feature for getting the sallary of each and
# particular employee
# 3. 
# 1. software should have a feature for updating the attandance of employee 
# automatically
# 2. software should have a feature for getting the attandance detail of
# each and particular employee
# 
# 
# 
# intially we don't have about imlimentation of the software so we will create 
# the interface for the requirement of the sofrware and than we will start working 
# on it.
# 
# 
# interface for the requirement
# 

from abc import ABC,abstractmethod
# interface class
class college_automation(ABC):
    @abstractmethod
    def update_salary():
        pass 
    @abstractmethod
    def get_salary():
        pass 
    @abstractmethod
    def get_attandance():
        pass 
    @abstractmethod
    def update_attandance():
        pass 

# suppose after a period of time we got solution for some requirement 
# of the software so the class with partially implimentation is called 
# abstract class------------>
# abstract class 
class Absclass(college_automation):
    def update_salary(self):
        print('updating salary') 
    def update_attandance(self):
        print('updating attendance') 

# the class with full imlimentation is called cocrete class/normal class
class Concrete(Absclass):
    def get_attandance(self):
        print('getting attandance details') 
    def get_salary(self):
        print('getting salary details') 

c=Concrete()
c.get_attandance()
c.get_salary()
c.update_attandance()
c.update_salary()


# we can't create the objects for interface class and abtact class
#  but we  can create obj of concrete class 

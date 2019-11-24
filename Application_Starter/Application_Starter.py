'''
Description of the module:
    - this is the starting point of the application
'''

from Repository.Repository import ShoppingListRepository
from Controller.Controller import Controller
from User_Interface.User_Interface import UserInterface
from Test.Test_All import runTests



repository = ShoppingListRepository()
controller = Controller(repository)
userInterface = UserInterface(controller)



runTests()
userInterface.runApplication()
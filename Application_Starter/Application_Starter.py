from Test.Test_All import runTests
from Repository.Repository import ShoppingListRepository
from Controller.Controller import Controller
from User_Interface.User_Interface import UserInterface



repository = ShoppingListRepository()
controller = Controller(repository)
userInterface = UserInterface(controller)



runTests()
userInterface.runApplication()
'''
Description of the module:
    - it contains all the code used for testing the functionalities from the repository
'''

from Domain.Domain import ShoppingListItem
from Repository.Repository import ShoppingListRepository



class TestRepository:
    
    '''
    Description:
        - it defines all the tests for the class "Repository"
    '''
    
    
    def __init__ (self):
        
        '''
        Description:
            - it initializes the list with some data
        Input:
            - none
        Output:
            - the attributes of the class are initialized
        '''
        
        self.__item_1 = ShoppingListItem("bread", 2)
        self.__item_2 = ShoppingListItem("milk", 4, True)
        self.__item_3 = ShoppingListItem("cake")
        
        self.__list_1 = ShoppingListRepository([self.__item_1, self.__item_2, self.__item_3])
        self.__list_2 = ShoppingListRepository()
        self.__list_3 = ShoppingListRepository([self.__item_2])
        
    
    def test_getListOfItems (self):
        
        '''
            Description:
                - it tests the "getListOfItems" method inside the class "ShoppingListRepository"
            Input:
                - none
            Output:
                - true, if all the tests pass (the method works correctly)
                - false, otherwise
        '''
        
        assert self.__list_1.getListOfItems() == [self.__item_1, self.__item_2, self.__item_3]
        assert self.__list_2.getListOfItems() == []
        assert self.__list_3.getListOfItems() == [self.__item_2]
    
    
    def test_getSizeOfList (self):
        
        '''
            Description:
                - it tests the "getSizeOfList" method inside the class "ShoppingListRepository"
            Input:
                - none
            Output:
                - true, if all the tests pass (the method works correctly)
                - false, otherwise
        '''
        
        assert self.__list_1.getSizeOfList() == 3
        assert self.__list_2.getSizeOfList() == 0
        assert self.__list_3.getSizeOfList() == 1
        
        
    def test_getItemOnPosition (self):
        
        '''
            Description:
                - it tests the "getItemOnPosition" method inside the class "ShoppingListRepository"
            Input:
                - none
            Output:
                - true, if all the tests pass (the method works correctly)
                - false, otherwise
        '''
        
        assert self.__list_1.getItemOnPosition(1) == self.__item_2
        assert self.__list_1.getItemOnPosition(2) == self.__item_3
        assert self.__list_3.getItemOnPosition(0) == self.__item_2
        
        
    def test_itemExists (self):
        
        '''
            Description:
                - it tests the "itemExists" method inside the class "ShoppingListRepository"
            Input:
                - none
            Output:
                - true, if all the tests pass (the method works correctly)
                - false, otherwise
        '''
        
        assert self.__list_1.itemExists(self.__item_1) == 0
        assert self.__list_1.itemExists(self.__item_3) == 2
        assert self.__list_2.itemExists(self.__item_3) == -1
        assert self.__list_3.itemExists(self.__item_2) == -1
        
        
    def test_addItem (self):
        
        '''
            Description:
                - it tests the "addItem" method inside the class "ShoppingListRepository"
            Input:
                - none
            Output:
                - true, if all the tests pass (the method works correctly)
                - false, otherwise
        '''
        
        newItem_1 = ShoppingListItem("Coke", 2)
        newItem_2 = ShoppingListItem("Eggs", 1)
        newItem_3 = ShoppingListItem("Chair", 3)
        
        self.__list_1.addItem(newItem_1)
        self.__list_1.addItem(newItem_2)
        self.__list_1.addItem(newItem_3)
        self.__list_2.addItem(newItem_2)
        
        assert self.__list_1.getListOfItems() == [self.__item_1, self.__item_2, self.__item_3, newItem_1, newItem_2, newItem_3]
        assert self.__list_2.getListOfItems() == [newItem_2]
        
    
    def test_crossCheck (self):
        
        '''
            Description:
                - it tests the "crossCheck" method inside the class "ShoppingListRepository"
            Input:
                - none
            Output:
                - true, if all the tests pass (the method works correctly)
                - false, otherwise
        '''
        
        self.__list_1.crossCheck(self.__item_1)
        self.__list_1.crossCheck(self.__item_3)
        self.__list_3.crossCheck(self.__item_2)
        
        assert self.__list_1.getItemOnPosition(0).getItemCrossChecked() == True
        assert self.__list_1.getItemOnPosition(1).getItemCrossChecked() == True
        assert self.__list_1.getItemOnPosition(2).getItemCrossChecked() == True
        assert self.__list_3.getItemOnPosition(0).getItemCrossChecked() == True
    
    
    def runRepositoryTests (self):
        
        '''
            Description:
                - it runs all the repository-related tests
            Input:
                - none
            Output:
                - true, if all the tests pass (all the functionalities work correctly)
                - false, otherwise
        '''
        
        self.test_getListOfItems()
        self.test_getSizeOfList()
        self.test_getItemOnPosition()
        self.test_itemExists()
        self.test_addItem()
        self.test_crossCheck()
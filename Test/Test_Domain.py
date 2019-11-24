'''
Description of the module:
    - it contains all the code used for testing the functionalities from the domain
'''

from Domain.Domain import ShoppingListItem



class TestDomain:
    
    '''
    Description:
        - it defines all the tests for the class "ShoppingListItem"
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


    def test_getItemName (self):
        
        '''
        Description:
            - it tests the "getItemName" method inside the class "ShoppingListItem"
        Input:
            - none
        Output:
            - true, if all the tests pass (the method works correctly)
            - false, otherwise
        '''
        
        assert self.__item_1.getItemName() == "bread"
        assert self.__item_2.getItemName() == "milk"
        assert self.__item_3.getItemName() == "cake"
    
    
    def test_getItemQuantity (self):
        
        '''
        Description:
            - it tests the "getItemQuantity" method inside the class "ShoppingListItem"
        Input:
            - none
        Output:
            - true, if all the tests pass (the method works correctly)
            - false, otherwise
        '''
        
        assert self.__item_1.getItemQuantity() == 2
        assert self.__item_2.getItemQuantity() == 4
        assert self.__item_3.getItemQuantity() == 1
        
        
    def test_getItemCrossChecked (self):
        
        '''
        Description:
            - it tests the "getItemCrossChecked" method inside the class "ShoppingListItem"
        Input:
            - none
        Output:
            - true, if all the tests pass (the method works correctly)
            - false, otherwise
        '''
        
        assert self.__item_1.getItemCrossChecked() == False
        assert self.__item_2.getItemCrossChecked() == True
        assert self.__item_3.getItemCrossChecked() == False
    
    
    def test_setItemQuantity (self):
        
        '''
        Description:
            - it tests the "setItemQuantity" method inside the class "ShoppingListItem"
        Input:
            - none
        Output:
            - true, if all the tests pass (the method works correctly)
            - false, otherwise
        '''
        
        self.__item_1.setItemQuantity(5)
        self.__item_2.setItemQuantity(1)
        self.__item_3.setItemQuantity(4)
        
        assert self.__item_1.getItemQuantity() == 5
        assert self.__item_2.getItemQuantity() == 1
        assert self.__item_3.getItemQuantity() == 4
        
        
    def test_setItemCrossChecked (self):
        
        '''
        Description:
            - it tests the "setItemCrossChecked" method inside the class "ShoppingListItem"
        Input:
            - none
        Output:
            - true, if all the tests pass (the method works correctly)
            - false, otherwise
        '''
        
        self.__item_1.setItemCrossChecked(True)
        self.__item_2.setItemCrossChecked(False)
        self.__item_3.setItemCrossChecked(True)
        
        assert self.__item_1.getItemCrossChecked() == True
        assert self.__item_2.getItemCrossChecked() == False
        assert self.__item_3.getItemCrossChecked() == True
    
    
    def runDomainTests (self):
        
        '''
        Description:
            - it runs all the domain-related tests
        Input:
            - none
        Output:
            - true, if all the tests pass (all the functionalities work correctly)
            - false, otherwise
        '''
        
        self.test_getItemName()
        self.test_getItemQuantity()
        self.test_getItemCrossChecked()
        self.test_setItemQuantity()
        self.test_setItemCrossChecked()
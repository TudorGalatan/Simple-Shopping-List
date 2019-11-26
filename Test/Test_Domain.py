'''
    This module contains all the code used for testing the functionalities from the domain.
'''

from Domain.Domain import ShoppingListItem



class TestDomain:
    
    '''
        This class defines all the tests for the class "ShoppingListItem".
    '''


    def __init__ (self):
        
        '''
            This method initializes the class with some data.
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        self.__item_1 = ShoppingListItem("bread", 2)
        self.__item_2 = ShoppingListItem("milk", 4, True)
        self.__item_3 = ShoppingListItem("cake")


    def test_getItemName (self):
        
        '''
            This method tests the "getItemName" method inside the class "ShoppingListItem".
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        assert self.__item_1.getItemName() == "bread"
        assert self.__item_2.getItemName() == "milk"
        assert self.__item_3.getItemName() == "cake"
    
    
    def test_getItemQuantity (self):
        
        '''
            This method tests the "getItemQuantity" method inside the class "ShoppingListItem".
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        assert self.__item_1.getItemQuantity() == 2
        assert self.__item_2.getItemQuantity() == 4
        assert self.__item_3.getItemQuantity() == 1
        
        
    def test_getItemCrossChecked (self):
        
        '''
            This method tests the "getItemCrossChecked" method inside the class "ShoppingListItem".
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        assert self.__item_1.getItemCrossChecked() == False
        assert self.__item_2.getItemCrossChecked() == True
        assert self.__item_3.getItemCrossChecked() == False
    
    
    def test_setItemQuantity (self):
        
        '''
            This method tests the "setItemQuantity" method inside the class "ShoppingListItem".
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        self.__item_1.setItemQuantity(5)
        self.__item_2.setItemQuantity(1)
        self.__item_3.setItemQuantity(4)
        
        assert self.__item_1.getItemQuantity() == 5
        assert self.__item_2.getItemQuantity() == 1
        assert self.__item_3.getItemQuantity() == 4
        
        
    def test_setItemCrossChecked (self):
        
        '''
            This method tests the "setItemCrossChecked" method inside the class "ShoppingListItem".
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        self.__item_1.setItemCrossChecked(True)
        self.__item_2.setItemCrossChecked(False)
        self.__item_3.setItemCrossChecked(True)
        
        assert self.__item_1.getItemCrossChecked() == True
        assert self.__item_2.getItemCrossChecked() == False
        assert self.__item_3.getItemCrossChecked() == True
    
    
    def runDomainTests (self):
        
        '''
            This method runs all the domain-related tests.
            Input Parameters:
                - none
            Output Parameters:
                - none
        '''
        
        self.test_getItemName()
        self.test_getItemQuantity()
        self.test_getItemCrossChecked()
        self.test_setItemQuantity()
        self.test_setItemCrossChecked()
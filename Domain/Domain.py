'''
    This module contains the definition of the class used to represent a
    shopping list item and the operations that can be performed on
    that item.
'''



class ShoppingListItem:
    
    '''
        This class defines a shopping list item and the operations that
        can be performed on it.
    '''
    
    
    def __init__ (self, itemName = None, itemQuantity = 1, itemCrossChecked = False):
        
        '''
            This method initializes the shopping list item object with the
            given or the implicit values.
            Input Parameters:
                - "itemName", the name of the item
                - "quantity", the quantity of the item (if not specified,
                  it is implicitly considered to be 1)
                - "crossChecked":
                    - False, if the item was not cross-checked (default)
                    - True, otherwise
            Output Parameters:
                - none
        '''
        
        self.__itemName = itemName
        self.__itemQuantity = itemQuantity
        self.__itemCrossChecked = itemCrossChecked
        
        
    def __str__ (self):
        
        '''
            This method defines the look of an object of the class as
            displayed on the screen.
            Input Parameters:
                - none
            Output Parameters:
                - "lookString", the string that defines the look of an
                  object on the screen
        '''
        
        lookString = self.__itemName + ' ' + str(self.__itemQuantity)
        
        return lookString
        
        
    def getItemName (self):
        
        '''
            This method returns the item name.
            Input Parameters:
                - none
            Output Parameters:
                - "itemName", the item name
        '''
        
        itemName = self.__itemName
        
        return itemName
    
    
    def getItemQuantity (self):
        
        '''
            This method returns the item quantity.
            Input Parameters:
                - none
            Output Parameters:
                - "itemQuantity", the item quantity
        '''
        
        itemQuantity = self.__itemQuantity
        
        return itemQuantity
    
    
    def getItemCrossChecked (self):
        
        '''
            This method returns the item's cross-checked value.
            Input Parameters:
                - none
            Output Parameters:
                - "itemCrossChecked", the item's cross-checked value
        '''
        
        itemCrossChecked = self.__itemCrossChecked
        
        return itemCrossChecked
    
    
    def setItemQuantity (self, newItemQuantity):
        
        '''
            This method changes the item quantity.
            Input Parameters:
                - "newItemQuantity", the new quantity of the item
            Output Parameters:
                - none
        '''
        
        self.__itemQuantity = newItemQuantity
        
        
    def setItemCrossChecked (self, newItemCrossChecked):
        
        '''
            This method changes the item's cross-checked value.
            Input Parameters:
                - "newItemCrossChecked", the new cross-checked value of the item
            Output Parameters:
                - none
        '''
        
        self.__itemCrossChecked = newItemCrossChecked
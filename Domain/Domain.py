'''
Description of the module:
    - it contains the definition of the class used to represent a
    shopping list item and the operations that can be performed on
    that item
'''



class ShoppingListItem:
    
    '''
    Description:
        - it defines a shopping list item and the operations that
          can be performed on it
    '''
    
    
    def __init__ (self, itemName = None, quantity = 1, crossChecked = False):
        
        '''
        Description:
            - it initializes the shopping list item object
        Input:
            - "itemName", the name of the item
            - "quantity", the quantity of the item (if not specified,
              it is implicitly considered to be 1)
            - "crossChecked":
                - False, if the item was not cross-checked (default)
                - True, otherwise
        Output:
            - the attributes of the class are initialized
        '''
        
        self.__itemName = itemName
        self.__itemQuantity = quantity
        self.__itemCrossChecked = crossChecked
        
        
    def __str__ (self):
        
        '''
        Description:
            - it defines the aspect of an object of the class as displayed on
              the screen
        Input:
            - none
        Output:
            - 
        '''
        
        string = self.__itemName + ' ' + str(self.__itemQuantity)
        
        return string
        
        
    def getItemName (self):
        
        '''
        Description:
            - it returns the item name
        Input:
            - none
        Output:
            - the item name
        '''
        
        return self.__itemName
    
    
    def getItemQuantity (self):
        
        '''
        Description:
            - it returns the item quantity
        Input:
            - none
        Output:
            - the item quantity
        '''
        
        return self.__itemQuantity
    
    
    def getItemCrossChecked (self):
        
        '''
        Description:
            - it returns the item cross-checked value
        Input:
            - none
        Output:
            - the item cross-checked value
        '''
        
        return self.__itemCrossChecked
    
    
    def setItemQuantity (self, newQuantity):
        
        '''
        Description:
            - it changes the item quantity
        Input:
            - "newQuantity", the new quantity of the item
        Output:
            - the item quantity is changed
        '''
        
        self.__itemQuantity = newQuantity
        
        
    def setItemCrossChecked (self, newCrossChecked):
        
        '''
        Description:
            - it changes the item cross-checked value
        Input:
            - "newCrossChecked", the new cross-checked value of the item
        Output:
            - the item cross-checked value is changed
        '''
        
        self.__itemCrossChecked = newCrossChecked
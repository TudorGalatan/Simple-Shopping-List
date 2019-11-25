'''
Description of the module:
    - it contains the definition of the class used to represent a
    list items repository and the operations that can be performed
    on that repository
'''



class ShoppingListRepository:
    
    '''
    Description:
        - it defines the repository of list items
    '''
    
    
    def __init__ (self, listOfItems = []):
        
        '''
        Description:
            - it initializes the repository of shopping list
              items with the list of items
        Input:
            - "listOfItems", the initial list of items which
              can be empty
        Output:
            - the repository is initialized with the list of
              items
        '''
        
        self.__listOfItems = listOfItems
        
        
    def getListOfItems (self):
        
        '''
        Description:
            - it returns the list of items
        Input:
            - none
        Output:
            - the list of items
        '''
        
        return self.__listOfItems
    
    
    def getSizeOfList (self):
        
        '''
        Description:
            - it returns the size of the list of items (the number
              of items in the list)
        Input:
            - none
        Output:
            - the size of the list of items
        '''
        
        return len(self.__listOfItems)
    
    
    def getItemOnPosition (self, position):
        
        '''
        Description:
            - it returns the item on the specified position
        Input:
            - "position": the given position
        Output:
            - the element on the given position
        '''
        
        return self.__listOfItems[position]
    
    
    def itemExists (self, item):
        
        '''
        Description:
            - it checks whether or not an item exists in the list
              of items
        Input:
            - "item", the item to be checked
        Output:
            - the position of the item on the list, if the
              item exists on the list
            - -1, otherwise
        '''
        
        for position in range (0, self.getSizeOfList()):
            if self.__listOfItems[position].getItemName() == item and self.__listOfItems[position].getItemCrossChecked() == False:
                return position
        
        return -1
    
    
    def addItem (self, newItem):
        
        '''
        Description:
            - it adds a new item to the list of items
        Input:
            - "newItem", the item to be added to the list
        Output:
            - the new item is added to the list of items, if it is not
              already on the list
            - the quantity of the item is increased by 1, if it is
              already on the list
        '''
        
        position = self.itemExists(newItem)
        
        if position == -1:
            self.__listOfItems.append(newItem)
            
        else:
            quantity = self.getItemOnPosition(position).getItemQuantity()
            newQuantity = quantity + 1
            self.__listOfItems[position].setItemQuantity(newQuantity)
            
    
    def crossCheck (self, item):
        
        '''
        Description:
            - it cross-checks the given item
        Input:
            - "item", the given item
        Output:
            - the given item is cross-checked on the list
        '''
        
        position = self.itemExists(item)
        
        if position == -1:
            return False
        
        self.__listOfItems[position].setItemCrossChecked(True)
        return True
    
    
    def removeCrossCheckedItem (self, itemName):
        
        '''
        Description:
            - it removes the cross-checked item
        Input:
            - "item", the given item
        Output:
            - the given cross-checked item is removed from the list
        '''
        
        position = self.itemExists(itemName)
        
        item = self.__listOfItems[position]
        
        if item.getItemCrossChecked() == True:
            self.__listOfItems.remove(item)
            return True
        
        return False
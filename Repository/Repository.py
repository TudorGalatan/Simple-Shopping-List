'''
    This module contains the definition of the class used to represent a
    list items repository and the operations that can be performed
    on that repository.
'''



class ShoppingListRepository:
    
    '''
        This class defines the repository of list items.
    '''
    
    
    def __init__ (self, listOfItems = []):
        
        '''
            This method initializes the repository of shopping list
            items with the list of items, if given, or with an empty
            list, otherwise.
            Input Parameters:
                - "listOfItems", the initial list of items, if given
            Output Parameters:
                - none
        '''
        
        self.__listOfItems = listOfItems
        
        
    def getListOfItems (self):
        
        '''
            This method returns the list of items.
            Input Parameters:
                - none
            Output Parameters:
                - "listOfItems", the list of items
        '''
        
        listOfItems = self.__listOfItems
        
        return listOfItems
    
    
    def getSizeOfList (self):
        
        '''
            This method returns the size of the list of items, i.e. the number
            of items in the list.
            Input Parameters:
                - none
            Output Parameters:
                - "sizeOfList", the size of the list of items
        '''
        
        sizeOfList = len(self.__listOfItems)
        
        return sizeOfList
    
    
    def getItemOnPosition (self, position):
        
        '''
            This method returns the item on the specified position.
            Input Parameters:
                - "position", the given position
            Output Parameters:
                - the element on the given position
        '''
        
        itemOnPosition = self.__listOfItems[position]
        
        return itemOnPosition
    
    
    def getPositionOfItem (self, itemName):
        
        '''
            This method returns the position on which the item with the given name is
            situated.
            Input Parameters:
                - "itemName", the name of the item to be found
            Output Parameters:
                - "positionOfItem", the position of the item in the list, if the
                  item exists, or -1, if it doesn't exist
        '''
        
        itemFound = False
        
        for position in range (0, self.getSizeOfList()):
            if itemFound == False and self.getItemOnPosition(position).getItemName() == itemName:
                positionOfItem = position
                itemFound = True
        
        if itemFound == False:
            positionOfItem = -1
        
        return positionOfItem
    
    
    def addItem (self, newItem):
        
        '''
            This method adds a new item to the list of items.
            Input Parameters:
                - "newItem", the item to be added to the list
            Output Parameters:
                - none
        '''
        
        positionOfItem = self.getPositionOfItem(newItem)
        
        if positionOfItem == -1:
            self.__listOfItems.append(newItem)
            
        elif self.getItemOnPosition(positionOfItem).getItemCrossChecked() == True:
            self.__listOfItems[positionOfItem].setItemCrossChecked() = False
            
        else:
            itemQuantity = self.getItemOnPosition(positionOfItem).getItemQuantity()
            newItemQuantity = itemQuantity + 1
            self.__listOfItems[positionOfItem].setItemQuantity(newItemQuantity)
            
    
    def crossCheck (self, item):
        
        '''
            This method marks an item as cross-checked.
            Input Parameters:
                - "item", the given item
            Output Parameters:
                - none
        '''
        
        positionOfItem = self.getPositionOfItem(item)
        
        if positionOfItem == -1 or self.getItemOnPosition(positionOfItem).getItemCrossChecked() == True:
            return False
        
        self.__listOfItems[positionOfItem].setItemCrossChecked(True)
        return True
    
    
    def removeCrossCheckedItem (self, itemName):
        
        '''
            This method removes the given cross-checked item.
            Input Parameters:
                - "itemName", the name of the given item
            Output Parameters:
                - none
        '''
        
        positionOfItem = self.getPositionOfItem(itemName)
        
        item = self.getItemOnPosition(positionOfItem)
        
        if item.getItemCrossChecked() == True:
            self.__listOfItems.remove(item)
            return True
        
        return False
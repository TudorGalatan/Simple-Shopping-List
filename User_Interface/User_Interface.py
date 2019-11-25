'''
Description of the module:
    - it contains the definition of the class used to represent the
      user interface
'''

from Domain.Domain import ShoppingListItem



class UserInterface:
    
    '''
    Description:
        - it contains the definition of the user interface functionalities
    '''
    
    
    def __init__ (self, controller):
        
        '''
        Description:
            - it initializes the user interface with the controller
        Input:
            - "controller", the controller to be used
        Output:
            - the user interface is initialized with the controller
        '''
        
        self.__controller = controller
        
    
    def printAllItems (self):
        
        '''
        Description:
            - it prints all the items on the screen
        Input:
            - none
        Output:
            - all the items are printed on the screen
        '''
        
        for item in self.__controller.getListOfItems():
            print(item, '\n')
            
            
    def printCrossCheckedItems (self):
        
        '''
        Description:
            - it prints all the cross-checked items on the screen
        Input:
            - none
        Output:
            - all the cross-checked items are printed on the screen
        '''
        
        for item in self.__controller.getListOfItems():
            if item.getItemCrossChecked() == True:
                print(item, '\n')
                
                
    def printUnCrossCheckedItems (self):
        
        '''
        Description:
            - it prints all the un-cross-checked items on the screen
        Input:
            - none
        Output:
            - all the un-cross-checked items are printed on the screen
        '''
        
        for item in self.__controller.getListOfItems():
            if item.getItemCrossChecked() == False:
                print(item, '\n')
                
                
    def addItem (self):
        
        '''
        Description:
            - it adds a new item to the repository, using the controller
        Input:
            - "item", the item to be added to the repository
        Output:
            - the new item is added to the repository, if it is not
              already in it
            - the quantity of the item is increased by 1, if it is
              already in the repository
        '''
        
        itemName = input("\nType the name of the item: ")
        itemQuantity = int(input("Type the quantity: "))
        
        item = ShoppingListItem(itemName, itemQuantity)
        
        self.__controller.addItem(item)
        
        
    def crossCheck (self):
        
        '''
        Description:
            - it cross-checks the given item
        Input:
            - "item", the given item
        Output:
            - the given item is cross-checked on the list
        '''
        
        item = input("\nType the name of the item: ")
        
        self.__controller.crossCheck(item)
        
        
    def removeCrossCheckedItem (self):
        
        '''
        Description:
            - it removes the cross-checked item
        Input:
            - "item", the given item
        Output:
            - the given cross-checked item is removed from the list
        '''
        
        item = input("\nType the name of the item: ")
        
        result = self.__controller.removeCrossCheckedItem(item)
        
        if result == True:
            print("\nThe operation succeeded.\n")
        else:
            print("\nThe item was not cross-checked.\n")
        
        
    def printMenu (self):
        
        '''
        Description:
            - it prints the menu with the available options on the screen
        Input:
            - none
        Output:
            - the menu is printed on the screen
        '''
        
        print("\n\t\tMENU\n\n")
        print("The available options are:\n")
        print("1. Print all the items.\n")
        print("2. Print all the cross-checked items.\n")
        print("3. Print all the un-cross-checked items.\n")
        print("4. Add a new item.\n")
        print("5. Cross-check an item.\n")
        print("6. Remove a cross-checked item.\n")
        print("7. Close the application.\n")
        
    
    def runApplication (self):
        
        '''
        Description:
            - it starts the user interface
        Input:
            - none
        Output:
            - the user interface starts running
        '''
        
        while (True):
            
            self.printMenu()
            print("Type the desired option: ")
            option = int(input())
            
            if option == 1:
                self.printAllItems()
                
            elif option == 2:
                self.printCrossCheckedItems()
            
            elif option == 3:
                self.printUnCrossCheckedItems()
            
            elif option == 4:
                self.addItem()
            
            elif option == 5:
                self.crossCheck()
            
            elif option == 6:
                self.removeCrossCheckedItem()
                
            elif option == 7:
                exit()
                
            else:
                print("This is not a valid option.\n")
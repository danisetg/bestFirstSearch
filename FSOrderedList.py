#Ordered List class

class HashTable:
    def __init__(self):
        self.table = {}  #We need to check the size table
    
    def Insert(self, value): #Input elements
        if not self.table.get(value):
            self.table.update({value: True})
   
    def Search(self,value): #Search elements
        if not self.table.get(value):
            return None
        else:
            return self.table.get(value)
  
    def Remove(self,value): #Delete elements
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            print("There are not elements with this value", value)
        else:
            print("Element with value ", value, " deleted")
            self.table[hash] is None

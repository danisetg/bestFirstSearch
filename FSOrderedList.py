#Ordered List class

class HashTable:
    def __init__(self):
        self.table = [None] * 127  #We need to check the size table
    
    # Función hash
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value): #Input elements
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value): #Search elements
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
    def Remove(self,value): #Delete elements
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            print("There are not elements with this value", value)
        else:
            print("Element with value ", value, " deleted")
            self.table[hash] is None

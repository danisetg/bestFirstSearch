#Ordered List class

class HashTable:
    def __init__(self):
        self.table = [None] * 127
    
    # Función hash
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value): # Metodo para ingresar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value): # Metodo para buscar elementos
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
    def Remove(self,value): # Metodo para eleminar elementos
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[hash] is None;
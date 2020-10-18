DATA = [[123,"Robin","AB4"],
        [124,"Nguyen","HD12"],
        [125,"Jev","L18"],
        [126,"Will","OX5"],
        [127,"Lily","CH3"],
        [128,"Jonny","YO12"],
        [129,"Clara","BS1"],
        [130,"Callum","BA1"]]

ATTRIBUTES = ["number", "name", "license plate"]

class HashTable:
    _lower_limit = 0.25
    _upper_limit = 0.75
    _linked_length = 3
    
    def __init__(self, items: list, attributes: list):
        self._bucket = []
        self._hash_table = []
        self._occupied = 0
        
        self._attributes = attributes
        self._length = int(len(items) / 0.75) + 1
        
        self.setup_table(items)
    
    def setup_table(self, items):
        self.new_table()
        
        for item in items:
            self.add_item(item)
            
        self.rehash_check()
    
    def new_table(self):
        self._hash_table = [[None] * HashTable._linked_length for i in range(self._length)]

    def add_item(self, item, converted=False):
        if not converted:
            item = self.convert_to_dict(item)
        index = item["key"] % self._length
         
        counter = 0
        item_added = False
        while counter < HashTable._linked_length and not item_added:
            if not self._hash_table[index][counter]:
                if counter == 0:
                    self._occupied += 1
                self._hash_table[index][counter] = item
                item_added = True
            counter += 1
        if not item_added:
            self._bucket.append(item)
                
    def hash(self, n):
        return n**2
    
    def convert_to_dict(self, item):
        converted_item = {}
        
        for i in range(len(self._attributes)):
            converted_item[self._attributes[i]] = item[i]
        
        key = self.hash(item[0])
        converted_item["key"] = key
        
        return converted_item

    def rehash_check(self):
        length_ratio = self._occupied / self._length
        
        if length_ratio < HashTable._lower_limit:
            self._length = self._length // 2 + 1
            self.rehash()
        elif length_ratio > HashTable._upper_limit:
            self._length *= 2
            self.rehash()
    
    def rehash(self):
        table_copy = self._hash_table.copy()
        self._occupied = 0
        self.new_table()
        
        for row in table_copy:
            for item in row:
                if item:
                    self.add_item(item, converted=True)

def main():
    members = HashTable(DATA, ATTRIBUTES)
    
    new_member = [131,"Kirsten","SE2"]
    members.add_item(new_member)
   
    members._length = 15
    members.rehash()

if __name__ == "__main__":
    main()
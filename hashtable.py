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


def main():
    members = HashTable(DATA, ATTRIBUTES)
    
    new_member = [131,"Kirsten","SE2"]
    members.add_item(new_member)
    for row in members._hash_table: print(row)
    
    print(members._occupied, members._length)
    
if __name__ == "__main__":
    main()
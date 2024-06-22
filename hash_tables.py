#hash tables
#hash é deterministico, por isso é tao eficiente que busquemos um valor pela key, pois é facil achar seu endereço na hash table
#pode ser que duas key produzam a mesma hash-- colisões
#separate chaining -  poe no mesmo endereço os hash que sao iguais
# open adreessing - ex linear probing (vai indo paa o proximo endereço ate achar um que esteja vazio)
#no pyhton é dicionario
#pode sr uma lista de lista o lista de lista de linked list
#o(i) assume-se que havera poucas colisoes, portando, get_item é o(1)
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None]*size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23 ) % len(self.data_map)
             #vai ir ate 6 que é o numero de endereços
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
         self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] == None:
            return None
        for pair in self.data_map[index]:
          if pair[0] == key:
            return pair[1]
        return None

    def keys(self):
      all_keys = []
      for list_pairs in self.data_map:
          if list_pairs is not None:
              for pair in list_pairs:
                  all_keys.append(pair[0])
      return all_keys



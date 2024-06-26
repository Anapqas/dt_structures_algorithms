##stacks##  Last In, First Out (LIFO)
#pop de uma linked list é o(n) entao o que a gnt quer é remover a tail e deixar só o head, que sera chamado de top
class Node:
    def __init__(self,value):
      self.value = value
      self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_top = Node(value)
        if self.height > 0:
          new_top.next = self.top

        self.top = new_top

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


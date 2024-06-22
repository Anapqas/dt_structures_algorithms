##linked list##
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # WRITE THE PRINT_LIST METHOD HERE #
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
      appended_node = Node(value)
      if(self.lenght == 0):
        self.head = appended_node
        self.tail = appended_node
      else:
        self.tail.next = appended_node
        self.tail = appended_node

      self.lenght +=1
      return True

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            penultimo = self.head
            while temp.next is not None:
                if temp.next == self.tail: #entao temp é o penultimo nó
                    penultimo = temp
                temp = temp.next
            self.tail = penultimo
            self.tail.next = None
            self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop2(self):
        if self.length == 0:
            return None

        pre = self.head
        temp = self.head
        while (temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend (self, value):
        new_node = Node(value)
        if self.length == 0:
           self.tail = new_node
        else:
           new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        temp.next = None
        self.length -=1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        node = self.get(index)
        if node:
           node.value = value
           return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)
        if index ==  self.length:
            return self.append(value)

        new_node =  Node(value)

        pre = self.get(index - 1)
        after = self.get(index)

        new_node.next = after
        pre.next = new_node
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        if index == (self.length - 1):
            return self.pop()

        pre  = self.get(index-1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self): #!!!
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before #flips the pointer
            before = temp #starts fixing the gap
            temp = after # fix the gap

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while (fast.next is not None):
            slow = slow.next
            if (fast.next == self.tail):
                break
            fast = fast.next.next
        return slow

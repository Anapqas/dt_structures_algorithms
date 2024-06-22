##TREE
##SE cada parente tem dois filhos é binaria
##a arvore pode ser full complete,e/ perfect
#full -  se o no tem duas ou nenhuma child
#complete - se os childs estao dispostos da esquerda para a direite sem gaps
#perfect - todos os nós estao completos
#um no pode ter apenas um parent
# um no sem filhos é leaf
# procurar alguam coisa em uma arvore - o(logn)
#para adicionar no final, list ou linked list é melhor o(1), mas para remover ou lookup, binary é melhor o(logn)
class Node:
    def __ini__(self, value):
      self.value = value
      self.right = None
      self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if (self.root is None):
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False #sai do loop, não insere se ja tem
            if (new_node.value < temp.value):
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left  #go left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                #desce o ponteiro
                temp = temp.right #go right

    def contains(self, value):
        if (self.root is None):
            return False
        temp = self.root
        while (True):
            if value == temp.value:
                return True #sai do loop
            if (value < temp.value):
                if temp.left is None:
                    return False
                temp = temp.left  #go left
            else:
                if temp.right is None:
                    return False
                #desce o ponteiro
                temp = temp.right #go right

    def contains(self, value):
        if (self.root is None):
            return False

        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left  #go left
            elif value > temp.value:
                #desce o ponteiro
                temp = temp.right #go right
            else:
                return True
        return False

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            __r_contains(current_node.value.left, value)
        if value > current_node.value:
            __r_contains(current_node.value.right, value)


    def r_contains(self, value):
        return self.__r_contains(self.root ,value)

my_tree = BinarySearchTree()

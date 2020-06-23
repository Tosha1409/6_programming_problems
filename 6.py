#Implementing linked list . Source https://realpython.com/linked-lists-python/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
       self.head = None
       if nodes is not None:
         node = Node(data=nodes.pop(0))
         self.head = node
         for elem in nodes:
            node.next = Node(data=elem)
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    #method for swamp nodes in pairs(task itself)
    def change_pairs(self):
        node = self.head

        #head element
        if node.next is not None: 
           self.head=node.next
           node.next, (self.head).next =(self.head).next, node

        #rest of elements
        while node.next is not None and node.next.next is not None:
           node.next, node.next.next, node.next.next.next = node.next.next, node.next, node.next.next.next
           node=node.next.next

#test
l=LinkedList(['1','2','3','4','5','6','7'])
print (l)
l.change_pairs()
print (l)
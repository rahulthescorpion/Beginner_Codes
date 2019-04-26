class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


class List:
    def __init__(self):
        self.head = None

    def printlist(self):
        t = self.head
        while t:
            print t.data
            t = t.pointer

    def insertNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            # self.next = None
        else:

            last = self.head
            # last.next = new_node
            while last.pointer:
                last = last.pointer
            last.pointer = new_node

    def insertNodeFirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.pointer = self.head
            self.head = new_node
            # print new_node.data
            # self.head = new_node

    def insertNodeAtPoint(self, position, data):
        pass

    def deleteNode(self, data):
        if self.head is None:
            print "Linked List is empty.."
        else:
            pass

li = List()

li.insertNode(1)
li.insertNode(2)
li.insertNode(3)
li.insertNode(4)

li.insertNodeFirst(5)

li.printlist()


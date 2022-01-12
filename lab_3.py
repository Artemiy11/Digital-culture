class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def insert_node(self, data):
		newNode = Node(data)
		if (self.head):
			current = self.head
			while (current.next):
				current = current.next
			current.next = newNode
		else:
			self.head = newNode

	def printLL(self):
		current = self.head
		while (current):
			print(current.data)
			current = current.next

def reversePrint(llist):
	current = llist

	while (current.next):
		current = current.next

	while (current != llist):
		print(current.data)  	


tests = int(input())

for tests_itr in range(tests):
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    reversePrint(llist.head)


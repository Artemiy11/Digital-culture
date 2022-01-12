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

def deleteNode(llist, position):
	llistLen = 0
	current = llist
	currentLen = llist
	newList = SinglyLinkedList()
	idx = 0

	while (idx != position):
		newList.insert_node(current.data)
		idx += 1
		current = current.next

	while (currentLen):
		llistLen += 1
		currentLen = currentLen.next

	while (position < llistLen - 1):
		position += 1
		current = current.next
		newList.insert_node(current.data)

	return newList.head



llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

position = int(input())

llist1 = deleteNode(llist.head, position


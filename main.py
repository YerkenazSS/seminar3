from linked_class import MyList, ListNode

lst = MyList()

nd = ListNode(10)
lst.enqueue(nd)
nd = ListNode(11)
lst.enqueue(nd)
nd = ListNode(12)
lst.enqueue(nd)
lst.dequeue(11)
#lst.remove(10)

for data in lst:
print(data)

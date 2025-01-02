# ArrayList
class ArrayList:
    def __init__(self):
        self.list = []
    
    def add(self, value):
        self.list.append(value)

    def remove(self, value):
        self.list.remove(value)
    
    def insert(self, index, value):
        self.list.insert(index, value)
    
    def get(self, index):
        return self.list[index]
    
    def size(self):
        return len(self.list)

# 定义链表的基本结构
class Node:
    def __init__(self, value):
        # Node value 定义结点的数值
        self.value = value
        # Next node 定义下一个结点的指针，指向下一个结点的地址
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # 链表头部添加结点(头插法)
    def add_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    # 链表尾部添加结点(尾插法)
    def add_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # 删除链表中的结点
    def remove(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        
    def inset(self, index, value):
        new_node = Node(value)
        current = self.head
        for i in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == '__main__':
    # Test ArrayList
    arrayList = ArrayList()
    arrayList.add(1)
    arrayList.add(2)
    arrayList.add(3)
    print(arrayList.get(0))
    print(arrayList.size())
    arrayList.remove(2)
    print(arrayList.size())
    
    # Test LinkedList
    linkedList = LinkedList()
    linkedList.add_tail(1)
    linkedList.add_tail(2)
    linkedList.add_tail(3)
    print(linkedList.get(0))
    print(linkedList.size())
    linkedList.remove(2)
    print(linkedList.size())
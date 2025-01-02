# stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
# 定义链表的基本结构
class Node:
    def __init__(self, value):
        # Node value 定义结点的数值
        self.value = value
        # Next node 定义下一个结点的指针，指向下一个结点的地址
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None

    # 往栈中插入数据
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    # 从栈中剔除数据
    def pop(self):
        if self.head == None:
            return None
        elif self.head != None and self.head.next == None:
            result = self.head.value
            self.head = None
            return result
        else:
            current_node = self.head
            next_node = self.head.next
            while next_node.next is not None:
                current_node  = next_node
                next_node = next_node.next
            result = current_node.next.value
            current_node.next = None
            return result

    # 显示栈中指定位置的值
    def show(self, index):
        if self.head == None:
            return None
        else:
            if index >= self.size():
                return "out of index"
            sub_index = 0
            current_node = self.head
            while sub_index != index:
                current_node = current_node.next
                sub_index +=1
            return current_node.value


    # 显示栈的长度
    def size(self):
        if self.head == None:
            return 0
        else:
            count = 1
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
                count +=1
            return count


class LinkedQueue:
    def __init__(self):
        self.head = None

    # 向队列中插入数据
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    # 从队列中剔除数据
    def pop(self):
        self.head = self.head.next
    

    # 显示栈中指定位置的值
    def show(self, index):
        if self.head == None:
            return None
        else:
            if index >= self.size():
                return "out of index"
            sub_index = 0
            current_node = self.head
            while sub_index != index:
                current_node = current_node.next
                sub_index +=1
            return current_node.value

    # 显示栈的长度
    def size(self):
        if self.head == None:
            return 0
        else:
            count = 1
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
                count +=1
            return count

if __name__ == "__main__":
    linkedStack = LinkedStack()
    linkedStack.add(1)
    linkedStack.add(2)
    linkedStack.add(3)
    linkedStack.add(4)
    print(linkedStack.show(3))
    print(linkedStack.size())

    linkedQueue = LinkedQueue()
    linkedQueue.add(128)
    linkedQueue.add(256)
    linkedQueue.add(512)
    print(linkedQueue.show(0))
    print(linkedQueue.size())
    
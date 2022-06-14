#! /usr/bin/python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

class Stack:
    def __init__(self):
        self.stack = list()
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1


class Queue:
    def __init__(self):
        self.queue = list()
    
    def push(self, value):
        self.queue.append(value)
    
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1


class Priority_Queue:
    def __init__(self):
        self.priority_queue = list()

    def push(self, value):
        self.priority_queue.append(value)
    
    def pop(self):
        if self.priority_queue:
            max_value = max(self.priority_queue)
            self.priority_queue.remove(max_value)
            return max_value
        else:
            return -1


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        stack = Stack()
        list_stack = list()

        queue = Queue()
        list_queue = list()

        priority_queue = Priority_Queue()
        list_priority_queue = list()

        for _ in range(n):
            command, x = [int(val) for val in input().split()]

            if command == 1:
                stack.push(x)
                queue.push(x)
                priority_queue.push(x)
            
            else:
                if stack.pop() == x:
                    list_stack.append(True)
                else:
                    list_stack.append(False)

                if queue.pop() == x:
                    list_queue.append(True)
                else:
                    list_queue.append(False)

                if priority_queue.pop() == x:
                    list_priority_queue.append(True)
                else:
                    list_priority_queue.append(False)
        
        data_structures = list()
        if all(list_stack):
            data_structures.append("stack")

        if all(list_queue):
            data_structures.append("queue")

        if all(list_priority_queue):
            data_structures.append("priority queue")

        if len(data_structures) == 0:
            print("impossible")
        elif len(data_structures) == 1:
            print(data_structures[0])
        else:
            print("not sure")


if __name__ == '__main__':
    main()
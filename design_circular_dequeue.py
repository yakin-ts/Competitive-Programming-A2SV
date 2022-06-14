class MyCircularDeque:
    
    def __init__(self, k: int):
        self.circular = [-]*k
        self.front = -1
        self.rear = -1
        self.count=0
        self.max = k
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.count==0:
                self.front +=1
                self.rear +=1
                self.circular[self.front]=value
            else:  
                if self.front==0:
                    self.front = self.max - 1
                else:
                    self.front -=1
                self.circular[self.front]=value
            self.count +=1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.count==0:
                self.rear +=1
                self.front +=1
                self.circular[self.rear]=value
            else:
                if self.rear==self.max-1:
                    self.rear = 0
                else:
                    self.rear +=1
            self.circular[self.rear]=value
            self.count +=1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.count==1:
                self.front = -1
                self.rear = -1
            elif self.front==self.max-1:
                self.front = 0
            else:
                self.front +=1
            self.count -=1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.count==1:
                self.front=-1
                self.rear=-1
            elif self.rear==0:
                self.rear = self.max -1
            else:
                self.rear -=1
            self.count -=1
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.circular[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.circular[self.rear]

    def isEmpty(self) -> bool:
        return self.count==0

    def isFull(self) -> bool:
        return self.count == self.max


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
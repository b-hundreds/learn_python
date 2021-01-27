class node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, d=None):
        self.data = d
    def set_next(self, d=None):
        self.next = d
class linked_note:
    def __init__(self, r=None, size=0):
        self.roof = r
        self.size = 0
    def add(self, d=None):
        new = node(d, self.roof)
        self.size += 1
        self.roof = new
    def get_size(self):
        return self.size
    def remove(self, d):
        now = self.roof
        if now.get_data() == d:
            self.size -= 1
            self.roof = now.get_next()
        else:
            while now.get_next().get_data() != d:
                now = now.get_next()
                if now.get_next().get_next() == None:
                    return print("Error")
            now.set_next(now.get_next().get_next())
    def find(self, d=None):
        a = self.roof
        while a.get_data() != d:
            if a.get_next() == None:
                return  print("Error")
            a = a.get_next()
        return print('Tồn tại')

if __name__ == "__main__":
    ln = linked_note()
    ln.add(1)
    ln.add(2)
    ln.add(3)
    ln.add(4)
    ln.add(5)
    ln.find(
#Thử nghiệm nên thêm vào
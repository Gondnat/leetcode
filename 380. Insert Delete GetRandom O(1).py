import random


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.vals.append(val)
        self.hash[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        index = self.hash.get(val, -1)
        if index == -1:
            return False
        self.vals[index] = self.vals[-1]
        self.hash[self.vals[index]] = index
        self.vals.pop()
        self.hash.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
if __name__ == '__main__':
    val = 1
    obj = RandomizedSet()
    param_1 = obj.insert(0)
    param_1 = obj.insert(1)
    param_2 = obj.remove(0)
    param_1 = obj.insert(2)
    param_2 = obj.remove(1)

    param_3 = obj.getRandom()
    print(param_3)
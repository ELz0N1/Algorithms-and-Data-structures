import ctypes


class DynamicArray(object):
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.arr = self.make_array(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if not 0 <= i < self.length:
            return IndexError(f"index {i} is out of bounds!")

        return self.arr[i]

    def append(self, element):
        if self.length == self.capacity:
            self.resize(2 * self.capacity)

        self.arr[self.length] = element
        self.length += 1

    def remove(self):
        if self.length == 0:
            print("Array is empty!")
            return

        self.arr[self.length - 1] = 0
        self.length -= 1

    def resize(self, new_capacity):
        new_arr = self.make_array(new_capacity)

        for k in range(self.length):
            new_arr[k] = self.arr[k]

        self.arr = new_arr
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == "__main__":
    array = DynamicArray()

    array.append(1)
    array.append(2)
    array.append(3)

    for i in range(len(array)):
        print(array[i], end=" ")
    print()

    print(array[0], array[1], array[2], array[3])

    array.remove()

    for i in range(len(array)):
        print(array[i], end=" ")

    print()
    array.remove()
    array.remove()
    array.remove()

class CycleFIFO:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = 0
        self.end = 0
        self.count = 0
        self.FIFO = list(range(0, capacity))

    def __move_left(self):
        if self.front < self.capacity - 1:
            self.front += 1
        else:
            self.front = 0

    def __change_count(self):
        if self.count < self.capacity:
            self.count += 1
        else:
            pass

    def add_value(self, value):
        if self.end <= self.capacity - 1:
            if (self.end == self.front) and (self.count != 0):
                self.__move_left()
            self.FIFO[self.end] = value
            self.end += 1
            self.__change_count()
        else:
            self.end = 0
            if (self.end == self.front) and (self.count != 0):
                self.__move_left()
            self.FIFO[self.end] = value
            self.end += 1
            self.__change_count()

    def pop_front(self):
        if self.count > 0:
            self.count -= 1
            self.__move_left()
        else:
            pass

    def get_front_value(self):
        if self.count > 0:
            temp = self.FIFO[self.front]
            return temp
        else:
            return 'FIFO is empty!'

    def show_count(self):
        return 'Count of variables in FIFO: ' + str(self.count)


def main():
    print('Classic FIFO ;)....')
    fifo = CycleFIFO(5)
    fifo.add_value(1)
    fifo.add_value(2)
    fifo.add_value(3)
    fifo.pop_front()
    fifo.pop_front()
    fifo.add_value(4)
    fifo.add_value(5)
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.add_value(6)
    fifo.add_value(7)
    fifo.add_value(8)
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.add_value(9)
    fifo.add_value(10)
    fifo.add_value(11)
    fifo.add_value(12)
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.pop_front()
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.pop_front()
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.pop_front()
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.pop_front()
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.pop_front()
    print(fifo.get_front_value())
    print(fifo.show_count())
    fifo.pop_front()


if __name__ == '__main__':
    main()

class CycleFIFO:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.count = 0
        self.FIFO = list(range(0, capacity))

    def __change_count(self):
        if self.count < self.capacity:
            self.count += 1
        else:
            pass

    def add_value(self, value):
        self.FIFO[-1] = value
        self.__change_count()
        self.FIFO.insert(0, self.FIFO.pop())

    def get_front_value(self):
        if self.count > 0:
            temp = self.FIFO[self.count - 1]
            return temp
        else:
            return 'FIFO is empty!'

    def pop_front(self):
        for i in range(self.count - 1):
            self.FIFO.append(self.FIFO.pop())
        self.count -= 1

    def show_count(self):
        return 'Count of variables in FIFO: ' + str(self.count)


def main():
    print('FIFO 2 with shifts....')
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

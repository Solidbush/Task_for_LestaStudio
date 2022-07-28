from FIFO_1_Classic import CycleFIFO as CFIFO
from FIFO_2_with_shifts import CycleFIFO as SFIFO


class Menu:
    def __init__(self):
        pass

    def command_list(self):
        print('[1] Add values to FIFO_1')
        print('[2] Show front value in FIFO_1')
        print('[3] Pop front value in FIFO_1')
        print('[4] Show count of elements in FIFO_1')
        print('[5] Add values to FIFO_2')
        print('[6] Show front value in FIFO_2')
        print('[7] Pop front value in FIFO_2')
        print('[8] Show count of elements in FIFO_2')
        print('[9] Show commands again')
        print('[0] For exit...')

    def start(self):
        command = -1
        capacity_1 = int(input('Enter capacity for FIFO_1: '))
        capacity_2 = int(input('Enter capacity for FIFO_2: '))
        c_fifo = CFIFO(capacity=capacity_1)
        s_fifo = SFIFO(capacity=capacity_2)
        self.command_list()
        while command != 0:
            command = int(input('Enter command: '))
            if command == 1:
                value = int(input('[+] Enter value: '))
                c_fifo.add_value(value=value)
                print('Values added!')
            elif command == 2:
                print('Front value in FIFO_1: ' + str(c_fifo.get_front_value()))
            elif command == 3:
                c_fifo.pop_front()
                print('Front value in FIFO_1 deleted...')
            elif command == 4:
                print('Size of FIFO_1: ' + str(c_fifo.show_count()))
            elif command == 5:
                value = int(input('[+] Enter value: '))
                s_fifo.add_value(value=value)
                print('Values added!')
            elif command == 6:
                print('Front value in FIFO_1: ' + str(s_fifo.get_front_value()))
            elif command == 7:
                s_fifo.pop_front()
                print('Front value in FIFO_1 deleted...')
            elif command == 8:
                print('Size of FIFO_1: ' + str(s_fifo.show_count()))
            elif command == 9:
                self.command_list()
            else:
                print('Goodbye...')
                command = 0


def main():
    menu = Menu()
    menu.start()


if __name__ == '__main__':
    main()




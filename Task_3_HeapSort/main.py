from art import tprint

def heapSort(array):
    n = len(array)
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if (l < n) and (array[i] < array[l]):
            largest = l
        if (r < n) and (array[largest] < array[r]):
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(n=n, i=largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n=n, i=i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(n=i, i=0)

def main():
    array = []
    tprint('Heap Sort')
    string = input('[+] Enter values separated by spaces: ')
    for a in string.split():
        array.append(int(a))
    print('[+] Process...')
    print(f'[+] Initial values: {string}')
    heapSort(array=array)
    print(f'[+] Sorted values: {str(array)}')


if __name__ == '__main__':
    main()
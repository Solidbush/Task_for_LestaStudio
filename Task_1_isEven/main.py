from art import tprint

def is_Even(value):
    return value & 1 == 0

def main():
    tprint('is Even?')
    value = int(input('[+] Enter an integer: '))
    print('[+] Process...')
    print(f'[+] Answer: {str(is_Even(value=value))}')

if __name__ == '__main__':
    main()
import main

def start():
    while True:
        print('warung mini')
        harga = int(input('total harga: '))

        if harga == 0:
           main.menu()
           
if __name__ == '__main__':
    start()
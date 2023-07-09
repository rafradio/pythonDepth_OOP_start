from Fibo import Fibo 

def main():
    fibo = Fibo()
    for i in range(1, fibo.x+1): 
        print(f'{fibo.calc(i)= } {fibo.count = }')


if __name__ == '__main__':
    main()
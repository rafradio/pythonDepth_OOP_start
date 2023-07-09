from Fibo import Fibo 

def main():
    fibo = Fibo()
    acc = fibo.generator()
    it: int = 1
    for f in acc:
        print(f'fibo {it} = {f} {fibo.count}')
        acc.send(it:= it + 1)
        

if __name__ == '__main__':
    main()
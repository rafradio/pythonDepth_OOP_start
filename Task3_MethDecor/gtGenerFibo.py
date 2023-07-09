from FiboDecor import FiboDecor as FD 

def main():
    obj = FD()
 
    it = 1
    for f in obj.generator():
        print(f'fibo {it} = {f} ')
        it += 1


        

if __name__ == '__main__':
    main()
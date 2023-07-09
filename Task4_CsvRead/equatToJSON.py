import os, csv, math, re
from ClassForPrint import ClassForPrint as PrintMeth

def main():
    obj = PrintMeth()
    myPrint = obj.dumpToJSON

    def decor(func):
        def quardro():
            x = func()
            next(x)
            result = {}
            for row in x:
                b = list(map(int, row))
                d = b[2]**2 - 4*b[1]*b[3]
                res = (round((-b[2]+math.sqrt(d))/2*b[1], 2), round((-b[2]-math.sqrt(d))/2*b[1], 2)) if d >= 0 else 'Уравнение не имеет решений'
                result[b[0]] = res
            return result
        return quardro
    
    mathFunc = decor

    @myPrint
    @mathFunc
    def data():
        PATH_TO_FILE = os.path.join(os.getcwd(), 'DumpedFiles', 'data.csv')
        for row in open(PATH_TO_FILE, 'r', newline=''):
            yield re.sub('\n|\r|"', "", row).split(',')


    data()

   


if __name__ == '__main__':
    main()
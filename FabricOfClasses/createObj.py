import Modules as m

def main():
    myDog = m.Fabric.create(m.Dog, 'Sharik')
    print(isinstance(myDog, m.Dog))
    print(myDog)
    print(myDog.name)

if __name__ == '__main__':
    main()
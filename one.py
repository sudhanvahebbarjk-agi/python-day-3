class Arithmetic:
    def add(self):
        print("Sum : ", a + b)

    def sub(self):
        print("Sub : ", a - b)

    def mul(self):
        print("Mul : ", a * b)

    def div(self):
        if a > b:
            print("A%B :", a // b)
        else:
            print("B%A :", b // a)


arithmetic = Arithmetic()

a = int(input('enter a value :'))
b = int(input('enter b value :'))

arithmetic.add()
arithmetic.sub()
arithmetic.mul()
arithmetic.div()

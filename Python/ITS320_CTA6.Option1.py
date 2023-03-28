class numbers(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self):
        return (self.real + self.imaginary)

    def sub(self):
        return (self.real - self.imaginary)

    def mul(self):
        # enter your code here
        return (self.real * self.imaginary)

    def div(self):
        # enter your code here
        return (self.real / self.imaginary)

    def mod(self):
        # enter your code here
        return (self.real % self.imaginary)


if __name__ == '__main__':

    num1, num2 = input("Enter two numbers giving a space here: ").split()
        #Convert to floats
    num1, num2 = float(num1), float(num2)
        #Create Instance
    total = numbers(num1, num2)


    print ('Inputs:', num1, num2)
    print ('Add:', num1, '+', num2, '=', total.add())
    print ('Subtract:', num1, '-', num2, '=', total.sub())
    print ('Multiple:', num1, '*', num2, '=', total.mul())
    print ('Divide:', num1,  '/',num2, '=', total.div())
    print ('Modular:', num1, '%', num2, '=', total.mod())

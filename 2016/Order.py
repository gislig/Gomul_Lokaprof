class Order:
    def __init__(self):
        pass

class OrderLine(Order):
    def __init__(self, name, price, count, discount):
        super().__init__(name, price, count, discount)

def main():
    pass

main()
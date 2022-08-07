class Product:

    def __init__(self, price: int, description: str):
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.price}, {self.description}"


class Customer:

    def __init__(self, name: str, surname: str, phone: str):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.surname} {self.name[0]}., {self.phone}"


class Order:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_order(self, product: Product, quantity: int):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self):
        res = 0
        for index, item in enumerate(self.products):
            res += item.price * self.quantities[index]
        return res

    def __str__(self):
        res = f'{self.customer}\n'

        for index, item in enumerate(self.products):
            res += f'\t{item} x {self.quantities[index]} = {item.price * self.quantities[index]} грн.\n'

        res += f'Total price: {self.total()} грн.'
        return res


product_1 = Product(100, "Pizza small")
product_2 = Product(150, "Pizza Middle")
product_3 = Product(200, "Pizza Large")

cust_1 = Customer("Matt", "Leblanc", "555-55-55")
cust_2 = Customer("David", "Schwimmer", "555-01-02")


total_order_1 = Order(cust_1)
total_order_2 = Order(cust_2)

total_order_1.add_order(product_2, 1)
total_order_1.add_order(product_3, 2)

total_order_2.add_order(product_1, 1)
total_order_2.add_order(product_2, 1)
total_order_2.add_order(product_3, 1)

print(total_order_1)
print()
print(total_order_2)
class Product:

    def __init__(self, price, description, gabarites):

        self.price = price
        self.description = description
        self.gabarites = gabarites

    def __str__(self):
        return f"{self.price}, {self.description}, {self.gabarites}"


class Customer:

    def __init__(self, name, surname, age):

        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"


class Order:
    def __init__(self, cust):
        self.title = cust
        self.orders = []

    def add_order(self, product: Product):
        self.orders.append(product)

    def __str__(self):
        res = f"{self.title}\n"
        res += "\n".join(map(str, self.orders))
        return res

    def total_sum(self, product: Product):
        t_sum = 0
        t_sum += product[0]
        return f"Total sum = {t_sum}"


product_1 = Product(100, "High_quality", "10-10-10" )
product_2 = Product(150, "Extra_quality", "15-20-10")
product_3 = Product(200, "De-Luxe", "15-15-15")

cust_1 = Customer("Matt", "Leblanc", 55)
cust_2 = Customer("David", "Schwimmer", 55)
cust_3 = Customer("Lisa", "Kudrow", 59)


total_order = Order(cust_1)
total_order.add_order(product_2)
total_order.add_order(product_3)


print(total_order)

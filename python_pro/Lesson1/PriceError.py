class PriceError(Exception):
    """
    Create class for exception
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"


try:
    price = float(input("Input product price: "))
    """
    Call our class for exception
    """
    if price <= 0:
        raise PriceError("Price can't be <= 0")
    """
    If price isn't number-type call ValueError
    """
    if not isinstance(price, float):
        raise ValueError
    print("Price = ", price, "UAH")

except PriceError as err:
    """
    Print text from PriceError class __str__-function
    """
    print(err)
except ValueError:
    """
    Print text in case ValueError raised
    """
    print("Oops, price must be a number! Try again.")

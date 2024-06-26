class Product:
    def __init__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code

string = list(map(str, input().split()))

hi = Product("codetree", "50")
print("product " + hi.product_code + " is " + hi.product_name)
hi = Product(string[0], string[1])

print("product " + hi.product_code + " is " + hi.product_name)
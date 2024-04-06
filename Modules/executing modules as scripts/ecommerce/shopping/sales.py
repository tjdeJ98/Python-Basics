def calc_tax():
    pass


def calc_shipping():
    pass


# If we launch this file from here then __name__ will be main,
# But if we launch it from another file then __name__ is the package ecommerce.shopping.sales
if __name__ == "__main__":
    print("sales started")
    calc_tax()

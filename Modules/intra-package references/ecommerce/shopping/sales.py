# To import a module from an other package we can use a
# Absolute or relative import statement
# absolute import: <- best practive unless it become REALLY LONG like a.b.c.d.e...
from ..customer import contact
from ecommerce.customer import contact

contact.contact_customer()

# Relative import:


def calc_tax():
    pass


def calc_shipping():
    pass

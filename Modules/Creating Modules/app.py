# There are different ways to import functions from modules
# Note using a * is bad practice. As it could overwrite a function in the module
# You can import specific objects from a module
from sales import calc_shipping, calc_tax
# Or import a object and use the functions from the object
import sales

sales.calc_tax()
sales.calc_shipping()

calc_shipping()
calc_tax()

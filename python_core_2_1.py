import this
import codecs

zen_python = codecs.encode(this.s, 'rot13')


quantity_better = zen_python.count("better")
quantity_never = zen_python.count("never")
quantity_is = zen_python.count("is")

print(zen_python.upper())

zen_python = zen_python.replace("i", "&")

print(quantity_better, quantity_never, quantity_is)

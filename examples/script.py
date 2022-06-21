"""
This is a Python module explaining some basic Python features.
"""

x = 10
print(x)

if x > 0:
    print("Larger than 0")
    print("Something else")

print("Outside if")


x = "hello"
print(x)


# Implicit line joining
print("A physical line is what you see as a single line in the program whereas"
      " a logical line is what Python sees as a single line in the program or "
      "more appropriately, what Python sees as a single statement in the "
      "program.")

my_shopping_list = [
    'apples',
    'bananas',
    'oranges',
    'pears',
    'peaches',
    'cherries',
]

sales_january = 100
sales_february = 500
sales_march = 130
sales_april = 120
sales_may = 650

# Explicit line joining
total_sales = sales_january + \
              sales_february + \
              sales_march + \
              sales_april + \
              sales_may
print(total_sales)

# Implicit line joining
total_sales_v2 = (
        sales_january +
        sales_february +
        sales_march +
        sales_april +
        sales_may
)

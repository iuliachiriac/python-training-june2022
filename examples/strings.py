multiline_str = """
Newlines

included
"""

multiline_str.upper()  # doesn't modify the string because strings are immutable

print(multiline_str)

print("Newline" in multiline_str)

print("Escape backslash: \\")
print("Escape double quote: \"")
print('Escape simple quote: \'')

print(r"Raw string containing backslash: \.")
# raw strings are usually used for regular expressions (regex)

name = 'George'
age = 40

# %-formatting
sentence = "My name is %s and I am %d years old" % (name, age)
print(sentence)

# str.format method
sentence = "My name is {} and I am {} years old".format(name, age)
print(sentence)

sentence = "- My name is {0} and I am {1} years old.\n- Hi, {0}!".format(
    name,
    age
)
print(sentence)

# f-strings
sentence = f"My name is {name.upper()} and I am {age} years old"
print(sentence)

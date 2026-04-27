text = "  Hello, Python!  "
print(repr(text.strip()))
print(text.lower(), text.upper())

s = "abcdefghij"
print(s[0], s[-1])
print(s[2:5])
print(s[::2])

print("Hello" + " " + "World")
print(f"Length: {len(s)}")

path = "Line one\nLine two\ttab"
print(path)

print("Pi ~= {:.2f}".format(3.14159))

import re

text = "Call 079-1234567 or 078-9998888"
phones = re.findall(r"\d{3}-\d{7}", text)
print(phones)

print(re.sub(r"\s+", "_", "a   b  c"))

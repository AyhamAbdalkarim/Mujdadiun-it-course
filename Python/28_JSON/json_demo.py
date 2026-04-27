import json

data = {"name": "Ayham", "scores": [10, 20], "ok": True}
text = json.dumps(data)
print(text)

parsed = json.loads(text)
print(parsed["name"], parsed["scores"])

from os import stat


test = 1123
stats = {"ok": 1, "test": test, None : "test"}
test = stats["test"]
stats["test"] = test + 1
print(stats["test"])
print(stats[None])
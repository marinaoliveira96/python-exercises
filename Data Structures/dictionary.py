point= {"x": 1, "y": 2}
point = dict(x=1, y=2)

# temo que buscar epla key
point["x"] = 10
point["z"]=12
print(point)

if "a" in point:
  print(point["a"])

print(point.get("a", 0)
)

del point["x"]
print(point)


for key, value in point.items():
  print(key, value)
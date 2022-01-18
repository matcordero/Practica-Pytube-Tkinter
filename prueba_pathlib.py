import pathlib
print("1")
print(pathlib.Path(__file__).parent.absolute())
print("2")
print(pathlib.Path().absolute())
print("3")
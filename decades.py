age = int(input("How old are you?\n"))
# integer division with // operator, discards the decimal part
decades = age // 10
# remainder, modules operator
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")
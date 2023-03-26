def square_number(a):
  return a * a
number = [4,5,2,9]
print("Sample List: ", number)
result = map(square_number, number)
print("Square the elements of the list:")
print(list(result))

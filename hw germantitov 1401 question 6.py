pizza: int= 4
pizza_slice: int= 8
people: int= 5

print("each guest gets",(pizza*pizza_slice)//people,"slices")
print("left over pizza slices",(pizza*pizza_slice)%people)
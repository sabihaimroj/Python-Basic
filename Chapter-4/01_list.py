team = ["Arpita", "Ovi", 10, 5.55, True, "Rabbi"]
print(team)
print(team[5])

# Reassign
team[4] = "False"   #lists are mutable  #but strings are not
print(team)

# slicing method
print(team[1:4])

# append method
team.append("Mim")   #append() add itemes at the end of the array list
print(team)



# sort method
marks = [50, 29, 77, 91, 68, 10]
marks.sort()
print(marks)

# reverse method
marks.reverse()
print(marks)

# insert method 
marks.insert(3, 100)
print(marks)

# pop method
marks.pop(6)
print(marks)


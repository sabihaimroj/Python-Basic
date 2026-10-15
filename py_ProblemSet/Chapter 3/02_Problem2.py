name = input("Name: ")
date = input("Date: ")

letter = "Dear [Name]\nYou are selected!\n[Date]"

print(letter.replace("[Name]", name).replace("[Date]", date))
# git testing

marks = {
    "Sabiha" : 88,
    "Imroj"  : 77,
    "Mim"    : 90
}

print(marks.items()) # item() method

print(marks.keys()) # keys() method

print(marks.values()) # values() method

marks.update({"Mim" : 92, "Soad" : 99})  # update() method
print(marks)  

print(marks.get("Imroj"))  # get() method , invalid kichu dile Error return korbe

print(marks["Imroj"])   # etao Imroj key er value dekhabe,tobe invalid kichu dile Error return korbe


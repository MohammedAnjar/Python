student = {
    "name" : "arun",
    "score" : {
        "maths" : 78.5,
        "phy" : 56.77,
        "chem" : 79,
    },
    "colloge" : "apna college"
}

#print(student.keys()) 
#print(student.values())
#print(student.items())

#pairs = list(student.items())
#print(pairs[0])

#print(student["name2"]) # error
#print(student.get("name2")) # return none


new_dict = {"name" : "neha kumar", "city" : "delhi"}
student.update(new_dict)
print(student)
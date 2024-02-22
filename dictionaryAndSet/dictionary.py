info = {
    "name" : "apna college",
    "subjects" : ["c++", "python", "Mysql"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    "marks" : 95.6,
}

print(info)
print(type(info))



print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["is_adult"])

info["name"] = "shardha"
info["surname"] = "khapra"

print(info)

null_dictionary = {}
null_dictionary["name"] = "apnacolloge"
print(null_dictionary)
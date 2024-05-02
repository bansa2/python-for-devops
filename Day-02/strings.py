
str1 = "Aayush"
str2 = "Bansal"

result = str1 + " " + str2

substring = "Ayush"
if substring in result:
    print("present")
else:
    print("not present")

print(result)
print(len(result))
print(result.lower())
print(result.upper())
print(result.replace("Bansal","Bansa"))
print(result.split())
print(result.strip())


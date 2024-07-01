print("List")
#list creation
a=["vaishnavi","Isha","Sharvi","Kanchan"]
print(a) #printing list
print(a[1]) #printing element at index 1
a[1]="srushti" #adding element
print(a)
for x in a: #list comprehension
  print(x)
print("------------------------------------")
print("Dictonary")
#Dictonary creation
dict = {
  "Vaishnavi": "Wakchaure",
  "Trupti": "Nabriya",
  "Isha": "Patil"
}
print(dict)
#accessing dictionary
x =dict["Isha"]
print(x)
#dictoinary comprehension
for x in dict:
    print(x)
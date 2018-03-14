#List
Student = ["Avi", "Anu","Gru","Sush","Mahi","Saa"]

print("#To print in reverse Order.")
print(Student[-1])
print(Student[-2])
print(Student[-3])

print("---------------------")
print("#To Print In a Order.")
print(Student[0])
print(Student[1])
print(Student[2])

print("---------------------")
print("To Check if a value is present in it")
print("Avi" in Student)
print("Adi" in Student)

print("---------------------")
print("To Append a Data in the tail")
Student.append("Adi")
print("Adi" in Student)
print(len(Student))

print("---------------------")
print("To Delete a Element From the List")
print(Student)
del Student[-2]
print(Student)

print("---------------------")
print("List Slicing...")
print(Student)

print(Student[1:])
print(Student[1:-1])
print(Student[-3:-1])


 
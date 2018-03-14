# Boolean


python_course = True;
java_course = False;

print(f"Python Course is Love of my life: {python_course}");
print(f"Java is also love of my life: {java_course}");

print(int(python_course) == 1)
int(java_course) == 0;

print(python_course)
print()

number = 5;

if number or python_course:
    print("Number")
else:
    print("Not a Number")

if number and java_course:
    print("Number")
else:
    print("Not a Number")

# Ternary If statemnets

print()
a = 3
b = 4

print("a is bigger" if a > b  else "a is smaller")
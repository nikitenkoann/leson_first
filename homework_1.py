#1  завдання Вхідні дані:
#Alex
#Вихідні дані:
#Hello, Alex!

name = input ("what is your name?")
print("Hello, " + name + "!")


#2 Дано двоцифрове число. Знайдіть число десятків у ньому.
#Вхідні дані: 42 67 81
#Вихідні дані:4 6 8 


number_a = 42
number_b = 67 
number_c = 81
print (number_a // 10)
print (number_b // 10)
print (number_c // 10)


#Напишіть програму, яка отримує значення радіуса кола від користувача та обчислює площу круга і довжину кола.
#Вхідні дані: 5
#Вихідні дані: 78.53981633974483 31.41592653589793
PI = 3.14
radius = int(input ("Enter the radius of the circle:"))
print (PI*radius**2)

#Напишіть програму для перетворення висоти (вказується у футах (1 фут = 30,48 см) і
#дюймах (1 дюйм = 2,54 см) у сантиметри.
#Вхідні дані: Feet: 10 Inches: 5
#Вихідні дані: Your height is: 317.5 cm.??????  помилка!!!

FEET = 30.48
INCHES = 2.54
height_feet = int (input("Enter your height in feet: "))
height_inches = int (input("Enter your height in inches: "))
total_cm = (height_feet * FEET) + (height_inches * INCHES)
print("Your height is:", total_cm, "cm")



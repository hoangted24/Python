__author__ = 'HOANGTED'
print("Hi, Good day for you!")
print("your weight?")
weight = float(input())
print("your height?")
height = float(input())

BMI = (weight/ 0.45359237)/ ((height/ 0.0254)*(height/ 0.0254))
print("Body Mass Index is ",BMI)
if BMI >= 30.0:
    print('You are Obese')
elif BMI >= 25:
    print('You are Overweight')
elif BMI >= 18.5:
    print('You are Normal')
else:
    print('You are Underweight')


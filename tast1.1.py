'''
Task 1. Who are you?

You flew to the planet of ultra developers. In order for you to be accepted in society, you need to introduce yourself correctly. For this you need to declare yourself. To do this, write your first official submission program, which will display your full name and surname, nickname, email, as well as age and native language.

The conclusion should be made according to the template:

Hi, my name is [name] [surname] and I`m still alive for [age] days!


Example:


Input data:
Rick
Sanchez           
70


Output data:
Hi, my name is Rick Sanchez and I`m still alive for 25500 days!
'''


name, surname, age = input(),input(),int(input())
print("Hi, my name is", name, surname, "and I`m still alive for" , age*365, "days!")
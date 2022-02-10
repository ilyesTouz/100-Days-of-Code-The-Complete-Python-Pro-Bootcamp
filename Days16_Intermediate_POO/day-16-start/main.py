from turtle import Turtle, Screen
import another_module

"""
print(another_module.variable)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

myscreen = Screen()
print(myscreen.canvheight)
myscreen.exitonclick()"""

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon', ["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type', ["Electric", "Water", "Fire"])
table.align = "l"
print(table)





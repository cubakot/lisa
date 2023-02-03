from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
# Первое число
first_number = random.randint(1, 100)
# Второе число
second_number = random.randint(1, 70)
while second_number > first_number:
    first_number = random.randint(1, 100)
H = (first_number + second_number)
while H > 100:
    first_number = random.randint(1, 100)
    H = (first_number+second_number)
print("Найти сумму чисел")
print( "Первое число",first_number)
print( "Второе число", second_number)
p = (first_number + second_number)

class AlisaApp(App):

    def build(self):
        self.lbl = Label(text= "0")
        bl = BoxLayout(orientation='vertical')
        bl.add_widget(self.lbl)
        return bl


if __name__ == '__main__':
    AlisaApp().run()
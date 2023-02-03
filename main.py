from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
class AlisaApp(App):
    def zapusk(self, instance):
        self.first_number = random.randint(1, 100)
        self.second_number = random.randint(1, 70)
        while self.second_number> self.first_number:
            self.first_number = random.randint(1, 100)
        H = (self.first_number + self.second_number)
        while H > 100:
            self.first_number = random.randint(1, 100)
            H = (self.first_number + self.second_number)
        self.o = str(self.first_number)
        self.t = str(self.second_number)
        p = str(self.first_number + self.second_number)
        self.ou.text = self.o
        self.ot.text = self.t
        if (self.formula == "0"):
            self.formula = ""
        self.formula = "0"
        self.update_lambel()
        print(p)

    def otvet(self, instance):

        if self.formula == str(self.first_number + self.second_number):
            self.lbl.text = "Правильный ответ"
            if self.lbl.text == "Правильный ответ":
                self.formula = ""

        else:
            self.lbl.text = "Не правильный ответ"
            self.formula = ""

    def update_lambel(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        self.formula += str(instance.text)
        self.update_lambel()

    def cal_rezul(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        self.formula = "0"
        self.update_lambel()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_lambel()

    def build(self):
        self.first_number = "0"
        self.second_number = "0"

        self.lbl = Label(text="", font_size='23sp', size_hint = [.99, .1])
        self.ou = Label( text="", font_size='23sp', size_hint = [.99, .1])
        self.ot = Label(text="", font_size='23sp', size_hint = [.99, .1])
        self.formula = "0"
        bl = BoxLayout(orientation='vertical',padding = [6, 6] )
        gl = GridLayout(cols=3,spacing = 2)
        bl.add_widget(Label(text="Первое число", font_size='23sp', size_hint = [.99, .1]))
        bl.add_widget(self.ou)
        bl.add_widget(Label(text="Второе число", font_size='23sp', size_hint = [.99, .1]))
        bl.add_widget(self.ot)
        bl.add_widget(Label(text="Найти сумму чисел", font_size='23sp', size_hint = [.99, .1]))
        bl.add_widget(self.lbl)
        gl.add_widget(Label())
        gl.add_widget(Button(text="Запуск", on_press=self.zapusk))
        gl.add_widget(Label())
        gl.add_widget(Button(text="7", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="9", on_press=self.add_number))
        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text="Ответ", on_press=self.otvet))

        gl.add_widget(Button(text="Сброс", on_press=self.cal_rezul))


        bl.add_widget(gl)

        return bl

if __name__ == '__main__':
    AlisaApp().run()

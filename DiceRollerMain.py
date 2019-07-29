import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from rolls import roll
from rolls import searchfor
from rolls import analyze_result
class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 2

        self.inside = GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="Ile kostek?"))
        self.dices = TextInput(multiline=False)
        self.inside.add_widget(self.dices)

        self.inside.add_widget(Label(text="ToHit"))
        self.tohit = TextInput(multiline=False)
        self.inside.add_widget(self.tohit)

        self.inside.add_widget(Label(text="ToWound"))
        self.towound = TextInput(multiline=False)
        self.inside.add_widget(self.towound)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        dices = self.dices.text
        tohit = self.tohit.text
        towound = self.towound.text
        roll(int(dices),lista)
        print(lista)
        analyze_result(lista)
        emptylist = []
        listapo=searchfor(int(tohit),lista, emptylist)
        print(listapo)
        print(len(listapo))
        analyze_result(listapo)
        roll(len(listapo),lista2)
        print(listapo)
        print(lista2)
        emptylist=[]
        listapo2=searchfor(int(towound),lista2, emptylist)
        print(listapo2)
        #print(len(listapo2))
        #analyze_result(listapo2)
        self.tohit.text= ""
        self.dices.text= ""
        self.towound.text= ""
lista=[]
lista2=[]
listapo=[]
listapo2=[]
emptylist=[]
class DiceRoller(App):

    def build(self):
        return Grid()

if __name__ == "__main__":
    DiceRoller().run()


import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from rolls import roll

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="Hi"))
        self.howmany = TextInput(multiline=False)
        self.inside.add_widget(self.howmany)

        self.inside.add_widget(Label(text="Hi"))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        howmany = self.howmany.text
        name = self.name.text
        roll(int(howmany),lista)
        print(lista)
        self.name.text= ""
        self.howmany.text= ""
lista=[]
class DiceRoller(App):

    def build(self):
        return Grid()

if __name__ == "__main__":
    DiceRoller().run()


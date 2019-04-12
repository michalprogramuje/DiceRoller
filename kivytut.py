import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass
class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

CustomWidget = CustomWidgetApp()
CustomWidget.run()
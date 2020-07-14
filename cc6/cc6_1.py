from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty

import random

class ScatterTextWidget(BoxLayout):
    
    # Give data from python to kivy
    text_colour = ListProperty([1, 0, 0, 1])

    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        self.text_colour = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
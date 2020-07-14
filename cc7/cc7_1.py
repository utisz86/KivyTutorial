from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty, ObjectProperty

from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)

from kivy.graphics.context_instructions import Color

import random

class ScatterTextWidget(BoxLayout):
    
    # Give data from python to kivy
    text_colour = ObjectProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)

        # You can draw here
        with self.canvas.before:
            Color(0, 1, 0, 1)
            Rectangle(pos=(0, 100), size=(300, 300))
            Ellipse(pos=(0, 400), size=(300, 100))
            Line(ponts=[0, 0, 500, 600, 400, 300],
            close=True, width=3)


    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        self.text_colour = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
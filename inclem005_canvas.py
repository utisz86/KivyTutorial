from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 0, 0, 1)  # arguments are red, green, blue, alpha
            Rectangle(size=(300, 100),
            pos=(300, 200))

class DrawingApp(App):
    def build(self):
        root_widget = DrawingWidget()
        return root_widget

DrawingApp().run()
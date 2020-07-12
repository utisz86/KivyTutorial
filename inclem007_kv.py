from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Interface(BoxLayout):
    pass

class DrawingApp(App):
    
    def build(self):
        root_widget = Interface()
        return root_widget



DrawingApp().run()        
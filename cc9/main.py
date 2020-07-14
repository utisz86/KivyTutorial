from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.properties import StringProperty

from kivy.base import runTouchApp
from kivy.lang import Builder

Builder.load_string('''
<ScrollableLabel>:
    text: str("some really really long stirng " * 100)
    Label:
        text: root.text
        font_size: 50
        text_size: self.width, None    # wrap text
        size_hint_y: None
        height: self.texture_size[1]
''')

class ScrollableLabel(ScrollView):
    text = StringProperty('')

runTouchApp(ScrollableLabel())
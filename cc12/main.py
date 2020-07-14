from kivy.app import App

# For android
from plyer.notification import notify

class AndroidApp(App):
    def build(self):
        notify('Some title', 'Some message text')

AndroidApp().run()
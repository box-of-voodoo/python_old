from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass


class SimpleKivy(App):
    def build(self):
        return Widgets()



if __name__ == "__main__":
    SimpleKivy().run()

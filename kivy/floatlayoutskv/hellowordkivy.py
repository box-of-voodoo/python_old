from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.floatlayout import FloatLayout


class SimpleKivy(App):
    def build(self):
        return FloatLayout()



if __name__ == "__main__":
    SimpleKivy().run()

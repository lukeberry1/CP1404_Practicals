from kivy.app import App
from kivy.lang import Builder





class Convert_M_To_Km(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_kilometers.kv')
        return self.root

    def handle_calculate(self):

        Convert_M_To_Km().run()
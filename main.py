from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from googletrans import Translator
from kivy.core.window import Window

Window.size  =(430, 300)
translate = Translator()

class ScreenMain(Widget):
    text_Translate = ObjectProperty(None)

    def TranslateText(self):
        text = self.ids.VietNamese.text
        result = translate.translate(text)
        self.text_Translate = result.text
        

class Translate(MDApp):
    def build(self):
        return Builder.load_file("translate.kv")

if __name__ == "__main__":
    Translate().run()
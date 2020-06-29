from kivy.config import Config
Config.set('graphics', 'height', '450')
Config.set('graphics', 'resizable', False)
Config.write()
from kivy.app import App
# kivy.require("1.11.1")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import newsType_helper as nt
import preprocess as pp
import pyperclip as pc
from kivy.core.window import Window

WINDOW_MIN_WIDTH = 1600
WINDOW_MIN_HEIGHT = 1000

class MainScreen(Screen):
    pass

class ProcessScreen(Screen):
    def processText(self):
        text = self.ids.tI_InputText.text
        print(self.checkActive())
        if text != "Paste Text Here" and text !="" and self.checkActive() != 0:
            self.ids.tI_InputText.text = text
            text = self.ids.tI_InputText.text
            if self.ids.cB_ToLowercase.active:
                text = text.lower()
            if self.ids.cB_Possessives.active:
                text = pp.removePosessives(text)
            if self.ids.cB_EscapeCharacters.active:
                text = pp.removeEscapeCharacters(text)
            if self.ids.cB_DuplicateSpaces.active:
                text = pp.removeDuplicateSpaces(text)
            if self.ids.cB_Punctuation.active:
                text = pp.removePunctuation(text)
            if self.ids.cB_StopWords.active:
                text = pp.removeStopWords(text)
            if self.ids.cB_Lemmatize:
                text = pp.lemmatize(text)
            self.ids.tI_OutputText.text = text
    def checkActive(self):
        c = 0
        if self.ids.cB_ToLowercase.active:
            c = 1
        if self.ids.cB_Possessives.active:
            c = 1
        if self.ids.cB_EscapeCharacters.active:
            c = 1
        if self.ids.cB_DuplicateSpaces.active:
            c = 1
        if self.ids.cB_Punctuation.active:
            c = 1
        if self.ids.cB_StopWords.active:
            c = 1
        if self.ids.cB_Lemmatize.active:
            c = 1
        return c
    def copyToClip(self):
        text = self.ids.tI_OutputText.text
        pc.copy(text)

class ClassifyScreen(Screen):
    def pressClassify(self, *args, alG = ("SVM",'None')):
        print(alG)
        alG = alG[0]
        text = self.ids.classificationInput.text
        if text != "Paste news article text here" and text !="" :
            print(alG)
            classification = str(nt.classify2(text,alG))
            print(classification)
            self.ids.classificationLabel.text = classification
        else:
            pass
    def setAlg(self, alg):
        global alG
        print(alg)
        alG = alg

class AlgScreen(Screen):
    SVM = ObjectProperty(True)
    GBC1 = ObjectProperty(False)
    XGB = ObjectProperty(False)
    RFC = ObjectProperty(False)

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class newsTypeApp(App):
    alg = ("SVM",'None')
    def build(self):
        print(Window.size)
        return presentation

if __name__ == "__main__":
    newsTypeApp().run()

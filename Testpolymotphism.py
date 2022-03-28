from abc import ABC, abstractmethod


class UIcontrol(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIcontrol):
    def draw(self):
        print("Textbox")


class DropDownList(UIcontrol):
    def draw(self):
        print("DrawDownList")


def draw(control):
    control.draw

ddl= DropDownList()
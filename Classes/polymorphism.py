from abc import ABC, abstractmethod


class UIControl(ABC):
    # For polymorphism we need a common method for it's derivatives
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDowList")

# Polymorphism = Many Forms
# Poly = many
# Morph = from
# In this care our draw Method is taking many different forms.
# We could be calling the draw method on a textbox or a dropdownlist or maybe a radiobutten etc.


def draw(controls: list):
    for control in controls:
        control.draw()


ddl = DropDownList()
textBox = TextBox()
print(isinstance(ddl, UIControl))
draw([ddl, textBox])

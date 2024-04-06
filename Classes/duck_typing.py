# In python we can still achieve polymorphism without a base class.
# This is possible because Python is a dynamic language
#


class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDowList")

# As long a controls is iterable python is happy in this method.
# As long as each individual part in the iterable had a draw method
# As both TextBox and DropDownlist have.
# This is called Duck Typing. If it walks like a duck and talks like a duck it is a duck.
# So for polymorphic behaviour we don't nessecaraly need a Base class.
# But is it good practice to have a Base method as it forces the Dev to always create a draw method
# For each new 'UIControl' Sub/Child


def draw(controls: list):
    for control in controls:
        control.draw()


ddl = DropDownList()
textBox = TextBox()
print(isinstance(ddl, UIControl))
draw([ddl, textBox])

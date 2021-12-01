# run this example to type
# $ manimgl start.py SquareToCircle 
from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        square = Square()
        text=Text("这是一个画出基本图形的简单尝试。")
        text.next_to(square,UP,buff=0.5)
        self.play(Write(text))
        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        ## self.embed()

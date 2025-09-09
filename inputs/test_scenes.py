from manim import *
from manim_chemistry import *

class V1(Scene):
    def construct(self):
        all_scenes = [SquareToCircle, SquareToCircle]
        for cls in all_scenes:
            cls.setup(self)
            cls.construct(self)
            self.wait(1)
            self.next_section()



class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
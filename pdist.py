from manim import *
import numpy as np


class squares(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"Probability",
            x_axis_label=r"number of dates",
            y_min=0,
            y_max=1,
            x_min=0,
            x_max=10,
            axes_color=BLUE,
            y_num_decimal_places=3,
            y_labeled_nums=[0,1],
            y_label_position = LEFT,
            x_label_position = DOWN,
            x_labeled_nums=np.linspace(0, 10, 11),
            **kwargs)

    def construct(self):
        data = [0.6, 0.2, 0.1, 0.05, 0.03, 0.02]
        x = [1, 2, 3, 4, 5, 6, 7]
        self.setup_axes(animate=True)
        for state, p in enumerate(data):
                line = Line(self.coords_to_point(x[state], 0), self.coords_to_point(x[state],p), color =RED)
                dot = SmallDot().move_to(self.coords_to_point(x[state],p))
                disp = Text(str(p)).scale(0.4) 
                disp.move_to(self.coords_to_point(x[state],p+0.08))
                self.play(ShowCreation(line), run_time =1)
                self.play(ShowCreation(dot),run_time = 0.3)
                self.play(Write(disp), run_time=0.2)
        self.wait(3)

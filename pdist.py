from manimlib.imports import *
import numpy as np


class squares(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 7,
        "x_axis_width": 7,
        "x_axis_label":r"dates",
        "x_labeled_nums": range(8),
        "y_min": 0,
        "y_max": 1,
        "y_axis_height": 5,
        "y_axis_label": r"probability",
        "axes_color": BLUE,
        "graph_origin": 2 * DOWN + 4.5 * LEFT,
        "exclude_zero_label": False,
        "include_tip": True,  # add tip at the end of the axes
        "x_axis_visibility": True,  # show or hide the x axis
        "y_axis_visibility": True,  # show or hide the y axis
        "x_label_position": LEFT,  # where to place the label of the x axis
        "y_label_position": DOWN ,  # where to place the label of the y axis
        "x_axis_config": {},
        "y_axis_config": {},
    } 


    def construct(self):
        data = [0.6, 0.2, 0.1, 0.05, 0.03, 0.02]
        x = [1, 2, 3, 4, 5, 6, 7]
        self.setup_axes(animate=True)
        heading = TextMobject(r"PMF", color = GOLD).to_edge(TOP)
        for state, p in enumerate(data):
                line = Line(self.coords_to_point(x[state], 0), self.coords_to_point(x[state],p), color =RED)
                dot = SmallDot().move_to(self.coords_to_point(x[state],p))
                disp = TexMobject(str(p)).scale(0.5) 
                disp.move_to(self.coords_to_point(x[state],p+0.08))
                self.play(ShowCreation(line), run_time =0.7)
                self.play(ShowCreation(dot),run_time = 0.4)
                self.play(Write(disp), run_time=0.2)
        self.play(Write(heading))
        self.wait(10)

from manim import *
import numpy as np
import math

class exponen(GraphScene):
    def __init__(self, **kwargs):
        self.CONFIG = {
        "x_min" :0,
        "x_max": 10,
        "y_min" :0,
        "y_max" :3,
#            "y_tick_frequency":0.1,
        "x_tick_frequency":1,
        "x_axis_width":6,
        "y_axis_height":4,
        "y_axis_label": "$p(x; \lambda)$",
        "exclude_zero_label" :False,
        "axes_color":BLUE,
        "graph_origin":LEFT*3 + DOWN*1.2,        
        "x_labeled_nums":[0] 
    }
        self.lamb = 0.5 
        GraphScene.__init__(self, **self.CONFIG) 

    def construct(self):
        
        self.setup_axes(animate=True)
        
        img = ImageMobject('/home/niwhskal/Downloads/Untitled45.png').scale(0.2).to_corner(DR)
        self.add(img)
       

        def func(x):
            return self.lamb*np.exp(-self.lamb*x)
        self.graph = self.get_graph(func,x_min=0, x_max = 10, color = ORANGE) 
        la_tracker = ValueTracker(0.5)
        
        title1 = Tex("Exponential Distribution").scale(0.7).to_edge(UP).shift(RIGHT*2)
        self.add(title1)

        self.play(ShowCreation(self.graph))
        
        la_nl = NumberLine(width = 10, x_min = 0, x_max = 2.5, include_numbers = True, numer_scale_val = 0.8, numbers_to_show =np.linspace(0,2.5,5),decimal_number_config={'num_decimal_places': 1})

        la_nl.move_to(ORIGIN + DOWN *2.9)
        la_nl.scale(0.65)
        la_txt = Tex("$\\lambda$", color =PURPLE_D).scale(0.6)
    
        la = DecimalNumber(0.5, color = PURPLE_D).scale(0.55)
        la.next_to(la_nl, LEFT)
        la_txt.next_to(la, LEFT)

        la_obj = Circle(color = PURPLE_D, opacity = 1)
        la_obj.set_opacity(1)
        la_obj.scale(0.15)
        la_obj.move_to(la_nl.n2p(0))

        la.add_updater(lambda m: m.set_value(la_tracker.get_value()))

        la_obj.add_updater(lambda m: m.move_to(la_nl.n2p(la_tracker.get_value())))

        self.play(ShowCreation(la_nl), FadeIn(la_obj), FadeIn(la), FadeIn(la_txt))

        self.wait(1)
        def funcone(x, lamb):
            return lamb*np.exp(-lamb*x)
 

        self.graph.add_updater(lambda m : m.become(self.get_graph(lambda x: funcone(x, la_tracker.get_value()), color = ORANGE)))

        equation = Tex("$p(x;\\lambda) = \\lambda$", "$e^{-\\lambda x}$")
        equation[0][4].set_color(PURPLE_D)
        equation[0][7].set_color(PURPLE_D)
        equation[1][2].set_color(PURPLE_D)
        equation.scale(0.7).next_to(la_nl, UP*1.5)

        self.play(FadeIn(equation))

        self.wait(1)


        self.play(la_tracker.animate.set_value(0), run_time=2)
        self.play(la_tracker.animate.set_value(1.5), run_time=2)
        self.wait(1)
        self.play(la_tracker.animate.set_value(2.5), run_time=2)
        self.wait(5)

 

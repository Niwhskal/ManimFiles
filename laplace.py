from manim import *
import numpy as np
import math

class laplace(GraphScene):
    def __init__(self, **kwargs):
        self.CONFIG = {
        "x_min" :-5,
        "x_max": 5,
        "y_min" :0,
        "y_max" :2,
#            "y_tick_frequency":0.1,
        "x_tick_frequency":1,
        "x_axis_width":6,
        "y_axis_height":4,
        "y_axis_label": "$p(x;\mu, \lambda)$",
        "exclude_zero_label" :False,
        "axes_color":BLUE,
        "graph_origin":ORIGIN + DOWN,        
        "x_labeled_nums": [-5,0,5]
    }
        self.lamb = 0.5
        self.mu = 0 
        GraphScene.__init__(self, **self.CONFIG) 

    def construct(self):
        
        self.setup_axes(animate=True)
        
        img = ImageMobject('/home/niwhskal/Downloads/Untitled45.png').scale(0.2).to_corner(DR)
        self.add(img)
        
        title1 = Tex("Laplace Distribution").scale(0.7).to_edge(UP).shift(LEFT*3)
        self.add(title1)
       

        def func(x):
            return (1/2*self.lamb)*np.exp(-(abs(x-self.mu))/self.lamb)


        self.graph = self.get_graph(func,x_min=-5, x_max = 5, color = ORANGE) 
        la_tracker = ValueTracker(0.5)

        self.play(ShowCreation(self.graph))
        
        la_nl = NumberLine(width = 10, x_min = 0, x_max = 2.5, include_numbers = True, numer_scale_val = 0.8, numbers_to_show =np.linspace(0,2.5,5),decimal_number_config={'num_decimal_places': 1})

        la_nl.move_to(ORIGIN + DOWN *2.2)
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
# Bias Value
        bias_tracker = ValueTracker(0)



        bias_nl = NumberLine(width=10,
        x_min=-3, x_max=3,
        include_numbers=True,
        number_scale_val=0.8,
        numbers_to_show=range(-3, 4),
        color=GREY)
        bias_nl.next_to(la_nl, DOWN)
        bias_nl.scale(0.65)
        bias_txt = Tex("$\\mu$", color=MAROON_D).scale(0.6)

        bias = DecimalNumber(0, color=MAROON_D).scale(0.5)
        bias.next_to(bias_nl, LEFT)
        bias_txt.next_to(bias, LEFT)

        bias_obj = Circle(color=MAROON_D, opacity=1)
        bias_obj.set_opacity(1)
        bias_obj.scale(0.15)
        bias_obj.move_to(bias_nl.n2p(0))

        bias.add_updater(lambda m: m.set_value(bias_tracker.get_value()))
        bias_obj.add_updater(
            lambda m: m.move_to(bias_nl.n2p(bias_tracker.get_value()))
        )


        self.play(ShowCreation(bias_nl), FadeIn(bias_obj), FadeIn(bias), FadeIn(bias_txt))

        def funcone(x, lamb, mu):
            return (1/2*lamb)*np.exp(-(abs(x-mu))/lamb)
 

        self.graph.add_updater(lambda m : m.become(self.get_graph(lambda x: funcone(x, la_tracker.get_value(), bias_tracker.get_value()), color = ORANGE)))

        equation = Tex("$L(x;\\mu,\\lambda) = \\frac{1}{2 \\lambda}$", "$e^{\\frac{-|x-\\mu|}{\\lambda}}$")
        equation[0][4].set_color(MAROON_D)
        equation[0][6].set_color(PURPLE_D)
        equation[0][12].set_color(PURPLE_D)
        equation[1][5].set_color(MAROON_D)
        equation[1][7].set_color(PURPLE_D)
        equation.scale(0.7).to_edge(LEFT, buff=0.5).shift(UP)

        self.play(FadeIn(equation))

        self.wait(1)


        self.play(la_tracker.animate.set_value(0.5), run_time=2)
        self.play(la_tracker.animate.set_value(1.5), run_time=2)
        self.wait(1)
        self.play(la_tracker.animate.set_value(2.5), run_time=2)

        self.play(bias_tracker.animate.set_value(1), run_time=2)
        self.wait(1)
        self.play(bias_tracker.animate.set_value(-1), run_time=2)
        self.wait(1)
        self.play(bias_tracker.animate.set_value(-3), run_time=2)
        self.play(bias_tracker.animate.set_value(3), run_time=4)

        self.wait(5)


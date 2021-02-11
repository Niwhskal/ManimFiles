from manim import *
import numpy as np
import math

NEW_BLUE = "#68a8e1"

class Thumbnail(GraphScene):
    def __init__(self, **kwargs):
        self.CONFIG = {
            "x_min" :0,
            "x_max": 4,
            "y_min" :0,
#            "y_tick_frequency":0.1,
            "x_tick_frequency":1,
            "x_axis_width":6,
            "y_axis_height":4,
            "exclude_zero_label" :False,
            "axes_color":GREY,
            "graph_origin":ORIGIN-2 +LEFT,        
            "x_labeled_nums":[0,2,4] 
        }
        GraphScene.__init__(self, **self.CONFIG) 
 
    def construct(self):
        self.show_function_graph()


    def show_function_graph(self):
        self.setup_axes(animate=True)
        img = ImageMobject('/home/niwhskal/Downloads/Untitled45.png').scale(0.2).to_corner(DR)
        self.add(img)
        y_ax = Tex(r"Number\\of\\students $\uparrow$").next_to(self.axes[1], LEFT).scale(0.6)
        x_ax = Tex(r"GPA $\rightarrow$").next_to(self.axes[0], DOWN).scale(0.6)
        self.play(Write(y_ax))
        self.play(Write(x_ax))
        def func(x):
            return 15*(1/np.sqrt(2*np.pi*1))*(np.exp(-((x-2)**2)/(2*1)))

        def rect(x):
            return 2.775*(x-1.5)+3.862
        recta = self.get_graph(rect,x_min=0,x_max=4)
        graph = self.get_graph(func,x_min=0,x_max=4)
        graph.set_color(NEW_BLUE)
        
        input_tracker_p1 = ValueTracker(1.5)
        input_tracker_p2 = ValueTracker(3.5)

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker):
            return self.coords_to_point(0, get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)

        kwargs = {
            "x_min" : 0,
            "x_max" : 4,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25}
        self.graph=graph
        iteraciones=6

        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteraciones,start_color=PURPLE,end_color=ORANGE, **kwargs
        )
        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x : 0), dx = 0.5,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs
        )
        rects = self.rect_list[0]
        pop = Tex(r"Student \\ population").scale(0.7).next_to(self.graph, UP*2)
        self.play(Write(pop))

        equalto = Tex("= 100").scale(0.7).next_to(pop, RIGHT)
        self.play(Write(equalto))
        self.transform_between_riemann_rects(
            flat_rects, rects, 
            replace_mobject_with_target_in_scene = True,
            run_time=1 
        )
        
        for j in range(4,6):
            for w in self.rect_list[j]:
                    color=w.get_color()
                    w.set_stroke(color,1.5)
        for j in range(1,6):
            num1 = 1000*j*j
            eq = Tex("= ", str(num1), color = GREEN).scale(0.7).next_to(pop,RIGHT) 
            self.play(ReplacementTransform(equalto, eq))
            self.transform_between_riemann_rects(
            self.rect_list[j-1], self.rect_list[j], dx=1,
            replace_mobject_with_target_in_scene = True,
            run_time=2
            )
            equalto = eq
        
        self.play(ShowCreation(graph))
        self.wait(2)
    
        y_axNew = Tex(r"probability\\density $\uparrow$").next_to(self.axes[1], LEFT).scale(0.6)
        self.remove(pop)
        self.remove(eq)
        self.remove(equalto)
        self.play(ReplacementTransform(y_ax, y_axNew))

        self.play(ApplyMethod(self.graph.shift, UP))
        
        gau_eqn = Tex("=", "$\\frac{1}{\\sqrt{2\\pi\\sigma^2}}$", "$e^{\\frac{(x-\\mu)^2}{2\\sigma^2}}$").next_to(self.graph, RIGHT)

        gau_eqn[1][6].set_color(PURPLE_D)
        gau_eqn[2][4].set_color(BLUE)
        gau_eqn[2][9].set_color(PURPLE_D)
#        gau_eqn.set_color_by_tex("$\sigma$", PURPLE_D)

        self.play(Write(gau_eqn))
        self.play(ApplyMethod(self.graph.shift, DOWN))
        
        line1 = self.get_vertical_line_to_graph(2, graph, DashedLine, color = BLUE)
        dot = Dot(color = BLUE).move_to(self.coords_to_point(2,0))
        m_text = Tex(r"$\mu$", color = BLUE).scale(0.8).next_to(dot, UP).shift(RIGHT*0.3)
        self.play(ShowCreation(line1), ShowCreation(dot), Write(m_text))


        setts = {
        "dash_length": 0.05,
        "dash_spacing": None,
        "positive_space_ratio": 0.5,
    }

        line_sig = DoubleArrow(self.coords_to_point(1,func(1)), self.coords_to_point(3, func(3)), color = PURPLE_D, **setts)

        sigtext = Tex(r"$\sigma$", color = PURPLE_D).scale(0.7).next_to(line_sig, UP*0.5).shift(LEFT*0.3)
        
        self.play(ShowCreation(line_sig), Write(sigtext))
        self.wait(5)
        

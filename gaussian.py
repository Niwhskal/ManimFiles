from manim import *
import numpy as np
import math

NEW_BLUE = "#68a8e1"

class PlotGraph(GraphScene):

    def __init__(self, func, color=BLUE_D, **kwargs):
        GraphScene.__init__(self, **kwargs)
        self.func = func
        self.color = color
        self.title = None
        self.setup()

    def setup(self):
        #graph = create_plot(GraphScene)
        self.setup_axes(animate=False)
        self.graph = self.get_graph(self.func, color=self.color)

    def set_title(self, title, color=DARK_GREY, scale=0.75):
        title = Tex(title, color=color)
        title.next_to(self.axes, UP)
        title.scale(scale)
        return title

    def get_figure(self):
        return VGroup(self.axes, self.graph)

    def align_y_axis_to_left(self):
        self.axes[1].align_to(self.axes[0], LEFT).shift(LEFT * 0.12)

class ActivationFunc(GraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(self)

    def construct(self):
        sigmoid_settings = {
            "y_max":1,
            "y_min":0,
            "x_max":10,
            "x_min":0,
            "y_tick_frequency":1,
            "x_tick_frequency":1,
            "x_axis_width":5,
            "y_axis_height":3,
            "axes_color":GREY,
            "graph_origin": ORIGIN + DOWN,
#            "x_labeled_nums": list(range(0, 10)),
#            "y_labeled_nums": list(range(0, 2))
        }

        def sigmoid(x):
            return (1/np.sqrt(2*np.pi*1))*(np.exp(-((x-5)**2)/(2*1)))


        def plot_figure(title, function, color, settings):
            graph = PlotGraph(function, color, **settings)
            #graph.align_y_axis_to_left()
            fig = graph.get_figure()
            fig.scale(2)
            fig.move_to(ORIGIN)
            title = graph.set_title(title)
            fig = VGroup(*fig, title)
            return fig, graph

        sig_fig, sig_graph = plot_figure("Sigmoid", sigmoid, BLUE_D, sigmoid_settings)
        self.play(ShowCreation(sig_fig[0]))
        self.play(ShowCreation(sig_fig[1]))
        self.play(FadeIn(sig_fig[2]))




class Thumbnail(GraphScene):
    CONFIG = {
            "x_min":0,
            "y_tick_frequency":1,
            "x_tick_frequency":1,
            "x_axis_width":5,
            "y_axis_height":3,
            "axes_color":GREY,
            "graph_origin": ORIGIN + DOWN,
            "x_labeled_nums": list(range(0, 10)),
            "y_labeled_nums": list(range(0, 2))
        }

    
    def construct(self):
        self.show_function_graph()


    def show_function_graph(self):
        self.setup_axes(animate=True)
        img = ImageMobject('/home/niwhskal/Downloads/Untitled45.png').scale(0.2).to_corner(DR)
        self.add(img)
        y_ax = Tex(r"probability\\density").move_to(UP+5.4*LEFT)
        x_ax = Tex(r"GPA $\rightarrow$").move_to(3*DOWN)
        self.add(y_ax)
        self.add(x_ax)
        def func(x):
            return 15*(1/np.sqrt(2*np.pi*1))*(np.exp(-((x-5)**2)/(2*1)))

        def rect(x):
            return 2.775*(x-1.5)+3.862
        recta = self.get_graph(rect,x_min=0,x_max=9)
        graph = self.get_graph(func,x_min=0,x_max=9)
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
        # 
       # reposition mobjects
        #x_label_p1.next_to(v_line_p1, DOWN)
        #x_label_p2.next_to(v_line_p2, DOWN)
        #output_label_p1.next_to(h_line_p1, LEFT)
        #output_label_p2.next_to(h_line_p2, LEFT)
        #input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
        #input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
        #output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
        #output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
        #graph_dot_p1.move_to(get_graph_point(input_tracker_p1))
        #graph_dot_p2.move_to(get_graph_point(input_tracker_p2))

        #updaters


#       self.play(ShowCreation(graph)) 
        # Animacion del punto a
        ###################
        solpe_recta = self.get_secant_slope_group(
            1.9, recta, dx = 1.4,
            df_label = None,
            dx_label = None,
            dx_line_color = PURPLE,
            df_line_color= ORANGE,
            )
        grupo_sec = self.get_secant_slope_group(
            1.5, graph, dx = 2,
            df_label = None,
            dx_label = None,
            dx_line_color = "#942357",
            df_line_color= "#3f7d5c",
            secant_line_color = RED,
        )
        start_dx = grupo_sec.kwargs["dx"]
        start_x = grupo_sec.kwargs["x"]
        def update_slope(group, alpha):
            dx = interpolate(start_dx, 0.001, alpha)
            x = interpolate(start_x, 1.5, alpha)
            kwargs = dict(grupo_sec.kwargs)
            kwargs["dx"] = dx
            kwargs["x"] = x
            new_group = self.get_secant_slope_group(**kwargs)
            group.become(new_group)
            return group
 
        #self.add_foreground_mobjects(grupo_sec)
        #self.add_foreground_mobjects(graph_dot_p1,graph_dot_p2)
  #      self.play(FadeIn(grupo_sec))
  #      self.wait()
        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25}
        self.graph=graph
        iteraciones=6

        pop = Tex(r"Student \\ population").scale(0.7).next_to(graph, UP)
        self.add(pop)

        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteraciones,start_color=PURPLE,end_color=ORANGE, **kwargs
        )
        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x : 0), dx = 0.5,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs
        )
        rects = self.rect_list[0]
        equalto = Tex("= 100").scale(0.7).next_to(pop, RIGHT)
        self.play(Write(equalto))
        self.transform_between_riemann_rects(
            flat_rects, rects, 
            replace_mobject_with_target_in_scene = True,
            run_time=5 
        )
        
        for j in range(4,6):
            for w in self.rect_list[j]:
                    color=w.get_color()
                    w.set_stroke(color,1.5)
        for j in range(1,6):
            num1 = 1000*j*j
            eq = Tex("= ", str(num1)).scale(0.7).next_to(pop,RIGHT) 
            self.play(ReplacementTransform(equalto, eq))
            self.transform_between_riemann_rects(
            self.rect_list[j-1], self.rect_list[j], dx=1,
            replace_mobject_with_target_in_scene = True,
            run_time=1
            )
            equalto = eq
        
        self.play(ShowCreation(graph))
        self.wait(5)


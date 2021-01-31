from manimlib.imports import *
import numpy as np

class exp(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_min" : -4,
        "x_max" : 4,
        "x_axis_label": 'X',
        "y_axis_label": r'probability \\density',
        "axes_color" : BLUE, 
        "y_label_direction": LEFT,
        "x_label_direction": UP,
        
    }
    
    def construct(self):
        self.setup_axes()
        self.pdist = self.get_graph(lambda x: 1.5*(1/np.sqrt(2*np.pi))*np.exp(-((x)**2)/ 2), color = RED, x_min = -4.0, x_max = 4.0) 
        dtext = TextMobject(r"Say you pick inputs from this distribution...").next_to(self.pdist, 4*TOP)
        graph_group = VGroup(self.pdist, self.x_axis, self.y_axis, self.axes, dtext)
        graph_group.scale_in_place(0.4).to_edge(LEFT)

        self.play(ShowCreation(self.pdist))
        self.play(Write(dtext))    

        eqn = TextMobject("$f(X) = X^2$", color = BLUE)
        etext = TextMobject(r"...and feed it to:").next_to(eqn, TOP)
        textgroup = VGroup(eqn, etext)
        textgroup.next_to(graph_group, 4*RIGHT).scale(0.6) 

        self.play(Write(etext))
        self.wait(0.5)
        self.play(Write(eqn))
        self.play(ShowCreation(SurroundingRectangle(eqn, color = GOLD)))

        x_vals = np.random.normal(0.0, 1.0, 10)
        dot ={}
        for n, val in enumerate(x_vals):
           dot[n] = SmallDot(fill_opacity =0.8).move_to(self.coords_to_point(val,0)) 
           
    
        self.y_axis_label ="$f(X)$" 
        self.x_axis_label = ""
        self.x_min =-4
        self.x_max = +4
        self.y_min =0
        self.x_label_direction = 3*DOWN
        self.x_leftmost_tick = self.x_max+1
        self.y_bottom_tick = self.y_max+1
         
        self.setup_axes()

        ftext = TextMobject(r"and then plot f(x)") 
        label = TextMobject(r'X').scale(0.7)
        label.next_to(self.x_axis, DOWN)
        self.add(label)

        freq_group = VGroup(self.x_axis, self.y_axis, self.axes, label)
        freq_group.scale_in_place(0.4).next_to(textgroup, 7*RIGHT) 
        for k, v in enumerate(x_vals):
            self.play(ShowCreation(dot[k]))
            ndot = dot[k].move_to(self.coords_to_point(v, v*v)) 
            freq_group.add(ndot)


        ftext.next_to(freq_group, 0.2*TOP).scale(0.5)

        self.play(Write(ftext))
 
        self.wait(10)

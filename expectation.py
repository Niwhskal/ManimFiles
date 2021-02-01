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

        eqn = TexMobject("f(X) = X^2", color = GOLD).next_to(graph_group, 4*RIGHT)
        etext = TextMobject(r"...and feed it to:").next_to(eqn, TOP).scale(0.6)

        self.play(Write(etext))
        self.wait(0.5)
        self.play(Write(eqn))

        x_vals = np.random.normal(0.0, 1.0, 10)
        dot ={}
        for n, val in enumerate(x_vals):
           dot[n] = SmallDot().move_to(self.coords_to_point(val,0)) 
                      
    
        self.y_axis_label ="$f(X)$" 
        self.x_axis_label = ""
        self.x_min =-4
        self.x_max = +4
        self.y_min =0
        self.y_max = 16
        self.x_label_direction = 3*DOWN
#        self.x_leftmost_tick = self.x_max+1
#        self.y_bottom_tick = self.y_max+1

        ftext = TextMobject(r"then plot f(x)") 
        ftext.next_to(eqn, 7*RIGHT+ 1.5*TOP).scale(0.5)
        self.play(Write(ftext))

        self.setup_axes()

        label = TextMobject(r'X').scale(0.7)
        label.next_to(self.x_axis, DOWN)
        self.add(label)
           
        freq_group = VGroup(self.x_axis, self.y_axis, self.axes, label)
        freq_group.scale_in_place(0.4).next_to(eqn, 7*RIGHT) 
        for k, v in enumerate(x_vals):
            self.play(ShowCreation(dot[k]))
            dottext = TexMobject(str(round(v,2))).next_to(dot[k], 0.2*DOWN).scale(0.5)
            self.add(dottext)
            if k ==0:
                prev_eqn= eqn
        
            rn_rate = np.log(1+np.exp(-k))
            new_eqn = TexMobject("f("+str(round(v,2))+") = "+str(round((v*v),2))).next_to(graph_group, 4*RIGHT)
        
            self.play(ReplacementTransform(prev_eqn, new_eqn), run_time =rn_rate)
            ndot = dot[k].move_to(self.coords_to_point(v, v*v)) 
            freq_group.add(ndot)
            prev_eqn = new_eqn
            self.remove(dottext) 



        self.wait(10)

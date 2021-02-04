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

        self.add(self.pdist)
        self.play(Write(dtext))    

        eqn = TexMobject("ML \\ model", color = BLUE).next_to(graph_group, 6*RIGHT)
        rect = SurroundingRectangle(eqn, color = GOLD)
        self.play(Write(eqn))
        self.add(rect)
        etext = TextMobject(r"...and feed it to:").next_to(eqn, TOP).scale(0.6)

        self.play(Write(etext))

        x_vals = np.random.normal(0.0, 1.0, 5)
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
            dotx = TexMobject('x =').next_to(dottext, LEFT).scale(0.5)
            
            self.add(dottext)
            self.add(dotx)
            
            rn_rate = np.log(2+np.exp(-k))
            inp_text = TexMobject(str(round(v,2))).next_to(eqn, LEFT).scale(0.5)
            self.play(ShowCreation(inp_text, run_time = rn_rate))
            self.wait(0.5)
            otext = TexMobject(str(round(v*v,2))).next_to(eqn, RIGHT).scale(0.5)
            self.play(ShowCreation(otext), run_time =rn_rate)
            ndot = dot[k].move_to(self.coords_to_point(v, v*v)) 
            freq_group.add(ndot)
            self.remove(dottext) 
            self.remove(dotx)
            self.remove(inp_text)
            self.remove(otext)

        
        final_text = TexMobject("Most of values are clustered near 0,\\ therefore the expected value of f(x) is 0").move_to(2*DOWN)
        self.play(Write(final_text))
        self.wait(10)

           





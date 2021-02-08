from manim import *
import numpy as np

class barch(Scene):
    CONFIG = {
        "height" : 5,
        "width" : 12,
        "n_ticks" : 5,
        "tick_width" : 0.2,
        "label_y_axis" : True,
        "max_value" : 1,
        "bar_colors": ['#f5922f','#1de0bd'],
        "bar_names": ['Yes', 'No'],
        "bar_fill_opacity": 0.8,
        "bar_stroke_width": 1,
        "bar_label_scale_val": 0.75,
}

    def construct(self):
        data = [0.0, 1.0]
        chart = BarChart(values = data, **self.CONFIG).shift(UP).scale(0.6)
        title = TextMobject("Bernoulli Distribution").next_to(chart, UP).scale(0.7)
        self.add(title)
        
        phi_tracker = ValueTracker(0)
        nl = NumberLine(width = 10, x_min=0, x_max=1,include_numbers=True, number_scale_val=0.8, numbers_to_show=np.linspace(0,1,10), decimal_number_config={'num_decimal_places': 1})
        nl.move_to(ORIGIN+DOWN *2.4)
        nl.scale(0.6) 
        phi_text = Tex("$\\phi$", color = '#fc5353').scale(0.9)

        phi = DecimalNumber(1, color = '#fc5353').scale(0.7) 
        phi.next_to(nl,LEFT)
        phi_text.next_to(phi,LEFT)
        
        phi_dot = Circle(color ='#fc5353', opacity = 1)
        phi_dot.set_opacity(1)
        phi_dot.scale(0.13)
        phi_dot.move_to(nl.n2p(0))
        
        phi.add_updater(lambda m : m.set_value(phi_tracker.get_value()))        
        phi_dot.add_updater(lambda m: m.move_to(nl.n2p(phi_tracker.get_value())))
        
        self.play(ShowCreation(nl), FadeIn(phi_dot), FadeIn(phi), FadeIn(phi_text))

        equation = Tex("$P(X) = $", "$\phi^{x}$", "$(1-\phi)^{1-x}$")
        equation.set_color_by_tex("$\phi^{x}$", color = '#f5922f')
        equation.set_color_by_tex("$(1-\phi)^{1-x}$", color = '#1de0bd')
        equation.next_to(nl, UP).scale(0.6)
        self.play(FadeIn(equation))

   
        self.play(Write(chart))
        self.wait(1)
        
        def bernoulli(x, phi):
            if x ==1:
                return phi
            elif x ==0:
                return 1 -phi
            else:
                raise Exception("Some other state passed")
        chart.add_updater(lambda m: m.become(BarChart([bernoulli(1, phi_tracker.get_value()), bernoulli(0, phi_tracker.get_value())], **self.CONFIG)).shift(UP).scale(0.6))
#        chart.change_bar_values([bernoulli(1, phi_tracker.get_value()), bernoulli(0, phi_tracker.get_value())])
        
                
        self.wait(1)
    
        self.play(phi_tracker.animate.set_value(0.2), run_time =2)
        self.wait(1)
        self.play(phi_tracker.animate.set_value(0.9), run_time = 3)
        self.wait(1)
        self.play(phi_tracker.animate.set_value(0.5), run_time = 2)
        self.wait(1)
        self.play(phi_tracker.animate.set_value(0.1), run_time = 3)
        self.wait(5)


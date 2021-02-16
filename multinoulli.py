from manim import *
import numpy as np

class multinou(Scene):
    CONFIG = {
        "height" : 5,
        "width" : 12,
        "n_ticks" : 4,
        "tick_width" : 0.2,
        "label_y_axis" : True,
        "max_value" : 1,
        "bar_colors": ['#b8b4b4','#1de0bd','#ffc014','#27d0e3'],
        "bar_names": ['Bitcoin', 'Ethereum', 'DogeCoin', 'Ripple' ],
        "bar_fill_opacity": 0.8,
        "bar_stroke_width": 1,
        "bar_label_scale_val": 0.7,
}

    def construct(self):
        data = [0.25, 0.25, 0.25, 0.25]
        img = ImageMobject('/home/niwhskal/Downloads/Untitled45.png').scale(0.2).to_corner(DR)
        self.add(img)

        chart = BarChart(values = data, **self.CONFIG).scale(0.6)
        title = TextMobject("Multinoulli Distribution").next_to(chart, UP).scale(0.7)
        self.add(title)
        
        
        phi_tracker_1 = ValueTracker(0)
        phi_tracker_2 = ValueTracker(0)
        phi_tracker_3 = ValueTracker(0)
        phi_tracker_4 = ValueTracker(0)


        y_axis = TextMobject("Probability").next_to(chart, LEFT).scale(0.6)
        self.add(y_axis)

        self.play(Write(chart))
        self.wait(1)
        eqn = Tex("$P(BTC) + P(ETH) + P(Doge)+P(RIP) = 1$").to_edge(DOWN, buff = 0.8).scale(0.5)
        self.play(Write(eqn))

        
        chart.add_updater(lambda m: m.become(BarChart([phi_tracker_1.get_value(), phi_tracker_2.get_value(),phi_tracker_3.get_value(),phi_tracker_4.get_value()], **self.CONFIG)).scale(0.6))
#        chart.change_bar_values([bernoulli(1, phi_tracker.get_value()), bernoulli(0, phi_tracker.get_value())])
         
    
        self.play(phi_tracker_1.animate.set_value(0.6), phi_tracker_2.animate.set_value(0.1),phi_tracker_3.animate.set_value(0.2),phi_tracker_4.animate.set_value(0.1), run_time =1)
        self.wait(1)
        self.play(phi_tracker_1.animate.set_value(0.3), phi_tracker_2.animate.set_value(0.2),phi_tracker_3.animate.set_value(0.4),phi_tracker_4.animate.set_value(0.1), run_time =2) 
        self.wait(1) 

        self.play(phi_tracker_1.animate.set_value(0.0), phi_tracker_2.animate.set_value(0.1),phi_tracker_3.animate.set_value(0.8),phi_tracker_4.animate.set_value(0.1), run_time =2) 
        self.wait(5)






from manimlib.imports import *

class SumRule(Scene):
    def construct(self):
        image = ImageMobject("/home/niwhskal/Pictures/table_final.png").scale(1.3) 
        self.play(FadeIn(image)) 
        self.wait(3)
        image.generate_target()
        image.target.to_edge(LEFT)
        self.play(MoveToTarget(image))
        
        introtext = TextMobject(r"P(Y = Indian) =").to_corner(UL).scale(0.6)
        que = TextMobject(r"?").next_to(introtext).scale(0.7)
        self.play(Write(introtext))
        self.play(Write(que))

        self.wait(1)
        rect = Rectangle(height=0.65, width=7.12, color = RED).next_to(image).shift(7.4*LEFT + 0.3*UP)
        self.play(ShowCreation(rect)) 
        self.remove(que)
        self.wait(1)
        arrow = CurvedArrow(rect.get_edge_center(UP), introtext.get_edge_center(RIGHT),angle= -TAU/4,color = BLUE)
        self.play(ShowCreation(arrow))

        sumtext_or = TextMobject(r"P(0 dates, Indian) OR P(1 date, Indian) OR P(2 dates, Indian)").scale(0.6).next_to(introtext) 

        sumtext = TextMobject(r"P(0 dates, Indian) + P(1 date, Indian) + P(2 dates, Indian)").scale(0.6).next_to(introtext) 
        self.wait(0.5)
        self.remove(arrow)
        self.wait(1)
        finaltext = TextMobject("$= \\sum_{x \in {0,1,2}} P(X=x, Y=Indian)$").next_to(sumtext, DOWN).scale(0.6)
        rule = TextMobject(r"Sum Rule").next_to(finaltext, RIGHT).scale(0.6)
        self.play(Write(sumtext_or,run_time=4))
        self.wait(2)
        self.play(Transform(sumtext_or, sumtext))
        self.wait(2)
        self.play(Write(finaltext))
        self.play(ShowCreation(SurroundingRectangle(finaltext, fill_opacity=0)))
        self.play(Write(rule))
        self.wait(10)

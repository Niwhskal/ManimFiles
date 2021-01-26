from manimlib.imports import *

class SumRule(Scene):
    def construct(self):
        image = ImageMobject("/home/niwhskal/Desktop/project/media/designs/raster_images/table.png")
        self.play(FadeIn(image)) 
        image.generate_target()
        image.target.to_edge(LEFT)
        self.play(MoveToTarget(image))
        self.wait(10)

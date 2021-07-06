from manim import *
#from manim_fonts import *
import numpy as np
from PIL import Image


class AutomataMobject(VGroup):
	def __init__(self, dims, rows, cols):
		VGroup.__init__(self)
		self.rows = rows
		self.cols = cols
		self.dims = dims
		self.create_automata()
		
	def create_automata(self):
			self.CA_group = VGroup()
			self.Math_group = VGroup()
			for co, k in enumerate(range(self.rows)):
				for count, i in enumerate(range(self.cols)):
					if count ==0:
						square = Square(color =LIGHT_GREY)
						self.CA_group.add(square)
					else:
						square = Square(color =LIGHT_GRAY).next_to(self.CA_group, 0.3*RIGHT)	
						self.CA_group.add(square)

				if co ==0:
					self.Math_group.add(self.CA_group)
				else:
					self.CA_group = self.CA_group.next_to(self.Math_group, 0.3*DOWN)
					self.Math_group.add(self.CA_group)

				self.CA_group = VGroup()

			self.add(self.Math_group)


class lenia_scene(Scene):
	def construct(self):
#		with RegisterFont("Poppins") as fonts:
		text = Text("Cellular Automata").set_color(BLUE).scale(2)
		self.play(FadeIn(text))
		self.wait(1)
		self.play(ApplyMethod(text.scale, 0.5))
		self.play(ApplyMethod(text.to_edge, UP))
		undl = Underline(text, buff=0.2)
		self.play(FadeIn(undl))
		self.wait(1)

		img_1 = Image.open('images/ulam.jpg')
		img_ulam = ImageMobject(img_1).scale(0.4).move_to(RIGHT *2)
		text_ulam = Text("Stanislaw Ulam").scale(0.3).next_to(img_ulam, DOWN)
		img_1_vg = Group(img_ulam, text_ulam)
		self.play(FadeIn(img_1_vg))

		self.wait(1)

		img_2 = Image.open('images/von_neumann.jpeg')
		img_von = ImageMobject(img_2).scale(1.8).move_to(LEFT*2)
		text_von = Text("John von Neumann").scale(0.3).next_to(img_von, DOWN)
		img_2_vg = Group(img_von, text_von)
		self.play(FadeIn(img_2_vg))

		self.wait(4)

		self.remove(img_1_vg)
		self.remove(img_2_vg)
		
		self.wait(1)

		CA = AutomataMobject(1, 1, 5)
		CA.scale(0.5).center()
		self.play(Write(CA))
		self.wait(10)
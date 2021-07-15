#Lenia intro

from manim import *
#from manim_fonts import *
import numpy as np
from PIL import Image

class AutomataMobject(VGroup):
	def __init__(self, rows, cols, s_w=1.0):
		VGroup.__init__(self)
		self.rows = rows
		self.cols = cols
		self.s_w = s_w
		self.create_automata()
		
	def create_automata(self):
		self.CA_group = VGroup()
		self.Math_group = VGroup()
		for co, k in enumerate(range(self.rows)):
			for count, i in enumerate(range(self.cols)):
				if count ==0:
					square = Square().set_stroke(color=LIGHT_GRAY, width=self.s_w)
					self.CA_group.add(square)
				else:
					square = Square().set_stroke(color =LIGHT_GRAY, width=self.s_w).next_to(self.CA_group, 0.3*RIGHT)	
					self.CA_group.add(square)

			if co ==0:
				self.Math_group.add(self.CA_group)
			else:
				self.CA_group = self.CA_group.next_to(self.Math_group, 0.3*DOWN)
				self.Math_group.add(self.CA_group)

			self.CA_group = VGroup()

		self.add(self.Math_group)


class fifth_scene(Scene):
	def construct(self):
		cell = Square().center().scale(0.9).set_stroke(LIGHT_GRAY, width=0.5)
		disc_h1 = Text("Discrete").scale(0.4).next_to(cell, DOWN)
		disc_label = Text("0").set_height(0.3*cell.get_height()).move_to(cell)
		cell.set_fill(RED, opacity=1.0)

		self.play(FadeIn(cell))
		self.add(disc_label)
		self.add(disc_h1)
		self.wait(0.6)
		disc_label_1 = Text("1").set_height(0.3*cell.get_height()).move_to(cell)
		self.remove(disc_label)
		cell.set_fill(GREEN, opacity=1.0)
		self.add(disc_label_1)
		cell_group = Group(cell, disc_h1, disc_label, disc_label_1)

		self.wait(1)
		self.remove(*cell_group)

		cell_2 = Square().center().scale(0.9).set_stroke(LIGHT_GRAY, width=0.5)
		cont_h1 = Text("Continuous").scale(0.4).next_to(cell_2, DOWN)
		cell_2_label = Text("0").scale(0.3*cell_2.get_height()).move_to(cell_2)
		grad = color_gradient([RED, GREEN], length_of_output = 10)
		self.play(FadeIn(cell_2))
		self.add(cont_h1)
		for n, col in enumerate(grad):
			cell_2_label_mod = Text(f"{(n+1)/len(grad)}").set_height(0.3*cell_2.get_height()).move_to(cell_2)
			self.play(Transform(cell_2_label, cell_2_label_mod), run_time=0.2)
			cell_2.set_fill(col, opacity=1.0)
			self.wait(0.5)

		cell_2_group = Group(cell_2, cont_h1, cell_2_label, cell_2_label_mod)

		self.wait(2)	
		self.remove(*cell_2_group)

		lenia_h1 = Text("LENIA", gradient=(RED, GREEN))
		undl = Underline(lenia_h1, buff=0.2)
		self.add(lenia_h1)
		self.add(undl)
		h1_group = Group(lenia_h1, undl)

		CA_grid = AutomataMobject(10,10, s_w = 0.08).scale(0.2).center().shift(2*RIGHT)

		for i in range(10):
			for j in range(10):
				if(np.random.rand(1)[0] > 0.5):
					CA_grid.Math_group[i][j].set_fill(PURPLE, opacity=1.0)
				else:
					CA_grid.Math_group[i][j].set_fill(BLUE, opacity =1.0)
				
		self.play(ApplyMethod(h1_group.to_edge, UP))
		self.add(CA_grid)
		rules_h1 = Text(f"Rule = f(x)", gradient=(PURPLE, BLUE)).scale(0.7).center().shift(3*LEFT)
		self.add(rules_h1)
		arrow = CurvedArrow([0,0,0], [2,0,0]).next_to(rules_h1, UR)#Arrow(rules_h1, CA_grid.Math_group[4][1])
		arrow.flip(RIGHT)
		self.wait(1)
		self.play(FadeIn(arrow))

		grid_group = Group(CA_grid, rules_h1, arrow)

		#insert image of the paper, and bert's twitter image.
		self.remove(*grid_group)
		self.wait(10)

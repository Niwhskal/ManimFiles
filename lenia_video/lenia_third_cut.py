#2D CA's Basics

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


class Third_Scene(Scene):
	def construct(self):
		intro_h1 = Text("2-D Cellular Automata", color = BLUE).scale(0.5).to_edge(UP)
		underl = Underline(intro_h1, buff=0.2)
		intro_text_group = Group(intro_h1, underl)
		self.play(FadeIn(intro_text_group))

		self.wait(1)

		ROWS, COLUMNS = 11, 11

		CA = AutomataMobject(ROWS, COLUMNS)

		CA.scale(0.2).center()

		self.play(Write(CA))

		CA.Math_group[ROWS//2][COLUMNS//2].set_fill(BLUE, opacity=1.0)
		neighbor_grid = Square(color=YELLOW, stroke_width =2.0)
		neighbor_grid.set_height(CA.Math_group[0][0].get_height() *3)
		neighbor_grid.align_to(CA.Math_group[0][(ROWS//2)-1], LEFT)

		self.play(FadeIn(neighbor_grid))

		self.play(FadeOut(neighbor_grid))
		self.play(FadeOut(CA))
		self.play(FadeOut(intro_text_group))

		self.remove(neighbor_grid)
		self.remove(CA)
		self.remove(intro_text_group)

		#new_clear screen

		rules_h1 = Text("CA Rules").scale(0.4)
		unrl = Underline(rules_h1, buff=0.2)
		rules_text_group = Group(rules_h1, unrl)
		rules_text_group.to_edge(UP)
		self.add(rules_text_group)

		rule_1 = Text("1. Any cell with fewer than 2 live neighbors dies [Underpopulation]").scale(0.4)

		CA_small = AutomataMobject(3,3)
		CA_small.scale(0.3).next_to(rule_1, UP)
		CA_small.Math_group[1][1].set_fill(GREEN, opacity=1.0)
		CA_small.Math_group[0][0].set_fill(RED, opacity=1.0)
		CA_small.Math_group[0][1].set_fill(RED, opacity=1.0)
		CA_small.Math_group[0][2].set_fill(GREEN, opacity=1.0)
		CA_small.Math_group[1][0].set_fill(RED, opacity=1.0)
		CA_small.Math_group[1][2].set_fill(RED, opacity=1.0)
		CA_small.Math_group[2][0].set_fill(RED, opacity=1.0)
		CA_small.Math_group[2][1].set_fill(RED, opacity=1.0)
		CA_small.Math_group[2][2].set_fill(RED, opacity=1.0)


		self.play(Write(rule_1))
		self.play(FadeIn(CA_small))
		self.play(ApplyMethod(CA_small.Math_group[1][1].set_fill, RED))	

		self.remove(CA_small)
		self.play(ApplyMethod(rule_1.shift, DOWN))

		rule_2 = Text("2. Any cell with 2 or 3 live neighbors lives on").scale(0.4)

		CA_small_2 = AutomataMobject(3,3)
		CA_small_2.scale(0.3).next_to(rule_2, UP)
		CA_small_2.Math_group[1][1].set_fill(GREEN, opacity=1.0)
		CA_small_2.Math_group[0][0].set_fill(GREEN, opacity=1.0)
		CA_small_2.Math_group[0][1].set_fill(RED, opacity=1.0)
		CA_small_2.Math_group[0][2].set_fill(GREEN, opacity=1.0)
		CA_small_2.Math_group[1][0].set_fill(RED, opacity=1.0)
		CA_small_2.Math_group[1][2].set_fill(RED, opacity=1.0)
		CA_small_2.Math_group[2][0].set_fill(GREEN, opacity=1.0)
		CA_small_2.Math_group[2][1].set_fill(RED, opacity=1.0)
		CA_small_2.Math_group[2][2].set_fill(RED, opacity=1.0)

		self.play(Write(rule_2))
		self.play(FadeIn(CA_small_2))
#		self.play(ApplyMethod(CA_small_2.Math_group[1][1].set_fill, GREEn))	

		self.remove(CA_small_2)
		rule_2.next_to(rule_1, DOWN)
		rule_2.align_to(rule_1, LEFT)

		rule_3 = Text("3. Any live cell with >3 live neighbords dies").scale(0.4)

		CA_small_3 = AutomataMobject(3,3)
		CA_small_3.scale(0.3).next_to(rule_3, UP)
		CA_small_3.Math_group[1][1].set_fill(GREEN, opacity=1.0)
		CA_small_3.Math_group[0][0].set_fill(RED, opacity=1.0)
		CA_small_3.Math_group[0][1].set_fill(GREEN, opacity=1.0)
		CA_small_3.Math_group[0][2].set_fill(GREEN, opacity=1.0)
		CA_small_3.Math_group[1][0].set_fill(RED, opacity=1.0)
		CA_small_3.Math_group[1][2].set_fill(GREEN, opacity=1.0)
		CA_small_3.Math_group[2][0].set_fill(RED, opacity=1.0)
		CA_small_3.Math_group[2][1].set_fill(GREEN, opacity=1.0)
		CA_small_3.Math_group[2][2].set_fill(RED, opacity=1.0)


		self.play(Write(rule_3))
		self.play(FadeIn(CA_small_3))
		self.play(ApplyMethod(CA_small_3.Math_group[1][1].set_fill, RED))	

		self.remove(CA_small_3)
		rule_3.next_to(rule_2, DOWN)
		rule_3.align_to(rule_2, LEFT)

		rule_4 = Text("4. Any dead cell with =3 live neighbors becomes a live cell").scale(0.4)

		CA_small_4 = AutomataMobject(3,3)
		CA_small_4.scale(0.3).next_to(rule_4, UP)
		CA_small_4.Math_group[1][1].set_fill(RED, opacity=1.0)
		CA_small_4.Math_group[0][0].set_fill(GREEN, opacity=1.0)
		CA_small_4.Math_group[0][1].set_fill(RED, opacity=1.0)
		CA_small_4.Math_group[0][2].set_fill(RED, opacity=1.0)
		CA_small_4.Math_group[1][0].set_fill(GREEN, opacity=1.0)
		CA_small_4.Math_group[1][2].set_fill(RED, opacity=1.0)
		CA_small_4.Math_group[2][0].set_fill(RED, opacity=1.0)
		CA_small_4.Math_group[2][1].set_fill(RED, opacity=1.0)
		CA_small_4.Math_group[2][2].set_fill(GREEN, opacity=1.0)


		self.play(Write(rule_4))
		self.play(FadeIn(CA_small_4))
		self.play(ApplyMethod(CA_small_4.Math_group[1][1].set_fill, GREEN))	

		self.remove(CA_small_4)
		rule_4.next_to(rule_3, DOWN)
		rule_4.align_to(rule_3, LEFT)

		self.remove(rules_h1)
		self.remove(rule_1, rule_2, rule_3, rule_4)
		
		CA_main = AutomataMobject(32, 32, s_w = 0.1)
		for i in range(ROWS):
			for j in range(COLUMNS):
				rand_no = np.random.randint(0,2)
				if rand_no == 0:
					CA_main.Math_group[i][j].set_fill(RED, opacity=1.0)
				else:
					CA_main.Math_group[i][j].set_fill(GREEN, opacity=1.0)

		CA_main.scale(0.2).center()
		self.play(FadeIn(CA_main))

		self.wait(10)

		
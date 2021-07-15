from manim import *
#from manim_fonts import *
import numpy as np
from PIL import Image


class AutomataMobject(VGroup):
	def __init__(self, rows, cols):
		VGroup.__init__(self)
		self.rows = rows
		self.cols = cols
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

	#def label_cells(self, s_or_d):
		# label = MathTex("0")
		# label.set_height(self.Math_group[0].get_height())
		# self.play(Transition(self.Math_group[0].set_color, RED))
		# self.wait(1)


class lenia_scene(Scene):
	def construct(self):
#		with RegisterFont("Poppins") as fonts:
		intro_text_group = Group()
		text = Text("Cellular Automata").set_color(BLUE).scale(2)
		self.play(FadeIn(text))
		self.wait(1)
		self.play(ApplyMethod(text.scale, 0.5))
		self.play(ApplyMethod(text.to_edge, UP))
		undl = Underline(text, buff=0.2)
		self.play(FadeIn(undl))
		self.wait(1)
		intro_text_group.add(text,undl)

		ROWS = 1
		COLUMNS = 6

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

		CA = AutomataMobject(ROWS, COLUMNS)
		CA.scale(0.3).center()
		self.play(Write(CA))

		temp_label = MathTex("0")
		temp_label.set_height(0.3*CA.Math_group[0][0].get_height())
		temp_label.move_to(CA.Math_group[0][0])
		CA.Math_group[0][0].set_fill(RED, opacity=1.0)

		temp_label_1 = MathTex("1").set_height(0.3*CA.Math_group[0][0].get_height()).move_to(CA.Math_group[0][0])

		self.play(Transform(temp_label, temp_label_1), ApplyMethod(CA.Math_group[0][0].set_fill, GREEN, opacity=1.0) )

		#Random config showcase
		self.remove(temp_label)
		self.remove(temp_label_1)

		text_group = Group()
		rand_list = [1,0,1,1,0,1]
		for i, rand_num in enumerate(rand_list):
			rand_label = MathTex(f"{rand_num}")
			rand_label.set_height(0.3*CA.Math_group[0][0].get_height())
			rand_label.move_to(CA.Math_group[0][i])
			self.play(FadeIn(rand_label))
			if rand_num ==0:
				CA.Math_group[0][i].set_fill(RED, opacity=1.0)
			elif rand_num ==1:
				CA.Math_group[0][i].set_fill(GREEN, opacity=1.0)
			self.wait(1)
			text_group.add(rand_label)

		init_h1 = Text("Initial State").scale(0.3).next_to(CA.Math_group, LEFT)
		self.play(FadeIn(init_h1))
		CA_text_group = Group(init_h1, CA.Math_group, text_group)

		self.remove(rand_label)

		self.play(ApplyMethod(CA_text_group.shift, UP))

		rule_h1 = Text("1. If the Current cell is surrounded by <2 alive neighbors, it dies").scale(0.4).shift(2*DOWN)
		rule_h2 = Text("2. If the Current cell is surrounded by two alive neighbors, it becomes alive").scale(0.4).next_to(rule_h1, DOWN)
		rules_group = Group(rule_h1, rule_h2)

		self.play(Write(rule_h1))
		self.play(Write(rule_h2))
		self.play(FadeOut(intro_text_group))
		self.remove(intro_text_group)
		window = Square().set_stroke(YELLOW, 6).shift(2*UP)
		window.height = (CA.Math_group[0][0].get_height())
		window.align_to(CA.Math_group[0][0], LEFT)

		self.play(ApplyMethod(CA_text_group.shift, UP))

		#arrow

		arrow = Arrow(start =UP, end=0.5*DOWN, buff=0.45, max_tip_length_to_length_ratio=0.3).next_to(window, DOWN)

		#arrow+window group

		ar_win_group = Group(arrow, window)

		#new state CA
		CA_1 = AutomataMobject(ROWS, COLUMNS)
		CA_1.scale(0.3).center().next_to(arrow, DOWN).align_to(CA, LEFT)

		ca_1_text = Text("State: 1").scale(0.3).next_to(CA_1, LEFT).align_to(init_h1, LEFT)

		self.play(FadeIn(window))

		#group

		CA_1_text_group = Group(CA_1, ca_1_text)

		#show new empty grid

		self.add(CA_1_text_group)
		second_text_group = Group()
		nu = [0,1,0,0,1,0]

		for i in range(COLUMNS):
			ar_win_group.align_to(CA.Math_group[0][i], LEFT)
			self.add(ar_win_group)

			#change new_cell state 

			r_label = MathTex(f"{nu[i]}")
			r_label.set_height(0.3*CA_1.Math_group[0][0].get_height())
			r_label.move_to(CA_1.Math_group[0][i])
			self.play(FadeIn(r_label))

			if nu[i] ==0:
				CA_1.Math_group[0][i].set_fill(RED, opacity=1.0)
			elif nu[i] ==1:
				CA_1.Math_group[0][i].set_fill(GREEN, opacity=1.0)
			second_text_group.add(r_label)

			self.wait(1)

		CA_1_text_group.add(second_text_group)

		self.remove(ar_win_group)
		self.play(ApplyMethod(CA_text_group.shift, UP))

		self.play(ApplyMethod(CA_1_text_group.shift, UP))


		window_2 = Square().set_stroke(YELLOW, 6).shift(1.3*UP)
		window_2.height = (CA_1.Math_group[0][0].get_height())
		window_2.align_to(CA_1.Math_group[0][0], LEFT)

		self.add(window_2)

		#arrow_2

		arrow_2 = Arrow(start =UP, end=0.5*DOWN, buff=0.45, max_tip_length_to_length_ratio=0.3).next_to(window_2, DOWN)

		#arrow+window group_2

		ar_win_group_2 = Group(arrow_2, window_2)

		#new state CA_2
		CA_2 = AutomataMobject(ROWS, COLUMNS)
		CA_2.scale(0.3).center().next_to(arrow_2, DOWN).align_to(CA_1, LEFT)

		ca_2_text = Text("State: 2").scale(0.3).next_to(CA_2, LEFT).align_to(ca_1_text, LEFT)

		self.play(FadeIn(window_2))

		#group_2

		CA_2_text_group = Group(CA_2, ca_2_text)

		#show new empty grid

		self.add(CA_2_text_group)

		third_text_group = Group()
		for i in range(COLUMNS):
			ar_win_group_2.align_to(CA_1.Math_group[0][i], LEFT)
			self.add(ar_win_group_2)

			#change new_cell state 

			r_label_2 = MathTex(f"0")
			r_label_2.set_height(0.3*CA_2.Math_group[0][0].get_height())
			r_label_2.move_to(CA_2.Math_group[0][i])
			self.play(FadeIn(r_label_2))

			CA_2.Math_group[0][i].set_fill(RED, opacity=1.0)
			third_text_group.add(r_label_2)

			self.wait(1)

		CA_2_text_group.add(third_text_group)

		self.remove(ar_win_group_2)

		self.play(FadeOut(CA_text_group))

		self.remove(CA_text_group)

		self.play(ApplyMethod(CA_1_text_group.shift, UP), ApplyMethod(CA_2_text_group.shift, UP))

		dotted_text = Tex('\\vdots').next_to(CA_2, DOWN)

		copy_CA_2 = AutomataMobject(ROWS, COLUMNS) 
		copy_CA_2.scale(0.3).center().next_to(dotted_text, DOWN).align_to(CA_2, LEFT)

		nth_text = Tex("State: $\\infty$").next_to(copy_CA_2, LEFT).scale(0.6).align_to(ca_2_text, LEFT)

		self.play(FadeIn(dotted_text))
		self.play(FadeIn(nth_text), FadeIn(copy_CA_2))

		self.wait(10)
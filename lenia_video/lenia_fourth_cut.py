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


class fourth_scene(Scene):

	def construct(self):
		ROWS, COLUMNS=32, 32

		CA_main = AutomataMobject(ROWS, COLUMNS, s_w = 0.1)
		for i in range(ROWS):
			for j in range(COLUMNS):
				rand_no = np.random.randint(0,2)
				if rand_no == 0:
					CA_main.Math_group[i][j].set_fill(RED, opacity=1.0)
				else:
					CA_main.Math_group[i][j].set_fill(GREEN, opacity=1.0)

		
		CA_main.scale(0.05).center()
		self.play(FadeIn(CA_main))

		for i in range(ROWS):
			for j in range(COLUMNS):
				if str(CA_main.Math_group[i][j].get_color()) == '#fc6255':
					CA_main.Math_group[i][j].set_fill(BLACK, opacity=1.0)

		self.add(CA_main)

		text_iter = Text("Iteration:").scale(0.4).next_to(CA_main, LEFT)
		self.add(text_iter)

		for iter in range(20):
				num_text = Text(f"Iteration: {iter}").next_to(CA_main, LEFT).scale(0.4)
				for i in range(ROWS):
					for j in range(COLUMNS):
						curr_cell = str(CA_main.Math_group[i][j].get_color())
						try:
							n_D = str(CA_main.Math_group[i+1][j].get_color())
						except IndexError:
							n_D = 'YOLO'

						try:
							n_U = str(CA_main.Math_group[i-1][j].get_color())
						except IndexError:
							n_U = 'YOLO'

						try:
							n_R = str(CA_main.Math_group[i][j+1].get_color())
						except IndexError:
							n_R = 'YOLO'

						try:	
							n_L = str(CA_main.Math_group[i][j-1].get_color())
						except IndexError:
							n_L = 'YOLO'

						try:	
							n_DR = str(CA_main.Math_group[i+1][i+1].get_color())
						except IndexError:
							n_DR = 'YOLO'

						try:	
							n_UL = str(CA_main.Math_group[i-1][i-1].get_color())
						except IndexError:
							n_UL='YOLO'

						try:	
							n_UR = str(CA_main.Math_group[i-1][i+1].get_color())
						except IndexError:
							n_UR = 'YOLO'
						try:	
							n_DL = str(CA_main.Math_group[i+1][i-1].get_color())
						except IndexError:
							n_DL = 'YOLO'

						unique, counts = np.unique([n_D, n_U, n_R, n_L, n_DR, n_UL, n_UR, n_DL], return_counts=True)
						d = dict(zip(unique, counts))
						try:
							test = d["black"]
						except KeyError:
							d["black"] = 0

						try:
							test = d['#83c167']
						except KeyError:
							d['#83c167'] = 0

						if	curr_cell == '#83c167' and d["#83c167"] < 2:
							CA_main.Math_group[i][j].set_fill(BLACK, opacity=1.0)

						elif curr_cell =='#83c167' and d["#83c167"] >3:
							CA_main.Math_group[i][j].set_fill(BLACK, opacity=1.0)

						elif curr_cell == 'black' and d["#83c167"] ==3:
							CA_main.Math_group[i][j].set_fill(GREEN, opacity=1.0)

				self.play(Transform(text_iter, num_text))
				self.add(CA_main)
				self.wait(0.4)

		self.wait(10)

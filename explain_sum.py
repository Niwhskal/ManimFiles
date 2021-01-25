from manimlib.imports import *

class PythagoreanProof(Scene):
    CONFIG = {
        "square_scale": 5,
    }
    def construct(self):
        
        d = {0: "#fcb103", 1: "#00993b", 2: "#00a6b5", 3: "#5e1973"}
        square = Square()
        square.scale(2) 
        dots2 = [
            square.point_from_proportion(i * 1/4 + j * 1/16)
            for i,j in zip(range(4),[1,3,3,1])
        ]
        dots_corners2 = [
            square.point_from_proportion(i * 1/4) 
            for i in range(4)
        ]
        middle = np.array([
            dots2[0][0],
            dots2[1][1],
            0
        ])
        
        all_rectangles = VGroup(*[
            Polygon(
                dots_corners2[i],
                dots2[i],
                middle,
                dots2[i-1],
                fill_opacity=0.5,
                color = d[i]
            )
            for i in range(4)
        ])
        # rectancles: rectangles of the triangles
        rectangles = all_rectangles[0::2]
        # Big and small squares
        squares = all_rectangles[1::2]
        # IMPORTANT
        # use total_points = 3 if you are using the 3/feb release
        # use total_points = 4 if you are using the most recent release
        total_points = 4
        rect_dot = [
            [
                rectangles[i].points[total_points*j]
                for j in range(4)
            ]
            for i in range(2)
        ]

        main = TextMobject("P(X = ").to_edge(UP)
        text1 = TextMobject("0.15")
        text2 = TextMobject("0.6")
        text3 = TextMobject("0.20")
        text4 = TextMobject("0.05")
        
        self.add(square) 
        self.add(main)
        state2 = TextMobject("no dates)= ").next_to(main, RIGHT) 
        self.play(ShowCreation(state2))
        text2.next_to(state2, RIGHT)
        self.play(ShowCreation(text2))
        
        self.play(ShowCreation(all_rectangles[1])) 
        text2.generate_target()
        text2.target.move_to(all_rectangles[1].get_center())
        self.play(MoveToTarget(text2))    
        self.remove(state2)


#-----
        state3 = TextMobject("1 date)=").next_to(main, RIGHT)
        self.play(ShowCreation(state3)) 
        text3.next_to(state3, RIGHT)
        self.play(ShowCreation(text3))
        self.play(ShowCreation(all_rectangles[2]))
        text3.generate_target()
        text3.target.move_to(all_rectangles[2].get_center())
        self.play(MoveToTarget(text3))
        self.remove(state3)        
#-----

        state1 = TextMobject("2 dates)=").next_to(main, RIGHT)
        self.play(ShowCreation(state1))
        text1.next_to(state1, RIGHT)
        self.play(ShowCreation(text1))
        self.play(ShowCreation(all_rectangles[0]))
        text1.generate_target()

        text1.target.move_to(all_rectangles[0].get_center())
        self.play(MoveToTarget(text1))
        self.remove(state1)
#-----
 
        state4 = TextMobject("3 dates)=").next_to(main, RIGHT)
        self.play(ShowCreation(state4))
        text4.next_to(state4, RIGHT)
        self.play(ShowCreation(text4))
        self.play(ShowCreation(all_rectangles[3]))
        text4.generate_target()

        text4.target.move_to(all_rectangles[3].get_center())
        self.play(MoveToTarget(text4))


# Remove main
        self.remove(state4)
        self.remove(main)
        
        iftext1 = TextMobject("If, out of three, one cancels, then: P(x=3) = 0").to_edge(UP)
        self.play(ShowCreation(iftext1)) 





        self.wait(10)

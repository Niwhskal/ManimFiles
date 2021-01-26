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

        ma = {2: "no dates)= ", 3: "1 date)= ", 1: "2 dates)= ", 4: "3 dates)= "}
        text_order = {2: "text2", 3:"text3", 1: "text1", 4: "text4"} 
        rect_order = {0:1, 1:2, 2:0, 3:3}
        for i, val in enumerate([2,3,1,4]): 

            state2 = TextMobject(ma[val]).next_to(main, RIGHT)
            self.play(ShowCreation(state2))
            eval(text_order[val]).next_to(state2, RIGHT)
            self.play(ShowCreation(eval(text_order[val])))        
            self.play(ShowCreation(all_rectangles[rect_order[i]])) 
            eval(text_order[val]).generate_target()
            eval(text_order[val]).target.move_to(all_rectangles[rect_order[i]].get_center())
            self.play(MoveToTarget(eval(text_order[val])))    
            self.remove(state2)
# Remove main
        self.remove(state2)
        self.remove(main)
        
        iftext1 = TextMobject("suppose one cancels, then: P(x=3) = 0").to_edge(UP)

        iftext2 = TextMobject("then another cancels: P(X=2) =0").to_edge(UP)

        iftext3 = TextMobject("finally the last one cancels: P(X=1) = 0").to_edge(UP)

        ifdict = {0: "iftext1", 1: "iftext2", 2: "iftext3"}

        trndict = {3: 2, 0:1, 2: 1}
        rm_text = {3: "text4", 0: "text1", 2: "text3"}
        sumdict = {3: "0.25", 0: "0.75", 2: "1.0"}
        replacedict = {3: "text3", 0: "text2", 2: "text2"}
        for m, num in enumerate([3,0,2]):
            self.play(ShowCreation(eval(ifdict[m]))) 
            if num ==2:
                all_rectangles[3].set_color(d[trndict[num]])
            self.play(FadeToColor(all_rectangles[num], d[trndict[num]]))
            self.remove(eval(rm_text[num]))
        
            temp_1 = TextMobject(sumdict[num])
            temp_1.move_to(all_rectangles[trndict[num]].get_center())
            self.play(Transform(eval(replacedict[num]), temp_1))
                
            self.remove(eval(ifdict[m]))
        
        textfin = TextMobject(r"The only state left is 'no date' \\ and it will certainly happen.").shift(3*UP)
        self.add(textfin)
        self.wait(5)

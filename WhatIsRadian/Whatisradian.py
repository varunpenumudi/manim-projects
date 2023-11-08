from manim import *
from manim.opengl import *
DEFAULT_STROKE_WIDTH=2
#Scene1
class IntroText(Scene):
  def construct(self):
    text1 = Text("Radian అంటే ఏంటి?", font="Noto Sans Telugu").scale(1.5)
    self.wait()
    self.play(Write(text1), run_time=2)
    self.wait(2)
    self.play(FadeOut(text1))   

#Scene2
class WhyAngles(Scene):
  def construct(self):
    text = Text("Angles?")
    line1 = Line(ORIGIN, 2*RIGHT, color=BLUE)
    arrow = Arrow(start=1*LEFT,end=1*RIGHT, color=RED)
    line1.next_to(arrow, RIGHT).shift(1*RIGHT)
    text.next_to(arrow, LEFT).shift(0.5*LEFT)
    line2 = line1.copy().rotate(29*DEGREES, about_point=line1.get_start())
    angle = always_redraw(lambda : Angle(line1, line2)) 

    self.play(Write(text),Create(arrow), run_time=2)
    self.play(FadeIn(line1), rate_func=rush_into)
    self.play(FadeIn(line2), Create(angle), lag_ratio=1)
    self.play(Rotate(line2, PI/1.5, about_point=line1.get_start()), rate_func=rush_from, run_time=0.5)
    self.play(Rotate(line2, -PI/3, about_point=line1.get_start()), rate_functions=rush_from, run_time=0.5)
    self.wait()

#Scene3
class Rotations(Scene):
  def construct(self):
    line1 = Line(ORIGIN, 2*RIGHT, color=BLUE)
    line2 = line1.copy()
    dot = Dot(radius=0.02)
    self.play(Create(line1),Create(line2))
    self.add(dot)
    self.wait(2)

    fr_text = Text("Full Rotation", font="Sans").next_to(dot, 9*UP)
    self.play(Rotate(line1,2*PI,about_point=ORIGIN), run_time=3)
    self.play(Write(fr_text))
    self.wait()
    self.play(FadeOut(fr_text))

    hr_text = Text("Half Rotation", font="Sans").next_to(dot,9*UP)
    self.play(Rotate(line1, PI, about_point=ORIGIN))
    self.play(Write(hr_text))
    self.wait()
    self.play(FadeOut(hr_text), FadeOut(line1))

    rot_text = Text("Rotation?", font="Sans").next_to(dot,9*UP)
    line1.rotate(PI, about_point=ORIGIN)
    self.play(FadeIn(line1))
    self.play(Rotate(line1, PI/6, about_point=ORIGIN), run_time=2)
    self.play(Write(rot_text))
    self.wait()


#Scene4
class Degrees(Scene):
  def construct(self):
    line1 = Line(ORIGIN, 2*RIGHT, color=BLUE)
    line2 = line1.copy().rotate(PI/12, about_point=line1.get_start())
    circle = Circle(radius=2, color=BLUE)
    angle = always_redraw(lambda : Angle(line1, line2, color=GOLD_A))
    dot = Dot().scale(0.4)

    # Decimal number for angle value
    ang_val = DecimalNumber(angle.get_value(degrees=True),num_decimal_places=0, unit="^{\circ}").scale(0.5)
    ang_val.next_to(line1, UP).shift(0.5*RIGHT)
    def angval_updater(mobj):
      ang = (line2.get_angle()-line1.get_angle())/DEGREES
      if ang < 0:
        ang = 360+ang
      mobj.set_value(ang)
      mobj.next_to(angle, UR, buff=0.01)
    ang_val.add_updater(angval_updater)

    self.play(Write(circle))
    self.play(Write(line1), Write(line2), FadeIn(dot), lag_ratio=0)
    self.play(Write(angle), Write(ang_val))
    self.play(Rotate(line2,PI/4,about_point=line2.get_start()), run_time=2)
    self.play(Rotate(line2,PI,about_point=line2.get_start()), run_time=1)
    self.play(Rotate(line2,-PI/1.9,about_point=line2.get_start()), run_time=1)

    text = Text("Degrees", font="Sans")
    text.to_edge(UP)
    self.play(Write(text))
    self.play(Rotate(line2, -145*DEGREES, about_point=line2.get_start()))
    self.play(Rotate(line2, 359.6*DEGREES, about_point=line2.get_start()), run_time=3)
    self.wait(3)
    self.wait()

    #points on circle
    points = [circle.point_at_angle(i*DEGREES) for i in range(1,361)]
    lines_group = VGroup(*[Line(ORIGIN, 0.1*RIGHT, stroke_width=1.5, color=RED_E).move_to(p).rotate((i+1)*DEGREES) for i,p in enumerate(points)])
    self.play(Write(lines_group))
    self.play(FadeOut(lines_group[1:][:-1]))
    self.play(Indicate(lines_group[0]))

    self.play(Rotate(line2, 1.4*DEGREES, about_point=line2.get_start()))
    self.wait(3)


class WhatIsRadian(Scene):
  def construct(self):
    # intro text
    text1 = Text("What is a Radian?").scale(1.5)
    dot = Dot().scale(0.2)
    self.play(Write(text1))
    self.wait(2)
    self.play(FadeOut(text1)) 
    
    # text about angle
    text2 = Text("angle?").scale(1.5)
    self.play(Write(text2), run_time=2)
    self.play(text2.animate.to_edge(UL))
    self.play(Transform(text2, Text("Angle:").scale(1.5).to_edge(UL, buff=0.8)))
    
    # creating lines and angles
    line1 = Line(start=ORIGIN, end=3*RIGHT, color=BLUE)
    line2 = line1.copy()
    line3 = line1.copy().rotate(-20 * DEGREES, about_point=ORIGIN)
    dummy_angle = Angle(line1,line3, radius=0.4).set_stroke(width=0)
    angle = dummy_angle
    
    # angle updater and value_num updater
    def updater_angle(mob):
      try:
        mob.become(Angle(line1, line2, radius=0.4, other_angle=True))
      except:
        mob.become(dummy_angle)
        
    value_num = DecimalNumber(0, num_decimal_places=0, unit="^{\circ}")
    
    angle.add_updater(updater_angle)
    def valnumUpdater(mobj):
        ang = (line1.get_angle()-line2.get_angle())/DEGREES
        
        if ang < 0:
          ang = 360+ang

        mobj.set_value(ang)
        mobj.next_to(angle, UR)

    value_num.add_updater(valnumUpdater)
    
    
    # adding lines, angle, dot, value_num and rotate line1
    self.play(Create(line1), Create(line2))
    self.play(Create(angle), Create(dot))
    self.wait(1)
    self.play(Rotate(line1,PI/2, about_point=ORIGIN), run_time=2)
    self.play(FadeIn(value_num), run_time=1)
    self.play(Rotate(line1,PI/4, about_point=ORIGIN), run_time=2)
    self.play(Rotate(line1,PI/2, about_point=ORIGIN), run_time=2)
    
    self.wait(3) 
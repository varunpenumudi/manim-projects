from manim import *
from manim.opengl import *


class Intro(Scene):
  def construct(self):
    text1 = Text("What is Radian?").scale(1.5)
    dot = Dot().scale(0.2)
    self.play(Write(text1))
    self.wait(2)
    self.play(FadeOut(text1))   
    
    text2 = Text("angle?").scale(1.5)
    self.play(Write(text2), run_time=2)
    self.play(text2.animate.to_edge(UL))
    self.play(Transform(text2, Text("Angle:").scale(1.5).to_edge(UL, buff=0.8)))

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
from manim import *

class SolveByFactoring(Scene):
    def construct(self):
        # 1) 最初の式を「手書き風」に描く
        eq1 = MathTex(r"x^2 + 2x + 1 = 0", font_size=72)
        self.play(Write(eq1), run_time=2.0)
        self.wait(0.3)

        # 2) 因数分解の形を補助表示（色付け）
        hint = MathTex(r"(x+1)^2 = 0", font_size=72).next_to(eq1, DOWN, buff=0.6)
        self.play(FadeIn(hint, shift=DOWN, scale=0.95))
        self.play(Indicate(eq1[0:5]), Indicate(hint[0:5]))
        self.wait(0.4)

        # 3) 本体の式を「対応付けを保ったまま」変形
        #    TransformMatchingTex を使うと、共通部分が滑らかに一致して変形される
        eq2 = MathTex(r"(x+1)^2 = 0", font_size=72)
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.2)
        self.wait(0.3)

        # 4) 解の提示
        eq3 = MathTex(r"x = -1", font_size=72).next_to(eq2, DOWN, buff=0.8)
        self.play(Write(eq3), run_time=1.0)
        box = SurroundingRectangle(eq3, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(1.0)

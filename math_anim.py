from manim import *

class SolveByFactoring(Scene):
    def construct(self):
        # 1) 最初の式
        eq1 = MathTex(r"x^2 + 2x + 1 = 0", font_size=72)
        self.play(Write(eq1), run_time=2.0)
        self.wait(0.3)

        # 2) 下にヒントを出す
        hint = MathTex(r"(x+1)^2 = 0", font_size=72).next_to(eq1, DOWN, buff=0.6)
        self.play(FadeIn(hint, shift=DOWN, scale=0.95))
        self.play(Indicate(eq1[0:5]), Indicate(hint[0:5]))
        self.wait(0.4)

        # 3) 「下の式を上に持ってくる」＝ 下を上の位置に置き換え、元の上は消す
        next_top = MathTex(r"(x+1)^2 = 0", font_size=72).move_to(eq1)  # ← 画面に add しない
        self.play(
            ReplacementTransform(hint, next_top),  # 下 → 上の最終形へ置き換え（下は消える）
            FadeOut(eq1),                           # 旧トップは消す
            run_time=1.2
        )
        eq2 = next_top  # 以後の“上段”参照を更新
        self.wait(0.3)

        # 4) 解の提示（上のすぐ下に出す）
        eq3 = MathTex(r"x = -1", font_size=72).next_to(eq2, DOWN, buff=0.8)
        self.play(Write(eq3), run_time=1.0)
        box = SurroundingRectangle(eq3, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(1.0)

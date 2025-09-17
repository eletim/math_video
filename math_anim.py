from manim import *

class SolveByFactoringScene(Scene):
    def countdown_under(self, anchor_mobj, seconds=3, scale=1.8, gap=1.3):
        """問題の真下に大きめカウントダウン。gapで間隔を広げる。"""
        spot = anchor_mobj.get_bottom() + DOWN * gap
        ring = Circle(radius=0.55*scale).set_stroke(width=6).move_to(spot)
        self.play(GrowFromCenter(ring), run_time=0.25)
        for s in range(seconds, 0, -1):
            num = MathTex(str(s), font_size=96).scale(scale).move_to(spot)
            self.play(Write(num, run_time=0.30))
            self.wait(0.70)            # 表示キープ
            self.play(FadeOut(num, run_time=0.20))
        self.play(FadeOut(ring), run_time=0.20)

    def construct(self):
        # タイトル → 下線（先に出す）
        title = MathTex(r"x \;=\; ?", font_size=72).to_edge(UP)
        underline = Underline(title).set_stroke(width=2)
        self.play(FadeIn(title), Create(underline, run_time=0.3))

        # ① 問題文：タイトルのすぐ下（即表示・手書きにしない）
        eq1 = MathTex(r"x^2 + 2x + 1 = 0", font_size=72).next_to(underline, DOWN, buff=0.55)
        self.add(eq1)  # 0秒で出す

        # ② タイマー：問題文のさらに下（間隔を広めに：gap=1.3）
        self.countdown_under(eq1, seconds=3, scale=1.8, gap=1.3)

        # ③ ヒントを問題のすぐ下に（ここは手書き演出のまま）
        hint = MathTex(r"(x+1)^2 = 0", font_size=60).next_to(eq1, DOWN, buff=0.65)
        self.play(Write(hint, run_time=0.9))

        # 式変形前に1秒の間
        self.wait(1.0)

        # ④ 問題を消し、ヒントを上へ昇格（非手書き遷移）
        eq2_top = MathTex(r"(x+1)^2 = 0", font_size=72).next_to(underline, DOWN, buff=0.6)
        self.play(
            ReplacementTransform(hint, eq2_top),
            FadeOut(eq1),
            run_time=1.0
        )

        # 次提示前に1秒の間
        self.wait(1.0)

        # ⑤ 解の提示（下に手書き）
        eq3 = MathTex(r"x = -1", font_size=72).next_to(eq2_top, DOWN, buff=0.85)
        self.play(Write(eq3, run_time=0.9))
        self.play(Create(SurroundingRectangle(eq3, color=YELLOW, buff=0.22)), run_time=0.3)
        self.wait(0.6)

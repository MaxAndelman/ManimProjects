from manim import *


class Genus(Scene):
    def construct(self):

        intro = Text(
            "Let's start with the first one: the genus of I(V,F)",
            font_size=30,
            color=WHITE
        )
        intro.shift(UP*1.6)


        euler = Paragraph(
            "We know the number of vertices and faces"
            "\n(V and F, respectively),"
            "\nso we just need to find the number of edges"
            "\nto be able to solve for the genus"
            "\nusing Euler's characteristic Formula",
            font_size=30,
            color=WHITE,
            alignment="center",
            line_spacing=1.1
        )
        euler.shift(DOWN)

        self.play(Write(intro), run_time = 1.8)
        self.wait(0.5)
        self.play(Write(euler), run_time=3.5)
        self.wait(3)
        self.play(FadeOut(intro), FadeOut(euler))

        edges1 = Paragraph(
            "Since all edges connect two vertices,\n"
            "\nE = 1/2Σ(v∈V) d(v)",
            font_size=30,
            color=WHITE,
            alignment="center"
        )
        edges1.shift(UP*1.5)

        edges2 = Paragraph(
            "By excess definition, \n"
            "\nΣ(v∈V) d(v) = e + VF\n"
            "\nSo E = 1/2(e + VF)",
            font_size=30,
            color=WHITE,
            alignment="center"
        )
        edges2.shift(DOWN)

        self.play(Write(edges1), run_time = 1.8)
        self.wait(0.5)
        self.play(Write(edges2), run_time = 2)
        self.wait(3)
        self.play(FadeOut(edges1), FadeOut(edges2))

        # Equation derivation steps
        steps = [
            MathTex(r"2 - 2g = V - \frac{1}{2}(e + VF) + F"),
            MathTex(r"4 - 4g = 2V + 2F - e - VF"),
            MathTex(r"-4g = 2V + 2F - e - VF - 4"),
            MathTex(r"4g = -2V - 2F + e + VF + 4"),
            MathTex(r"4g = (V - 2)(F - 2) + e"),
            MathTex(r"g = \frac{(V - 2)(F - 2)}{4} + \frac{e}{4}")
        ]

        quickAlgebra = Text(
            "Some quick algebra:",
            font_size=30,
            color=WHITE
        )
        quickAlgebra.shift(UP*1.5)

        # Scale equations to fit nicely
        for step in steps:
            step.scale(1.2)

        self.play(Write(quickAlgebra), run_time = 1)

        # Display first equation
        self.play(Write(steps[0]))
        self.wait(1)

        # Transform through each step
        for i in range(len(steps) - 1):
            self.play(Transform(steps[0], steps[i + 1]), run_time=1)
            self.wait(0.2)

        self.wait(2)
        self.play(FadeOut(quickAlgebra))

        ele3 = Text(
            "Since g is an integer, if e ≤ 3, then",
            font_size=30,
            color=WHITE,
        )
        ele3.shift(UP*0.5)

        ele3 = Text(
            "Since g is an integer, if e ≤ 3, then",
            font_size=30,
            color=WHITE,
        )
        ele3.shift(UP * 1.3)

        genus = MathTex(r"g = \bigg\lceil\frac{(m - 2)(n - 2)}{4}\bigg\rceil")

        self.play(Write(ele3))
        self.play(Transform(steps[0], genus))
        self.wait(1.5)

        end = Paragraph(
            "Now, we just need to show that I(V,F) with e ≤ 3 exists"
            "\nto show that this is also the genus of K(V,F)",
            font_size=30,
            color=WHITE,
            alignment="center",
            line_spacing=1.1
        )
        end.shift(DOWN * 1.5)

        self.play(Write(end), run_time = 2.5)
        self.wait(3)
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
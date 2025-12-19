from manim import *
import numpy as np


class Conclusion(Scene):
    def construct(self):
        intro = Paragraph(
            "All of these base cases can be done with"
            "a construction. I'm not going to show all of them,"
            "\nbut I will end with the construction"
            "\nof I(6,3) with 0 excess, the base case"
            "\nof the induction the I(6,n) exists.",
            font_size=30,
            color=WHITE,
            alignment="center",
            line_spacing=1.1
        )
        self.play(Write(intro), run_time=3)
        self.wait(2)
        self.play(FadeOut(intro))

        # Create a square frame
        square = Square(side_length=5)

        top_arrow = Arrow(start=ORIGIN + UP * 2.5 + LEFT * 0.5, end=ORIGIN + UP * 2.5 + RIGHT * 0.5, buff=0,
                          stroke_width=0)
        bottom_arrow = Arrow(start=ORIGIN + DOWN * 2.5 + LEFT * 0.5, end=ORIGIN + DOWN * 2.5 + RIGHT * 0.5, buff=0,
                             stroke_width=0)
        left_arrow1 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.8, end=ORIGIN + LEFT * 2.5 + DOWN * 0.2, buff=0,
                            stroke_width=0)
        left_arrow2 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.2, end=ORIGIN + LEFT * 2.5 + DOWN * 0.8, buff=0,
                            stroke_width=0)
        right_arrow1 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.8, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.2, buff=0,
                             stroke_width=0)
        right_arrow2 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.2, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.8, buff=0,
                             stroke_width=0)

        self.play(
            Create(square),
            Create(top_arrow), Create(bottom_arrow),
            Create(left_arrow1), Create(left_arrow2),
            Create(right_arrow1), Create(right_arrow2)
        )

        # Radius for hexagon
        radius = 1.8

        nodes = []
        for k, theta in enumerate(np.linspace(0, 2 * np.pi, 6, endpoint=False)):
            pos = radius * np.array([np.cos(theta), np.sin(theta), 0])
            node = Dot(pos, color=BLUE, radius=0.12)
            nodes.append(node)

        for node in nodes:
            self.play(FadeIn(node), run_time=0.2)

        edges = [(i, (i + 1) % 6) for i in range(6)]
        for i, j in edges:
            self.play(Create(Line(nodes[i].get_center(), nodes[j].get_center())), run_time=0.2)

        # Wrapping lines representing torus topology
        # Line 1: Left vertex (node 3) wraps across left edge to right vertex (node 0)
        line1_left = Line(nodes[3].get_center(), np.array([-2.5, nodes[3].get_center()[1], 0]), color=RED)
        line1_right = Line(np.array([2.5, nodes[3].get_center()[1], 0]), nodes[0].get_center(), color=RED)

        # Line 2: Bottom left vertex (node 4) wraps across bottom edge to top right vertex (node 1)
        line2_bottom = Line(nodes[4].get_center(), np.array([0, -2.5, 0]), color=GREEN)
        line2_top = Line(np.array([0, 2.5, 0]), nodes[1].get_center(), color=GREEN)

        # Line 3: Bottom right vertex (node 5) wraps across corner to top left vertex (node 2)
        line3_bottom_right = Line(nodes[5].get_center(), np.array([2.5, -2.5, 0]), color=YELLOW)
        line3_top_left = Line(np.array([-2.5, 2.5, 0]), nodes[2].get_center(), color=YELLOW)

        self.play(LaggedStart(Create(line1_left), Create(line1_right), lag_ratio=0.45, run_time=0.4))
        self.play(LaggedStart(Create(line2_bottom), Create(line2_top), lag_ratio=0.45, run_time=0.5))
        self.play(LaggedStart(Create(line3_bottom_right), Create(line3_top_left), lag_ratio=0.45, run_time=0.7))

        # Create 7 polygons for the 7 regions
        # Region 1: Central hexagon
        poly1 = Polygon(*[n.get_center() for n in nodes], color=PURPLE, fill_opacity=0.3, stroke_width=0)

        # Region 2: Top region
        poly2 = Polygon(
            nodes[1].get_center(), nodes[2].get_center(),
            np.array([-2.5, 2.5, 0]), np.array([0, 2.5, 0]),
            color=ORANGE, fill_opacity=0.3, stroke_width=0
        )

        # Region 3: Top right region
        poly3 = Polygon(
            nodes[0].get_center(), nodes[1].get_center(),
            np.array([0, 2.5, 0]), np.array([2.5, 2.5, 0]),
            np.array([2.5, nodes[0].get_center()[1], 0]),
            color=TEAL, fill_opacity=0.3, stroke_width=0
        )

        # Region 4: Bottom right region
        poly4 = Polygon(
            nodes[5].get_center(), nodes[0].get_center(),
            np.array([2.5, nodes[0].get_center()[1], 0]),
            np.array([2.5, -2.5, 0]),
            color=ORANGE, fill_opacity=0.3, stroke_width=0
        )

        # Region 5: Bottom region
        poly5 = Polygon(
            nodes[4].get_center(), nodes[5].get_center(),
            np.array([2.5, -2.5, 0]), np.array([0, -2.5, 0]),
            color=TEAL, fill_opacity=0.3, stroke_width=0
        )

        # Region 6: Bottom left region
        poly6 = Polygon(
            nodes[3].get_center(), nodes[4].get_center(),
            np.array([0, -2.5, 0]), np.array([-2.5, -2.5, 0]),
            np.array([-2.5, nodes[3].get_center()[1], 0]),
            color=ORANGE, fill_opacity=0.3, stroke_width=0
        )

        # Region 7: Top left region
        poly7 = Polygon(
            nodes[2].get_center(), nodes[3].get_center(),
            np.array([-2.5, nodes[3].get_center()[1], 0]),
            np.array([-2.5, 2.5, 0]),
            color=TEAL, fill_opacity=0.3, stroke_width=0
        )

        label = Text(
            "I(6,3)",
            font_size=50,
            color=WHITE
        )
        label.shift(DOWN * 3.3)

        # Animate the polygons
        self.play(FadeIn(poly1),
            FadeIn(poly2),
            FadeIn(poly3),
            FadeIn(poly4),
            FadeIn(poly5),
            FadeIn(poly6),
            FadeIn(poly7),
            Write(label),
        )

        excess = Text(
            "All vertices have degree 3"
            "\nand there are 3 faces,"
            "\nso total excess is 0",
            font_size=26,
            color=WHITE
        )
        excess.to_edge(LEFT)

        self.play(Write(excess))

        self.wait(3)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        final = Paragraph(
            "This video is based on a 1975 paper by André Bouchet.",
            "\nAnimation made using Manim, with coding assistance by Claude AI.",
            font_size=24,
            color=WHITE,
            alignment="center",
            line_spacing = 1
        )

        self.play(Write(final, run_time=2))

        self.wait(1)

        self.play(FadeOut(final))

        self.wait(0.5)

        goodbye = Paragraph(
            "Thanks for watching!",
            font_size=40,
            color=WHITE,
        )

        self.play(Write(goodbye), run_time=3.5)

        self.wait(2)
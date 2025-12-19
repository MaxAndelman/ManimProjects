from manim import *


class GraphComposition(Scene):
    def construct(self):
        intro = Paragraph(
            "We will prove this graph exists through induction."
            "\nThe inductive step requires a way to combine complete incidence graphs."
            "\nThese combinations are called compositions,"
            "\nand are defined as follows.",
            font_size=30,
            color=WHITE,
            alignment="center",
            line_spacing=1.1
        )
        self.play(Write(intro), run_time = 2.5)
        self.wait(5)
        self.play(FadeOut(intro))

        # Create two square frames side by side
        square1 = Square(side_length=4).shift(LEFT * 3.5)
        square2 = Square(side_length=4).shift(RIGHT * 3.5)

        # Create arrows for both squares
        # Left square arrows
        top_arrow1 = Arrow(start=LEFT * 3.5 + UP * 2 + LEFT * 0.5, end=LEFT * 3.5 + UP * 2 + RIGHT * 0.5, buff=0, stroke_width=0)
        bottom_arrow1 = Arrow(start=LEFT * 3.5 + DOWN * 2 + LEFT * 0.5, end=LEFT * 3.5 + DOWN * 2 + RIGHT * 0.5, buff=0, stroke_width=0)
        left_arrow1a = Arrow(start=LEFT * 5.5 + UP * 0.8, end=LEFT * 5.5 + DOWN * 0.2, buff=0, stroke_width=0)
        left_arrow1b = Arrow(start=LEFT * 5.5 + UP * 0.2, end=LEFT * 5.5 + DOWN * 0.8, buff=0, stroke_width=0)
        right_arrow1a = Arrow(start=LEFT * 1.5 + UP * 0.8, end=LEFT * 1.5 + DOWN * 0.2, buff=0, stroke_width=0)
        right_arrow1b = Arrow(start=LEFT * 1.5 + UP * 0.2, end=LEFT * 1.5 + DOWN * 0.8, buff=0, stroke_width=0)

        # Right square arrows
        top_arrow2 = Arrow(start=RIGHT * 3.5 + UP * 2 + LEFT * 0.5, end=RIGHT * 3.5 + UP * 2 + RIGHT * 0.5, buff=0, stroke_width=0)
        bottom_arrow2 = Arrow(start=RIGHT * 3.5 + DOWN * 2 + LEFT * 0.5, end=RIGHT * 3.5 + DOWN * 2 + RIGHT * 0.5, buff=0, stroke_width=0)
        left_arrow2a = Arrow(start=RIGHT * 1.5 + UP * 0.8, end=RIGHT * 1.5 + DOWN * 0.2, buff=0, stroke_width=0)
        left_arrow2b = Arrow(start=RIGHT * 1.5 + UP * 0.2, end=RIGHT * 1.5 + DOWN * 0.8, buff=0, stroke_width=0)
        right_arrow2a = Arrow(start=RIGHT * 5.5 + UP * 0.8, end=RIGHT * 5.5 + DOWN * 0.2, buff=0, stroke_width=0)
        right_arrow2b = Arrow(start=RIGHT * 5.5 + UP * 0.2, end=RIGHT * 5.5 + DOWN * 0.8, buff=0, stroke_width=0)

        # Create vertices for left square
        vertex1_left = Dot(LEFT * 3.5 + UP * 1.2, color=BLUE, radius=0.12)
        vertex2_left = Dot(LEFT * 3.5 + DOWN * 0.8 + LEFT * 0.96, color=BLUE, radius=0.12)
        vertex3_left = Dot(LEFT * 3.5 + DOWN * 0.8 + RIGHT * 0.96, color=BLUE, radius=0.12)

        # Create vertices for right square
        vertex1_right = Dot(RIGHT * 3.5 + UP * 1.2, color=BLUE, radius=0.12)
        vertex2_right = Dot(RIGHT * 3.5 + DOWN * 0.8 + LEFT * 0.96, color=BLUE, radius=0.12)
        vertex3_right = Dot(RIGHT * 3.5 + DOWN * 0.8 + RIGHT * 0.96, color=BLUE, radius=0.12)

        # Create triangle edges for left square
        edge1_left = Line(vertex1_left.get_center(), vertex2_left.get_center(), color=YELLOW)
        edge2_left = Line(vertex2_left.get_center(), vertex3_left.get_center(), color=YELLOW)
        edge3_left = Line(vertex3_left.get_center(), vertex1_left.get_center(), color=YELLOW)

        # Create triangle edges for right square
        edge1_right = Line(vertex1_right.get_center(), vertex2_right.get_center(), color=YELLOW)
        edge2_right = Line(vertex2_right.get_center(), vertex3_right.get_center(), color=YELLOW)
        edge3_right = Line(vertex3_right.get_center(), vertex1_right.get_center(), color=YELLOW)

        # Create wrap-around lines for left square
        direction1_left = vertex1_left.get_center() - vertex2_left.get_center()
        direction2_left = vertex1_left.get_center() - vertex3_left.get_center()
        slope1_left = direction1_left / np.linalg.norm(direction1_left)
        slope2_left = direction2_left / np.linalg.norm(direction2_left)

        t1_left = ((LEFT * 3.5 + DOWN * 2)[1] - vertex2_left.get_center()[1]) / direction1_left[1]
        bottom_intersect1_left = vertex2_left.get_center() + direction2_left * t1_left
        t_top1_left = (vertex1_left.get_center()[1] - (LEFT * 3.5 + UP * 2)[1]) / slope1_left[1]
        top_start1_left = vertex1_left.get_center() - t_top1_left * slope1_left

        t2_left = ((LEFT * 3.5 + DOWN * 2)[1] - vertex3_left.get_center()[1]) / direction2_left[1]
        bottom_intersect2_left = vertex3_left.get_center() + direction1_left * t2_left
        t_top2_left = (vertex1_left.get_center()[1] - (LEFT * 3.5 + UP * 2)[1]) / slope2_left[1]
        top_start2_left = vertex1_left.get_center() - t_top2_left * slope2_left

        wrap_line1_left = VGroup(
            Line(vertex2_left.get_center(), bottom_intersect1_left, color=RED),
            Line(top_start1_left, vertex1_left.get_center(), color=RED)
        )
        wrap_line2_left = VGroup(
            Line(vertex3_left.get_center(), bottom_intersect2_left, color=RED),
            Line(top_start2_left, vertex1_left.get_center(), color=RED)
        )

        # Create wrap-around lines for right square
        direction1_right = vertex1_right.get_center() - vertex2_right.get_center()
        direction2_right = vertex1_right.get_center() - vertex3_right.get_center()
        slope1_right = direction1_right / np.linalg.norm(direction1_right)
        slope2_right = direction2_right / np.linalg.norm(direction2_right)

        t1_right = ((RIGHT * 3.5 + DOWN * 2)[1] - vertex2_right.get_center()[1]) / direction1_right[1]
        bottom_intersect1_right = vertex2_right.get_center() + direction2_right * t1_right
        t_top1_right = (vertex1_right.get_center()[1] - (RIGHT * 3.5 + UP * 2)[1]) / slope1_right[1]
        top_start1_right = vertex1_right.get_center() - t_top1_right * slope1_right

        t2_right = ((RIGHT * 3.5 + DOWN * 2)[1] - vertex3_right.get_center()[1]) / direction2_right[1]
        bottom_intersect2_right = vertex3_right.get_center() + direction1_right * t2_right
        t_top2_right = (vertex1_right.get_center()[1] - (RIGHT * 3.5 + UP * 2)[1]) / slope2_right[1]
        top_start2_right = vertex1_right.get_center() - t_top2_right * slope2_right

        wrap_line1_right = VGroup(
            Line(vertex2_right.get_center(), bottom_intersect1_right, color=RED),
            Line(top_start1_right, vertex1_right.get_center(), color=RED)
        )
        wrap_line2_right = VGroup(
            Line(vertex3_right.get_center(), bottom_intersect2_right, color=RED),
            Line(top_start2_right, vertex1_right.get_center(), color=RED)
        )

        # Create horizontal wrap-around lines for both squares
        left_intersect_left = np.array([-5.5, vertex1_left.get_center()[1], 0])
        right_intersect_left = np.array([-1.5, vertex1_left.get_center()[1], 0])
        wrap_line_horizontal_left = VGroup(
            Line(vertex1_left.get_center(), left_intersect_left, color=RED),
            Line(right_intersect_left, vertex1_left.get_center(), color=RED)
        )

        left_intersect_right = np.array([1.5, vertex1_right.get_center()[1], 0])
        right_intersect_right = np.array([5.5, vertex1_right.get_center()[1], 0])
        wrap_line_horizontal_right = VGroup(
            Line(vertex1_right.get_center(), left_intersect_right, color=RED),
            Line(right_intersect_right, vertex1_right.get_center(), color=RED)
        )

        lower_left_intersect_right = np.array([1.5, vertex2_right.get_center()[1], 0])
        lower_right_intersect_right = np.array([5.5, vertex2_right.get_center()[1], 0])
        lower_wrap_line_horizontal_right = VGroup(
            Line(vertex2_right.get_center(), lower_left_intersect_right, color=RED),
            Line(lower_right_intersect_right, vertex3_right.get_center(), color=RED)
        )

        # Create regions for left square
        region1_left = Polygon(
            vertex1_left.get_center(), vertex2_left.get_center(), vertex3_left.get_center(),
            fill_color=BLUE, fill_opacity=0.3, stroke_width=0
        )

        region2_left = Polygon(
            np.array([-5.5, 2, 0]), top_start2_left, vertex1_left.get_center(), left_intersect_left,
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region3_left = Polygon(
            np.array([-1.5, 2, 0]), top_start1_left, vertex1_left.get_center(), right_intersect_left,
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region4_left = Polygon(
            vertex2_left.get_center(), bottom_intersect1_left, np.array([-5.5, -2, 0]),
            np.array([-5.5, vertex1_left.get_center()[1], 0]), left_intersect_left, vertex1_left.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region5_left = Polygon(
            vertex1_left.get_center(), right_intersect_left, np.array([-1.5, vertex1_left.get_center()[1], 0]),
            np.array([-1.5, -2, 0]), bottom_intersect2_left, vertex3_left.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region6_left = Polygon(
            vertex2_left.get_center(), vertex3_left.get_center(), bottom_intersect2_left, bottom_intersect1_left,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        region7_left = Polygon(
            vertex1_left.get_center(), top_start1_left, top_start2_left,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        # Create regions for right square
        region1_right = Polygon(
            vertex1_right.get_center(), vertex2_right.get_center(), vertex3_right.get_center(),
            fill_color=BLUE, fill_opacity=0.3, stroke_width=0
        )

        region2_right = Polygon(
            np.array([1.5, 2, 0]), top_start2_right, vertex1_right.get_center(), left_intersect_right,
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region3_right = Polygon(
            np.array([5.5, 2, 0]), top_start1_right, vertex1_right.get_center(), right_intersect_right,
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region4_right = Polygon(
            vertex2_right.get_center(), bottom_intersect1_right, np.array([1.5, -2, 0]),
            lower_left_intersect_right, # vertex1_right.get_center(), np.array([1.5, vertex1_right.get_center()[1], 0]),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region5_right = Polygon(
            lower_right_intersect_right, # np.array([5.5, vertex1_right.get_center()[1], 0]),
            np.array([5.5, -2, 0]), bottom_intersect2_right, vertex3_right.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        region6_right = Polygon(
            vertex2_right.get_center(), vertex3_right.get_center(), bottom_intersect2_right, bottom_intersect1_right,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        region7_right = Polygon(
            vertex1_right.get_center(), top_start1_right, top_start2_right,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        region8_right = Polygon(
            vertex1_right.get_center(), vertex2_right.get_center(), lower_left_intersect_right, left_intersect_right,
            fill_color=RED, fill_opacity=0.3, stroke_width=0
        )

        region9_right = Polygon(
            vertex1_right.get_center(), vertex3_right.get_center(), lower_right_intersect_right, right_intersect_right,
            fill_color=RED, fill_opacity=0.3, stroke_width=0
        )

        # Create labels for vertices
        label1_left = Text("1", font_size=24, color=WHITE).next_to(vertex1_left, UP, buff=0.15)
        label2_left = Text("2", font_size=24, color=WHITE).next_to(vertex2_left, DOWN + LEFT, buff=0.15)
        label3_left = Text("3", font_size=24, color=WHITE).next_to(vertex3_left, DOWN + RIGHT, buff=0.15)

        label1_right = Text("1", font_size=24, color=WHITE).next_to(vertex1_right, UP, buff=0.15)
        label2_right = Text("2", font_size=24, color=WHITE).next_to(vertex2_right, DOWN + LEFT, buff=0.15)
        label3_right = Text("3", font_size=24, color=WHITE).next_to(vertex3_right, DOWN + RIGHT, buff=0.15)

        rect_label_left = Text(
            "I(3,3)",
            color=WHITE,
            font_size=36,
        )
        rect_label_left.shift(DOWN * 2.8 + LEFT * 3.5)

        rect_label_right = Text(
            "I(3,4)",
            color=WHITE,
            font_size=36,
        )
        rect_label_right.shift(RIGHT * 3.5 + DOWN * 2.8)

        explanation1 = Text(
            "Take two complete incident graphs with the same number of vertices.",
            color=WHITE,
            font_size=30,
        )
        explanation1.to_edge(UP)

        # Animate everything
        self.play(
            Create(square1), Create(square2),
            Create(top_arrow1), Create(bottom_arrow1),
            Create(left_arrow1a), Create(left_arrow1b),
            Create(right_arrow1a), Create(right_arrow1b),
            Create(top_arrow2), Create(bottom_arrow2),
            Create(left_arrow2a), Create(left_arrow2b),
            Create(right_arrow2a), Create(right_arrow2b),
            FadeIn(vertex1_left), FadeIn(vertex2_left), FadeIn(vertex3_left),
            FadeIn(vertex1_right), FadeIn(vertex2_right), FadeIn(vertex3_right),
            Create(edge1_left), Create(edge2_left), Create(edge3_left),
            Create(wrap_line1_left), Create(wrap_line2_left),
            Create(edge1_right), Create(edge2_right), Create(edge3_right),
            Create(wrap_line1_right), Create(wrap_line2_right),
            Create(wrap_line_horizontal_left),
            Create(wrap_line_horizontal_right),
            Create(lower_wrap_line_horizontal_right),
            Create(region8_right), Create(region9_right),
            FadeIn(region1_left), FadeIn(region2_left), FadeIn(region3_left),
            FadeIn(region4_left), FadeIn(region5_left), FadeIn(region6_left), FadeIn(region7_left),
            FadeIn(region1_right), FadeIn(region2_right), FadeIn(region3_right),
            FadeIn(region4_right), FadeIn(region5_right), FadeIn(region6_right), FadeIn(region7_right),
            # FadeIn(label1_left), FadeIn(label2_left), FadeIn(label3_left),
            # FadeIn(label1_right), FadeIn(label2_right), FadeIn(label3_right),
            FadeIn(rect_label_left), FadeIn(rect_label_right),
            Write(explanation1)
        )
        self.wait(2)

        # Group all objects for scaling and moving
        all_objects_left = VGroup(
            square1, top_arrow1, bottom_arrow1, left_arrow1a, left_arrow1b, right_arrow1a, right_arrow1b,
            vertex1_left, vertex2_left, vertex3_left,
            edge1_left, edge2_left, edge3_left,
            wrap_line1_left, wrap_line2_left, wrap_line_horizontal_left,
            region1_left, region2_left, region3_left, region4_left, region5_left, region6_left, region7_left,
            label1_left, label2_left, label3_left, rect_label_left
        )

        all_objects_right = VGroup(
            square2, top_arrow2, bottom_arrow2, left_arrow2a, left_arrow2b, right_arrow2a, right_arrow2b,
            vertex1_right, vertex2_right, vertex3_right,
            edge1_right, edge2_right, edge3_right,
            wrap_line1_right, wrap_line2_right, wrap_line_horizontal_right, lower_wrap_line_horizontal_right,
            region1_right, region2_right, region3_right, region4_right, region5_right, region6_right, region7_right,
            region8_right, region9_right,
            label1_right, label2_right, label3_right, rect_label_right
        )

        # Scale down and move to top
        self.play(
            all_objects_left.animate.scale(0.5).move_to(LEFT * 3 + UP * 2),
            all_objects_right.animate.scale(0.5).move_to(RIGHT * 3 + UP * 2),
            FadeOut(explanation1)
        )
        self.wait(0.7)

        # Create three new points in the center/bottom area
        new_vertex1 = Dot(ORIGIN, color=BLUE, radius=0.12)
        new_vertex2 = Dot(DOWN * 2 + LEFT * 1.55, color=BLUE, radius=0.12)
        new_vertex3 = Dot(DOWN * 2 + RIGHT * 1.55, color=BLUE, radius=0.12)

        # Create labels for new vertices
        new_label1 = Text("1", font_size=24, color=WHITE).next_to(new_vertex1, UP, buff=0.15)
        new_label2 = Text("2", font_size=24, color=WHITE).next_to(new_vertex2, DOWN + LEFT, buff=0.15)
        new_label3 = Text("3", font_size=24, color=WHITE).next_to(new_vertex3, DOWN + RIGHT, buff=0.15)

        explanation2 = Paragraph(
            "Identify vertices on the originals.\nCreate a vertex on the new graph for each identified pair.",
            font_size=28,
            color=WHITE,
            alignment="center"
        )
        explanation2.shift(DOWN * 3.3)

        # Animate new points and labels
        self.play(
            FadeIn(new_vertex1), FadeIn(new_vertex2), FadeIn(new_vertex3),
            FadeIn(new_label1), FadeIn(new_label2), FadeIn(new_label3),
            Write(explanation2)
        )
        self.wait(3.5)

        explanation3 = Paragraph(
            "For each pair of vertices on the composition, including a vertex and itself,"
            "\nconnect those vertices a number of times equal to the total number of connections"
            "\nbetween those vertices on the two original graphs.",
            font_size=24,
            color=WHITE,
            alignment="center"
        )
        explanation3.shift(DOWN * 3.3)

        self.play(FadeOut(explanation2, run_time=0.5), Write(explanation3, run_time=3))

        self.wait(5)

        explanation4 = Text(
            "Both graphs have a loop\nfrom 1 to itself, so\n1 has two self-connections\nin the composition",
            font_size=24,
            color=WHITE,
        )
        explanation4.to_edge(RIGHT)
        explanation4.shift(DOWN)

        # Highlight pairs of numbers (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)
        # Pair (1,1) - highlight all points labeled "1" and draw 2 self-loops
        self.play(
            vertex1_left.animate.set_color(RED).scale(1.5),
            vertex1_right.animate.set_color(RED).scale(1.5),
            new_vertex1.animate.set_color(RED).scale(1.5),
        )

        # Draw 2 self-loops on new_vertex1
        loop1_11 = Circle(radius=0.4, color=GREEN, stroke_width=3).move_to(
            new_vertex1.get_center() + LEFT * 0.45 + UP * 0.1)
        loop2_11 = Circle(radius=0.4, color=GREEN, stroke_width=3).move_to(
            new_vertex1.get_center() + RIGHT * 0.45 + UP * 0.1)

        self.play(Create(loop1_11), Create(loop2_11), Write(explanation4))
        self.wait(1)
        self.play(
            vertex1_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex1_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex1.animate.set_color(BLUE).scale(1 / 1.5)
        )
        # Pair (1,2) - highlight all points labeled "1" and "2" and draw 4 curves
        self.play(
            vertex1_left.animate.set_color(RED).scale(1.5),
            vertex1_right.animate.set_color(RED).scale(1.5),
            new_vertex1.animate.set_color(RED).scale(1.5),
            vertex2_left.animate.set_color(RED).scale(1.5),
            vertex2_right.animate.set_color(RED).scale(1.5),
            new_vertex2.animate.set_color(RED).scale(1.5),
            FadeOut(explanation4)
        )

        explanation5 = Text(
            "Both graphs have two\nedges from 1 to 2,\nso 1 and 2 are connected\nfour times in the composition",
            font_size=24,
            color=WHITE,
        )
        explanation5.to_edge(LEFT)
        explanation5.shift(DOWN)


        # Draw 4 curves between new_vertex1 and new_vertex2 (well separated, no arrows)
        curve1_12 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex2.get_center(), angle=-1, color=GREEN,
                                     stroke_width=3)
        curve2_12 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex2.get_center(), angle=-0.4, color=GREEN,
                                     stroke_width=3)
        curve3_12 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex2.get_center(), angle=0.4, color=GREEN,
                                     stroke_width=3)
        curve4_12 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex2.get_center(), angle=1, color=GREEN,
                                     stroke_width=3)

        self.play(Create(curve1_12), Create(curve2_12), Create(curve3_12), Create(curve4_12), Write(explanation5))
        self.wait(1)
        self.play(
            vertex1_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex1_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex1.animate.set_color(BLUE).scale(1 / 1.5),
            vertex2_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex2_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex2.animate.set_color(BLUE).scale(1 / 1.5)
        )

        # Pair (1,3) - highlight all points labeled "1" and "3" and draw 4 curves
        self.play(
            vertex1_left.animate.set_color(RED).scale(1.5),
            vertex1_right.animate.set_color(RED).scale(1.5),
            new_vertex1.animate.set_color(RED).scale(1.5),
            vertex3_left.animate.set_color(RED).scale(1.5),
            vertex3_right.animate.set_color(RED).scale(1.5),
            new_vertex3.animate.set_color(RED).scale(1.5),
            FadeOut(explanation5)
        )

        # Draw 4 curves between new_vertex1 and new_vertex3 (well separated, no arrows)
        curve1_13 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex3.get_center(), angle=-1, color=GREEN,
                                     stroke_width=3)
        curve2_13 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex3.get_center(), angle=-0.4, color=GREEN,
                                     stroke_width=3)
        curve3_13 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex3.get_center(), angle=0.4, color=GREEN,
                                     stroke_width=3)
        curve4_13 = ArcBetweenPoints(new_vertex1.get_center(), new_vertex3.get_center(), angle=1, color=GREEN,
                                     stroke_width=3)

        self.play(Create(curve1_13), Create(curve2_13), Create(curve3_13), Create(curve4_13))
        self.wait(1)
        self.play(
            vertex1_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex1_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex1.animate.set_color(BLUE).scale(1 / 1.5),
            vertex3_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex3_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex3.animate.set_color(BLUE).scale(1 / 1.5)
        )

        explanation6 = Text(
            "Neither graph has a\nself-connection from\n2 to 2, so the\ncomposition doesn't either",
            font_size=24,
            color=WHITE,
        )
        explanation6.to_edge(LEFT)
        explanation6.shift(DOWN)

        # Pair (2,2) - highlight all points labeled "2" and draw no curves
        self.play(
            vertex2_left.animate.set_color(RED).scale(1.5),
            vertex2_right.animate.set_color(RED).scale(1.5),
            new_vertex2.animate.set_color(RED).scale(1.5),
            Write(explanation6)
        )
        self.wait(1)
        self.play(
            vertex2_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex2_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex2.animate.set_color(BLUE).scale(1 / 1.5)
        )

        explanation7 = Text(
            "I(3,3) has one edge\nfrom 2 to 3,\nand I(4,3) has two, so\nthe composition has 3",
            font_size=24,
            color=WHITE,
        )
        explanation7.to_edge(LEFT)
        explanation7.shift(DOWN)

        # Pair (2,3) - highlight all points labeled "2" and "3" and draw 3 curves
        self.play(
            vertex2_left.animate.set_color(RED).scale(1.5),
            vertex2_right.animate.set_color(RED).scale(1.5),
            new_vertex2.animate.set_color(RED).scale(1.5),
            vertex3_left.animate.set_color(RED).scale(1.5),
            vertex3_right.animate.set_color(RED).scale(1.5),
            new_vertex3.animate.set_color(RED).scale(1.5),
            LaggedStart(FadeOut(explanation6, run_time=0.5), Write(explanation7), lag_ratio=0.5)
        )

        # Draw 3 curves between new_vertex2 and new_vertex3 (well separated, no arrows)
        curve1_23 = ArcBetweenPoints(new_vertex2.get_center(), new_vertex3.get_center(), angle=-0.6, color=GREEN,
                                     stroke_width=3)
        curve2_23 = ArcBetweenPoints(new_vertex2.get_center(), new_vertex3.get_center(), angle=0, color=GREEN,
                                     stroke_width=3)
        curve3_23 = ArcBetweenPoints(new_vertex2.get_center(), new_vertex3.get_center(), angle=0.6, color=GREEN,
                                     stroke_width=3)

        self.play(Create(curve1_23), Create(curve2_23), Create(curve3_23))
        self.wait(1)
        self.play(
            vertex2_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex2_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex2.animate.set_color(BLUE).scale(1 / 1.5),
            vertex3_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex3_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex3.animate.set_color(BLUE).scale(1 / 1.5)
        )

        # Pair (3,3) - highlight all points labeled "3" and draw no curves
        self.play(
            FadeOut(explanation7),
            vertex3_left.animate.set_color(RED).scale(1.5),
            vertex3_right.animate.set_color(RED).scale(1.5),
            new_vertex3.animate.set_color(RED).scale(1.5)
        )
        self.wait(1)
        final_label = Text(
            "I(4,3) + I(3,3)",
            color=WHITE,
            font_size=36,
        )
        final_label.shift(DOWN * 2.8)

        self.play(
            FadeOut(explanation3, run_time=0.5),
            vertex3_left.animate.set_color(BLUE).scale(1 / 1.5),
            vertex3_right.animate.set_color(BLUE).scale(1 / 1.5),
            new_vertex3.animate.set_color(BLUE).scale(1 / 1.5),
            Write(final_label),
        )

        self.wait(1.7)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        final = Paragraph(
            "Composition has some important properties:\n"
            "\n1. I(m,n1) + I(m,n2) can be embedded on the surface formed\n"
            "by the connected sums of the surfaces they are embedded on\n"
            "\n2. Total excess adds across composition",
            font_size=24,
            color=WHITE,
            alignment="center",
            line_spacing = 1
        )
        final.shift(UP * 2)

        self.play(Write(final), duration=3)

        final1 = Paragraph(
            "These properties can be used to show that"
            "\nif I(6,n) with total excess 0 exists,"
            "I(6,n+1) = I(6,n) + I(6,3)"
            "\nand I(6,n+1) has excess 0."
            "\nBy duality, I(n,6) also exists for all n.",
            font_size=24,
            color=WHITE,
            alignment="center",
            line_spacing = 1
        )
        final1.shift(DOWN)

        self.play(Write(final1), duration=3)

        self.wait(8)

        final2 = Paragraph(
            "From there, it can be shown that if I(m,n)"
            "\nexists with e ≤ 3, I(m,n+4) exists"
            "\nwith e ≤ 3 because it is I(m,n+4) + I(m,6)."
            "\nThen, because of the duality symmetry,"
            "\nto show the genus of K(m,n) is the ceiling of"
            "\n(m-2)(n-2)/4 for all m,n ≥ 2,"
            "\nwe only need that such an I(m,n) exists"
            "\nfor the 8 unordered paris (m,n), 2 ≤ m,n ≤ 5",
            font_size=24,
            color=WHITE,
            alignment="center",
            line_spacing = 1
        )

        self.play(FadeOut(final1, run_time=0.5), FadeOut(final,run_time=0.5), Write(final2, run_time=4))
        self.wait(8)
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
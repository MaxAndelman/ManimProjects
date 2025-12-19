from manim import *


class CompleteIncidenceGraph(Scene):
    def construct(self):

        intro = Text(
            "To figure this out, let's reframe in terms of complete incidence graphs.",
            font_size=30,
            color=WHITE
        )
        intro.shift(UP* 0.8)

        definition = Paragraph(
            "Definition:\nA complete incidence graph is an embedded graph\nwhere all faces contain all vertices on their boundary."
            "\nThese graphs can include self-connections and multi-connections.\nI will denote one with v vertices and f faces I(v,f).",
            font_size=30,
            color=WHITE,
            alignment="center"
        )
        definition.shift(DOWN* 0.8)

        self.play(Write(intro), run_time = 1.8)
        self.wait(0.5)
        self.play(Write(definition), run_time = 2.5)
        self.wait(8)
        self.play(FadeOut(intro), FadeOut(definition))

        intro1 = Paragraph(
            "Let's look at I(3,3) on the familiar square torus\nto see the connection",
            font_size=36,
            color=WHITE,
            alignment="center"
        )

        self.play(Write(intro1), run_time = 1)
        self.wait(1.3)
        self.play(FadeOut(intro1))

        # Create a square frame
        square = Square(side_length=5)

        top_arrow = Arrow(start=ORIGIN + UP * 2.5 + LEFT * 0.5, end=ORIGIN + UP * 2.5 + RIGHT * 0.5, buff=0, stroke_width=0)
        bottom_arrow = Arrow(start=ORIGIN + DOWN * 2.5 + LEFT * 0.5, end=ORIGIN + DOWN * 2.5 + RIGHT * 0.5, buff=0, stroke_width=0)
        left_arrow1 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.8, end=ORIGIN + LEFT * 2.5 + DOWN * 0.2, buff=0, stroke_width=0)
        left_arrow2 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.2, end=ORIGIN + LEFT * 2.5 + DOWN * 0.8, buff=0, stroke_width=0)
        right_arrow1 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.8, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.2, buff=0, stroke_width=0)
        right_arrow2 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.2, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.8, buff=0, stroke_width=0)

        self.wait()

        # Create triangle vertices
        vertex1 = Dot(ORIGIN + UP * 1.5, color=BLUE, radius=0.12)
        vertex2 = Dot(ORIGIN + DOWN * 1 + LEFT * 1.2, color=BLUE, radius=0.12)
        vertex3 = Dot(ORIGIN + DOWN * 1 + RIGHT * 1.2, color=BLUE, radius=0.12)

        self.play(
            Create(square),
            Create(top_arrow), Create(bottom_arrow),
            Create(left_arrow1), Create(left_arrow2),
            Create(right_arrow1), Create(right_arrow2)
        )

        self.wait()

        explanation1 = Text(
            "Start off with three vertices",
            font_size=36,
            color=WHITE
        )
        explanation1.to_edge(DOWN)
        explanation1.shift(UP * 0.4)

        # Animate vertices first
        self.play(
            FadeIn(vertex1), FadeIn(vertex2), FadeIn(vertex3), Write(explanation1, run_time = 1.5)
        )

        self.wait(2)

        # Create triangle edges as separate lines
        edge1 = Line(vertex1.get_center(), vertex2.get_center(), color=YELLOW)
        edge2 = Line(vertex2.get_center(), vertex3.get_center(), color=YELLOW)
        edge3 = Line(vertex3.get_center(), vertex1.get_center(), color=YELLOW)

        # Create torus wrap-around lines (from bottom vertices to top vertex)
        # Calculate the direction vector from vertex2 to vertex1
        direction1 = vertex1.get_center() - vertex2.get_center()
        # Calculate the direction vector from vertex3 to vertex1
        direction2 = vertex1.get_center() - vertex3.get_center()

        # Normalize to get the slope
        slope1 = direction1 / np.linalg.norm(direction1)

        # Find where this line intersects the bottom edge
        t1 = (ORIGIN[1] - 2.5 - vertex2.get_center()[1]) / direction1[1]
        bottom_intersect1 = vertex2.get_center() + direction2 * t1

        # Calculate top starting point: need to find point on top edge such that
        # the line from that point to vertex1 has the same slope
        # If we go from top edge to vertex1, we need: top_start1 + t * slope1 = vertex1
        # where top_start1[1] = 2.5
        t_top1 = (vertex1.get_center()[1] - (ORIGIN[1] + 2.5)) / slope1[1]
        top_start1 = vertex1.get_center() - t_top1 * slope1

        wrap_line1 = VGroup(
            Line(vertex2.get_center(), bottom_intersect1, color=RED),
            Line(top_start1, vertex1.get_center(), color=RED)
        )
        # Normalize to get the slope
        slope2 = direction2 / np.linalg.norm(direction2)

        # Find where this line intersects the bottom edge
        t2 = (ORIGIN[1] - 2.5 - vertex3.get_center()[1]) / direction2[1]
        bottom_intersect2 = vertex3.get_center() + direction1 * t2

        # Calculate top starting point with same slope
        t_top2 = (vertex1.get_center()[1] - (ORIGIN[1] + 2.5)) / slope2[1]
        top_start2 = vertex1.get_center() - t_top2 * slope2

        wrap_line2 = VGroup(
            Line(vertex3.get_center(), bottom_intersect2, color=RED),
            Line(top_start2, vertex1.get_center(), color=RED)
        )

        explanation2 = Text(
            "Add edges to separate it into 3 regions",
            font_size=34,
            color=WHITE
        )
        explanation2.to_edge(DOWN)
        explanation2.shift(UP * 0.2)

        # Animate triangle edges and wrap-around lines
        self.play(
             Create(edge1), Create(edge2), Create(edge3),
            Create(wrap_line1), Create(wrap_line2), LaggedStart(FadeOut(explanation1, run_time = .5), Write(explanation2, run_time=1.5), lag_ratio = 0.5)
        )

        self.wait(2)

        # Create horizontal wrap-around line from top vertex through left edge to right edge
        # This line goes horizontally from vertex1 to the left edge, then reappears on right edge
        left_intersect = np.array([-2.5, vertex1.get_center()[1], 0])
        right_intersect = np.array([2.5, vertex1.get_center()[1], 0])

        wrap_line_horizontal = VGroup(
            Line(vertex1.get_center(), left_intersect, color=RED),
            Line(right_intersect, vertex1.get_center(), color=RED)
        )

        line_vertical = Line((2, 2.5, 0), (2, -2.5, 0), color=PURPLE)

        explanation3 = Text(
            "It's not embedded yet because\nthis curve is a circle",
            font_size=30,
            color=WHITE
        )
        explanation3.to_edge(DOWN)

        self.play(Create(line_vertical), LaggedStart(FadeOut(explanation2, run_time = .5), Write(explanation3, run_time=1.5), lag_ratio = 0.5))

        self.wait(1.5)

        self.play(FadeOut(line_vertical))

        explanation4 = Text(
            "Add this self-connection\nto make the graph embedded",
            font_size=30,
            color=WHITE
        )
        explanation4.to_edge(DOWN)

        # Draw horizontal wrap line separately
        self.play(Create(wrap_line_horizontal), LaggedStart(FadeOut(explanation3, run_time = .5), Write(explanation4, run_time=1.5), lag_ratio = 0.5))

        self.wait(2.5)

        # Create polygons to fill all 7 regions
        # Region 1: Central triangle
        region1 = Polygon(
            vertex1.get_center(), vertex2.get_center(), vertex3.get_center(),
            fill_color=BLUE, fill_opacity=0.3, stroke_width=0
        )

        # Region 2: Top-left corner
        region2 = Polygon(
            np.array([-2.5, 2.5, 0]), top_start2, vertex1.get_center(), left_intersect,
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        # Region 3: Top-right corner
        region3 = Polygon(
            np.array([2.5, 2.5, 0]), top_start1, vertex1.get_center(), right_intersect,
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        # Region 4: Bottom-left region
        region4 = Polygon(
            vertex2.get_center(), bottom_intersect1, np.array([-2.5, -2.5, 0]),
            np.array([-2.5, vertex1.get_center()[1], 0]), left_intersect, vertex1.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        # Region 5: Bottom-right region
        region5 = Polygon(
            vertex1.get_center(), right_intersect, np.array([2.5, vertex1.get_center()[1], 0]),
            np.array([2.5, -2.5, 0]), bottom_intersect2, vertex3.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        # Region 6: Bottom center region (below triangle)
        region6 = Polygon(
            vertex2.get_center(), vertex3.get_center(), bottom_intersect2, bottom_intersect1,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        # Region 7: Top center region
        region7 = Polygon(
            vertex1.get_center(), top_start1, top_start2,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        explanation5 = Text(
            "Here are the three regions",
            font_size=36,
            color=WHITE
        )
        explanation5.to_edge(DOWN)
        explanation5.shift(UP * 0.3)

        # Animate filling all regions
        self.play(
            FadeIn(region1), FadeIn(region2), FadeIn(region3),
            FadeIn(region4), FadeIn(region5), FadeIn(region6), FadeIn(region7),
            LaggedStart(FadeOut(explanation4, run_time=.5), Write(explanation5, run_time=1), lag_ratio=0.5)
        )

        self.wait(1.8)

        # Create blue circles around vertices
        circle1 = Circle(radius=0.3, color=BLUE).move_to(vertex1.get_center())
        circle2 = Circle(radius=0.3, color=BLUE).move_to(vertex2.get_center())
        circle3 = Circle(radius=0.3, color=BLUE).move_to(vertex3.get_center())

        explanation6 = Text(
            "All vertices are surrounded by all faces,\nmaking this a complete incidence graph",
            font_size=28,
            color=WHITE
        )
        explanation6.to_edge(DOWN)

        # Animate vertices and circles, then fade out circles immediately
        self.play(
            LaggedStart(Create(circle1), Create(circle2), Create(circle3), lag_ratio=0.4),
            LaggedStart(FadeOut(explanation5, run_time=.5), Write(explanation6, run_time=3), lag_ratio=0.5)
        )
        self.play(
            FadeOut(circle1), FadeOut(circle2), FadeOut(circle3)
        )

        self.wait(2)

        explanation7 = Text(
            "The top vertex has degree 6\nwhile there are 3 faces",
            font_size=26,
            color=WHITE
        )
        explanation7.to_edge(LEFT)
        explanation7.shift(UP + LEFT * 0.5)

        explanation8 = Text(
            "We say that this vertex has\nexcess e(v) = 6 - 3 = 3\n\nThe total excess e,\nor sum of each vertex's excess,\nof this embedding is also 3\n",
            font_size=24,
            color=WHITE
        )
        explanation8.to_edge(LEFT)
        explanation8.shift(UP * -0.7 + LEFT * 0.5)

        explanation9 = Text(
            "In general, if each vertex\nhas degree d(v),\n\ne = Σ(v∈V) d(v) - VF",
            font_size=28,
            color=WHITE
        )
        explanation9.to_edge(RIGHT)
        explanation9.shift(UP * 0.6 + RIGHT * 0.5)

        # tex9 = MUathTex(
        #         #     "e = \sum_{v \in V} d(v) - VF",
        #         #     font_size=28,
        #         #     color=WHITE
        #         # )
        #         # tex9.to_edge(RIGHT)
        #         # tex9.shift(P * 0.6 + RIGHT * 0.5)

        self.play(Write(explanation7), run_time=2)
        self.wait(1.5)
        self.play(Write(explanation8), run_time=2)
        self.wait()
        self.play(Write(explanation9), run_time = 2)
        self.wait(7)
        self.play(FadeOut(explanation6), FadeOut(explanation7), FadeOut(explanation8), FadeOut(explanation9))

        # Add red points at the center of regions 1 and 6
        # Region 1 center: centroid of triangle
        region1_center = (vertex1.get_center() + vertex2.get_center() + vertex3.get_center()) / 3
        point_region1 = Dot(region1_center, color=RED, radius=0.12)

        # Region 6 center: centroid of the quadrilateral
        region6_center = (vertex2.get_center() + vertex3.get_center() + bottom_intersect2 + bottom_intersect1) / 4
        point_region6 = Dot(region6_center, color=RED, radius=0.12)

        # Add red points at all 4 corners
        corner_tl = Dot(np.array([-2.5, 2.5, 0]), color=RED, radius=0.12)
        corner_tr = Dot(np.array([2.5, 2.5, 0]), color=RED, radius=0.12)
        corner_bl = Dot(np.array([-2.5, -2.5, 0]), color=RED, radius=0.12)
        corner_br = Dot(np.array([2.5, -2.5, 0]), color=RED, radius=0.12)

        explanation10 = Text(
            "Let's look at the dual of this graph",
            font_size=36,
            color=WHITE
        )
        explanation10.to_edge(UP)

        self.play(Write(explanation10), run_time = 1.5)

        self.wait()

        explanation11 = Text(
            "Remember all 4 corners represent the same point on the torus",
            font_size=32,
            color=WHITE
        )
        explanation11.to_edge(DOWN)
        explanation11.shift(UP * 0.3)


        # Animate all red points
        self.play(
            FadeIn(point_region1), FadeIn(point_region6),
            FadeIn(corner_tl), FadeIn(corner_tr), FadeIn(corner_bl), FadeIn(corner_br),
            FadeIn(explanation11),
        )

        self.wait(2.5)

        # Add 7 green lines
        # 1. Between two center red dots
        line_center_to_center = Line(region1_center, region6_center, color=GREEN)

        # 2-3. From region1_center to bottom corners
        line_r1_to_bl = Line(region1_center, corner_bl.get_center(), color=GREEN)
        line_r1_to_br = Line(region1_center, corner_br.get_center(), color=GREEN)

        # 4-5. From region6_center to bottom corners
        line_r6_to_bl = Line(region6_center, corner_bl.get_center(), color=GREEN)
        line_r6_to_br = Line(region6_center, corner_br.get_center(), color=GREEN)

        # 6-7. Along the sides of the box between top and bottom red corners
        line_left_side = Line(corner_tl.get_center(), corner_bl.get_center(), color=GREEN)
        line_right_side = Line(corner_tr.get_center(), corner_br.get_center(), color=GREEN)

        explanation12 = Text(
            "Connect adjacent faces a number of times\nequal to the number of edges they share",
            font_size=26,
            color=WHITE
        )
        explanation12.to_edge(DOWN)

        # Animate all green lines
        self.play(
            Create(line_center_to_center),
            Create(line_r1_to_bl), Create(line_r1_to_br),
            Create(line_r6_to_bl), Create(line_r6_to_br),
            # Create(line_left_side), Create(line_right_side),
            FadeOut(explanation10, run_time = .5),
            LaggedStart(FadeOut(explanation11, run_time=.5), Write(explanation12, run_time=3), lag_ratio=0.5)
        )

        explanation13 = Text(
            "Don't forget the\nself-connection",
            font_size=26,
            color=WHITE
        )
        explanation13.to_edge(LEFT)
        explanation13.shift(UP + RIGHT * 0.5)

        self.play(
        Create(line_left_side), Create(line_right_side),
             Write(explanation13, run_time = 1.5)
        )

        self.wait(2.5)

        # REMOVE ALL LINES
        self.play(
            FadeOut(edge1), FadeOut(edge2), FadeOut(edge3),
            FadeOut(wrap_line1), FadeOut(wrap_line2),
            FadeOut(wrap_line_horizontal), FadeOut(explanation13),
        )

        self.wait(2)

        # Create new regions bounded by the green lines
        # Region A: Triangle formed by region1_center and bottom two corners
        new_region1 = Polygon(
            region1_center, corner_bl.get_center(), region6_center,
            fill_color=YELLOW, fill_opacity=0.3, stroke_width=0
        )

        new_region2 = Polygon(
            region1_center, region6_center, corner_br.get_center(),
            fill_color=BLUE, fill_opacity=0.3, stroke_width=0
        )

        # Region B: Top
        new_region3 = Polygon(
            corner_tl.get_center(), corner_bl.get_center(), region1_center, corner_br.get_center(), corner_tr.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        # Region C: Bottom
        new_region4 = Polygon(
    region6_center,corner_br.get_center(), corner_bl.get_center(),
            fill_color=PURPLE, fill_opacity=0.3, stroke_width=0
        )

        # Animate the new regions
        self.play(
            FadeOut(region1), FadeOut(region2), FadeOut(region3),
            FadeOut(region4), FadeOut(region5), FadeOut(region6), FadeOut(region7),
            FadeIn(new_region1), FadeIn(new_region2),
            FadeIn(new_region3), FadeIn(new_region4)
        )

        self.wait()

        # Create red circles around vertices
        rcircle1 = Circle(radius=0.3, color=RED).move_to(region6_center)
        rcircle2 = Circle(radius=0.3, color=RED).move_to(region1_center)
        rcircle3 = Circle(radius=0.3, color=RED).move_to(corner_bl.get_center())
        rcircle4 = Circle(radius=0.3, color=RED).move_to(corner_br.get_center())

        explanation14 = Text(
            "This is also a complete incidence graph",
            font_size=30,
            color=WHITE
        )
        explanation14.to_edge(DOWN)

        explanation15 = Text(
            "In general, the dual of I(m,n) is I(n,m)",
            font_size=36,
            color=WHITE
        )
        explanation15.to_edge(UP)

        # Animate vertices and circles, then fade out circles immediately
        self.play(
            LaggedStart(Create(rcircle1), Create(rcircle2), Create(rcircle3), Create(rcircle4), lag_ratio=0.4),
            LaggedStart(FadeOut(explanation12, run_time=.5), Write(explanation14, run_time=3), lag_ratio=0.5)
        )
        self.play(
            FadeOut(rcircle1), FadeOut(rcircle2), FadeOut(rcircle3), FadeOut(rcircle4), Write(explanation15, run_time=1.5)
        )

        self.wait(2)

        # Reset to before dual
        self.play(
            FadeOut(line_center_to_center),
            FadeOut(line_r1_to_bl), FadeOut(line_r1_to_br),
            FadeOut(line_r6_to_bl), FadeOut(line_r6_to_br),
            FadeOut(new_region1), FadeOut(new_region2),
            FadeOut(new_region3), FadeOut(new_region4),
            FadeOut(line_left_side), FadeOut(line_right_side),
            FadeIn(region1), FadeIn(region2), FadeIn(region3),
            FadeIn(region4), FadeIn(region5), FadeIn(region6), FadeIn(region7)
        )

        # Connect all 3 blue vertices to the center dot (region1)
        line_v1_to_center = Line(vertex1.get_center(), region1_center, color=YELLOW)
        line_v2_to_center = Line(vertex2.get_center(), region1_center, color=YELLOW)
        line_v3_to_center = Line(vertex3.get_center(), region1_center, color=YELLOW)

        # Connect vertex2 and vertex3 to region6 dot directly
        line_v2_to_r6 = Line(vertex2.get_center(), region6_center, color=YELLOW)
        line_v3_to_r6 = Line(vertex3.get_center(), region6_center, color=YELLOW)

        # Connect vertex1 to region6 dot wrapping over the top
        # Calculate direction from vertex1 to region6 (wrapping upward)
        direction_v1_r6 = region6_center - vertex1.get_center()
        # We want to go up and wrap over the top
        # Going upward from vertex1
        top_edge_y = 2.5

        # Calculate intersection with top edge going from vertex1 upward toward region6
        # We need to find where line from v1 toward r6 (wrapping) hits top edge
        # Since we're wrapping vertically, the x-coordinate stays roughly the same
        # but we exit at top and enter at bottom

        # Line segment from vertex1 going up to top edge
        top_intersect_v1 = np.array([vertex1.get_center()[0], top_edge_y, 0])

        # Line segment from bottom edge coming down to region6
        bottom_edge_y = -2.5
        bottom_start_v1 = np.array([vertex1.get_center()[0], bottom_edge_y, 0])

        wrap_line_v1_to_r6 = VGroup(
            Line(vertex1.get_center(), top_intersect_v1, color=RED),
            Line(bottom_start_v1, region6_center, color=RED)
        )

        # Connect left blue dot (vertex2) to bottom-left red corner
        line_v2_to_bl = Line(vertex2.get_center(), corner_bl.get_center(), color=YELLOW)

        # Connect right blue dot (vertex3) to bottom-right red corner
        line_v3_to_br = Line(vertex3.get_center(), corner_br.get_center(), color=YELLOW)

        # Connect top blue dot (vertex1) to top-right red corner
        line_v1_to_tr = Line(vertex1.get_center(), corner_tr.get_center(), color=YELLOW)

        explanation16 = Text(
            "The incidence condition\nmeans all red dots can be\nconnected to all blue dots\nin a graph embedded\non the same surface",
            font_size=24,
            color=WHITE
        )
        explanation16.to_edge(LEFT)

        # Animate all connections
        self.play(
            Create(line_v1_to_center), Create(line_v2_to_center), Create(line_v3_to_center),
            Create(line_v2_to_r6), Create(line_v3_to_r6),
            Create(wrap_line_v1_to_r6),
            Create(line_v2_to_bl), Create(line_v3_to_br), Create(line_v1_to_tr), FadeOut(explanation14),
            LaggedStart(FadeOut(explanation15, run_time=.5), Write(explanation16, run_time=3), lag_ratio=0.5)
        )

        self.wait(3)

        explanation17 = Text(
            "The graph formed by doing this is K(m,n)",
            font_size=36,
            color=WHITE
        )
        explanation17.to_edge(UP)

        self.play(Write(explanation17))

        self.wait(2)

        # Animate fading out regions
        self.play(
            FadeOut(region1), FadeOut(region2), FadeOut(region3),
            FadeOut(region4), FadeOut(region5), FadeOut(region6), FadeOut(region7)
        )

        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        final = Paragraph(
            "Now we just need two more things:\n"
            "\n1. The genus of the surface I(m,n) is embedded on"
            "\n2. Proof that I(m,n) always exists for all m,n ≥ 2",
            font_size=28,
            color=WHITE,
            alignment="center"
        )

        self.play(Write(final))
        self.wait(3)
        self.play(FadeOut(final))
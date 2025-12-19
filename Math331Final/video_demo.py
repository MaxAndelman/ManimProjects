from manim import *
import numpy as np


class VideoDemo(Scene):
    def construct(self):
        # Create a square frame
        square = Square(side_length=5)

        top_arrow = Arrow(start=ORIGIN + UP * 2.5 + LEFT * 0.5, end=ORIGIN + UP * 2.5 + RIGHT * 0.5, buff=0, stroke_width=0)
        bottom_arrow = Arrow(start=ORIGIN + DOWN * 2.5 + LEFT * 0.5, end=ORIGIN + DOWN * 2.5 + RIGHT * 0.5, buff=0, stroke_width=0)
        left_arrow1 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.8, end=ORIGIN + LEFT * 2.5 + DOWN * 0.2, buff=0, stroke_width=0)
        left_arrow2 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.2, end=ORIGIN + LEFT * 2.5 + DOWN * 0.8, buff=0, stroke_width=0)
        right_arrow1 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.8, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.2, buff=0, stroke_width=0)
        right_arrow2 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.2, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.8, buff=0, stroke_width=0)

        self.play(
            Create(square),
            Create(top_arrow), Create(bottom_arrow),
            Create(left_arrow1), Create(left_arrow2),
            Create(right_arrow1), Create(right_arrow2)
        )

        # Radius for hexagon
        radius = 1.8
        colors = [RED, BLUE, RED, BLUE, RED, BLUE]

        nodes = []
        for k, theta in enumerate(np.linspace(0, 2 * np.pi, 6, endpoint=False)):
            pos = radius * np.array([np.cos(theta), np.sin(theta), 0])
            node = Dot(pos, color=colors[k], radius=0.12)
            nodes.append(node)

        for node in nodes:
            self.play(FadeIn(node), run_time=0.2)

        edges = [(i, (i + 1) % 6) for i in range(6)]
        for i, j in edges:
            self.play(Create(Line(nodes[i].get_center(), nodes[j].get_center())), run_time=0.2)

        # Recompute midpoints
        bottom_mid = square.get_bottom()
        top_mid = square.get_top()
        left_mid = square.get_left()
        right_mid = square.get_right()

        # Yellow lines (two-segment chains, drawn without pause)
        y0 = Line(nodes[3].get_center(), nodes[0].get_center(), color=YELLOW)

        # y1, y2 (outside path, two segments)
        y1 = Line(nodes[5].get_center(), bottom_mid, color=YELLOW)
        y2 = Line(top_mid, nodes[2].get_center(), color=YELLOW)

        # y3, y4 (outside path, two segments)
        y3 = Line(nodes[4].get_center(), left_mid, color=YELLOW)
        y4 = Line(right_mid, nodes[1].get_center(), color=YELLOW)

        # Draw y0
        self.play(Create(y0))
        self.play(LaggedStart(Create(y1), Create(y2), lag_ratio=.45))
        self.play(LaggedStart(Create(y3), Create(y4), lag_ratio=.45))

        # Add K_{3,3} label at the top
        k33_label = Text("K₃,₃", font_size=60).to_edge(UP)
        self.play(Write(k33_label))
        self.wait(0.5)

        # Highlight the two regions separated by y0
        # Region colors - 8 total (2 trapezoids + 6 outer shapes)
        region_colors = [TEAL, MAROON]

        # 2 TRAPEZOIDS INSIDE THE HEXAGON (divided by y0)
        # Upper trapezoid: nodes 0, 1, 2 and back through center (y0 line)
        trapezoid_upper = Polygon(
            nodes[0].get_center(),
            nodes[1].get_center(),
            nodes[2].get_center(),
            nodes[3].get_center(),  # Following y0 back
            fill_color=region_colors[0],
            fill_opacity=0.2,
            stroke_width=0
        )

        # Lower trapezoid: nodes 3, 4, 5 and back through center (y0 line)
        trapezoid_lower = Polygon(
            nodes[3].get_center(),
            nodes[4].get_center(),
            nodes[5].get_center(),
            nodes[0].get_center(),  # Following y0 back
            fill_color=region_colors[1],
            fill_opacity=0.2,
            stroke_width=0
        )

        # Region 3: The area inside the square but outside the hexagon
        # Create a square with a hexagon cut out
        square_filled = Square(side_length=5, fill_color=ORANGE, fill_opacity=0.15, stroke_width=0)

        # Create hexagon polygon to subtract
        hexagon_points = [node.get_center() for node in nodes]
        hexagon_filled = Polygon(*hexagon_points, fill_color=BLACK, fill_opacity=1, stroke_width=0)

        # Use Difference to cut out hexagon from square
        region3 = Difference(square_filled, hexagon_filled, fill_color=ORANGE, fill_opacity=0.15, stroke_width=0)

        self.play(FadeIn(trapezoid_upper), FadeIn(trapezoid_lower))
        self.play(FadeIn(region3))
        self.wait(1)

        # Remove the outside region
        self.play(FadeOut(region3))

        # Add red dots at the corners of the square
        corner_dots = []
        corners = [
            square.get_corner(UL),
            square.get_corner(UR),
            square.get_corner(DL),
            square.get_corner(DR)
        ]
        for corner in corners:
            dot = Dot(corner, color=RED, radius=0.12)
            corner_dots.append(dot)

        self.play(*[FadeIn(dot) for dot in corner_dots])

        # Draw lines from blue dots to closest corner dots
        blue_nodes = [nodes[i] for i in range(6) if colors[i] == BLUE]  # nodes 1, 3, 5

        lines_to_corners = []
        for blue_node in blue_nodes:
            blue_pos = blue_node.get_center()
            # Find closest corner
            min_dist = float('inf')
            closest_corner = None
            for corner in corners:
                dist = np.linalg.norm(blue_pos - corner)
                if dist < min_dist:
                    min_dist = dist
                    closest_corner = corner
            # Create line to closest corner
            line = Line(blue_pos, closest_corner, color=ORANGE)
            lines_to_corners.append(line)

        self.play(*[Create(line) for line in lines_to_corners])

        # Update label to K_{4,3}
        k43_label = Text("K₄,₃", font_size=60).to_edge(UP)
        self.play(Transform(k33_label, k43_label))
        self.wait(0.5)

        # Get blue node positions and their closest corners
        blue_indices = [1, 3, 5]
        blue_to_corner = {}
        for idx in blue_indices:
            blue_pos = nodes[idx].get_center()
            min_dist = float('inf')
            closest_corner = None
            for corner in corners:
                dist = np.linalg.norm(blue_pos - corner)
                if dist < min_dist:
                    min_dist = dist
                    closest_corner = corner
            blue_to_corner[idx] = closest_corner

        region_colors = [PURPLE_A, GOLD, PINK]

        topPurple = Polygon(
            nodes[1].get_center(),
            nodes[2].get_center(),
            top_mid,
            blue_to_corner[1],
            fill_color=region_colors[0],
            fill_opacity=0.3,
            stroke_width=0
        )

        botPurple = Polygon(
            nodes[5].get_center(),
            blue_to_corner[5],
            bottom_mid,
            fill_color=region_colors[0],
            fill_opacity=0.3,
            stroke_width=0
        )

        rightPink = Polygon(
            nodes[1].get_center(),
            blue_to_corner[1],
            right_mid,
            fill_color=region_colors[2],
            fill_opacity=0.3,
            stroke_width=0
        )

        leftPink = Polygon(
            nodes[3].get_center(),
            nodes[4].get_center(),
            left_mid,
            blue_to_corner[3],
            fill_color=region_colors[2],
            fill_opacity=0.3,
            stroke_width=0
        )

        topGold = Polygon(
            nodes[2].get_center(),
            nodes[3].get_center(),
            blue_to_corner[3],
            top_mid,
            fill_color=region_colors[1],
            fill_opacity=0.3,
            stroke_width=0
        )

        leftGold = Polygon(
            nodes[4].get_center(),
            nodes[5].get_center(),
            bottom_mid,
            square.get_corner(DL),
            left_mid,
            fill_color=region_colors[1],
            fill_opacity=0.3,
            stroke_width=0
        )

        rightGold = Polygon(
            nodes[5].get_center(),
            nodes[0].get_center(),
            nodes[1].get_center(),
            right_mid,
            blue_to_corner[5],
            fill_color=region_colors[1],
            fill_opacity=0.3,
            stroke_width=0
        )

        # Group polygons by color and draw with edge highlights

        # Purple polygons with their shared edges
        purple_edges = [
            Line(top_mid, blue_to_corner[1], color=RED, stroke_width=10),
            Line(blue_to_corner[5], bottom_mid, color=RED, stroke_width=10)
        ]

        self.play(
            *[Create(edge) for edge in purple_edges])
        self.play(FadeIn(topPurple),
            FadeIn(botPurple)
        )
        self.wait(0.5)
        self.play(*[FadeOut(edge) for edge in purple_edges])

        # Gold polygons with their shared edges
        gold_edges = [
            Line(blue_to_corner[3], top_mid, color=RED, stroke_width=10),
            Line(bottom_mid, square.get_corner(DL), color=RED, stroke_width=10),
            Line(square.get_corner(DL), left_mid, color=BLUE, stroke_width=10),
            Line(right_mid, blue_to_corner[5], color=BLUE, stroke_width=10)
        ]

        self.play(
            *[Create(edge) for edge in gold_edges],
            FadeIn(topGold),
            FadeIn(leftGold),
            FadeIn(rightGold)
        )
        self.wait(0.5)
        self.play(*[FadeOut(edge) for edge in gold_edges])

        # Pink polygons with their shared edges
        pink_edges = [
            Line(blue_to_corner[1], right_mid, color=BLUE, stroke_width=10),
            Line(left_mid, blue_to_corner[3], color=BLUE, stroke_width=10)
        ]

        self.play(
            *[Create(edge) for edge in pink_edges],
            FadeIn(rightPink),
            FadeIn(leftPink)
        )
        self.wait(0.5)
        self.play(*[FadeOut(edge) for edge in pink_edges])

        # Fade out the gold areas
        self.play(
            FadeOut(topGold),
            FadeOut(leftGold),
            FadeOut(rightGold)
        )

        # Add blue dots on lower half of left and right sides
        left_lower_dot = Dot(left_mid + DOWN * 1.25, color=BLUE, radius=0.12)
        right_lower_dot = Dot(right_mid + DOWN * 1.25, color=BLUE, radius=0.12)

        self.play(FadeIn(left_lower_dot), FadeIn(right_lower_dot))

        # Draw lines from the new blue dots
        # Left blue dot to lower left red hexagon dot (node 4)
        line_left_to_hex = Line(left_lower_dot.get_center(), nodes[4].get_center(), color=GREEN)

        # Right blue dot to right hexagon dot (node 0)
        line_right_to_hex = Line(right_lower_dot.get_center(), nodes[0].get_center(), color=GREEN)

        # Left blue dot to lower left corner
        line_left_to_corner = Line(left_lower_dot.get_center(), square.get_corner(DL), color=GREEN)

        # Right blue dot to lower right corner
        line_right_to_corner = Line(right_lower_dot.get_center(), square.get_corner(DR), color=GREEN)

        # Two-segment path: left blue dot → left part of bottom → top edge → red dot
        left_bottom_point = bottom_mid + LEFT * 1.6
        top_left_point = top_mid + LEFT * 1.6

        line_to_bottom = Line(left_lower_dot.get_center(), left_bottom_point, color=GREEN)
        line_bottom_to_top = Line(left_bottom_point, top_left_point, color=GREEN)
        line_top_to_red = Line(top_left_point, nodes[2].get_center(), color=GREEN)

        self.play(
            Create(line_left_to_hex),
            Create(line_right_to_hex),
            Create(line_left_to_corner),
            Create(line_right_to_corner),
            LaggedStart(
                Create(line_to_bottom),
                Create(line_top_to_red),
                lag_ratio=0.45,
                run_time=1
            )
        )

        # Update label to K_{4,4}
        k44_label = Text("K₄,₄", font_size=60).to_edge(UP)
        self.play(Transform(k33_label, k44_label))
        self.wait(0.5)

        # Fill in the 7 remaining regions
        # Region 1: Left blue dot, node 4, left corner
        region1 = Polygon(
            left_lower_dot.get_center(),
            nodes[4].get_center(),
            left_mid,
            fill_color=BLUE_A,
            fill_opacity=0.5,
            stroke_width=0
        )

        # Region 2: Left blue dot, left corner, left bottom point
        region2 = Polygon(
            left_lower_dot.get_center(),
            square.get_corner(DL),
            left_bottom_point,
            fill_color=GRAY_BROWN,
            fill_opacity=0.5,
            stroke_width=0
        )

        # Region 3: Left bottom point, bottom left corner, bottom right corner, right blue dot
        region3 = Polygon(
            left_bottom_point,
            left_lower_dot.get_center(),
            nodes[4].get_center(),
            nodes[5].get_center(),
            bottom_mid,
            fill_color=YELLOW_A,
            fill_opacity=0.5,
            stroke_width=0
        )

        # Region 4: Right blue dot, right corner, node 0
        region4 = Polygon(
            right_lower_dot.get_center(),
            square.get_corner(DR),
            nodes[5].get_center(),
            nodes[0].get_center(),
            fill_color=RED_A,
            fill_opacity=0.5,
            stroke_width=0
        )

        # Region 5: Left blue dot, left bottom point, right blue dot, node 0, node 5, node 4
        region5 = Polygon(
            right_lower_dot.get_center(),
            nodes[0].get_center(),
            nodes[1].get_center(),
            right_mid,
            fill_color=BLUE_A,
            fill_opacity=0.5,
            stroke_width=0
        )

        # Region 6: Left bottom point, bottom mid, right blue dot (small triangle at bottom)
        region6 = Polygon(
            top_left_point,
            top_mid,
            nodes[2].get_center(),
            fill_color=YELLOW_A,
            fill_opacity=0.5,
            stroke_width=0
        )

        # Region 7: Left bottom point, top left point, node 2, top mid
        region7 = Polygon(
            top_left_point,
            nodes[2].get_center(),
            nodes[3].get_center(),
            square.get_corner(UL),
            fill_color=GRAY_BROWN,
            fill_opacity=0.5,
            stroke_width=0
        )

        self.play(
            FadeIn(region1),
            FadeIn(region2),
            FadeIn(region3),
            FadeIn(region4),
            FadeIn(region5),
            FadeIn(region6),
            FadeIn(region7)
        )

        self.wait(2)

        # Move all matching colored regions to opposite edges simultaneously
        # Purple: botPurple (bottom) moves up to match topPurple
        botPurple_target = botPurple.copy()
        botPurple_target.shift(UP * 5)

        # Pink: leftPink (left) moves right to match rightPink
        leftPink_target = leftPink.copy()
        leftPink_target.shift(RIGHT * 5)

        # BLUE_A: region1 (left) moves to right to match region5
        region1_target = region1.copy()
        region1_target.shift(RIGHT * 5)

        # GRAY_BROWN: region2 (bottom-left) moves to top to match region7
        region2_target = region2.copy()
        region2_target.shift(UP * 5)

        # YELLOW_A: region3 (bottom) moves to top to match region6
        region3_target = region3.copy()
        region3_target.shift(UP * 5)

        # Move label to the right
        k44_label_right = k33_label.copy()
        k44_label_right.shift(RIGHT * 3)

        self.play(
            Transform(botPurple, botPurple_target),
            Transform(leftPink, leftPink_target),
            Transform(region1, region1_target),
            Transform(region2, region2_target),
            Transform(region3, region3_target),
            Transform(k33_label, k44_label_right),
            run_time=2
        )

        self.wait(1)

        # Move all shapes back to their original positions
        # Create targets at original positions (reverse the shifts)
        botPurple_original = botPurple_target.copy()
        botPurple_original.shift(DOWN * 5)

        leftPink_original = leftPink_target.copy()
        leftPink_original.shift(LEFT * 5)

        region1_original = region1_target.copy()
        region1_original.shift(LEFT * 5)

        region2_original = region2_target.copy()
        region2_original.shift(DOWN * 5)

        region3_original = region3_target.copy()
        region3_original.shift(DOWN * 5)

        # Move label back to original position
        k44_label_original = k44_label_right.copy()
        k44_label_original.shift(LEFT * 3)

        self.play(
            Transform(botPurple, botPurple_original),
            Transform(leftPink, leftPink_original),
            Transform(region1, region1_original),
            Transform(region2, region2_original),
            Transform(region3, region3_original),
            Transform(k33_label, k44_label_original),
            run_time=2
        )

        self.wait(1)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        self.wait(0.5)

        endText = Paragraph("Since none of these regions contain all four blue dots, K₅,₄ can't be embedded in a torus.\n"
                       "\nA handle needs to be added to connect two regions.\n"
                       "\nI think I'm close to a proof using induction and an idea similar to this.",
                       font_size=20, alignment="center")

        self.play(Write(endText, run_time = 3))

        self.wait(8)
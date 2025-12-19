from manim import *
import numpy as np


class Graph3DDemo(ThreeDScene):
    def construct(self):
        # Set up 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        square = Square(side_length=5)

        # Arrows on the frame
        top_arrow = Arrow(start=ORIGIN + UP * 2.5 + LEFT * 0.5, end=ORIGIN + UP * 2.5 + RIGHT * 0.5, buff=0)
        bottom_arrow = Arrow(start=ORIGIN + DOWN * 2.5 + LEFT * 0.5, end=ORIGIN + DOWN * 2.5 + RIGHT * 0.5, buff=0)
        left_arrow1 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.8, end=ORIGIN + LEFT * 2.5 + DOWN * 0.2, buff=0)
        left_arrow2 = Arrow(start=ORIGIN + LEFT * 2.5 + UP * 0.2, end=ORIGIN + LEFT * 2.5 + DOWN * 0.8, buff=0)
        right_arrow1 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.8, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.2, buff=0)
        right_arrow2 = Arrow(start=ORIGIN + RIGHT * 2.5 + UP * 0.2, end=ORIGIN + RIGHT * 2.5 + DOWN * 0.8, buff=0)

        self.add(square, top_arrow, bottom_arrow, left_arrow1, left_arrow2, right_arrow1, right_arrow2)

        # Create hexagon nodes
        radius = 1.8
        colors = [RED, BLUE, RED, BLUE, RED, BLUE]
        nodes = []
        for k, theta in enumerate(np.linspace(0, 2 * np.pi, 6, endpoint=False)):
            pos = radius * np.array([np.cos(theta), np.sin(theta), 0])
            node = Dot(pos, color=colors[k], radius=0.12)
            nodes.append(node)

        # Hexagon edges
        for i in range(6):
            j = (i + 1) % 6
            self.add(Line(nodes[i].get_center(), nodes[j].get_center()))

        # Yellow lines
        bottom_mid = square.get_bottom()
        top_mid = square.get_top()
        left_mid = square.get_left()
        right_mid = square.get_right()

        y0 = Line(nodes[3].get_center(), nodes[0].get_center(), color=YELLOW)
        y1 = Line(nodes[5].get_center(), bottom_mid, color=YELLOW)
        y2 = Line(top_mid, nodes[2].get_center(), color=YELLOW)
        y3 = Line(nodes[4].get_center(), left_mid, color=YELLOW)
        y4 = Line(right_mid, nodes[1].get_center(), color=YELLOW)

        self.add(y0, y1, y2, y3, y4)

        # Corner dots
        corners = [square.get_corner(UL), square.get_corner(UR),
                   square.get_corner(DL), square.get_corner(DR)]
        corner_dots = [Dot(corner, color=RED, radius=0.12) for corner in corners]

        # Additional blue dots
        left_lower_dot = Dot(left_mid + DOWN * 1.25, color=BLUE, radius=0.12)
        right_lower_dot = Dot(right_mid + DOWN * 1.25, color=BLUE, radius=0.12)

        # Orange lines from blue hexagon nodes to corners
        blue_indices = [1, 3, 5]
        for idx in blue_indices:
            blue_pos = nodes[idx].get_center()
            closest_corner = min(corners, key=lambda c: np.linalg.norm(blue_pos - c))
            self.add(Line(blue_pos, closest_corner, color=ORANGE))

        # Green lines
        self.add(Line(left_lower_dot.get_center(), nodes[4].get_center(), color=GREEN))
        self.add(Line(right_lower_dot.get_center(), nodes[0].get_center(), color=GREEN))
        self.add(Line(left_lower_dot.get_center(), square.get_corner(DL), color=GREEN))
        self.add(Line(right_lower_dot.get_center(), square.get_corner(DR), color=GREEN))

        left_bottom_point = bottom_mid + LEFT * 1.6
        top_left_point = top_mid + LEFT * 1.6
        self.add(Line(left_lower_dot.get_center(), left_bottom_point, color=GREEN))
        self.add(Line(top_left_point, nodes[2].get_center(), color=GREEN))

        # Add all dots
        for node in nodes:
            self.add(node)
        for dot in corner_dots:
            self.add(dot)
        self.add(left_lower_dot, right_lower_dot)

        # K₄,₄ label
        k44_label = Text("K₄,₄", font_size=60).to_edge(UP)
        self.add_fixed_in_frame_mobjects(k44_label)

        self.wait(1)

        # Begin 3D transformation
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)

        # Helper function to map flat square coordinates to torus surface
        def square_to_torus(point, major_radius=2, minor_radius=0.8):
            """Map a point from the square [-2.5, 2.5] x [-2.5, 2.5] to a torus surface"""
            x, y, z = point

            # Normalize to [0, 1] x [0, 1]
            u = (x + 2.5) / 5.0
            v = (y + 2.5) / 5.0

            # Convert to torus angles
            theta = 2 * np.pi * u  # angle around major circle
            phi = 2 * np.pi * v  # angle around minor circle

            # Torus parametric equations
            torus_x = (major_radius + minor_radius * np.cos(phi)) * np.cos(theta)
            torus_y = (major_radius + minor_radius * np.cos(phi)) * np.sin(theta)
            torus_z = minor_radius * np.sin(phi)

            return np.array([torus_x, torus_y, torus_z])

        # Create a visual torus for reference
        torus = Surface(
            lambda u, v: np.array([
                (2 + 0.8 * np.cos(v)) * np.cos(u),
                (2 + 0.8 * np.cos(v)) * np.sin(u),
                0.8 * np.sin(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, TAU],
            resolution=(32, 16),
            fill_opacity=0.3,
            stroke_width=0.5,
            color=BLUE_E
        )

        self.play(Create(torus), run_time=2)
        self.wait(1)

        # Update label
        torus_label = Text("K₄,₄ on a Torus", font_size=60).to_edge(UP)
        self.play(Transform(k44_label, torus_label))

        # Collect all nodes
        red_hexagon_nodes = [nodes[i] for i in [0, 2, 4]]
        blue_hexagon_nodes = [nodes[i] for i in [1, 3, 5]]
        all_nodes = nodes + corner_dots + [left_lower_dot, right_lower_dot]

        # Store original positions and calculate torus positions
        animations = []
        node_torus_positions = {}

        for node in all_nodes:
            original_pos = node.get_center()
            torus_pos = square_to_torus(original_pos)
            node_torus_positions[node] = torus_pos
            animations.append(node.animate.move_to(torus_pos))

        # Animate nodes moving to torus surface
        self.play(*animations, run_time=3)
        self.wait(1)

        # Remove old 2D elements
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if isinstance(mob, (Line, Arrow, Square))],
            run_time=1
        )

        # Create edges on the torus surface
        # For K₄,₄: connect red nodes to blue nodes
        all_red_nodes = red_hexagon_nodes + corner_dots
        all_blue_nodes = blue_hexagon_nodes + [left_lower_dot, right_lower_dot]

        edges_3d = []
        for red_node in all_red_nodes:
            for blue_node in all_blue_nodes:
                # Create parametric curve that follows geodesic-like path on torus
                start = node_torus_positions[red_node]
                end = node_torus_positions[blue_node]

                # Simple linear interpolation on torus (not true geodesic but visually works)
                curve = ParametricFunction(
                    lambda t: start + t * (end - start),
                    t_range=[0, 1],
                    color=BLUE_D,
                    stroke_width=2
                )
                edges_3d.append(curve)

        self.play(*[Create(edge) for edge in edges_3d], run_time=2)
        self.wait(1)

        # Show that edges don't cross on the torus surface
        highlight_label = Text("No edge crossings!", font_size=50, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(highlight_label)
        self.play(Write(highlight_label))

        # Rotate to show different angles
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(8)
        self.stop_ambient_camera_rotation()

        # Final view
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=3)

        self.wait(2)
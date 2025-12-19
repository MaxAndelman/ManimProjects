from manim import *


class Complete_Bipartite(Scene):
    def construct(self):
        # Title
        title = Text("Definition of a Complete Bipartite Graph", font_size=36)  # K₃,₃
        title.to_edge(UP)

        # Create two sets of vertices
        left_vertices = VGroup()
        right_vertices = VGroup()

        # Left partition (3 vertices)
        left_positions = [UP * 1.5, ORIGIN, DOWN * 1.5]
        for i, pos in enumerate(left_positions):
            vertex = Circle(radius=0.3, color=BLUE, fill_opacity=0.7)
            vertex.move_to(LEFT * 3 + pos)
            vertex_group = VGroup(vertex)
            left_vertices.add(vertex_group)

        # Right partition (3 vertices)
        right_positions = [UP * 1.5, ORIGIN, DOWN * 1.5]
        for i, pos in enumerate(right_positions):
            vertex = Circle(radius=0.3, color=RED, fill_opacity=0.7)
            vertex.move_to(RIGHT * 3 + pos)
            vertex_group = VGroup(vertex)
            right_vertices.add(vertex_group)

        # Track which edges are in some_edges
        some_edges = VGroup()
        some_edges_coords = set()

        # Add edges to some_edges
        for left_v in left_vertices:
            edge = Line(
                left_v[0].get_center(),
                right_vertices[0][0].get_center(),
                color=GRAY,
                stroke_width=2
            )
            some_edges.add(edge)
            some_edges_coords.add((tuple(left_v[0].get_center()), tuple(right_vertices[0][0].get_center())))

        for right_v in right_vertices:
            edge = Line(
                left_vertices[1][0].get_center(),
                right_v[0].get_center(),
                color=GRAY,
                stroke_width=2
            )
            some_edges.add(edge)
            some_edges_coords.add((tuple(left_vertices[1][0].get_center()), tuple(right_v[0].get_center())))

        e1 = Line(
            left_vertices[2][0].get_center(),
            right_vertices[1][0].get_center(),
            color=GRAY,
            stroke_width=2
        )
        some_edges.add(e1)
        some_edges_coords.add((tuple(left_vertices[2][0].get_center()), tuple(right_vertices[1][0].get_center())))

        # Create edges that are NOT in some_edges
        edges = VGroup()
        for i, left_v in enumerate(left_vertices):
            for j, right_v in enumerate(right_vertices):
                coord_pair = (tuple(left_v[0].get_center()), tuple(right_v[0].get_center()))
                if coord_pair not in some_edges_coords:
                    edge = Line(
                        left_v[0].get_center(),
                        right_v[0].get_center(),
                        color=GRAY,
                        stroke_width=2
                    )
                    edges.add(edge)

        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)

        # Draw vertices
        self.play(
            LaggedStart(*[Create(v[0]) for v in left_vertices], *[Create(v[0]) for v in right_vertices], lag_ratio=0.2),
            run_time=1.5
        )

        explanation1 = Text(
            "Take two disjoint sets of vertices",
            font_size=30,
            color=WHITE
        )
        explanation1.to_edge(DOWN)
        explanation1.shift(UP* 0.8)

        self.play(Write(explanation1), run_time = 1)
        self.wait(2)
        self.play(FadeOut(explanation1))

        # Draw edges one by one
        self.play(
            LaggedStart(*[Create(edge) for edge in some_edges], lag_ratio=0.1),
            run_time=2
        )

        explanation2 = Text(
            "Each edge can connect one vertex from each set",
            font_size=28,
            color=WHITE
        )
        explanation2.to_edge(DOWN)
        explanation2.shift(UP* 0.8)

        self.play(Write(explanation2), run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(explanation2))

        # Add edge between u1 and u2 (invalid in bipartite graph)
        invalid_edge = Line(
            left_vertices[0][0].get_center(),
            left_vertices[1][0].get_center(),
            color=RED,
            stroke_width=3
        )

        self.play(Create(invalid_edge), run_time=1)
        self.wait(0.5)

        # Create red X over the edge
        edge_center = invalid_edge.get_center()
        x_mark = VGroup(
            Line(edge_center + UL * 0.3, edge_center + DR * 0.3, color=RED, stroke_width=6),
            Line(edge_center + UR * 0.3, edge_center + DL * 0.3, color=RED, stroke_width=6)
        )

        explanation3 = Text(
            "But edges cannot\nconnect vertices in\nthe same set",
            font_size=24,
            color=WHITE
        )
        explanation3.to_edge(LEFT)
        explanation3.shift(UP* 0.7)

        self.play(LaggedStart(Write(explanation3), Create(x_mark), lag_ratio = 0.8))

        self.wait()

        # Delete both the edge and the X and the explanation
        self.play(
            FadeOut(invalid_edge),
            FadeOut(x_mark), FadeOut(explanation3),
            run_time=1
        )

        # Draw remaining edges (not in some_edges)
        self.play(
            LaggedStart(*[Create(edge) for edge in edges], lag_ratio=0.1),
            run_time=2
        )

        explanation4 = Text(
            "If each vertex is connected to all vertices in the\nother set, it's known as a complete bipartite graph",
            font_size=26,
            color=WHITE
        )
        explanation4.to_edge(DOWN)
        explanation4.shift(UP* 0.8)

        self.play(Write(explanation4), run_time = 1.5)
        self.wait(3.5)
        self.play(FadeOut(explanation4))

        explanation5 = Text(
            "A complete bipartite graph with m red vertices and\nn blue vertices is denoted K(m,n). Shown is K(3,3)",
            font_size=26,
            color=WHITE
        )
        explanation5.to_edge(DOWN)
        explanation5.shift(UP * 0.8)

        self.play(Write(explanation5), run_time = 1.5)
        self.wait(3)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        theorem = Text(
            "What genus orientable surface\ncan K(m,n) be embedded on?",
            font_size=40,
            color=WHITE
        )

        self.play(Write(theorem), run_time = 1.2)
        self.wait(2)
        self.play(FadeOut(theorem))

        # Highlight one vertex and its connections
        # highlight_vertex = left_vertices[1][0].copy()
        # highlight_vertex.set_color(YELLOW).set_stroke(width=4)
        #
        # # Find all edges connected to middle left vertex (including from some_edges)
        # highlight_edges = VGroup()
        # all_edges = VGroup(*some_edges, *edges)
        # middle_left_pos = tuple(left_vertices[1][0].get_center())
        #
        # for edge in all_edges:
        #     start_pos = tuple(edge.get_start())
        #     if start_pos == middle_left_pos:
        #         highlight_edges.add(edge.copy().set_color(YELLOW).set_stroke(width=4))
        #
        # self.play(
        #     Create(highlight_vertex),
        #     *[Create(e) for e in highlight_edges],
        #     run_time=1.5
        # )
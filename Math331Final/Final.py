# combined_scenes.py
from manim import *
from complete_bipartite import Complete_Bipartite
from complete_incidence import CompleteIncidenceGraph
from genus_of_imn import Genus
from graph_composition import GraphComposition
from conclusion import Conclusion


class CombinedScenes(Scene):
    def construct(self):
        self.next_section("Scene 1")
        Complete_Bipartite.construct(self)

        self.next_section("Scene 2")
        CompleteIncidenceGraph.construct(self)

        self.next_section("Scene 3")
        Genus.construct(self)

        self.next_section("Scene 4")
        GraphComposition.construct(self)

        self.next_section("Scene 5")
        Conclusion.construct(self)
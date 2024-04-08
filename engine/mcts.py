from node import Node
from random import choice
from typing import Dict, List, Set
from collections import defaultdict
import numpy as np

class MCTS:
    """Monte Carlo Tree Search object."""
    def __init__(self, weight: float = 1.0) -> None:
        self.Q: Dict[Node, float] = defaultdict(int)
        self.N: Dict[Node, int] = defaultdict(int)
        self.children: Dict[Node, Set[Node]] = {}
        self.weight = weight

    def rollout(self, node: Node) -> None:
        path = self._select(node)
        self._expand(leaf := path[-1])
        reward = self._simulate(leaf)
        self._backpropagate(path, reward)

    def _select(self, node: Node) -> List[Node]:
        path = [node]
        while node in self.children and not node.is_terminal():
            if all(child in self.N for child in self.children[node]):
                # Select best child using UCB
                node = self.select_uct(node)
            else:
                # Not all children are visited, select one at random
                unvisited = [child for child in self.children[node]
                             if child not in self.N]
                node = choice(unvisited)
            path.append(node)
        return path

    def _expand(self, node: Node) -> None:
        if node.is_terminal():
            # No successors available; mark terminal node with set()
            self.children[node] = Set()
        elif node not in self.children:
            # Expand node if hasn't been visited
            self.children[node] = node.find_successors()

    def _simulate(self, node: Node) -> float:
        while not node.is_terminal():
            node = node.find_rand_successor() or node
        return node.get_reward()

    def _backpropagate(self, path: List[Node], reward: float) -> None:
        for node in reversed(path):
            self.N[node] += 1
            self.Q[node] += reward

    def select_uct(self, node: Node) -> Node:
        def _ucb1(node: Node) -> float:
            wi, ni = self.Q[node], self.N[node]
            Ni = sum(self.N[leaf] for leaf in self.children[node])
            return (wi / ni) + self.weight * np.sqrt(np.log(Ni) / self.N[node])

        return max(self.children[node], key=_ucb1)

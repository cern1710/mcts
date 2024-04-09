from typing import Optional, Protocol, Set

class Node(Protocol):
    """Interface for a node in the MCTS tree."""
    def find_successors(self) -> Set['Node']:
        return set()

    def find_next_successor(self) -> Optional['Node']:
        return None

    def is_terminal(self) -> bool:
        return True

    def get_reward(self) -> float:
        return 0.0
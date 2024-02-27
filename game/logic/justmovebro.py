from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


class JustMoveBro(BaseLogic) :
    # Constructor dulu bro
    def __init__(self) :
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_direction = 0
        
    # Bro just wanna move 
    def next_move(self, board_bot: GameObject, board: Board) :
        # Muter muter aja gak sih bro
        delta = self.directions[self.current_direction]
        delta_x = delta[0]
        delta_y = delta[1]
        self.current_direction = (self.current_direction + 1) % 4
        
        return delta_x, delta_y
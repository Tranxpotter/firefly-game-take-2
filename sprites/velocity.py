import math

class Velocity:
    def __init__(self, velo_x:float = 0, velo_y:float = 0) -> None:
        self.x = velo_x
        self.y = velo_y
    
    @property
    def magnitide(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    @property
    def degrees(self) -> float:
        return math.degrees(math.atan2(self.y, self.x))
    
    @property
    def radian(self) -> float:
        return math.atan2(self.y, self.x)
    
    def __repr__(self) -> str:
        return f"Velocity({self.x}, {self.y})"

    
    
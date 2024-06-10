import math

class Velocity:
    def __init__(self, velo_x:float = 0, velo_y:float = 0) -> None:
        self.x = velo_x
        self.y = velo_y
    
    @property
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    @property
    def degrees(self) -> float:
        return math.degrees(math.atan2(self.y, self.x))
    
    @degrees.setter
    def degrees(self, degrees:float):
        rad = math.radians(degrees)
        self.radian = rad
    
    @property
    def radian(self) -> float:
        return math.atan2(self.y, self.x)
    
    @radian.setter
    def radian(self, radian:float):
        magnitude = self.magnitude
        self.x = math.cos(radian) * magnitude
        self.y = math.sin(radian) * magnitude
    
    def __repr__(self) -> str:
        return f"Velocity({self.x}, {self.y})"

    
    
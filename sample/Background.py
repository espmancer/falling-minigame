"""
Background
This class is designed to represent the background color.
"""
class Background():
    def __init__(self, backgroundColor):
        self.backgroundColor = backgroundColor
    
    # Get the background color.
    def getBackground(self) -> tuple:
        return self.backgroundColor
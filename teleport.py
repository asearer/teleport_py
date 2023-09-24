class Location:
    """Represents a 2D location with x and y coordinates."""
    
    def __init__(self, x, y):
        """Initialize a Location object with the given x and y coordinates."""
        self.x = x
        self.y = y

class Character:
    """Represents a character with a location that can be teleported."""
    
    def __init__(self, location):
        """Initialize a Character object with the starting location."""
        self.location = location

    def teleport(self, new_location):
        """
        Teleport the character to a new location.
        
        Args:
            new_location (Location): The new location to teleport the character to.
        """
        self.location = new_location

def choose_destination():
    """
    Prompt the player to choose a destination and return the chosen Location.
    
    Returns:
        Location: The chosen destination Location.
    """
    x = float(input("Enter the x-coordinate of your destination: "))
    y = float(input("Enter the y-coordinate of your destination: "))
    return Location(x, y)

def main():
    # Create a Character object with an initial location at (0, 0)
    character = Character(Location(0.0, 0.0))
    
    print(f"Character's current location: ({character.location.x}, {character.location.y})")
    
    # Allow the player to choose a destination
    destination = choose_destination()
    
    # Teleport the character to the chosen destination
    character.teleport(destination)
    
    print(f"Character has been teleported to: ({character.location.x}, {character.location.y})")

if __name__ == "__main__":
    main()

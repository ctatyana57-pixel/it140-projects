"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# Create the gameplay loop required by the milestone.
while True:
    # 1. Display the current room.
    print(f"You are in the {current room}.")
    
    # 2. Prompt for a movement command or "exit".
command = input("Enter a direction(north,south,east,west) or 'exit': ").lower().strip()

# 3. Branch for a valid move, exit, or invalid input.
if command == "exit":
    print("Goodbye!")
    break

if command in rooms[current_room]:
    # 4. Update the room only after a valid movement command.
    current_room = rooms[current_room][command]
    print(f"You move {command}.")
else:
    # 5. Reject invalid input.
    print("Invalid direction. Please choose a valid direction or type 'exit'.)

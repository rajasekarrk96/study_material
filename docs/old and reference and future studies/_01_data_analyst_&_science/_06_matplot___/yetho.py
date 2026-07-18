# Importing the required library for plotting
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Function to draw a specified alphabet at a given size
def draw_alphabet(letter, size):
    # Create a figure and axes for the plot
    fig, ax = plt.subplots()  # `fig` is the entire figure, and `ax` is the specific plot area

    # Normalize the size input to make it compatible with the plot scale
    size = size / 10.0  # Scaling down size to adjust line thickness appropriately

    # Check which alphabet needs to be drawn
    if letter.upper() == 'A':  # If the input letter is 'A' (case-insensitive)
        # Draw the outline of the letter 'A' using lines
        ax.plot([0, 0.5, 1], [0, 1, 0], 'b-', lw=size * 2)  # Create a triangle shape
        # `plot([x-coordinates], [y-coordinates], 'color-style', lw=linewidth)`
        # [0, 0.5, 1]: x-coordinates of the triangle's vertices
        # [0, 1, 0]: y-coordinates of the triangle's vertices
        # 'b-': Blue line
        # lw=size * 2: Line width proportional to the input size

        # Draw the horizontal bar in the middle of 'A'
        ax.plot([0.25, 0.75], [0.5, 0.5], 'b-', lw=size * 2)  # A red horizontal line
        # [0.25, 0.75]: x-coordinates of the line
        # [0.5, 0.5]: y-coordinates (constant because it's horizontal)
        # 'r-': Red line
    elif letter.upper() == 'B':  # If the input letter is 'B'
        # Draw the straight vertical line of 'B'
        ax.plot([0, 0, 0, 0.5], [0, 1, 0.5, 0], 'g-', lw=size * 2)
        # `plot` creates a vertical line and a diagonal connection for aesthetics

        # Draw the top curved part of 'B'
        circle1 = plt.Circle((0.25, 0.75), 0.25, color='r', fill=False, lw=size * 2)
        # plt.Circle((x, y), radius, color, fill, linewidth)
        # (0.25, 0.75): Center of the circle
        # 0.25: Radius of the circle
        # color='r': Red outline
        # fill=False: No fill inside the circle
        # lw=size * 2: Line width proportional to the size

        # Draw the bottom curved part of 'B'
        circle2 = plt.Circle((0.25, 0.25), 0.25, color='r', fill=False, lw=size * 2)
        # Similar to the above but at a different position (0.25, 0.25)

        # Add both circles to the plot
        ax.add_artist(circle1)  # Adds the top circle to the axes
        ax.add_artist(circle2)  # Adds the bottom circle to the axes
    else:
        # If the letter is not implemented, print a message and exit
        print("Alphabet drawing for this letter is not implemented.")
        return  # Exit the function

    # Set the limits for the plot to ensure the alphabet fits well in the frame
    ax.set_xlim(-0.5, 1.5)  # x-axis range from -0.5 to 1.5
    ax.set_ylim(-0.5, 1.5)  # y-axis range from -0.5 to 1.5

    # Set the aspect ratio of the axes to be equal to avoid distortion
    ax.set_aspect('equal')  # Ensures the shapes are not stretched or squished

    # Turn off the axes for a cleaner look
    ax.axis('off')  # Hides the x and y axes

    # Display the final plot
    plt.show()  # Opens a window to show the plot


# Ask the user for an alphabet input
alphabet = input("Enter an alphabet to draw (e.g., A, B): ").strip()  # Get the alphabet and remove any extra spaces

# Ask the user for a size input
size = int(input("Enter the size for the alphabet: "))  # Convert the size input to an integer

# Call the function with the user's inputs
draw_alphabet(alphabet, size)

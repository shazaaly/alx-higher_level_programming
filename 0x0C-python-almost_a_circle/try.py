# Dimensions of the rectangle
width = 5
height = 5

# Position of the rectangle
x = 3
y = 7

# Loop over the rows
for row in range(y, y + height):
    # Loop over the columns
    for col in range(x, x + width):
        # Print a symbol to represent the rectangle
        print("*", end="")
    print()  # Move to the next line after each row

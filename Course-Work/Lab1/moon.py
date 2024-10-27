import cairo

# Create a surface and context
width, height = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
ctx = cairo.Context(surface)

# Fill background with black
ctx.set_source_rgb(0, 0, 0)  # Black background
ctx.paint()

# Set the color for the moon (using RGB for white)
ctx.set_source_rgb(1, 1, 1)

# Coordinates and radius for the moon
x, y = width - 100, 100  # Position near the top-right corner
outer_radius = 80  # Outer circle radius for the moon
inner_radius = 60  # Inner circle radius (for the crescent effect)

# Draw the outer part of the moon (a full circle)
ctx.arc(x, y, outer_radius, 0, 2 * 3.1416)  # Full circle for the moon
ctx.fill()

# Set background color (black again) to "cut" the crescent shape
ctx.set_source_rgb(0, 0, 0)

# Use a Bezier curve or an arc to draw the inner part (cut out the crescent shape)
ctx.arc(x + 30, y, inner_radius, 0, 2 * 3.1416)  # A slightly shifted arc to cut the moon
ctx.fill()

# Save the image
surface.write_to_png("crescent_moon.png")

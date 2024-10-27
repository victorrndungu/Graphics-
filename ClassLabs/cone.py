import cairo
import math

# Setup surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light gray background
ctx.paint()

# Set drawing color and line width
ctx.set_source_rgb(0, 0, 0)  # Black for lines
ctx.set_line_width(2)

# Cone parameters
x_center = 300  # Center of the base (x-coordinate)
y_center = 300  # Center of the base (y-coordinate)
radius = 150    # Radius of the arc
apex_x = 300    # Apex x-coordinate (tip of the cone)
apex_y = 100    # Apex y-coordinate (tip of the cone)

# Draw the left side of the cone
ctx.move_to(apex_x, apex_y)
ctx.line_to(x_center - radius, y_center)  # Left base point

# Draw the right side of the cone
ctx.move_to(apex_x, apex_y)
ctx.line_to(x_center + radius, y_center)  # Right base point

# Draw the arc (base of the cone)
ctx.arc(x_center, y_center, radius, math.pi, 0)  # Arc from left to right (half circle)

# Stroke the lines and arc
ctx.stroke()

# Save the image
surface.write_to_png("cone.png")


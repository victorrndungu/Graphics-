import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 900, 700

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Set background color (white)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set line width for the outlines
ctx.set_line_width(4)

# 1.House body (left section)
ctx.set_source_rgb(0, 0, 0)  # black color
ctx.move_to(200, 300)  # start point
ctx.line_to(200, 500)  # draw the left side
ctx.line_to(400, 500)  # draw the bottom
ctx.line_to(400, 300)  # draw the right side
ctx.stroke()

# 2.Roof (triangle for left side)
ctx.move_to(180, 320)
ctx.line_to(300, 200)
ctx.line_to(420, 320)

ctx.move_to(165, 305)
ctx.line_to(300, 175)
ctx.line_to(435, 305)

ctx.move_to(180, 320)
ctx.line_to(165, 305)

ctx.move_to(420, 320)
ctx.line_to(435, 305)
ctx.stroke()

# 3.Rectangular roof extension
ctx.move_to(425, 295)
ctx.line_to(800, 295)
ctx.move_to(325, 200)
ctx.line_to(700, 200)
ctx.line_to(800, 295)
ctx.stroke()

# 4. Draw the house body
ctx.move_to(790, 295)
ctx.line_to(790, 500)

ctx.move_to(185, 500)
ctx.line_to(800, 500)

ctx.move_to(185, 520)
ctx.line_to(800, 520)
ctx.line_to(800, 500)

ctx.move_to(185, 500)
ctx.line_to(185, 520)
ctx.stroke()

# 5. Draw the windows
# Left window
ctx.rectangle(250, 370, 100, 60)
ctx.stroke()

# Left window sill
ctx.rectangle(240, 430, 120, 10)
ctx.stroke()

# Right window
ctx.rectangle(650, 370, 100, 60)
ctx.stroke()

# Right window sill
ctx.rectangle(640, 430, 120, 10)
ctx.stroke()

# 6. Draw the small square window above the left window (roof window)
ctx.rectangle(275, 270, 50, 50)
ctx.stroke()

# 8. Draw the moon
# Draw the moon (crescent shape in the sky)
ctx.arc(700, 100, 40, 0,2 * 3.14)
ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light gray color for the moon
ctx.fill()
ctx.stroke()

# Draw the flipped crescent (facing left, simulating shadow)
ctx.arc(680, 100, 40, 0,2 * 3.14)  # Changed the center of the arc to the left
ctx.set_source_rgb(1, 1, 1)  # White color to create the crescent shadow
ctx.fill()

# Save the drawing to a PNG file
surface.write_to_png("Output.png")
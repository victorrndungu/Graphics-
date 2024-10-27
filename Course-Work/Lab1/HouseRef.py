import cairo
import math



# Helper functions to abstract repeated operations
def draw_rectangle(ctx, x, y, width, height, color_rgb):
    ctx.rectangle(x, y, width, height)
    ctx.set_source_rgb(*color_rgb)
    ctx.stroke()

def draw_arc(ctx, x, y, radius, angle1, angle2, color_rgb):
    ctx.arc(x, y, radius, angle1, angle2)
    ctx.set_source_rgb(*color_rgb)
    ctx.stroke()

def draw_divider(ctx, x1, y1, x2, y2, color_rgb):
    ctx.move_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.set_source_rgb(*color_rgb)
    ctx.stroke()

OUTPUT_DIR = "../../Test Labs/output_directory/"

# Create surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Frame of the house
ctx.move_to(250, 550)
for x, y in [(650, 550), (650, 285), (700, 285), (700, 205), (200, 205), (200, 285), (250, 285)]:
    ctx.line_to(x, y)
ctx.close_path()
draw_arc(ctx, 450, 205, 150, math.pi, 0, (0.23, 0.53, 0.85))

# Drawing door
draw_rectangle(ctx, 395, 335, 110, 215, (0.45, 0.8, 0.43))

# Drawing door knob
draw_arc(ctx, 493, 442.5, 7, 0, 2 * math.pi, (0.23, 0.53, 0.85))
ctx.set_line_width(2)
ctx.stroke()

# Left window
draw_rectangle(ctx, 275, 335, 85, 85, (0.45, 0.8, 0.43))
draw_divider(ctx, 317.5, 335, 317.5, 420, (0.23, 0.53, 0.85))  # Vertical divider
draw_divider(ctx, 275, 377.5, 360, 377.5, (0.23, 0.53, 0.85))  # Horizontal divider

# Right window
draw_rectangle(ctx, 540, 335, 85, 85, (0.45, 0.8, 0.43))
draw_divider(ctx, 582.5, 335, 582.5, 420, (0.23, 0.53, 0.85))  # Vertical divider
draw_divider(ctx, 540, 377.5, 625, 377.5, (0.23, 0.53, 0.85))  # Horizontal divider

# Drawing the moon
draw_arc(ctx, 700, 100, 80, 0, 2 * math.pi, (0.23, 0.53, 0.85))

# Save the result to a PNG file
surface.write_to_png(f'{OUTPUT_DIR}houseref.png')

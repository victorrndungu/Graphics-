import cairo
import math
# setup surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
# defining the arrow function
def arrow(ctx, x, y, width, height, a, b):
    ctx.move_to(x, y + b)
    ctx.line_to(x, y + height - b)
    ctx.line_to(x + a, y + height - b)
    ctx.line_to(x + a, y + height)
    ctx.line_to(x + width, y + height/2)
    ctx.line_to(x + a, y)
    ctx.line_to(x + a, y + b)
    ctx.close_path()

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()




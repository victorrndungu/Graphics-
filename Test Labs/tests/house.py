import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

ctx.rectangle(120,150,120,80)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

ctx.rectangle(110,230,140,10)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

ctx.rectangle(410,150,120,80)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

ctx.rectangle(400,230,140,10)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

surface.write_to_png('house.png')

print("Rectangle drawn and saved as 'rectangle.png'")




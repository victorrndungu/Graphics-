"""This module draws a rectangle on a canvas"""

import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(100,150,300, 200)
ctx.set_source_rgb(1,0,0)
ctx.fill()
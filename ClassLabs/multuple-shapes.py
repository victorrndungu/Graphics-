import os
from lib2to3.fixes.fix_input import context

import cairo
import math

import rectangle
import logging
logging.basicConfig(level=logging.INFO)

OUTPUT_DIR = "../Test Labs/output_directory/"
WIDTH, HEIGHT = 600, 600  # Adjusted to fit all shapes

if __name__ == '__main__':
    # Ensure the directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Create a surface and context for drawing
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(0.8, 0.8, 0.8)


    #Draw a line
    ctx.move_to(0,0)
    ctx.line_to(300, 300)
    ctx.set_dash([20,5,5,5])
    ctx.set_source_rgb(1,0,0)
    ctx.set_line_width(10)
    ctx.stroke()

    ctx.arc(300,300,200,0,2*math.pi)
    ctx.set_source_rgb(0,1,0)
    ctx.set_line_width(10)
    ctx.stroke()

    ctx.arc(300,300,300,0,2*math.pi)
    ctx.set_source_rgb(0,0,1)
    ctx.set_line_width(10)
    ctx.stroke()
    # Save the result to a PNG file
    surface.write_to_png(f'{OUTPUT_DIR}shapes.png')

    logging.info('Shapes were generated successfully')

"""This is the main module to run the project"""
import rectangle
import logging
logging.basicConfig(level=logging.INFO)

OUTPUT_DIR = "../Test Labs/output_directory/"
WIDTH, HEIGHT = 600, 400

if __name__ == '__main__':
    surface, context = rectangle.create_surface(WIDTH, HEIGHT, (0.8, 0.8, 0.8))
    rectangle.draw_rectangle(context, 150, 100, 100, 240, (1, 0, 0))

    surface.write_to_png(f'{OUTPUT_DIR}new_rectangle.png')

    logging.info('Rectangle was generated successfully')

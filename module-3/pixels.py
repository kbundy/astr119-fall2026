# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0

J = I.copy()  # make a copy of the image array

middle = 349 # the x-coords of the middle of the image

height = 712
def fib(height):
    """Returns the Fibonacci sequence up to n.
    (I wanted to use the fibonacci sequence to generate a pattern for the image, but I didn't get that far.)"""
    a, b = 0, 1
    result = []
    while a < height:
        result.append(a)
        a, b = b, a + b
    return result

J[:, :, 2] = I[:, :, 0]


for n in range(0, 2):
    J[np.array(fib(height))-1+n, :, :] = [1, 0.43, 0.78]  # set a horizontal line of pixels to pink at Fibonacci indices
    J[:, middle-1+n, :] = [0.5, 0, 0.5]  # set a vertical line of pixels to purple at the middle column

A = np.array((712, 698))
rows, cols = np.indices(A)
outside = (rows - 356)**2 + (cols - 349)**2 > 340**2

J[outside] = 0.0  # set pixels outside a circle of radius 2 to black


imsave("module-3/pixels_out.png", J)  # save the modified image

if __name__ == "__main__":
    print("shape:", I.shape)
    print(I.size)
    print(I[356,349])  # pixel at middle (row 356, column 349)
    print(I[0,0])  # pixel at top left
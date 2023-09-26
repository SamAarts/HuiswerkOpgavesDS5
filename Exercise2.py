import numpy as np
import matplotlib.pyplot as plt

def display_plaatje(array:np.array):
    '''
    display een mandelbrotplaatje 
    '''
    plt.imshow(array, extent=(-1.5,0.5,-1,1))
    plt.show()
def draw_mandel(input_width: int):
    '''
    draw mandelbrot figure given the size of the square
    
    input_width is expected to be an integer
    '''
    square = input_width
    x_range = (-1.5,0.5)     # x range of the mandelbrot
    y_range = (-1,1)         # y range of the mandelbrot
    maximum_iterations = 100 # max iterations before killing the program
    mandel_ding = np.zeros((square,square)) # create the array of given size for us a square
    for height in range(square):
        for width in range(square):
            x = x_range[0] + (x_range[1] - x_range[0]) * height/ (square -1) # x waarde berekenen
            y = y_range[0] + (y_range[1] - y_range[0]) * width/ (square -1) # y waarde berekenen
            c = complex(x,y) # complex getal maken
            z= 0
            for iteration in range(maximum_iterations): # iteraten om on eindigheid te vinden
                if abs(z) > 2:
                    mandel_ding[width,height] = iteration
                    break
                z = z * z + c
    return mandel_ding # return mandel zodat we het kunnen tekenen
mandel_ding = draw_mandel(200)
display_plaatje(mandel_ding)
     
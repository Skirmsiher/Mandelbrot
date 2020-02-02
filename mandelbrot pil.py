import numpy as np
from PIL import Image
from numba import jit

import multiprocessing

# TODO Multi-threading
# TODO Animation


def mandel_set(w, h, limit, rmax, colour=None):
    '''re_bound = np.linspace(-2.5, 1, eta[0])
    im_bound = np.linspace(0, 1, eta[1])'''
    c_escaped = []
    iteration_counts = [[] for i in range(limit)]

    for re in range(w):
        x0 = re * (1 - -2.5) / (w - 1) + -2.5
        for im in range(h//2):
            k = 0
            z0 = im * (1 - 0) / (h//2 - 1) + 0
            c = np.complex(x0, -z0)
            z = 0
            print(c)
            if not cardioid_check(c):
                while z.real**2 + z.imag**2 <= rmax*2 and k < limit:
                    k += 1
                    z_old = z
                    z = mandelbrot_function(z, c)
                    if z_old == z:
                        k = limit
                        break
                if k >= limit:
                    pass
                else:
                    img.putpixel((int(re), h//2 - 1 - int(im)), (k % 255 << 5, k % 255, k % 255 * 8))
                    img.putpixel((int(re), h//2 + int(im)), (k % 255 << 5, k % 255, k % 255 * 8))
            else:
                print('Pass')
    return np.array(iteration_counts), np.array(c_escaped)


def cardioid_check(c):
    p = np.sqrt((c.real - 1/4)**2 + c.imag**2)
    if (c.real <= p - 2 * p**2 + 1/4) or ((c.real+1)**2 + c.imag**2 <= 1/16):
        return True


def mandelbrot_function(z, c):
    return (z * z) + c          # return zn+1


w, h = 1920, 1080
s = 30
limit = 250
img = Image.new("RGB", (w*s, h*s))

iteration_counts, c_escaped = mandel_set(w*s, h*s, limit, 2)

img.show()
img.save('image_%01d_%03d.png' % (s, limit), dpi=(200, 200))

import numpy as np
import matplotlib.pyplot as plt


def mandel_set(eta, step, rmax, colour=None):
    c_num = []
    re_bound = np.linspace(-100, 100, eta)
    im_bound = np.linspace(-100, 100, eta)

    for re in re_bound:
        for im in im_bound:
            k = 0
            c = np.complex(re, im)
            z = 0
            print(c)
            while k < step:
                k += 1
                z = mandelbrot_function(z.real, z.imag, c)
                if abs(z) > rmax:
                    break
            if abs(z) < rmax:
                c_num.append(z)
    return c_num


def mandelbrot_function(re, im, c):
    z = np.complex(re, im)
    return (z * z) + c                         # return zn+1


c_num = mandel_set(1000000, 250, 2)

X = [x.real for x in c_num]
Y = [x.imag for x in c_num]
plt.figure(figsize=[8.16, 8.16])
plt.scatter(X, Y, color='red', s=1)
plt.show()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('计算色差')

root.resizable(False, False)
root.geometry('310x100+500+200')

img = Image.new('RGB', (30, 30), (0, 0, 0))
ig = ImageTk.PhotoImage(img)
view1 = Label(root, image = ig)
view1.grid(row = 0, column = 0)
view2 = Label(root, image = ig)
view2.grid(row = 1, column = 0)


def rgb2lab ( inputColor ) :
    num = 0
    RGB = [0, 0, 0]

    for value in inputColor :
        value = float(value) / 255

        if value > 0.04045 :
            value = ( ( value + 0.055 ) / 1.055 ) ** 2.4
        else :
            value = value / 12.92

        RGB[num] = value * 100
        num = num + 1

    XYZ = [0, 0, 0,]

    X = RGB [0] * 0.4124 + RGB [1] * 0.3576 + RGB [2] * 0.1805
    Y = RGB [0] * 0.2126 + RGB [1] * 0.7152 + RGB [2] * 0.0722
    Z = RGB [0] * 0.0193 + RGB [1] * 0.1192 + RGB [2] * 0.9505
    XYZ[ 0 ] = round( X, 4 )
    XYZ[ 1 ] = round( Y, 4 )
    XYZ[ 2 ] = round( Z, 4 )

    XYZ[ 0 ] = float( XYZ[ 0 ] ) / 95.047         # ref_X =  95.047   Observer= 2°, Illuminant= D65
    XYZ[ 1 ] = float( XYZ[ 1 ] ) / 100.0          # ref_Y = 100.000
    XYZ[ 2 ] = float( XYZ[ 2 ] ) / 108.883        # ref_Z = 108.883

    num = 0
    for value in XYZ :

        if value > 0.008856 :
            value = value ** ( 0.3333333333333333 )
        else :
            value = ( 7.787 * value ) + ( 16 / 116 )

        XYZ[num] = value
        num = num + 1

    Lab = [0, 0, 0]

    L = ( 116 * XYZ[ 1 ] ) - 16
    a = 500 * ( XYZ[ 0 ] - XYZ[ 1 ] )
    b = 200 * ( XYZ[ 1 ] - XYZ[ 2 ] )

    Lab [ 0 ] = round( L, 4 )
    Lab [ 1 ] = round( a, 4 )
    Lab [ 2 ] = round( b, 4 )

    return Lab

def checkColor (inputRGB, checkRGB):
    
    for i in range(3):
        inputRGB[i] = min(max(0, inputRGB[i]), 255)
        checkRGB[i] = min(max(0, checkRGB[i]), 255)
    Lab1 = np.array(rgb2lab(inputRGB))
    Lab2 = np.array(rgb2lab(checkRGB))

    return round(np.sqrt(np.sum(np.square(Lab1 - Lab2))), 4)

def getDeltaE ():

    DeltaE.set(checkColor([R1.get(), G1.get(), B1.get()], [R2.get(), G2.get(), B2.get()]))
    
    img1 = ImageTk.PhotoImage(Image.new('RGB', (30, 30), (R1.get(), G1.get(), B1.get())))
    view1.configure(image = img1)
    view1.image = img1

    img2 = ImageTk.PhotoImage(Image.new('RGB', (30, 30), (R2.get(), G2.get(), B2.get())))
    view2.configure(image = img2)
    view2.image = img2
    

R1 = IntVar()
G1 = IntVar()
B1 = IntVar()
R2 = IntVar()
G2 = IntVar()
B2 = IntVar()
DeltaE = StringVar()

Label(root, text = '红(R):', font = ('微软雅黑',9)).grid(row = 0, column = 1)
Label(root, text = '绿(G):', font = ('微软雅黑',9)).grid(row = 0, column = 3)
Label(root, text = '蓝(B):', font = ('微软雅黑',9)).grid(row = 0, column = 5)
Label(root, text = '红(R):', font = ('微软雅黑',9)).grid(row = 1, column = 1)
Label(root, text = '绿(G):', font = ('微软雅黑',9)).grid(row = 1, column = 3)
Label(root, text = '蓝(B):', font = ('微软雅黑',9)).grid(row = 1, column = 5)
Label(root, text = 'ΔE =', font = ('微软雅黑',9)).grid(row = 2, column = 0, sticky = E)

Entry(root, textvariable = R1, width = 5).grid(row = 0, column = 2)
Entry(root, textvariable = G1, width = 5).grid(row = 0, column = 4)
Entry(root, textvariable = B1, width = 5).grid(row = 0, column = 6)
Entry(root, textvariable = R2, width = 5).grid(row = 1, column = 2)
Entry(root, textvariable = G2, width = 5).grid(row = 1, column = 4)
Entry(root, textvariable = B2, width = 5).grid(row = 1, column = 6)

Label(root, textvariable = DeltaE, width = 10).grid(row = 2, column = 1, sticky = W)
Button(root, text = '计算', command = getDeltaE).grid(row = 2, column = 6, sticky = E)


root.mainloop()



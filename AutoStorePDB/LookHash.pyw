#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
import os, hashlib

root = Tk()
root.title('Hash')

filename = StringVar()
filename.set(' ')
filedir = StringVar()
filedir.set(' ')
md5 = StringVar()
md5.set(' ')

def changeFile():
    fn = askopenfilename(title=u"选择文件", filetypes=[('Files(*.exe, *.dll)',['exe', 'dll']), ('All Files(*.*)','*')])
    if os.path.exists(fn): 
        filename.set(os.path.basename(fn))
        filedir.set(os.path.dirname(fn))
        hmd5 = hashlib.md5()
        f = open(fn, 'rb')
        hmd5.update(f.read())
        f.close()
        md5.set(hmd5.hexdigest())
    

Label(root, text = '文件名:').grid(row = 0, column = 0, sticky = W)
Label(root, textvariable = filename).grid(row = 0, column = 1, sticky = E)
Label(root, text = 'Hash值:').grid(row = 1, column = 0, sticky = W)
Entry(root, textvariable = md5).grid(row = 1, column = 1, sticky = E)
Label(root, text = '文件路径:').grid(row = 2, column = 0, sticky = W)
Label(root, textvariable = filedir).grid(row = 2, column = 1, sticky = E)
Button(root, text = "文件选择", command = changeFile).grid(row = 3, column = 1, sticky = E)

root.mainloop()

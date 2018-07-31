#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import os, hashlib, shutil, datetime

root = Tk()
root.title('SetPDBName')

filename = StringVar()
filename.set(' ')
filedir = StringVar()
filedir.set(' ')
md5 = StringVar()
md5.set(' ')


def getFileName():
    fn = askopenfilename(title=u"选择文件", filetypes=[('Files(*.exe, *.dll)',['exe', 'dll']), ('All Files(*.*)','*')])
    if os.path.exists(fn): 
        filename.set(fn)

def getDir():
    fd = askdirectory(title=u'选择存储路径')
    if os.path.isdir(fd):
        filedir.set(fd + '/')

def setPDBName():
    fn = filename.get()
    fpdb = os.path.splitext(filename.get())[0] + '.pdb'
    if os.path.exists(fpdb):
        hmd5 = hashlib.md5()
        f = open(fn, 'rb')
        hmd5.update(f.read())
        md5.set(hmd5.hexdigest())
        f.close()
        target = filedir.get() + datetime.datetime.now().strftime('%m%d') + '_' + hmd5.hexdigest() + '.pdb'
        shutil.copy(fpdb, target)   


Label(root, text = '文件名:').grid(row = 0, column = 0, sticky = W)
Label(root, textvariable = filename).grid(row = 0, column = 1, sticky = E)
Label(root, text = '文件路径:').grid(row = 1, column = 0, sticky = W)
Label(root, textvariable = filedir).grid(row = 1, column = 1, sticky = E)
Label(root, text = 'Hash值:').grid(row = 2, column = 0, sticky = W)
Entry(root, textvariable = md5).grid(row = 2, column = 1, sticky = E)
Button(root, text = "文件选择", command = getFileName).grid(row = 0, column = 3, sticky = E)
Button(root, text = "路径选择", command = getDir).grid(row = 1, column = 3, sticky = E)
Button(root, text = "生成pdb", command = setPDBName).grid(row = 2, column = 3, sticky = E)

root.mainloop()

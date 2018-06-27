# 
# 功能：将当前路径下的pdb拷贝（重新命名为hash值）一份到指定路径
# 前提：在cmd中可以运行python；exe/dll和pdb在相同路径，并且路径文件存在
# 输入参数：无
# 版本：v1.0
#

import os, hashlib, shutil, datetime

# 设置参数
filename = '../x64/Release/CombineModelU.dll'
target = 'F:/PDB_symbols/CombineModel/'

print('FileName:', filename)
print('StoreDir:', target)

# 读取文件hash值
hmd5 = hashlib.md5()
f = open(filename, 'rb')
hmd5.update(f.read())
f.close()
s = hmd5.hexdigest()
target = target + datetime.datetime.now().strftime('%m%d') + '_' + s + '.pdb'

print('FileHash:', s)
a = input('Copy pdb [y/n]?')

# 复制PDB
if a == 'Y' or a == 'y':

    shutil.copy(os.path.splitext(filename)[0] + '.pdb', target)
    os.system('pause')


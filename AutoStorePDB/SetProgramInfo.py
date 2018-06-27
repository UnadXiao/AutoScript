# 
# 功能：更改程序详细信息
# 前提：在cmd中可以运行python命令；路径有空格需要加""。
# 输入参数：P1:文件名（带后缀） P2:附加信息 P3: 附加git Hash值
# 版本：v1.0
#

# 例 python SetProgramInfo.py "project.rc" "RD" "hash"

import sys, os, re, tempfile, shutil, datetime
import subprocess

# 获取参数
source = sys.argv[1]
info = sys.argv[2]

if len(sys.argv) == 4 and sys.argv[3] == 'hash':
    info = info + '-' + subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode("utf-8").replace('\n', '')

info = '"' + info + '-' + datetime.datetime.now().strftime('%y%m%d%H%M') +'"'

print(info)

# 修改文件内容
target = tempfile.gettempdir() + '\\' + os.path.basename(source)
lines = open(source).readlines()
f1 = open(source, 'r')
f2 = open(target, 'w+')
for line in f1:
    f2.write(re.sub(r'\"OriginalFilename\"(.*)\".*\"', r'"OriginalFilename"\1' + info, line))
f2.close()
f1.close()

# 清理文件
shutil.move(target, source)

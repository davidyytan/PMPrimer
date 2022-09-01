'''
创建人员: Nerium
创建日期: 2022/8/31
更改人员: Nerium
更改日期: 2022/8/31
'''

from piece.piecedefine import *

import subprocess, platform

#多序列比对、保守区间遍历、PCR设计等
class piecedesign() :
    def __init__(self, pbase, todo_path, filepath, model='simple') -> None:
        self._todo_path = todo_path
        self.model = model
        self.__platform = platform.system()

        self.filepath = filepath
        self.tmpfile_path = self.filepath.replace('.fasta', '.mc.fasta')

        self._base = pbase

    #subprocess调用muscle进行多序列比对
    def callmuscle(self) :
        cm = subprocess.Popen('{}/{} --align {} --output {}'.format\
            (self._todo_path, PLATFORM_TODO[self.__platform], self.filepath, self.tmpfile_path),\
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cm.wait()
        #self._base.debuglog(BASE_DEBUG_LEVEL1, cm.communicate()[1].decode())
        self._base.baselog(BASE_DEBUG_LEVEL1, 'MUSCLE 多序列比对完成' if cm.returncode == 0 else 'MUSCLE 多序列比对异常')
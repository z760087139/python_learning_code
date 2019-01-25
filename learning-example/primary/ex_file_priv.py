# -*- coding:utf-8 -*-
import os
import stat

os.chmod('d:/file_A', stat.S_IREAD)
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读
# stat.S_IROTH: 其他用户有读权限
# stat.S_IRGRP: 组用户有读权限
# stat.S_IRUSR: 拥有者具有读权限
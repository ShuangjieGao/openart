"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

``os`` 模块包含用于文件系统访问和挂载、终端重定向和复制以及 ``uname`` 和 ``urandom`` 函数的功能。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/os.rst
from __future__ import annotations
from typing import IO, Any, Iterator, Optional, Tuple
from _typeshed import Incomplete
from stdlib.os import *  # type: ignore
class VfsFat():
    """
        请参见 `vfs.VfsFat`。
    """
    def __init__(self, block_dev) -> None:
        ...
class VfsLfs1():
    """
        请参见 `vfs.VfsLfs1`。
    """
    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        ...
class VfsLfs2():
    """
        请参见 `vfs.VfsLfs2`。
    """
    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32, mtime=True) -> None:
        ...
class VfsPosix():
    """
        请参见 `vfs.VfsPosix`。
    """
    def __init__(self, root=None) -> None:
        ...
def uname() -> uname_result:
    """
       返回一个元组（可能是一个命名元组），其中包含关于底层机器和/或其操作系统的信息。元组按照以下顺序有五个字段，每个字段都是一个字符串：
    
            * ``sysname`` -- 底层系统的名称
            * ``nodename`` -- 网络名称（可以与 ``sysname`` 相同）
            * ``release`` -- 底层系统的版本
            * ``version`` -- MicroPython 版本和构建日期
            * ``machine`` -- 底层硬件的标识符（例如板子、CPU）
    """
    ...
def urandom(n) -> bytes:
    """
       返回一个包含 *n* 个随机字节的字节对象。尽可能使用硬件随机数生成器生成。
    """
    ...
def chdir(path) -> Incomplete:
    """
       更改当前目录。
    """
    ...
def getcwd() -> Incomplete:
    """
       获取当前目录。
    """
    ...
def ilistdir(dir: Optional[Any]=None) -> Iterator[Tuple]:
    """
       此函数返回一个迭代器，然后产生与其正在列出的目录中的条目对应的元组。如果没有参数，则列出当前目录，否则列出由*dir*给定的目录。
    
       元组的形式为 *(name, type, inode[, size])*:
    
        - *name*是一个字符串（如果 *dir* 是一个字节对象，则是字节）并且是条目的名称;
        - *type* 是一个整数，指定条目的类型，对于目录为0×4000，对于常规文件为0×8000;
        - *inode* 是文件的inode对应的整数，对于没有此概念的文件系统可能为0。
        - 一些平台可能返回包含条目的*size*的4元组。对于文件条目，*size*是一个表示文件大小的整数，如果大小未知则为-1。对于目录条目，其含义目前未定义。
    """
    ...
def listdir(dir: Optional[Any]=None) -> Incomplete:
    """
       如果没有参数，则列出当前目录。否则列出给定目录。
    """
    ...
def mkdir(path) -> Incomplete:
    """
       创建一个新的目录。
    """
    ...
def remove(path) -> None:
    """
       删除一个文件。
    """
    ...
def rmdir(path) -> None:
    """
       删除一个目录。
    """
    ...
def rename(old_path, new_path) -> None:
    """
       重命名一个文件。
    """
    ...
def stat(path) -> Incomplete:
    """
       获取文件或目录的状态。
    """
    ...
def statvfs(path) -> Tuple:
    """
       获取系统文件的状态。
    
       返回一个元组，其中包含以下顺序的文件系统信息：
    
            * ``f_bsize`` -- 文件系统块大小
            * ``f_frsize`` -- 片段大小
            * ``f_blocks`` -- 以f_frsize为单位的fs大小
            * ``f_bfree`` -- 空闲块数
            * ``f_bavail`` -- 非特权用户使用的空闲块数
            * ``f_files`` -- inode 数量
            * ``f_ffree`` -- 空闲 inode 数量
            * ``f_favail`` -- 非特权用户的可用空闲 inode 数量
            * ``f_flag`` -- 挂载标志
            * ``f_namemax`` -- 最大文件名长度
    
       与 inode 相关的参数：``f_files``、``f_ffree``、``f_avail`` 和 ``f_flags`` 参数可能返回 ``0``，因为它们可能在移植版本特定的实现中不可用。
    """
    ...
def sync() -> None:
    """
       同步所有文件系统。
    """
    ...
def dupterm(stream_object, index=0, ) -> IO:
    """
       复制或切换给定的 :std:term:`stream` 类对象上的 MicroPython 终端（REPL）。*stream_object* 参数必须是本机流对象，或派生自 ``io.IOBase`` 并实现 ``readinto()`` 和 ``write()`` 方法。流应处于非阻塞模式，如果没有数据可用于读取，则 ``readinto()`` 应返回 ``None``。
    
       调用此函数后，所有终端输出都会在此流上重复，任何可用于流上的输入都会传递到终端输入。
    
       *index* 参数应为非负整数，并指定设置的复制槽。给定移植版本可能实现多个槽（槽 0 总是可用），在这种情况下，终端输入和输出会复制到所有设置的槽上。
    
       如果将 ``None`` 作为 *stream_object* 传递，则在给定的 *index* 槽上取消复制。
    
       函数返回给定槽中的以前的类似流对象。
    """
    ...
def mount(fsobj, mount_point, *, readonly=False) -> Incomplete:
    """
        请参见 `vfs.mount`。
    """
    ...
def umount(mount_point) -> Incomplete:
    """
        请参见 `vfs.umount`。
    """
    ...

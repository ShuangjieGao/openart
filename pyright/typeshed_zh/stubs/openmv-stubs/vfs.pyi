"""
Virtual filesystem control.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/vfs.html

``vfs`` 模块包含用于创建文件系统对象以及在虚拟文件系统中挂载/卸载它们的函数。

文件系统挂载
-------------------

某些端口提供虚拟文件系统（VFS）功能，并能够在该 VFS 中挂载多个“真实”文件系统。文件系统对象可以挂载在 VFS 的根目录或根目录下的子目录中。这允许动态和灵活地配置 Python 程序所看到的文件系统。具有此功能的端口提供 :func:`mount` 和 :func:`umount` 函数，并可能提供由 VFS 类表示的各种文件系统实现。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/vfs.rst
from __future__ import annotations
from typing import Optional
from _typeshed import Incomplete
class VfsFat():
    """
        创建一个使用 FAT 文件系统格式的文件系统对象。FAT 文件系统的存储由 *block_dev* 提供。通过此构造函数创建的对象可以使用 :func:`mount` 进行挂载。
    """
    def __init__(self, block_dev) -> None:
        ...
    @staticmethod
    def mkfs(block_dev) -> None:
        """
                在 *block_dev* 上构建一个 FAT 文件系统。
        """
        ...
class VfsLfs1():
    """
        创建一个使用 `littlefs v1 文件系统格式`_ 的文件系统对象。littlefs 文件系统的存储由 *block_dev* 提供，*block_dev* 必须支持 :ref:`扩展接口 <block-device-interface>`。通过此构造函数创建的对象可以使用 :func:`mount` 进行挂载。
    
        有关更多信息，请参见 :ref:`filesystem`。
    """
    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        ...
    @staticmethod
    def mkfs(block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        """
                在 *block_dev* 上构建一个 Lfs1 文件系统。
        
            ``Note:`` 有报告显示 littlefs v1 在某些情况下会失败，详细信息请参见 `littlefs issue 347`_。
        """
        ...
class VfsLfs2():
    """
        创建一个使用 `littlefs v2 文件系统格式`_ 的文件系统对象。littlefs 文件系统的存储由 *block_dev* 提供，*block_dev* 必须支持 :ref:`扩展接口 <block-device-interface>`。通过此构造函数创建的对象可以使用 :func:`mount` 进行挂载。
    
        *mtime* 参数启用文件的修改时间戳，这些时间戳使用 littlefs 属性存储。此选项可以在每次挂载时启用或禁用，并且只有在启用 *mtime* 时，时间戳才会被添加或更新，否则时间戳将保持不变。没有时间戳的 Littlefs v2 文件系统可以在不重新格式化的情况下工作，一旦文件被打开进行写入，时间戳将自动添加到现有文件。启用 *mtime* 后，针对没有时间戳的文件，`os.stat` 将返回 0 作为时间戳。
    
        有关更多信息，请参见 :ref:`filesystem`。
    """
    def __init__(self, block_dev, readsize=32, progsize=32, lookahead=32, mtime=True) -> None:
        ...
    @staticmethod
    def mkfs(block_dev, readsize=32, progsize=32, lookahead=32) -> None:
        """
                在 *block_dev* 上构建一个 Lfs2 文件系统。
        
            ``Note:`` 有报告显示 littlefs v2 在某些情况下会失败，详细信息请参见 `littlefs issue 295`_。
        """
        ...
class VfsPosix():
    """
        创建一个访问主机 POSIX 文件系统的文件系统对象。如果指定了 *root*，则它应该是主机文件系统中用作 ``VfsPosix`` 对象根目录的路径。否则，将使用主机文件系统的当前目录。
    """
    def __init__(self, root=None) -> None:
        ...
class AbstractBlockDev():
    """
        构造一个块设备对象。构造函数的参数依赖于特定的块设备。
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete:
        """
                第一种形式读取对齐的块的倍数。从由 *block_num* 索引指定的块开始，将块从设备读取到 *buf*（一个字节数组）中。要读取的块数由 *buf* 的长度给出，且该长度将是块大小的倍数。
        
                第二种形式允许在块内的任意位置读取，并且支持任意长度。从块索引 *block_num* 开始，及该块内的字节偏移 *offset*，将字节从设备读取到 *buf*（一个字节数组）中。要读取的字节数由 *buf* 的长度给出。
        """
        ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Incomplete:
        """
                第一种形式写入对齐的块的倍数，并要求在写入之前，必须先通过此方法擦除（如果需要）要写入的块。从由 *block_num* 索引指定的块开始，将 *buf*（一个字节数组）中的块写入设备。要写入的块数由 *buf* 的长度给出，且该长度将是块大小的倍数。
        
                第二种形式允许在块内的任意位置写入，并且支持任意长度。只有正在写入的字节会被更改，调用此方法的代码必须确保通过之前的 ``ioctl`` 调用擦除了相关的块。从块索引 *block_num* 开始，及该块内的字节偏移 *offset*，将字节从 *buf*（一个字节数组）写入设备。要写入的字节数由 *buf* 的长度给出。
        
                请注意，如果指定了偏移量参数（即使是零），实现必须永远不隐式擦除块。
        """
        ...
    def ioctl(self, op, arg) -> int:
        """
                控制块设备并查询其参数。要执行的操作由 *op* 给出，*op* 是以下整数之一：
        
                  - 1 -- 初始化设备（*arg* 未使用）
                  - 2 -- 关闭设备（*arg* 未使用）
                  - 3 -- 同步设备（*arg* 未使用）
                  - 4 -- 获取块的数量，应返回一个整数（*arg* 未使用）
                  - 5 -- 获取块中的字节数，应返回一个整数，或者返回 ``None``，在这种情况下将使用默认值 512（*arg* 未使用）
                  - 6 -- 擦除一个块，*arg* 是要擦除的块号
        
               最少需要拦截 ``ioctl(4, ...)``；对于 littlefs，还必须拦截 ``ioctl(6, ...)``。其他的需求取决于硬件。
        
               在任何调用 ``writeblocks(block, ...)`` 之前，littlefs 会发出 ``ioctl(6, block)``。这使得设备驱动程序在写入之前擦除块（如果硬件要求的话）。或者，驱动程序可以拦截 ``ioctl(6, block)`` 并返回 0（成功）。在这种情况下，驱动程序负责检测是否需要擦除。
        
               除非另有说明，``ioctl(op, arg)`` 可以返回 ``None``。因此，实现可以忽略未使用的 ``op`` 值。当 ``op`` 被拦截时，操作 4 和 5 的返回值如上所述。其他操作应返回 0 表示成功，返回非零值表示失败，返回的值应为 ``OSError`` 错误号代码。
        """
        ...
def mount(fsobj, mount_point, *, readonly=False) -> Incomplete:
    """
        将文件系统对象 *fsobj* 挂载到 VFS 中由 *mount_point* 字符串指定的位置。*fsobj* 可以是具有 ``mount()`` 方法的 VFS 对象，也可以是块设备。如果是块设备，则会自动检测文件系统类型（如果未识别文件系统，则会引发异常）。*mount_point* 可以是 ``'/'``，表示将 *fsobj* 挂载到根目录，也可以是 ``'/<name>'``，表示将其挂载到根目录下的子目录。
    
        如果 *readonly* 为 ``True``，则文件系统以只读模式挂载。
    
        在挂载过程中，会调用文件系统对象的 ``mount()`` 方法。
    
        如果 *mount_point* 已经被挂载，将引发 ``OSError(EPERM)``。
    """
    ...
def umount(mount_point) -> Incomplete:
    """
        卸载文件系统。*mount_point* 可以是一个表示挂载位置的字符串，或者是一个之前已挂载的文件系统对象。在卸载过程中，会调用文件系统对象的 ``umount()`` 方法。
    
        如果未找到 *mount_point*，将引发 ``OSError(EINVAL)``。
    """
    ...

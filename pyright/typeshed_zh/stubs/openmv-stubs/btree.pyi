"""
Simple BTree database.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/btree.html

``btree`` 模块使用外部储存（磁盘文件，或在一般情况下为随机访问流）实现简单的键值数据库。键排序储存在数据库中，除对单个键值的有效检索外，数据库还支持高效的有序范围扫描（使用给定范围内的键来检索值）。在应用程序接口方面，B树数据库尽可能以与标准 `dict` 类型工作方式相似的方式运行，一个明显区别是键和值都须为 `bytes` 对象（因此，若您想要储存其他类型的对象，需首先将之序列化为 `bytes` ）。

该模块基于著名的BerkelyDB 库的1.xx版本。

例子::

    import btree

    # First, we need to open a stream which holds a database
    # This is usually a file, but can be in-memory database
    # using io.BytesIO, a raw flash partition, etc.
    # Oftentimes, you want to create a database file if it doesn't
    # exist and open if it exists. Idiom below takes care of this.
    # DO NOT open database with "a+b" access mode.
    try:
        f = open("mydb", "r+b")
    except OSError:
        f = open("mydb", "w+b")

    # Now open a database itself
    db = btree.open(f)

    # The keys you add will be sorted internally in the database
    db[b"3"] = b"three"
    db[b"1"] = b"one"
    db[b"2"] = b"two"

    # Assume that any changes are cached in memory unless
    # explicitly flushed (or database closed). Flush database
    # at the end of each "transaction".
    db.flush()

    # Prints b'two'
    print(db[b"2"])

    # Iterate over sorted keys in the database, starting from b"2"
    # until the end of the database, returning only values.
    # Mind that arguments passed to values() method are *key* values.
    # Prints:
    #   b'two'
    #   b'three'
    for word in db.values(b"2"):
        print(word)

    del db[b"2"]

    # No longer true, prints False
    print(b"2" in db)

    # Prints:
    #  b"1"
    #  b"3"
    for key in db:
        print(key)

    db.close()

    # Don't forget to close the underlying stream!
    f.close()
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/btree.rst
from __future__ import annotations
from typing import Any, Dict, Optional
from _typeshed import Incomplete
INCL: Incomplete
"""\
`keys()`, `values()`, `items()` 方法的标记, 指定扫描应该包含结束键。
"""
DESC: Incomplete
"""\
`keys()`, `values()`, `items()` 方法的标记, 指定扫描应按照键的下行方向进行。
"""
class btree():
    """ """
    def close(self) -> None:
        """
           关闭数据库。处理结束时关闭数据库是强制性的，因为某些未写入的数据可能仍留在缓存中。注意：这并不会关闭随数据库打开的基础流，基础流应单独关闭（这也是强制性的，以确保从缓冲区中刷新的数据进入底层储存）。
        """
        ...
    def flush(self) -> Incomplete:
        """
           将缓存中的任何数据刷新到底层流。
        """
        ...
    def __getitem__(self, key) -> Incomplete:
        """
           标准字典方法。
        """
        ...
    def get(self, key, default=None, ) -> Incomplete:
        """
           标准字典方法。
        """
        ...
    def __setitem__(self, key, val) -> Incomplete:
        """
           标准字典方法。
        """
        ...
    def __delitem__(self, key) -> Incomplete:
        """
           标准字典方法。
        """
        ...
    def __contains__(self, key) -> Incomplete:
        """
           标准字典方法。
        """
        ...
    def __iter__(self) -> Incomplete:
        """
           BTree对象可被直接迭代（与字典相似）以按顺序访问所有键。
        """
        ...
    def keys(self, start_key, end_key, flags: Optional[Any]=None) -> Incomplete:
        """
           这些方法类似于标准字典方法，但也可使用可选参数来迭代一个键子范围，而不是整个数据库。注意：这三种方法中， *start_key* 和 *end_key* 参数都代表键值。例如， ``values()`` 方法将迭代与给定键范围对应的值。无 *start_key* 值即意为“从首个键”，无 *end_key* 值或其值为None则意为“直到数据库结束”。默认情况下，范围包括 *start_key* ，而不包括 *end_key* ，您可以通过传递 `btree.INCL` 的标记来将 *end_key* 包括在迭代中。您可以通过传递 `btree.DESC` 的标记来按照下行键方向进行迭代。标记值可同为ORed。
        """
        ...
    def values(self, start_key, end_key, flags: Optional[Any]=None) -> Incomplete:
        """
           这些方法类似于标准字典方法，但也可使用可选参数来迭代一个键子范围，而不是整个数据库。注意：这三种方法中， *start_key* 和 *end_key* 参数都代表键值。例如， ``values()`` 方法将迭代与给定键范围对应的值。无 *start_key* 值即意为“从首个键”，无 *end_key* 值或其值为None则意为“直到数据库结束”。默认情况下，范围包括 *start_key* ，而不包括 *end_key* ，您可以通过传递 `btree.INCL` 的标记来将 *end_key* 包括在迭代中。您可以通过传递 `btree.DESC` 的标记来按照下行键方向进行迭代。标记值可同为ORed。
        """
        ...
    def items(self, start_key, end_key, flags: Optional[Any]=None) -> Incomplete:
        """
           这些方法类似于标准字典方法，但也可使用可选参数来迭代一个键子范围，而不是整个数据库。注意：这三种方法中， *start_key* 和 *end_key* 参数都代表键值。例如， ``values()`` 方法将迭代与给定键范围对应的值。无 *start_key* 值即意为“从首个键”，无 *end_key* 值或其值为None则意为“直到数据库结束”。默认情况下，范围包括 *start_key* ，而不包括 *end_key* ，您可以通过传递 `btree.INCL` 的标记来将 *end_key* 包括在迭代中。您可以通过传递 `btree.DESC` 的标记来按照下行键方向进行迭代。标记值可同为ORed。
        """
        ...
def open(stream, *, flags=0, pagesize=0, cachesize=0, minkeypage=0) -> Dict:
    """
       从随机存取的 :std:term:`stream` （类似一个打开的文件）中打开一个数据库。所有其他的参数都是可选的，且都只为关键字，并允许对数据库操作的高级参数进行调整（大多数用户并不会需要这个）:
    
       * *flags* - 当前未使用的。
       * *pagesize* - B树中用于节点的页面大小。可接受范围为512-65536。若为0，则会使用基础I/O块的大小（内存使用和性能之间的最佳协调）。
       * *cachesize* - 以字节计的建议最大内存缓存大小。对于一个由充足内存的板而言，使用更大值或许可以提高性能。该值只是推荐值，若该值设置过低，则模块可能会占用更多内存。
       * *minkeypage* - 每个页面存储的键的最小数量。默认值为0等于2。
    
       返回一个BTree对象，该对象实现一个字典协议（方法集）和下述的一些附加方法。
    """
    ...

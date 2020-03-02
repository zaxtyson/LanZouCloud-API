from typing import List

__all__ = ['FileList', 'FolderList']


class ItemList:
    """具有 name, id 属性对象的列表"""
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"<List {', '.join(it.__str__() for it in self)}>"

    def __lt__(self, other):
        """用于路径 List 之间排序"""
        return '/'.join(i.name for i in self) < '/'.join(i.name for i in other)

    @property
    def name_id(self):
        """所有 item 的 name-id 列表，兼容旧版"""
        return {it.name: it.id for it in self}

    def append(self, file):
        """插入元素"""
        self._items.append(file)

    def filter(self, condition) -> list:
        """筛选出满足条件的 item
        condition(item) -> True
        """
        return [it for it in self if condition(it)]

    def find_by_name(self, name: str):
        """使用文件名搜索(仅返回首个匹配项)"""
        for item in self:
            if name == item.name:
                return item
        return None

    def find_by_id(self, fid: int):
        """使用 id 搜索(精确)"""
        for item in self:
            if fid == item.id:
                return item
        return None

    def pop_by_id(self, fid):
        for item in self:
            if item.id == fid:
                self._items.remove(item)
                return item
        return None


class FileList(ItemList):
    """文件列表类"""
    pass


class FolderList(ItemList):
    """文件夹列表类"""
    pass

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    def __init__(self, max_taste: int):
        self.size = max_taste
        self.tree = [0] * (4 * self.size)


    def update(self, node: int, start: int, end: int, target_idx: int, diff: int) -> None:
        """
        특정 맛의 사탕 개수를 업데이트
            target_idx: 특정 맛
            diff: 사탕 개수 업데이트 양
        """
        if target_idx < start or target_idx > end:
            return
        
        self.tree[node] += diff
        
        if start != end:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, target_idx, diff)
            self.update(node * 2 + 1, mid + 1, end, target_idx, diff)


    def kth(self, node: int, start: int, end: int, k: int) -> int:
        """
        k번째로 맛있는 사탕의 맛 번호 반환
        """
        if start == end:
            return start
        
        mid = (start + end) // 2
        left_count = self.tree[node * 2]
        
        if k <= left_count:
            return self.kth(node * 2, start, mid, k)
        
        else:
            return self.kth(node * 2 + 1, mid + 1, end, k - left_count)


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()
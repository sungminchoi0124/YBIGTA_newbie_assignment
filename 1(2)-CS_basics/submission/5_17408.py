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


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()
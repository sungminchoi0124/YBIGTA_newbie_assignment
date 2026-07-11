from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        curr_idx = 0  
        
        for item in seq:
            found_idx = -1

            for child_idx in self[curr_idx].children:
                if self[child_idx].body == item:
                    found_idx = child_idx
                    break
            
            if found_idx == -1:
                new_node = TrieNode(body=item)
                self.append(new_node)
                new_idx = len(self) - 1
                
                self[curr_idx].children.append(new_idx)
                
                curr_idx = new_idx
            
            else:
                curr_idx = found_idx

        self[curr_idx].is_end = True

    # 구현하세요!
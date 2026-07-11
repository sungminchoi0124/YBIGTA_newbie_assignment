from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    input = sys.stdin.readline
    
    taste = 1000000
    
    seg_tree = SegmentTree[int, int](taste)
    
    n_str = input().strip()
    n = int(n_str)
    
    for _ in range(n):
        
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            rank = query[1]
            taste_idx = seg_tree.kth(1, 1, taste, rank)
            print(taste_idx)
            seg_tree.update(1, 1, taste, taste_idx, -1)
            
        elif query[0] == 2:
            taste_idx = query[1]
            count_diff = query[2]
            seg_tree.update(1, 1, taste, taste_idx, count_diff)

if __name__ == "__main__":
    main()
from lib import Trie
import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    """
    이름을 배열하는 경우의 수를 출력
    """
    # 구현하세요!
    input_data = sys.stdin.read().split()
    
    N = int(input_data[0])
    names = input_data[1:]
    
    trie: Trie[int] = Trie()
    
    for name in names:
        seq = [ord(c) - 65 for c in name]
        trie.push(seq)
        
    MOD = 1_000_000_007
    
    fact = [1] * 30
    for i in range(1, 30):
        fact[i] = (fact[i - 1] * i) % MOD
    
    ans = 1
    
    for node in trie:
        count = len(node.children)
        
        if node.is_end:
            count += 1
        
        ans = (ans * fact[count]) % MOD
        
    print(ans)


if __name__ == "__main__":
    main()
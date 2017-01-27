import sys

alice = list(map(int,raw_input().strip().split()))
bob = list(map(int,raw_input().strip().split()))
ascore=len([1 for a,b in zip(alice,bob) if a>b])
bscore=len([1 for a,b in zip(alice,bob) if b>a])
print ascore,bscore

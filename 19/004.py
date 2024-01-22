def stone_piles(n):
    stones = []
    for i in range(n):
        stones.append(n + 2*i)
    return stones

print(stone_piles(2))
print(stone_piles(10))
print(stone_piles(3))
print(stone_piles(17))
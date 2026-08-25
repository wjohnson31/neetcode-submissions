class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            biggest1 = -heapq.heappop(stones)
            biggest2 = -heapq.heappop(stones)

            if biggest1 != biggest2:
                heapq.heappush(stones, -(biggest1 - biggest2))

        return 0 if not stones else -stones[0]
class MedianFinder:

    def __init__(self):
        self.small = [] # smaller half, as negatives, to access largest of smalls
        self.large = [] # larger half, by default minheap so direct access to smallest

    def addNum(self, num: int) -> None:
        # first add to large by default
        heapq.heappush(self.large, num) 
        # then shift smallest from large to small, as a negative (to access largest from small)
        heapq.heappush(self.small, -heapq.heappop(self.large)) 
        # if large has less, rebalance
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
    def findMedian(self) -> float:
        # if large has 1 more then return its smallest value
        if len(self.large) > len(self.small):
            return float(self.large[0])
        # otherwise return the mean of the 2, largest of small and smallest of large
        return (self.large[0] + -self.small[0]) / 2
        
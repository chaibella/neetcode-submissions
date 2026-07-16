class MedianFinder:

    def __init__(self):
        self.small = [] # smaller half, as negatives to access largest from minheap
        self.large = [] # larger half, by default minheap with access to smallest

    def addNum(self, num: int) -> None:
        # first default add new num to one of two, let's say large
        heapq.heappush(self.large, num)
        # then move smallest from the large to small
        heapq.heappush(self.small, -heapq.heappop(self.large))
        # then if large has less than small, rebalance
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # don't forget to negate num when pushing to small, to access its largest
        # and of course undo the negation if/when shifting back to large

    def findMedian(self) -> float:
        # if large has more, then its smallest is the median
        if len(self.large) > len(self.small):
            return float(self.large[0])
        # otherwise take largest of small and smallest of large and return its mean
        return (-self.small[0] + self.large[0]) / 2
        # dont forget to undo negation from small
        
        
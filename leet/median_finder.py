import heapq

class MedianFinder:
    def __init__(self):

        self.small, self.large = [], []


    def add(self, num: int) -> None:

        # -1 to make heapq behave like max heap
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and
            (-1 * self.small[0]) > self.large[0]):

            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            print("small larger\n")
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:

            print("large smaller\n")
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def get_median(self) -> float:

        if len(self.small) > len(self.large):
            return self.small[0] * -1

        if len(self.large) > len(self.small):
            return self.large[0]

        return (self.large[0] + self.small[0] * -1) / 2


m_finder = MedianFinder()

m_finder.add(1)
m_finder.add(2)
m_finder.add(3)
m_finder.add(4)
m_finder.add(5)
m_finder.add(7)
m_finder.add(8)
m_finder.add(10)
m_finder.add(8)
print(m_finder.small)
print(m_finder.large)
#m_finder.add(9)
# m_finder.add(10)
# m_finder.add(15)

print(m_finder.get_median())

# t = []
#
# heapq.heappush(t, 3)
# heapq.heappush(t, 1)
# heapq.heappush(t, 5)
# heapq.heappush(t, 2)
# print(t)
#

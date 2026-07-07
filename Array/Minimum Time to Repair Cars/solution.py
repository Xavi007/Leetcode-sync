class Solution:
    def can_reaper(self, ranks, cars, time):
            reaperd_cars = 0
            for rank in ranks:
                reaperd_cars += int(math.sqrt(time // rank))
            return cars <= reaperd_cars 

    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, int(min(ranks) * math.pow(cars, 2))
        while l < r:
            mid = (l + r) // 2
            if self.can_reaper(ranks, cars, mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        
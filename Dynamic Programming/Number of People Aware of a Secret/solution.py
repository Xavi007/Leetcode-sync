class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        population = [0]*forget
        population[0] = 1
        for i in range(1,n):
            population = [0] + population[:-1]
            population[0] = sum(population[delay:forget])
        totpop = sum(population)
        return totpop%(7+10**9)
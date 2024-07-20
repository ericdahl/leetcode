class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        max_pop = -1
        max_year = -1

        for year in range(1950, 2051):
            current_population = 0

            for log in logs:
                if log[0] <= year and log[1] > year:
                    current_population += 1

            if current_population > max_pop:
                max_pop = current_population
                max_year = year

        return max_year

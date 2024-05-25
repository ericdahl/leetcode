class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # tasks isn't sorted by enqueue time, so we do that here and also persist
        # the original indexes
        tasks = [(t[0], t[1], t_i) for (t_i, t) in enumerate(tasks)]
        tasks.sort()

        # iterating through tasks without modification is faster, but less clear code
        current_time = 1
        q = []
        order = []

        while tasks or q:
            
            while tasks and tasks[0][0] <= current_time:
                t = tasks.pop(0)
                heapq.heappush(q, (t[1], t[2]))

            if q:
                task = heapq.heappop(q)
                # do work
                current_time += task[0]
                order.append(task[1])
            
            if not q and tasks and current_time < tasks[0][0]:
                current_time = tasks[0][0]

        return order

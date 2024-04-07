class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        user_activity = defaultdict(set)
        for (user_id, time) in logs:
            user_activity[user_id].add(time)

        result = [0] * k
        for user_id in user_activity.keys():
            uam = len(user_activity[user_id])
            result[uam - 1] += 1

        return result
        

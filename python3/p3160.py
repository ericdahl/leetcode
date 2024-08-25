class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        answer = []
        ball_color = {}
        color_balls = defaultdict(set)
        for (q_ball, q_color) in queries:


            # if ball already has a color, remove old entry and update color tracking
            if q_ball in ball_color:
                old_color = ball_color[q_ball]

                if old_color != q_color:
                    color_balls[old_color].remove(q_ball)
                    if not color_balls[old_color]:
                        # if empty set, remove it to allow len() to work on dict
                        del color_balls[old_color]

            ball_color[q_ball] = q_color
            color_balls[q_color].add(q_ball)
            answer.append(len(color_balls))


        return answer

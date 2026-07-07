class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
             ball_color = {}   
             color_freq = {}
             res = []   

             for query in queries:
                 ball, color = query

     
                 if ball in ball_color:
                     old_color = ball_color[ball]
                     color_freq[old_color] -= 1
                     if color_freq[old_color] == 0:
                         del color_freq[old_color]

                 ball_color[ball] = color

        
                 if color in color_freq:
                      color_freq[color] += 1
                 else:
                     color_freq[color] = 1

        
                 res.append(len(color_freq))

             return res

        
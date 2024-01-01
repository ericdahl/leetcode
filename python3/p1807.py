class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        d = defaultdict(lambda: '?')
        for pair in knowledge:
            d[pair[0]] = pair[1]

        result = []

        # maybe faster to not convert s to list
        # seemed like maybe simpler logic
        s = list(s)
        while s:
            c = s.pop(0)
            if c == '(':
                key = []
                while s[0] != ')':
                    key.append(s.pop(0))
                s.pop(0) # drop the )
                for vc in d[''.join(key)]:
                    result.append(vc)
            else:
                result.append(c)

        return ''.join(result)

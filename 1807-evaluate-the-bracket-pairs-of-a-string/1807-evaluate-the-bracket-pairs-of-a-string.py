class Solution:
    def evaluate(self, s: str, k: list[list[str]]) -> str:
        mp = {}
        n_k = len(k)
        for i in range(n_k):
            mp[k[i][0]] = k[i][1]
        print(mp)
        n_s = len(s)
        ans = []
        i = 0
        while i < n_s:
            if s[i] == '(':
                i += 1
                key = []
                while s[i] != ')':
                    key.append(s[i])
                    i += 1

                key = ''.join(key)
                ans.append(mp.get(key, '?'))
                i += 1

            else:
                ans.append(s[i])
                i += 1
        return ''.join(ans)
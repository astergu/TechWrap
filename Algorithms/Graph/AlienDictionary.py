"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
"""


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words_set = set(words)
        if len(words_set) == 1 and len(words[0]) == 1:
            return words[0]

        all_chars = set()
        orders = []
        for i in xrange(len(words) - 1):
            order = self.cmp_neighbor(words[i], words[i + 1])
            if order[0] is not None:
                orders.append(order)

        from collections import defaultdict
        imap, rmap = defaultdict(list), defaultdict(list)
        for k, v in orders:
            imap[k].append(v)
            rmap[v].append(k)
            all_chars.add(k)
            all_chars.add(v)

        import json
        ans = []
        num_chars = len(all_chars)
        while len(ans) != num_chars:
            next = self.find_next(all_chars, imap, rmap)
            if next is None:
                return ""
            right = imap[next]
            imap.pop(next, None)
            for key in right:
                rmap[key].remove(next)
                if not rmap[key]:
                    rmap.pop(key, None)
            ans.append(next)
            all_chars.remove(next)
        return ''.join(ans)


    def cmp_neighbor(self, a, b):
        min_len = min(len(a), len(b))
        for i in xrange(min_len):
            if a[i] != b[i]:
                return (a[i], b[i])
        return (None, None)

    def find_next(self, all_chars, imap, rmap):
        rvalues = rmap.keys()
        for c in all_chars:
            if c not in rvalues:
                return c
        return None


if __name__ == '__main__':
    words = ["zy","zx"]
    s = Solution()
    output = s.alienOrder(words)
    print output

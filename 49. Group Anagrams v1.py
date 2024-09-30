class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_set = {}
        for word in strs: # n words
            word_set = [0] * 26
            for char in word: # m chars
                word_set[ord(char)-ord("a")] += 1
            word_set = tuple(word_set)
            if word_set not in result_set:
                result_set[word_set] = [word]
            else:
                result_set[word_set].append(word)
        return list(result_set.values())
        # Time: O(n * m)
        # Space: O(n * m)

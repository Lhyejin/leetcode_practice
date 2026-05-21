class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        # method 1 
        # len_word1, len_word2 = len(word1), len(word2) 
        # last = "" 
        # remain_idx = abs(len_word1 - len_word2) 
        # if len_word1 > len_word2: 
        #     last = word1[-remain_idx:] 
        # elif len_word2 > len_word1: 
        #     last = word2[-remain_idx:] 
        #     for i, j in zip(word1, word2): 
        #         answer += i + j 
        # return answer + last

        # method 최적
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            answer.append(word1[i])
            answer.append(word2[i])
        
        answer.append(word1[min_length:])
        answer.append(word2[min_length:])
        return "".join(answer)
        
class Solution:
    def reverseVowels(self, s: str) -> str:
        # save vowel index and character
        # reverse vowel and replace
        s_arr = list(s)
        vowel_idx_arr = []
        vowel_arr = []
        for i, char in enumerate(s):
            # check vowel
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowel_idx_arr.append(i)
                vowel_arr.append(char)
        vowel_arr = vowel_arr[::-1]
        vowel_dict = {k: v for k, v in zip(vowel_idx_arr, vowel_arr)}
        for i in vowel_dict.keys():
            s_arr[i] = vowel_dict[i]

        # optimized solution
        # vowels = set('aeiouAEIOU')
        # s_arr = list(s)
        # left, right = 0, len(s_arr) - 1
        # while left < right:
        #     while left < right and s_arr[left] not in vowels:
        #         left += 1
        #     while left < right and s_arr[right] not in vowels:
        #         right -= 1
        #     s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
        #     left += 1
        #     right -= 1
        return "".join(s_arr)

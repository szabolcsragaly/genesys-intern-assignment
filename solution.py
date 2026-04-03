from typing import List

class Solution:
    def combinations(self, digits: str) -> List[str]:       # returns all possible letter combinations that the given digits could represent
        
        if not digits:
            return []

        if len(digits) > 4:       # input validation, for the constaints mentioned in the task
            raise ValueError("Maximum length is 4")

        if any(d not in "23456789" for d in digits):
            raise ValueError("Digits must be between 2 and 9")

        mapping = {             # we map the digits to letters, just like on the telephone buttons
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str):      # I chose backtracking instead of an iterative function
            if index == len(digits):
                result.append(path)
                return
            current_digit = digits[index]
            for letter in mapping[current_digit]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
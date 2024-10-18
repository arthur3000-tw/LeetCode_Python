class Solution:
    def isValid(self, s: str) -> bool:
        check_deque = deque()
        for char in s:
            if char == "(" or char == "[" or char == "{":
                check_deque.append(char)
            else:
                if len(check_deque) == 0:
                    return False
                pop_char = check_deque.pop()
                if char == ")":
                    if pop_char != "(":
                        return False
                elif char == "]":
                    if pop_char != "[":
                        return False
                elif char == "}":
                    if pop_char != "{":
                        return False
        if len(check_deque) == 0:
            return True
        else:
            return False

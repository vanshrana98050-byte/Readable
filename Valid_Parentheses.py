s = input()

stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            print("Invalid")
            break
        stack.pop()
else:
    if stack:
        print("Invalid")
    else:
        print("Valid")
n = int(input())

def generate(opened, closed, current):

    if len(current) == 2 * n:
        print(current)
        return

    if opened < n:
        generate(opened + 1, closed, current + "(")

    if closed < opened:
        generate(opened, closed + 1, current + ")")

generate(0, 0, "")
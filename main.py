while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    if not (1 <= d or d < n or n <= 10 ** 5):
        raise RuntimeError("Formato inválido: (1 ≤ D < N ≤ 10^5)")

    num = input().strip()
    if len(str(num)) != n:
        raise RuntimeError("A quantida de dígitos (n), não corresponde ao número inserido: (1 ≤ D < N ≤ 10^5)")

    stack = []
    for digit in num:
        while d > 0 and stack and stack[-1] < digit:
            stack.pop()
            d -= 1
        stack.append(digit)

    stack = stack[:-d] if d > 0 else stack
    result = ''.join(stack)
    print(result)

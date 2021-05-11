from math import sin

def func(x):
    return sin(x) / x

def method_of_rectangles(f, a: int, b: int, nseg: int,method = 'left') -> float:
    """
    Rectangle method for calculating integrals
        The calculation of the integral is based on the formula:
            h*[f(x0)+f(x1)+...+f(xn-1)

        a-bottom limit
        b-top limit
        nseg - the number of segments into which [a;b] is divided]
    """

    def get_result(frac):
        # current step
        h = (b - a) / nseg
        xstart = a + frac * h
        total = sum([f((xstart + (k * h))) for k in range(0, nseg)])
        # final answer
        result = h * total
        return result

    if method == 'left':
        return get_result(0.0)
    elif method == 'right':
        return get_result(1.0)
    elif method == 'centr':
        return get_result(0.5)


def simpson_rule(func, a: int, b: int, nseg: int):
    """
    Simpson`s method for calculating integrals

        The calculation of the integral is based on the formula:
            h/3*[f(a)+4f(a+h)+2f(a+2h)+...+4f(b-h)+f(b)]

        a-bottom limit
        b-top limit
        nseg - the number of segments into which [a;b] is divided]
    """
    if nseg == 2:
        return "input nseg > 2"
    # step verification
    if nseg % 2 == 1:
         nseg += 1
    h = 1.0 * (b - a) / nseg
    sum = (func(a) + 4 * func(a + h) + func(b))
    for i in range(1, int(nseg / 2)):
        sum += 2 * func(a + (2 * i) * h) + 4 * func(a + (2 * i + 1) * h)

    return sum * h / 3


def trapezoid_rule(func, a: int, b: int, nseg: int) -> float:
    """
    Trapezoid rule for calculating integrals

        The calculation of the integral is based on the formula:
            h[(f(a)+f(b))/2 + ?i=1,n-1 (f(a+ih))]
            where h = (b-a)/nseg

        a-bottom limit
        b-top limit
        nseg - the number of segments into which [a;b] is divided]
    """

    def get_result():
        h = 1.0 * (b - a) / nseg
        sum = 0.5 * (func(a) + func(b))
        for i in range(1, nseg):
            sum += func(a + i * h)
        return sum * h
    #checking the accuracy
    first_answer = get_result()
    nseg *= 2
    last_answer = get_result()
    while abs(first_answer - last_answer) > 0.001:
        nseg *= 2
        first_answer = get_result()
        nseg *= 2
        last_answer = get_result()

    return last_answer

if __name__ == '__main__':
    print(trapezoid_rule(func, 1, 10, 10))
    print(method_of_rectangles(func, 1, 10, 100,'centr'))
    print(simpson_rule(func, 1, 10, 12))
def main(x):
    if x == 1:
        return x

    ans = 1
    factorials = [1] * x
    # compute factorials using the concept of dynamic programming
    for i in range(1, x):
        factorials[i] = factorials[i-1] * (i+1)

    # calculate the value of e^x using taylor expansion
    for j in range(1, x+1):
        ans = ans + (pow(x, j) / factorials[j-1])

    return ans


if __name__ == "__main__":
    x = 3
    ans = main(x)
    print(ans)

"""
 * Tính số fibonacci thứ n
 *
 * @param n: chỉ số của số fibonacci tính từ 0
 *           vd: F0 = 0, F1 = 1, F2 = 1, F3 = 2
 * @return số fibonacci thứ n
"""
def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
print("1000 số đầu tiên của dãy số fibonacci: ");
sb = "";
for i in range(0, 1000):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)

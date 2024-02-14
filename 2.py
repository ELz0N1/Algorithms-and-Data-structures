def karatsuba(p: int, q: int):
    if len(str(p)) == 1 or len(str(q)) == 1:
        return p * q
    else:
        max_len = max(len(str(p)), len(str(q)))
        m2 = max_len // 2

        left_p = p // (10 ** m2)
        right_p = p % (10 ** m2)
        left_q = q // (10 ** m2)
        right_q = q % (10 ** m2)

        left_pq = karatsuba(left_p, left_q)
        right_pq = karatsuba(right_p, right_q)
        lprq_and_rplq = karatsuba((left_p + right_p), (left_q + right_q)) - left_pq - right_pq

        return (left_pq * (10 ** (2 * m2))) + ((lprq_and_rplq) * (10 ** m2)) + right_pq

print(karatsuba(1234,5678))
print(karatsuba(349,23140))
print(karatsuba(8459678687678,23))

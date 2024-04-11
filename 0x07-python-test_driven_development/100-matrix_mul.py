#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a)
                        else "m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty" if len(m_a) == 0 else "m_b can't be empty")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a) or \
       any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_a should contain only integers or floats" if
                        any(not all(isinstance(num, (int, float)) for num in row) for row in m_a)
                        else "m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_a must be of the same size" if
                         any(len(row) != len(m_a[0]) for row in m_a)
                         else "each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/100-matrix_mul.txt")

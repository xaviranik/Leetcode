def generate(numRows):
    triangle = []

    if numRows == 0:
        return triangle

    first_row = [1]
    triangle.append(first_row)

    for i in range(1, numRows):
        row = []
        prev_row = triangle[i - 1]

        row.append(1)

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle


print(generate(10))

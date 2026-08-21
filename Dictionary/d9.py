nums = range(1, 11)

even_squares = {
    i: i * i
    for i in nums
    if i % 2 == 0
}

print(even_squares)
# Lambda taking a list 'l' and returning a tuple (max, min)
max_min_lambda = lambda l: (max(l), min(l))
sample_input = [10, 6, 8, 90, 12, 56]
print(f"Output: {max_min_lambda(sample_input)}")
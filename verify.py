import math

a, b, c = 1/4, -3, 1/2

print("=== Verifying a=1/4, b=-3, c=1/2 ===\n")

exprs = [
    ("6c-4b", 6*c - 4*b),
    ("8-b", 8 - b),
    ("(a^b-4)/(6c+1)", (a**b - 4)/(6*c + 1)),
    ("(b+c)/(c-1)", (b+c)/(c-1)),
    ("b^2-b/c", b**2 - b/c),
    ("sqrt(30+a)/c", math.sqrt(30+a)/c),
    ("(a+b)/(c-3a)", (a+b)/(c-3*a)),
    ("(b-3a)/(a-c)", (b-3*a)/(a-c)),
    ("8a-2b", 8*a - 2*b),
    ("b/(a-c)", b/(a-c)),
    ("(b+9)/sqrt(c-a)", (b+9)/math.sqrt(c-a)),
    ("18/(ac+1)", 18/(a*c + 1)),
    ("c^b", c**b),
    ("(3+b^2)/sqrt(3+2c)", (3+b**2)/math.sqrt(3+2*c)),
    ("b/(a^2-c^2)", b/(a**2 - c**2)),
    ("sqrt(a+2)/a", math.sqrt(a+2)/a),
    ("a^b-12/a", a**b - 12/a),
    ("2c+c/a", 2*c + c/a),
    ("4a-5b", 4*a - 5*b),
    ("c+2a", c + 2*a),
    ("b/(9a-5c)", b/(9*a - 5*c)),
    ("(b^3+2c)/(b+2c)", (b**3 + 2*c)/(b + 2*c)),
    ("b/(a-1)", b/(a-1)),
    ("(c-b)/(2a)", (c-b)/(2*a)),
    ("b/(a-c) [2nd]", b/(a-c)),
    ("(b+c)/(a-c)", (b+c)/(a-c)),
    ("log_c(a)", math.log(a)/math.log(c)),
    ("(c^2-b)/a", (c**2 - b)/a),
    ("(b-1)^2", (b-1)**2),
    ("cbrt(43-ac)/a", (43-a*c)**(1/3)/a),  # cube root!
    ("(b-a)/(a-c)", (b-a)/(a-c)),
    ("11-b", 11 - b),
    ("(b-2a)/(a-c)", (b-2*a)/(a-c)),
    ("(c+3)/a", (c+3)/a),
    ("8c-b/c", 8*c - b/c),
    ("b^2", b**2),
    ("(2^b+1)/(ac)", (2**b + 1)/(a*c)),
]

print(f"{'Expression':<25} {'Value':>10} {'Int?':>5}")
print("-" * 45)

all_values = []
for name, val in exprs:
    rounded = round(val)
    is_int = abs(val - rounded) < 1e-9 and rounded >= 1
    marker = "✓" if is_int else "✗"
    print(f"{name:<25} {val:>10.4f} {marker:>5}")
    if is_int:
        all_values.append(rounded)
    else:
        all_values.append(None)

print(f"\nAll positive integers: {all(v is not None for v in all_values)}")
print(f"Values: {[v for v in all_values if v is not None]}")

# Check value frequency constraint
from collections import Counter
freq = Counter(v for v in all_values if v is not None)
print(f"\nValue frequencies:")
for k in sorted(freq):
    ok = "✓" if freq[k] <= k else "✗"
    print(f"  {k}: {freq[k]} labeled cells (max {k}) {ok}")

max_val = max(v for v in all_values if v is not None)
print(f"\nMax value = {max_val}, so N >= {max_val}")
print(f"N(N+1)/2 = {max_val*(max_val+1)//2}")

# Now organize by rows and compute row sums
# Based on the grid layout from the image
print("\n=== Row sums of labeled cells ===")
print("(Rows based on grid position in image)\n")

# Row assignments based on the puzzle grid image
# The grid appears to be 9 rows x 17 cols or 17 rows x 9 cols
# Let me organize the expressions by their row in the grid image

rows = {
    1: [("6c-4b", 15)],
    2: [("8-b", 11)],
    3: [("(a^b-4)/(6c+1)", 15), ("(b+c)/(c-1)", 5), ("b^2-b/c", 15),
        ("sqrt(30+a)/c", 11), ("(a+b)/(c-3a)", 11)],
    4: [("(b-3a)/(a-c)", 15), ("8a-2b", 8), ("b/(a-c)", 12),
        ("(b+9)/sqrt(c-a)", 12)],
    5: [("18/(ac+1)", 16), ("c^b", 8), ("(3+b^2)/sqrt(3+2c)", 6)],
    6: [("b/(a^2-c^2)", 16), ("sqrt(a+2)/a", 6)],
    7: [("a^b-12/a", 16), ("2c+c/a", 3), ("4a-5b", 16),
        ("c+2a", 1), ("b/(9a-5c)", 12)],
    8: [("(b^3+2c)/(b+2c)", 13), ("b/(a-1)", 4)],
    9: [("(c-b)/(2a)", 7), ("b/(a-c)", 12), ("(b+c)/(a-c)", 10)],
    10: [("log_c(a)", 2), ("(c^2-b)/a", 13), ("(b-1)^2", 16),
         ("cbrt(43-ac)/a", 14)],
    11: [("(b-a)/(a-c)", 13), ("11-b", 14), ("(b-2a)/(a-c)", 14),
         ("(c+3)/a", 14), ("8c-b/c", 10)],
    12: [("b^2", 9)],
    13: [("(2^b+1)/(ac)", 9)],
}

row_sums = {}
for r in sorted(rows):
    s = sum(val for _, val in rows[r])
    row_sums[r] = s
    vals = [str(val) for _, val in rows[r]]
    print(f"Row {r:2d}: {' + '.join(vals):>40s} = {s}")

print(f"\nMin row sum: {min(row_sums.values())}")
print(f"Max row sum: {max(row_sums.values())}")
print(f"Answer (min × max): {min(row_sums.values()) * max(row_sums.values())}")
print(f"Expected: 56 × 162 = {56*162}")

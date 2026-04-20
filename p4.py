print("By: Tristan Price, Nathan Byun, Ahran Dymond, Barrett Larson")
"""
PART 1
"""
print("--- PART 1: Difference Distribution Table ---")
# Difference Distribution Table (8x8) for the given 3-bit S-box
# S-box (from Project 3):
#   input (decimal 0-7) -> output (decimal)
#   0 (000) -> 6 (110)
#   1 (001) -> 5 (101)
#   2 (010) -> 1 (001)
#   3 (011) -> 0 (000)
#   4 (100) -> 3 (011)
#   5 (101) -> 2 (010)
#   6 (110) -> 7 (111)
#   7 (111) -> 4 (100)
#
# This code computes N_D(a', b') where:
#   - a' = input difference (0 to 7)
#   - b' = output difference (0 to 7)
#   - Each entry = number of pairs (x, x*) with x ⊕ x* = a' that produce y ⊕ y* = b'
# Analogous to the 16x16 table on slide 7 of §4.4 (but scaled to 3 bits → 8x8).
# Total per row must be exactly 8 (2^3 inputs).

S = [6, 5, 1, 0, 3, 2, 7, 4]  # S-box lookup table (decimal)

# 8x8 table: rows = a' (0-7), columns = b' (0-7)
table = [[0 for _ in range(8)] for _ in range(8)]

# Populate the table
for a_prime in range(8):          # input difference a' (0 to 7)
    for x in range(8):            # every possible x (0 to 7)
        x_star = x ^ a_prime      # x* = x ⊕ a'
        y = S[x]                  # output of S-box on x
        y_star = S[x_star]        # output of S-box on x*
        b_prime = y ^ y_star      # output difference b' = y ⊕ y*
        table[a_prime][b_prime] += 1

# Print the table in a clean, submission-ready format
# (labels match the style of the class-note table: decimal 0-7)
print("Difference Distribution Table N_D(a', b')")
print("a' \\ b' |  0    1    2    3    4    5    6    7")
print("--------|--------------------------------------")
for ap in range(8):
    row = f"   {ap}    | " + "   ".join(f"{table[ap][bp]:2d}" for bp in range(8))
    print(row)

# Verification: each row must sum to 8
print("\nVerification (row sums must all be 8):")
for ap in range(8):
    row_sum = sum(table[ap])
    print(f"a' = {ap}: sum = {row_sum} {'✓' if row_sum == 8 else '✗'}")

"""
PART 2
"""
print("--- PART 2: Distribution Trails ---")
"""
PART 3
"""
print("--- PART 3: Propagation Ratios ---")
"""
PART 4
"""
print("--- PART 4: Suitable Right 4-Tuples ---")
"""
PART 5
"""
print("--- PART 5: Determine Subkey Bits ---")

from fractions import Fraction
print("By: Tristan Price, Nathan Byun, Ahran Dymond, Barrett Larson")
"""
PART 1
"""
print("\n--- PART 1: Difference Distribution Table ---")
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
print("\n--- PART 2: Distribution Trails ---")

sketchTr1 = """
   Sketch of Tr1
   Plaintext Bits:   P1  P2  P3  P4  P5  P6
                      |   |   |   |   |   |
                      |   |   |   |   |   v   
                    +----------------------+
                    |          K1          |
                    +----------------------+ 
                      |   |   |   |   |   |     a6
                      |   |   |   |   |   v     1 -> {1,3} chose 1
                    +----------+ +---------+
                    |          | |   S12   |
                    +----------+ +---------+
                      |   \   \   |   |   |     b6 -> c6
                      |    \   \  /   /   |
                      |     \   \/   /    |
                      |      \  /\  /     |
                      |       \/  \/      |
                      |       /\  /\      |
                      |      /  \/  \     |
                      |     /   /\   \    |
                      |    /   /  |  |    v
                    +----------------------+
                    |          K2          |
                    +----------------------+ 
                      |   |   |   |   |   |     d6
                      |   |   |   |   |   v     1 -> {1,3} chose 1
                    +----------+ +---------+
                    |          | |   S22   |
                    +----------+ +---------+
                      |   \   \   |   |   |     e6 -> f6
                      |    \   \  /   /   |
                      |     \   \/   /    |
                      |      \  /\  /     |
                      |       \/  \/      |
                      |       /\  /\      |
                      |      /  \/  \     |
                      |     /   /\   \    |
                      |    /   /  |  |    v                             
                    +----------------------+
                    |          K3          |
                    +----------------------+ 
                      |   |   |   |   |   |     g6
                      |   |   |   |   |   v     1 -> {1,3} chose 1
                    +----------+ +---------+
                    |          | |   S32   |
                    +----------+ +---------+
                      |   |   |   |   |   |
                      |   |   |   |   |   v   
                                          h6
   ----------------------------------
"""
sketchTr2 = """
   Sketch of Tr2
   Plaintext Bits:   P1  P2  P3  P4  P5  P6
                      |   |   |   |   |   |
                      |   |   |   |   v   v   
                    +----------------------+
                    |          K1          |
                    +----------------------+ 
                      |   |   |   |   |   |     a6
                      |   |   |   |   v   v     1 -> {1,3} chose 1
                    +----------+ +---------+
                    |          | |   S12   |
                    +----------+ +---------+
                      |   \   \   |   |   |     b6 -> c6
                      |    \   \  /   /   |
                      |     \   \/   /    |
                      |      \  /\  /     |
                      |       \/  \/      |
                      |       /\  /\      |
                      |      /  \/  \     |
                      |     /   /\   \    |
                      |    /   v  |  |    v
                    +----------------------+
                    |          K2          |
                    +----------------------+ 
                      |   |   |   |   |   |     d6
                      |   |   v   |   |   v     1 -> {1,3} chose 1
                    +----------+ +---------+
                    |    S21   | |   S22   |
                    +----------+ +---------+
                      |   \   \   |   |   |     e6 -> f6
                      |    \   \  /   /   |
                      |     \   \/   /    |
                      |      \  /\  /     |
                      |       \/  \/      |
                      |       /\  /\      |
                      |      /  \/  \     |
                      |     /   /\   \    |
                      |    /   /  |   v   v                             
                    +----------------------+
                    |          K3          |
                    +----------------------+ 
                      |   |   |   |   |   |     g6
                      |   |   |   |   v   v     1 -> {1,3} chose 3
                    +----------+ +---------+
                    |          | |   S32   |
                    +----------+ +---------+
                      |   |   |   |   |   |
                      |   |   |   |   v   v   
                                      h5  h6
"""
sketchTr3 = """
   Sketch of Tr3
   Plaintext Bits:   P1  P2  P3  P4  P5  P6
                      |   |   |   |   |   |
                      |   |   |   v   v   v   
                    +----------------------+
                    |          K1          |
                    +----------------------+ 
                      |   |   |   |   |   |     a6
                      |   |   |   v   v   v     1 -> {1,3} chose 3
                    +----------+ +---------+
                    |          | |   S12   |
                    +----------+ +---------+
                      |   \   \   |   |   |     b6 -> c6
                      |    \   \  /   /   |
                      |     \   \/   /    |
                      |      \  /\  /     |
                      |       \/  \/      |
                      |       /\  /\      |
                      |      /  \/  \     |
                      |     /   /\   \    |
                      |    v   v  |  |    v
                    +----------------------+
                    |          K2          |
                    +----------------------+ 
                      |   |   |   |   |   |     d6
 1 -> {1,3} choose 1  |   v   v   |   |   v     1 -> {1,3} chose 1 
                    +----------+ +---------+
                    |    S21   | |   S22   |
                    +----------+ +---------+
                      |   \   \   |   |   |     e6 -> f6
                      |    \   \  /   /   |
                      |     \   \/   /    |
                      |      \  /\  /     |
                      |       \/  \/      |
                      |       /\  /\      |
                      |      /  \/  \     |
                      |     /   /\   \    |
                      |    /   /  v   v   v                             
                    +----------------------+
                    |          K3          |
                    +----------------------+ 
                      |   |   |   |   |   |     g6
                      |   |   |   v   v   v     3 -> {4, 5, 6, 7} chose 7
                    +----------+ +---------+
                    |          | |   S32   |
                    +----------+ +---------+
                      |   |   |   |   |   |
                      |   |   |   v   v   v   
                                 h4  h5  h6
"""


print(sketchTr1)
print(sketchTr2)
print(sketchTr3)


"""
PART 3
"""
print("--- PART 3: Propagation Ratios ---")
l = 3
denom = 2 ** l  # = 8

tr1_differentials = [(1, 1), (1, 1), (1, 1)]          # S12, S22, S32
tr2_differentials = [(1, 1), (1, 1), (1, 1), (1, 3)]  # S12, S21, S22, S32
tr3_differentials = [(1, 3), (1, 1), (1, 1), (3, 7)]  # S12, S21, S22, S32

def total_propagation_ratio(differentials, ddt, denom):

    ratio = Fraction(1)
    for (a_prime, b_prime) in differentials:
        nd = ddt[a_prime][b_prime]
        ratio *= Fraction(nd, denom)
    return ratio

R1 = total_propagation_ratio(tr1_differentials, table, denom)
R2 = total_propagation_ratio(tr2_differentials, table, denom)
R3 = total_propagation_ratio(tr3_differentials, table, denom)

print(f"\nTr1 active S-boxes and differentials (a', b'):")
for i, (a, b) in enumerate(tr1_differentials):
    nd = table[a][b]
    print(f"  S-box {i+1}: ({a}, {b})  N_D = {nd}  Rp = {nd}/{denom} = {Fraction(nd,denom)}")
print(f"  R1 = product = {R1} = {float(R1):.6f}")

print(f"\nTr2 active S-boxes and differentials (a', b'):")
for i, (a, b) in enumerate(tr2_differentials):
    nd = table[a][b]
    print(f"  S-box {i+1}: ({a}, {b})  N_D = {nd}  Rp = {nd}/{denom} = {Fraction(nd,denom)}")
print(f"  R2 = product = {R2} = {float(R2):.6f}")

print(f"\nTr3 active S-boxes and differentials (a', b'):")
for i, (a, b) in enumerate(tr3_differentials):
    nd = table[a][b]
    print(f"  S-box {i+1}: ({a}, {b})  N_D = {nd}  Rp = {nd}/{denom} = {Fraction(nd,denom)}")
print(f"  R3 = product = {R3} = {float(R3):.6f}")

print(f"\nSummary:")
print(f"  R1 = {R1}  (Tr1: 3 active S-boxes, all (1,1))")
print(f"  R2 = {R2}  (Tr2: 4 active S-boxes, three (1,1) and S32 with (1,3))")
print(f"  R3 = {R3}  (Tr3: 4 active S-boxes, S12(1,3), S21/S22(1,1), S32(3,7))")

"""
PART 4
"""
print("\n--- PART 4: Suitable Right 4-Tuples ---")
four_tuples = [
    ("100111", "100100", "100110", "111110"),  # 1
    ("000111", "110010", "000110", "110110"),  # 2
    ("001100", "111001", "001101", "100000"),  # 3
    ("011000", "011101", "011001", "011111"),  # 4
    ("001000", "001101", "001001", "000011"),  # 5
    ("011010", "101001", "011011", "101000"),  # 6
]

def xor_bits(a, b):
    return "".join("1" if ai != bi else "0" for ai, bi in zip(a, b))

print("\nFilter: keep only tuples with y<1..3> XOR y*<1..3> = 000")
print(f"{'#':>2}  {'x':>6}  {'y':>6}  {'x*':>6}  {'y*':>6}  |  x'      y'    verdict")
print("-" * 66)

right_tuples = []
for i, (x, y, xs, ys) in enumerate(four_tuples, start=1):
    xp = xor_bits(x, xs)    # input difference
    yp = xor_bits(y, ys)    # output difference
    keep = (yp[:3] == "000")
    verdict = "RIGHT" if keep else "reject"
    print(f"{i:>2}  {x:>6}  {y:>6}  {xs:>6}  {ys:>6}  |  {xp}  {yp}  {verdict}")
    if keep:
        right_tuples.append((i, x, y, xs, ys))

print(f"\nSuitable right 4-tuples ({len(right_tuples)} found):")
for i, x, y, xs, ys in right_tuples:
    print(f"  Tuple {i}: (x={x}, y={y}, x*={xs}, y*={ys})")
"""
PART 5
"""
print("\n--- PART 5: Determine Subkey Bits ---")

# Create the inverse S box
S_inv = [0] * 8
for index in range(8):
    S_inv[S[index]] = index

c1_counts = []
c2_counts = []
c3_counts = []
C_values = []

print("Key | c1 | c2 | c3 | C")
print("====|====|====|====|=========")

for k in range(8):
    c1 = c2 = c3 = 0
    
    for i, x, y, xs, ys in right_tuples:
        # Extract the last 3 bits of the ciphertext
        y_R = int(y[3:], 2)
        ys_R = int(ys[3:], 2)

        # XOR with the key guess to get the S box output J
        J = y_R ^ k
        Js = ys_R ^ k

        # Reverse the substitution to get the S box input H
        H = S_inv[J]
        Hs = S_inv[Js]

        # Find the input difference to S32
        H_prime = H ^ Hs

        # Increment counters based on the expected trail differences
        if H_prime == 1:
            c1 += 1
        if H_prime == 3:
            c2 += 1
        if H_prime == 7:
            c3 += 1

    c1_counts.append(c1)
    c2_counts.append(c2)
    c3_counts.append(c3)

    # Compute the weighted average C
    C = R1 * c1 + R2 * c2 + R3 * c3
    C_values.append(C)

    # Print in binary format
    key_bin = format(k, '03b')
    print(f"{key_bin} | {c1:2} | {c2:2} | {c3:2} | {float(C):.6f}")

best_key_idx = C_values.index(max(C_values))
best_key_bin = format(best_key_idx, '03b')

print(f"\n(e) The last three bits of the subkey K4 are: {best_key_bin}")

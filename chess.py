import math

def revise_with_border(height, width, block_size, symbols=("*", "#")):
    total_rows = height * block_size + 2
    total_cols = width * block_size + 2

    return "\n".join(
        "".join(
            # border condition
            "-" if i == 0 or i == total_rows - 1 or j == 0 or j == total_cols - 1
            else symbols[
                (math.floor((j - 1) / block_size) + math.floor((i - 1) / block_size)) % 2
            ]
            for j in range(total_cols)
        )
        for i in range(total_rows)
    )

print(revise_with_border(8, 8, 5))
# all elements are positive
#   input  1 2 3
#   output True
#
#   input -1 2 3
#   output False
print(
    all(
        map(
            lambda x: x > 0,
            map(
                int,
                input().split()
            )
        )
    )
)

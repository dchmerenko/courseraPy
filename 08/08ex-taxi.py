print(
    *map(
        lambda x: x[1][0] + 1,
        sorted(
            zip(
                sorted(
                    enumerate(
                        map(
                            int,
                            open('08ex-taxi-input.txt').readline().split()
                        )
                    ),
                    key=lambda x: x[1]
                ),
                sorted(
                    enumerate(
                        map(
                            int,
                            open('08ex-taxi-input.txt').readline().split()
                        )
                    ),
                    key=lambda x: x[1],
                    reverse=True)
            ),
            key=lambda x: x[0][0]
        )
    )
)


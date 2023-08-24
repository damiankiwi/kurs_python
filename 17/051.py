import cProfile


def przykladowa_funkcja():
    for i in range(1000000):
        _ = i * i


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    przykladowa_funkcja()

    profiler.disable()
    profiler.print_stats(sort='cumulative')

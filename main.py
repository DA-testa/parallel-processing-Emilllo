# 221RDB231 Emīlija Ostaševska 4.gr


def parallel_processing(n, m, data):
    
    output_pairs = []
    times = [0] * n
    
    for i in range(m):
        worker_index = times.index(min(times))
        start_time = times[worker_index]
        times[worker_index] += data[i]
        output_pairs.append((worker_index, start_time))

    return output_pairs


def main():

    n = 0
    m = 0

    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]

    data = list(map(int, input().split()))
    assert len(data) == m

    result = parallel_processing(n, m, data)

    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()

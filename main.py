# python3

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
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    arr = list(map(int, input().split()))

    n = arr[0]
    m = arr[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    assert len(data) == m

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()

def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print(f"Step {steps} : {list[start, end+1]}")
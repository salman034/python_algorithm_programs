def bubble_sort(nlist):
    for i in range(len(nlist) -1, 0, -1):
        for j in range(i):
            if nlist[j] > nlist[j + 1]:
                temp = nlist[j]
                nlist[j] = nlist[j + 1]
                nlist[j + 1] = temp


if __name__ == "__main__":
    nlist = [5, 3, 8, 2, 9, 0,3, 7, 6, 4, 1]
    bubble_sort(nlist)
    print(nlist)

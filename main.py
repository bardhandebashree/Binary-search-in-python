# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def binary_search(arr1, f, e, k):
    flag = 0
    c = 0
    length = len(arr1)
    print("*************************")

    if e >= f:
        print(f,e)
        m = (f + e) // 2
        print(m)
        if arr1[m] == k:
            print("found number in m")
            print(m)
        elif arr[m] > k:
            binary_search(arr1, f, m - 1, k)
        else:
            binary_search(arr1, m + 1, e, k)

    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [3, 91, 67, 72, 632]
    arr1=sorted(arr)
    print(arr1)
    f = 0
    e = 4
    k = int(input(':input number to be searched'))
    binary_search(arr1, f, e, k)



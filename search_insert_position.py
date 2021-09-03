def searchinsert(nums, target):
    head = 0
    tail = len(nums) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            tail = mid - 1
        elif nums[mid] < target:
            head = mid + 1
    return head


def main():
    n = []
    n.append(searchinsert([1, 3, 5, 6], 5))
    n.append(searchinsert([1, 3, 5, 6], 2))
    n.append(searchinsert([1, 3, 5, 6], 7))
    n.append(searchinsert([1, 3, 5, 6], 0))
    n.append(searchinsert([1], 0))
    print(n)


if __name__ == "__main__":
    main()

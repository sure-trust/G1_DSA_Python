import array as ary


class Sort:
    def __init__(self):
        self.arr = ary.array("i", [5, 2, 3, 1, 4])

    def bubble_sort(self):
        arr = self.arr
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        print(arr)

    def selection_sort(self):
        # Unsorted array
        x = self.arr
        n = len(x)
        # Loop for sorted array
        for i in range(n):
            min_idx = i
            # Loop for unsorted array
            for j in range((i + 1), n):
                if x[min_idx] > x[j]:
                    min_idx = j
            x[i], x[min_idx] = x[min_idx], x[i]
        print(x)

    def insertion_sort(self):
        # Unsorted array
        x = self.arr
        n = len(x)

        # Loop for sorted array
        for i in range(1, n):
            temp = x[i]
            j = i - 1
            # Loop for unsorted array
            while j >= 0:
                if x[j] > temp:
                    x[j + 1] = x[j]
                    j -= 1
                else:
                    break
            x[j + 1] = temp
        print(x)

    def __partition(self, f, l):
        p = self.arr[f]
        i = f + 1
        j = l
        while i <= j:
            while i <= j and p > self.arr[i]:
                i += 1
            while i <= j and p < self.arr[j]:
                j -= 1
            if i <= j:
                # self.__swap(self.arr, i, j)
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        # self.__swap(self.arr, f, j)
        self.arr[f], self.arr[j] = self.arr[j], self.arr[f]
        return j

    def quick_sort(self, f, l):
        if f <= l:
            key = self.__partition(f, l)
            self.quick_sort(f, key - 1)
            self.quick_sort(key + 1, l)
        return self.arr

    def __merge(self, f, mid, l):
        i = f
        j = mid + 1
        n1 = mid
        n2 = l
        ans = []

        while i <= n1 and j <= n2:
            if self.arr[i] < self.arr[j]:
                ans.append(self.arr[i])
                i += 1
            else:
                ans.append(self.arr[j])
                j += 1

        while i <= n1:
            ans.append(self.arr[i])
            i += 1

        while j <= n2:
            ans.append(self.arr[j])
            j += 1

        k = 0
        for i in range(f, l + 1):
            self.arr[i] = ans[k]
            k += 1

    def merge_sort(self, f, l):
        if f >= l:
            return

        mid = int((f + l) / 2)
        self.merge_sort(f, mid)
        self.merge_sort(mid + 1, l)
        self.__merge(f, mid, l)

        return self.arr


obj = Sort()
print("Bubble Sort for [5, 2, 3, 1, 4]:")
obj.bubble_sort()
print("Selection Sort for [5, 2, 3, 1, 4]:")
obj.selection_sort()
print("Insertion Sort for [5, 2, 3, 1, 4]:")
obj.insertion_sort()
print("Quick Sort for [5, 2, 3, 1, 4]:")
print(obj.quick_sort(0, len(obj.arr) - 1))
print("Merge Sort for [5, 2, 3, 1, 4]:")
print(obj.merge_sort(0, len(obj.arr) - 1))

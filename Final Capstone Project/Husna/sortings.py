class SortingAlg:
    
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = []
            right = []
            for element in arr[1:]:
                if element < pivot:
                    left.append(element)
                else:
                    right.append(element)
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)


obj = SortingAlg()

arr = [64, 34, 25, 12, 22, 11, 90]

obj.bubble_sort(arr)
print("Bubble Sort:", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
obj.insertion_sort(arr)
print("Insertion Sort:", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
obj.selection_sort(arr)
print("Selection Sort:", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
obj.merge_sort(arr)
print("Merge Sort:", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
arr = obj.quick_sort(arr)
print("Quick Sort:", arr)


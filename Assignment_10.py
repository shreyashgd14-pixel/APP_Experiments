import numpy as np

arr = np.arange(1, 11)

print("Original array:")
print(arr)


print("\nFirst five elements:")
print(arr[:5])

print("\nLast five elements:")
print(arr[5:])

print("\nElements from index 2 to 6:")
print(arr[2:7])

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5

print("\nArray after broadcasting (adding 5):")
print(arr)

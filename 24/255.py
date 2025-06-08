import numpy as np

def main():
    try:
        array_1_d = np.array([1, 2, 3, 4, 5, 6])
        array_3_d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

        print("Memory views:")
        mem_view_1_d = memoryview(array_1_d)
        print(mem_view_1_d)
        mem_view_3_d = memoryview(array_3_d)
        print(mem_view_3_d)

        print("\n1-D Memory View:")
        print(mem_view_1_d.tolist())

        print("\n3-D Memory View:")
        print(mem_view_3_d.tolist())
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
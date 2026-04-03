from solution import Solution

def main():
    print("Genesys Intern Assignment – Letter Combinations")
    digits = input("Enter digits (2-9): ")

    solver = Solution()
    try:
        result = solver.combinations(digits)
        print("Possible combinations:")
        print(result)
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
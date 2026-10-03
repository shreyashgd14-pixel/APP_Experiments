def generate_fibonacci_tabulation(n: int) -> list[int]:
 
    if n < 0:
        return []
    if n == 0:
        return [0]

  
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

   
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


if __name__ == "__main__":
    try:
        user_input = int(input("Enter N (number of terms - 1): "))
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            fib_sequence = generate_fibonacci_tabulation(user_input)
            
            print(f"\nFibonacci sequence up to N = {user_input}:")
            print(" -> ".join(map(str, fib_sequence)))
            print(f"\nThe {user_input}th Fibonacci number is: {fib_sequence[-1]}")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def longest_common_substring(s1: str, s2: str) -> tuple[int, str]:
 
    m, n = len(s1), len(s2)
    
  
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    end_index = 0 

 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                
              
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0  


    substring = s1[end_index - max_length : end_index]
    
    return max_length, substring


if __name__ == "__main__":
    string1 = input("Enter first string: ").strip() or "abcde"
    string2 = input("Enter second string: ").strip() or "abfce"

    length, match = longest_common_substring(string1, string2)

    print("\n--- Result ---")
    print(f"String 1: {string1}")
    print(f"String 2: {string2}")
    print(f"Length of Longest Common Substring: {length}")
    print(f"Matching Substring: '{match}'")

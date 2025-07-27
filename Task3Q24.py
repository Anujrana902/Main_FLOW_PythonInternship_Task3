def is_anagram_sort(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# Functions defined above...

if __name__ == "__main__":
   
    

    # Example for anagram check
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")
    print("Anagram?", is_anagram_sort(w1, w2))

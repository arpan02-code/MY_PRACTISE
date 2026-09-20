class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Vowels ka set lookup ke liye
        s_list = list(s)             # String ko list mein convert kiya
        left, right = 0, len(s_list) - 1
        
        while left < right:
            # Left pointer ko tab tak badhao jab tak vowel na mile
            while left < right and s_list[left] not in vowels:
                left += 1
                
            # Right pointer ko tab tak peeche lao jab tak vowel na mile
            while left < right and s_list[right] not in vowels:
                right -= 1
                
            # Dono vowels ko aapas mein swap kar do
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # Pointers ko aage move karo
            left += 1
            right -= 1
            
        return "".join(s_list)

        

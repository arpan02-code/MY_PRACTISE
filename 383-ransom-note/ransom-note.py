from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequencies of characters in both strings[cite: 4]
        count_note = Counter(ransomNote)
        count_mag = Counter(magazine)
        
        # Check if magazine has enough of each character
        for char, count in count_note.items():
            if count_mag[char] < count:
                return False
                
        return True
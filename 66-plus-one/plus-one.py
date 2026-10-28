class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Peeche (right side) se loop shuru karenge
        for i in range(n - 1, -1, -1):
            # Agar digit 9 se choti hai, toh usme 1 jod kar array return kar do
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # Agar digit 9 hai, toh woh 0 ban jayegi aur loop agle digit par jayega (carry)
            digits[i] = 0
            
        # Agar saari digits 9 thin (jaise [9, 9]), toh naya number [1, 0, 0] banega
        return [1] + digits
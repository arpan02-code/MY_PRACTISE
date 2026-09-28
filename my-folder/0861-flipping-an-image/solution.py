class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            l = 0
            r = len(row) - 1
            while l < r:  # Yahan '=' hata kar sirf '<' karein
                row[l], row[r] = (1 ^ row[r]), (1 ^ row[l])
                l += 1
                r -= 1
            
            # Agar length odd hai, toh beech wale element (middle element) ko yahin invert kar dein
            if l == r:
                row[l] = 1 ^ row[l]
                
        return image

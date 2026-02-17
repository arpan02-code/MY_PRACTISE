class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result=[]

        for hours in range (12):
            for min in range(60):
                ones =bin(hours).count("1") + bin(min).count("1")

                if ones == turnedOn :
                    time = str(hours)+ ":"+ str(min).zfill(2)
                    result.append(time)
        return result 

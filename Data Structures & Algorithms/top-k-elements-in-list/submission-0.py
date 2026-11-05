class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        sortedfreq=sorted(freq.items(),key=lambda x:x[1],reverse=True)

        freqsorted=dict(sortedfreq)

        result=[]
        for num in freqsorted:
            if len(result)==k:
                break
            result.append(num)
        
        return result
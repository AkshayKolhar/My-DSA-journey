class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        cu_sum=0
        pre={0:1}
        for num in nums:
            cu_sum+=num 

            if cu_sum-k in pre:
                count+=pre[cu_sum-k]

            pre[cu_sum]=pre.get(cu_sum,0)+1

        return count 

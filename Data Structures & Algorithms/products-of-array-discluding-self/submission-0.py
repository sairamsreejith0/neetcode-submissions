class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        suff = [0]*len(nums)
        res = []
        
        for i in range(len(nums)):
            if i==0:
                pref[i]=nums[i]*1
            else:
                pref[i] = nums[i]*pref[i-1]
        print(pref)
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                suff[j]=nums[j]*1
            else:
                suff[j] = nums[j]*suff[j+1]
        print(suff)
        for i in range(len(nums)):
            if i==0:
                t = 1*suff[i+1]
                res.append(t)
            elif i==len(nums)-1:
                t = 1*pref[i-1]
                res.append(t)
            else:
                t= pref[i-1]*suff[i+1]
                res.append(t)
        return res
            




        
class Solution:
    def trap(self, height: List[int]) -> int:
        pref_ = []
        mxpfx = float("-inf")
        for i in range(len(height)):
            if pref_ == []:
                pref_.append(0)
                mxpfx = height[i]
            else:
                pref_.append(mxpfx)
                mxpfx = max(mxpfx, height[i])

        sef_ = []
        mxsfx = float("-inf")
        for i in range(len(height)-1,-1,-1):
            if sef_ == []:
                sef_.append(0)
                mxsfx = height[i]
            else:
                sef_.insert(0,mxsfx)
                mxsfx = max(mxsfx, height[i])

        res_ = 0
        for i, v in enumerate(height):
            ith_val = min(pref_[i], sef_[i]) - v
            if ith_val > 0:
                res_ += ith_val

        return res_



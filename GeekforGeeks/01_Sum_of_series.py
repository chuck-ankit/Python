
#{ 
 # Driver Code Starts
                               #Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends


#User function Template for python3

class Solution:

	
	def seriesSum(self,n):
	    # code here
	    sum = 0
        for i in range(n):
            sum = sum + i   
        print(sum)

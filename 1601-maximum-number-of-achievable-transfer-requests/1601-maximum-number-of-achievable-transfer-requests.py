# Gist of the question
# In this question we are using a backtracking approach to get all the possible combinations of requests
# In this approach we are finding out all the combinations and checking if they are valid or not
# We first pick the requests and then we un-pick the requests
# Before running the un-picking requests we will make sure we get back the original state of the buildings net change

class Solution:
    def solve(self, idx, res, build, m, requests, count):
        if idx == m:  # Base Condition, we exit when we have traversed through all the requests
            isValid = True # A flag to check if the current combination of picked up requests is valid, initially marked as True 
            for i in build: # Checking if the net change in employee transfers is 0
                if i == 0:
                    continue
                else:
                    isValid = False # if the net change in the employee transfer is not zero, then isValid flag is turned to False 
                    break

            if(isValid):
                res[0] = max(res[0], count[0]) # If the current combination of requests is valid, then we update the result
                #We check if this count of the combination of requests is maximum compared to the previous stored value 

            return
        
        fr = requests[idx][0] # Stores the building an employee is from
        to = requests[idx][1] # Stores the building an employee wants to move to

        build[fr] -= 1 # Decrementing the net change in employee transfers
        build[to] += 1 # Incrementing the net change in employee transfers
        count[0] += 1 # After fulfiling this request we increment the count
        self.solve(idx + 1, res, build, m, requests, count) # We fulfiled the request hence we are picking the request therefore we call the pick recursive function
        count[0] -= 1
        build[fr] += 1 # We have done the pick choice, now we need to implement the not pick choice for that we will have to revert the changes back to if we didnt pick the element
        build[to] -= 1 # Then we will call the not pick recursive solve function
        self.solve(idx + 1, res, build, m, requests, count)# Once the not pick function is called we have made both the choices we had so we can return the function now 

        return


    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = [0] 
        build = [0] * n # A list to calculate the net change in employee transfers
        count = [0] # To keep a track of number of requests fulfiled
        m = len(requests) # Number of requests
        self.solve(0, res, build, m, requests, count) # Recursive function to get all the possible combinations of requests
                                                      # by the pick not pick combination of requests
        return res[0]



    
class Solution:
    def exclusiveTime(self, n, logs):
        stack = []
        result = [0] * n
        prev_time = 0
        
        for log in logs:
            func_id, typ, time = log.split(":")
            func_id = int(func_id)
            time = int(time)
            
            if typ == "start":
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(func_id)
                prev_time = time
            
            else:  
                result[stack[-1]] += time - prev_time + 1
                stack.pop()
                prev_time = time + 1
        
        return result


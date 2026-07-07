import collections

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        #split path /
        components = path.split('/')
        
        for component in components:
        # ignore if empty or .
            if component == "" or component == ".":
                continue
                # pop if ..
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        return "/" + "/".join(stack)



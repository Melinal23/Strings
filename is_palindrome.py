    def isPalindrome(self, s: str) -> bool:
         
        if s == "":    # an empty string is a palindrome
            return True
        
        s = "".join([x for x in s if x.isalpha() or x.isdigit()])
        
        start = 0
        end = len(s) - 1
        
        while(start <= end):
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True

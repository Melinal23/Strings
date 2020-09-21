class Solution:
    def myAtoi(self, str: str) -> int:
        
        if len(str) == 0:  # empty string
            return 0 
        
        temp = ""
        i = 0
        
        while(i < len(str)-1 and str[i] == " "):  # get rid of leading whitespace
            i += 1
        
        while (i < len(str)):
                
            if str[i].isdigit() or (str[i] == "-" and len(temp) == 0) or (str[i] == "+" and len(temp) == 0):
                temp += str[i]
            else:                                   # hit additional chars, not a part of num
                break
        
            i += 1
        
        if len(temp) > 0:
            if len(temp) == 1 and temp.isdigit() == False:
                return 0
            elif temp[0] == "-" and int(temp) < pow(-2,31):  # check lower bound
                return pow(-2,31)
            elif int(temp) > (pow(2,31)-1):                  # check upper bound
                return (pow(2,31)-1)
            else:
                return int(temp)
        else:
            return 0

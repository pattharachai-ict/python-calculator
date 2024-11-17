class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
      
        if b == 0:
            return 0
        
        result = 0
        is_negative = (a < 0) ^ (b < 0)  
        a, b = abs(a), abs(b)

        for _ in range(b):
            result += a
        
        return -result if is_negative else result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        is_negative = (a < 0) ^ (b < 0) 
        a, b = abs(a), abs(b)
        result = 0
        while a >= b:
            a -= b
            result += 1
        
        return -result if is_negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        
       
        result = a - (b * (a // b))
        if result < 0 and b > 0:  
            result += abs(b)
        return result

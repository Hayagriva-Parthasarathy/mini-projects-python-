import random
class Password:
    def generate_pass(self):
        n = int(input("ENTER NO OF ROLL NO:"))
        while True:
            length = int(input("ENTER THE LENGTH OF CHARACTERS: "))
            
            if length >= 3:
                break
            else:
                print("PASSWORD SHOULD HAVE A MINIMUM OF 3 CHARACTERS")
        
    
        for i in range(0,n):
            characters= "abcde&fghijklm*nopqrstuv(wxyzABCDE)FGHIJKLMNOPQRSTUVWX^YZ1234567890!@#$"
            char = "abcdefghijklmnopqrstuvwxyz"
            no = "123456789"
            symbols = "[]%$#@!"
            pass_lis=[]
        
            char_generate = random.choice(char)
            pass_lis.append(char_generate)
            char_generate = random.choice(no)
            pass_lis.append(char_generate)
            char_generate = random.choice(symbols)
            pass_lis.append(char_generate)
        
            for j in range(3,length):
                char_generate = random.choice(symbols)
                pass_lis.append(char_generate)
                
                    
            
            random.shuffle(pass_lis)
            password = "".join(pass_lis)
            print(password)

MCA_B= Password()
MCA_B.generate_pass()
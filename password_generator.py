import random
class Password:
    def generate_pass(self):
        n = int(input("ENTER NO OF ROLL NO:"))
        length = int(input("ENTER THE LENGTH OF CHARACTERS: "))
        for i in range(0,n):
            characters= "abcde&fghijklm*nopqrstuv(wxyzABCDE)FGHIJKLMNOPQRSTUVWX^YZ1234567890!@#$"
            pass_lis=[]
            for i in range(0,length):
                char_generate = random.choice(characters)
                pass_lis.append(char_generate)
            password = "".join(pass_lis)
            print(password)

MCA_B= Password()
MCA_B.generate_pass() 




    

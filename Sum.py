while(True):
    try: 
        x = int(input("Value for X:"))
        y = int(input("Value for Y:"))
        break
    except:
        print("Invalid Entry")
        
def my_math(x,y) :
  z=x+y
  return z

def main():
  my_num_1 = x
  my_num_2 = y
  sum = my_math(my_num_1, my_num_2)
  print( my_num_1, "+", my_num_2, "=",sum)

main()

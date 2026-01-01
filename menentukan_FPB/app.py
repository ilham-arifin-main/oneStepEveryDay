def main ():
    print("MENENTUKAN FPB")
    print("Input bilangan:")
    num1 = int(input())
    num2 = int(input())

    def menentukan_fpb(num1, num2):
        x = num1 if num1 > num2 else num2
        y = num2 if num2 < num1 else num1

        while True:
            z = x % y

            if (z == 0):
                return y
            
            x = y
            y = z
        
    
    hasil = menentukan_fpb(num1, num2)
    print(f"FPB dari {num1} dan {num2} adalah {hasil}")

if __name__ :
    main()

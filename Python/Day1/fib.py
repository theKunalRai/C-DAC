def fib():
    # fibonacci series: 0,1,1,2,3,5,8,13,21
    #sample input: 6
    #sample output: 0,1,1,2,3,5
    n = int(input("Enter the number of terms: "))
    prev,curr = 0,1
    count = 2

    print(prev,curr,end="")
    while(count <= n): # if entered 7; the loop will break when encountered 8 after increasing count to 8

        sum = prev + curr
        print(sum,end=" ")
        prev = curr
        curr = sum
        count += 1

        print(f"{sum},"end="")
        
fib()
def credit_check(str):
    #create int array from string
    num_list = [int(num) for num in str]
    sum = 0

    #loop through and double every other
    for i in range(0, len(num_list),2):
        num_list[i] = num_list[i] * 2

    #loop through and sum digits greater than 9
    for i in range(0, len(num_list)):
        if num_list[i] > 9:
            remain = num_list[i] % 10
            num_list[i] = ((num_list[i] - remain)/10) + remain
    
    #loop through and sum 
    for i in range(0, len(num_list)):
        sum += num_list[i]

    #check valid
    if (sum % 10 == 0):
        return "The number is valid!"
    else:
        return "The number is invalid!"
    


# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"


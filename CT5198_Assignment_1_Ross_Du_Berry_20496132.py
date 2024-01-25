# Ross Du Berry, 20496132, 19/01/24

# Create empty list
cust_list = []

# Ask user for input seven times
for i in range(7):
    # input for number of customers
    num_cust = int(input(f"Please enter number of customers for day {i+1}: "))
    # add number of customers to list
    cust_list.append(num_cust)

# function to get average customers


def avg(cust_list):
    # calculation to get an average
    avg = sum(cust_list) / len(cust_list)
    # rounding up for people
    avg_cust = round(avg)
    return avg_cust


print(max(cust_list))
print(min(cust_list))
print(avg(cust_list))

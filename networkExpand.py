
import ipaddress, sys

#Given the ip address with cidr notation
#this function will print out all the hosts within
#the subnet
def printCidr(ipNetwork):
    for ip in list(ipaddress.ip_network(ipNetwork).hosts()):
        print(str(ip))

#Given an ip address with a dash to denote a range
#this function will print out all the ip addresses of 
#hosts within that range.
def printRange(ipNetwork):
    #get the ip address from the input
    givenIpAddress = ipNetwork
    
    #convert ip address string to list 
    octetList = givenIpAddress.split(".")

    #make 2 copies of octet list for use as start and end range
    startRange = octetList.copy()
    endRange = octetList.copy()

    #find the index in the octet list that has the range values
    index = -1 
    for i in range(len(octetList)):
        if "-" in octetList[i]:
            index = i

    #split the given ip address so that the last element
    #on the left side is the start of the range and 
    #the first element of the right side is the end 
    #of the range
    leftOfDash, rightOfDash = givenIpAddress.split("-")
    leftList = leftOfDash.split(".")
    rightList = rightOfDash.split(".")

    #using the copies of the ip address replace the octet
    #with the range with the start value of the range at the 
    #index where the range values are in the list
    for i in range(len(octetList)):
        if i == index:
            startRange[i] = leftList[-1]

    #using the copies of the ip address replace the octet
    #with the range with the end value of the range at the
    #index where the range values are in the list
    for i in range(len(octetList)):
        if i == index:
            endRange[i] = rightList[0]

    #convert list back to string delimited with period
    start = ".".join(startRange)
    end = ".".join(endRange)
    print("start:", start)
    print("end:", end)

    #print out the range using the ipaddress module function
    #the start and end ip addresses are cast to int
    #for the iteration then cast back to ipaddress class
    #format for the printing
    start_ip = ipaddress.IPv4Address(start)
    end_ip = ipaddress.IPv4Address(end)
    for ip_int in range(int(start_ip), int(end_ip)):
        print(ipaddress.IPv4Address(ip_int))


def printWildCard(ipNetwork):
    #find the index in the octet list that has the wildcard
    #get the ip address from the input
    givenIpAddress = ipNetwork
    
    #convert ip address string to list 
    octetList = givenIpAddress.split(".")

    #get index of element with the wildcard
    index = -1 
    for i in range(len(octetList)):
        if "*" in octetList[i]:
            index = i
    
    for i in range(1, 255):
        octetList[index] = str(i)
        print(".".join(octetList))


def main(args):
    #remove hash to test cidr input
    #printCidr(args[1])

    #remove hash to test range input
    #printRange(args[1])

    #remove hash to test wildcard input
    printWildCard(args[1])

if __name__ == "__main__":
    main(sys.argv)
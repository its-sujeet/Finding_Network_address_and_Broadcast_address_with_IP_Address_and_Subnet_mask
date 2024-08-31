
# taking Ip_address as Input
ip_add= input("Enter the ip address: ")

# Splitting based on commas
ip_bits= ip_add.split(".")

# Coverting into Integer
for i in range (len(ip_bits)):
    ip_bits[i] = int(ip_bits[i])


# converting into Binary:
bin_ip=[]

for i in range(4):
    bin_ip.append((format(ip_bits[i],'08b' )  ) )




# Taking Subnet_mask as a Input

subnet_mask= input("Enter the Subnet Mask: ")
print("-----------------------------------------------------------------------------")
# Splitting based on commas


subnet_bits= subnet_mask.split(".")


# Coverting into Integer

for i in range (len(subnet_bits)):
    subnet_bits[i] = int(subnet_bits[i])


# converting into Binary:
bin_subnet_mask=[]

for i in range(4):
    bin_subnet_mask.append((format(subnet_bits[i],'08b' )  ) )


bin_network_add= []

for i in range(4):
    nw= int (bin_subnet_mask[i],2) & int (bin_ip[i],2)
    # bin_network_add.append(bin_subnet_mask[i] & bin_ip[i])
    bin_network_add.append(format(nw,'08b'))
    

network_add=[]

for i in range (4):
    network_add.append(int(bin_network_add[i],2))






print("Network Address: ", end=' ')

for j in range(4):
    if(j != 3):
        print(f"{network_add[j]}.", end='')
    else:
        print(network_add[j])


max_subnet_mask=[255,255,255,255]
brod_range=[]
for i in range(4):
    brod_range.append( max_subnet_mask[i] - subnet_bits[i])


broad_address=[]
for i in range(4):
    broad_address.append(network_add[i] + brod_range[i])

print("Broadcast Address: ",end=" ")
for j in range(4):
    if(j != 3):
        print(f"{broad_address[j]}.", end='')
    else:
        print(broad_address[j])

print("First Valid Ip: ", end=" ")

for j in range(4):
    if(j != 3):
        print(f"{network_add[j]}.", end='')
    else:
        print(network_add[j]+1)




print("Last Valid Ip: ", end=" ")
for j in range(4):
    if(j != 3):
        print(f"{broad_address[j]}.", end='')
    else:
        print(broad_address[j]-1)

sum=0
for i in range(4):
    sum+=bin_subnet_mask[i].count('1')
    # print(bin_subnet_mask)

print(f"No of Host: 2^{32 - sum } = {pow(2,(32-sum))}")

print(f"Total usable Ip Address: {pow(2,32-sum)-2}")



# for j in broad_address:
#     print(j)

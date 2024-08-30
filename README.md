# Finding Broadcast Address and Network Address

This Python script calculates the network address, broadcast address, valid IP range, and the number of hosts given an IP address and subnet mask.

## Features

- **Network Address Calculation:** Computes the network address based on the provided IP address and subnet mask.
- **Broadcast Address Calculation:** Determines the broadcast address for the given subnet mask.
- **Valid IP Range:** Provides the first and last valid IP addresses in the subnet.
- **Number of Hosts:** Calculates the number of usable IP addresses in the subnet.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/its-sujeet/Finding_Network_address_and_Broadcast_address_with_IP_Address_and_Subnet_mask.git
   cd Finding_Network_address_and_Broadcast_address_with_IP_Address_and_Subnet_mask
   ```

2. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the script:

   ```bash
   python Finding_Broadcast_address_and_Network_address.py
   ```

2. Input the IP address and subnet mask when prompted:

   ```
   Enter the IP address: 192.168.1.10
   Enter the Subnet Mask: 255.255.255.0
   ```

3. The script will output:

   - **Network Address:** The network address derived from the IP and subnet mask.
   - **Broadcast Address:** The broadcast address for the subnet.
   - **First Valid IP:** The first usable IP address within the subnet.
   - **Last Valid IP:** The last usable IP address within the subnet.
   - **Number of Hosts:** Total number of valid host IPs in the subnet.

## Example Output

For an IP address `192.168.1.10` and subnet mask `255.255.255.0`, the output will be:

```
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
First Valid IP: 192.168.1.1
Last Valid IP: 192.168.1.254
Number of Hosts: 254
```

## Code Explanation

1. **Input Handling:** Receives IP address and subnet mask from user input and splits them into octets.
2. **Binary Conversion:** Converts IP and subnet mask octets into binary format for computation.
3. **Address Calculations:** Uses bitwise operations to compute the network and broadcast addresses.
4. **Host Calculation:** Determines the total number of valid hosts in the subnet by calculating the number of bits used for hosts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on [GitHub](https://github.com/its-sujeet/Finding_Network_address_and_Broadcast_address_with_IP_Address_and_Subnet_mask) or contact me at [your email].

---

Feel free to replace `[your email]` with your actual email address and adjust any other details as needed. If there's anything specific you'd like to modify or add, just let me know!

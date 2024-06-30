from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('IP'):
        # Extracting relevant information from IP layer
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")

        # Checking if the packet has TCP or UDP layer
        if packet.haslayer('TCP'):
            try:
                payload = packet['TCP'].payload
                print(f"Payload (TCP): {payload}")
            except Exception as e:
                print(f"Error extracting payload (TCP): {e}")
        elif packet.haslayer('UDP'):
            try:
                payload = packet['UDP'].payload
                print(f"Payload (UDP): {payload}")
            except Exception as e:
                print(f"Error extracting payload (UDP): {e}")

        print("="*50)

# Sniffing packets on the network
sniff(prn=packet_callback, store=0)

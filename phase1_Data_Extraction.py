# Tanim's Final Data Extraction Script
# CSC 5290 - Cyber Security Practice
import pandas as pd
from scapy.all import sniff, IP
import os

def run_extraction():
    pcap_dir = './pcaps'
    # Grabs all pcap files in the folder
    all_files = [f for f in os.listdir(pcap_dir) if f.endswith('.pcap') or f.endswith('.pcapng')]
    
    if not all_files:
        print("!!! ERROR: No PCAP files found in the /pcaps folder.")
        return

    final_list = []

    for file_name in all_files:
        full_path = os.path.join(pcap_dir, file_name)
        print(f"Processing: {file_name}...")
        
        # --- LABELING LOGIC ---
        # If the file name is 'benign', it's normal (0). 
        # If it's DNS, LDAP, or UDP-lag, it's an attack (1).
        if 'benign' in file_name.lower():
            current_label = 0
            print("   -> Labeling as: NORMAL")
        else:
            current_label = 1
            print("   -> Labeling as: ATTACK")

        def process_packet(pkt):
            if IP in pkt:
                final_list.append({
                    'proto': pkt[IP].proto,
                    'port_src': pkt.sport if hasattr(pkt, 'sport') else 0,
                    'port_dst': pkt.dport if hasattr(pkt, 'dport') else 0,
                    'pkt_size': len(pkt),
                    'label': current_label
                })

        # We take 15,000 packets per file so the VM doesn't crash
        sniff(offline=full_path, prn=process_packet, count=15000)

    # Save to CSV
    if final_list:
        df = pd.DataFrame(final_list)
        df.to_csv('network_data_cleaned.csv', index=False)
        print(f"\nSUCCESS! Created 'network_data_cleaned.csv' with {len(df)} rows.")
        print("Now you can run phase2_ML_Training.py")
    else:
        print("Error: No data extracted.")

if __name__ == "__main__":
    run_extraction()

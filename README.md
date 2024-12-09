
# Corrupt Me

**Corrupt Me** is a research and testing tool designed to manipulate Word documents (`.docx`) and ZIP files by corrupting specific structures. These manipulations are intended for studying file recovery, AV evasion, and malware detection bypass mechanisms. **This tool is strictly for educational and research purposes only.**

---

## ⚠️ Disclaimer

This tool is provided for **legal and ethical use only**. Use it responsibly within the boundaries of the law. The author does not take any responsibility for misuse.

---

## Features

- **Add Extra Data to Local File Header (LFH):** Appends arbitrary data at the start of the LFH in a ZIP/Word file.
- **Zero Out Central Directory File Header (CDFH):** Fills the CDFH with zeros to simulate corruption.
- **Zero Out the End of Central Directory (EOCD):** Partially zeros out the EOCD to corrupt file recovery metadata.
- Provides insights into how attackers use file corruption to evade detection.

---

## Requirements

- **Python 3.x**
- **pyfiglet** (for the banner)

Install dependencies using pip:

```bash
pip install pyfiglet
```

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/corrupt-me.git
cd corrupt-me
```

2. Run the tool:

```bash
python corrupt_me.py
```

3. Follow the on-screen prompts to select a file and apply corruption techniques.

---

## Menu Options

### **1. Add Extra Data to LFH**
- Injects arbitrary data at the start of the Local File Header (LFH).
- Useful for testing how corrupted ZIP/Word files handle additional metadata.

### **2. Zero Out the Entire CDFH**
- Fills the Central Directory File Header (CDFH) with zeros.
- Simulates damage to the file index, affecting recovery.

### **3. Zero Out the End of EOCD**
- Zeros out the end of the End of Central Directory (EOCD) structure.
- Tests the recoverability of files with missing EOCD information.

### **4. Exit**
- Exits the program.

---

## Example Output

- **Extra data added to LFH:**
  ```
  Extra data added to the LFH. Saved as output_file.zip.
  ```
- **CDFH zeroed out:**
  ```
  CDFH zeroed out. Saved as output_file.zip.
  ```
- **EOCD partially zeroed out:**
  ```
  EOCD partially zeroed out. Saved as output_file.zip.
  ```

---

## Educational Context

### How Attackers Exploit Corrupted Files
Attackers use corrupted files to bypass antivirus by exploiting how tools handle structural errors. By tampering with headers, metadata, or archive components like the Central Directory, they confuse detection systems, allowing malicious payloads to evade scanning.

---

## License

This tool is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contribution

Feel free to contribute by submitting pull requests, reporting issues, or suggesting improvements. For inquiries, contact the author at [your-email@example.com].

---

## Author

Created by **[Your Name](https://github.com/yourusername)**.  
**GitHub Repository:** [Corrupt Me](https://github.com/yourusername/corrupt-me)

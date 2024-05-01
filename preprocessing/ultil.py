import re

def convert_tb_to_gb(value):
    if 'TB' in value:
        return float(value.replace('TB', '')) * 1024  # 1 TB = 1024 GB
    elif 'GB' in value:
        return float(value.replace('GB', ''))
    else:
        return float(value)

def remove_wh(value):
  if 'Wh' in value:
    return float(value.replace('Wh', ''))
  if 'WH' in value:
    return float(value.replace('WH', ''));
  if 'wh' in value:
    return float(value.replace('wh', ''))

def remove_gb(value):
    if 'B' in value:
        value.str.replace('B', '')
    if 'G' in value:
        value.str.replace('G', '')
    if 'GBB' in value:
        value.str.replace('B', '')
    return value

def get_first_number(s):
    if not isinstance(s, str):
        return None
    
    # Using regular expression to find the first number in the string
    match = re.search(r'\d+', s)
    if match:
        return int(match.group())
    else:
        return None

def get_number(s):
    if not isinstance(s, str):
        return None
    # Using regular expression to find the number in the string
    match = re.search(r'\d+,\d+', s)
    if match:
        return float(match.group().replace(',', '.'))
    else:
        return None
    
def get_first_word(s):
    if not isinstance(s, str):
        return None
    # Split the string by whitespace and take the first element
    words = s.split()
    if words:
        if words[1] == 'Core' or words[1] == 'Core™':
            return 'Intel'
        if words[1] == 'Ryzen':
            return 'AMD'
        return words[1]
    else:
        return None

def get_cpu_gen(s):
    if not isinstance(s, str):
        return None
    words = s.split()
    if len(words) <= 2:
        return "1"
    if words:
        if 'Ryzen' in words[1]:
            return f'Ryzen {words[2]}'
        if 'Ryzen' in words[2]:
            return f'Ryzen {words[3]}'
        if '-' in words[2]:
            return words[2].split('-')[0]
        return words[2]
    else:
        return None

def get_ram_max(s):
    match = re.search(r'(?:up to|tối đa)\s+(\d+)', s, re.IGNORECASE)
    if match:
        return int(match.group(1))
    else:
        return None

# Test cases
print(get_ram_max("8GB DDR4 3200MHz (Up to 16GB)"))  # Output: 16
print(get_ram_max("8GB DDR4 3200MHz (up to 32GB)"))  # Output: 32
print(get_ram_max("16GB (8GB Soldered DDR4-3200MHz + 8GB SO-DIMM DDR4-3200MHz) (Up to 16GB)"))  # Output: 64
import re

middle_endian = input("Date: ").strip()
mm,dd,yyyy = re.split('[ -/.]', middle_endian)
print(f"{yyyy} {mm} {dd}")
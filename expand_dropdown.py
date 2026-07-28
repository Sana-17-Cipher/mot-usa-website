import os
import glob
import re

dir_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main'
files_root = glob.glob(f'{dir_path}/*.html')
files_locations = glob.glob(f'{dir_path}/locations/*.html')
all_files = files_root + files_locations

for file in all_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Unhide the locations menu by removing 'hidden' and making it just 'flex flex-col'
    content = content.replace(
        'id="mobile-locations-menu" class="hidden flex-col',
        'id="mobile-locations-menu" class="flex flex-col'
    )

    # 2. Add 'rotate-180' to the chevron icon so it looks expanded by default
    content = content.replace(
        'id="mobile-locations-icon" class="w-5 h-5 transition-transform"',
        'id="mobile-locations-icon" class="w-5 h-5 transition-transform rotate-180"'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Expanded dropdown in {file}')

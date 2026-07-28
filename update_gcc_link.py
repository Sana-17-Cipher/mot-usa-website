import glob

files = glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/*.html') + glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/locations/*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the GCC link
    new_content = content.replace('href="https://gcc.momsonteaching.com/"', 'href="https://gulf.momsonteaching.com/"')
    
    # Just in case there was a typo and I put `#` in the initial script
    new_content = new_content.replace('href="#" target="_blank" class="hover:text-marigold transition flex items-center gap-1">GCC Website', 'href="https://gulf.momsonteaching.com/" target="_blank" class="hover:text-marigold transition flex items-center gap-1">GCC Website')

    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

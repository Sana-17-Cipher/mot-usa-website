import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The current padding is padding-top: 100px; for .hero-section in mobile view
content = content.replace(
    '.hero-section { min-height: auto; padding-top: 100px; padding-bottom: 0;',
    '.hero-section { min-height: auto; padding-top: 140px; padding-bottom: 0;'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Adjusted top padding.")

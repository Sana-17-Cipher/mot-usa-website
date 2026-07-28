import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section Paddings for mobile
content = content.replace('class="bg-parchment pt-12 pb-24 px-6 mt-6', 'class="bg-parchment pt-8 pb-16 md:pt-12 md:pb-24 px-6 mt-6')
content = content.replace('class="py-24 px-6', 'class="py-16 md:py-24 px-6')
content = content.replace('class="max-w-5xl mx-auto px-6 pb-24 pt-10"', 'class="max-w-5xl mx-auto px-6 pb-16 md:pb-24 pt-10"')

# 2. Update Font Sizes in Headings for mobile
content = content.replace('font-display text-5xl md:text-6xl text-navy', 'font-display text-4xl md:text-5xl lg:text-6xl text-navy')
content = content.replace('font-display text-4xl md:text-5xl text-navy', 'font-display text-3xl md:text-4xl lg:text-5xl text-navy')
content = content.replace('font-display text-4xl text-navy', 'font-display text-3xl md:text-4xl text-navy')

# 3. Fix Hero Image Height for mobile
content = content.replace('h-[500px] object-cover', 'h-[300px] md:h-[400px] lg:h-[500px] object-cover')
content = content.replace('border-[12px] border-white/50', 'border-[8px] md:border-[12px] border-white/50')

# 4. Fix Timeline Bullets alignment mathematically
# -left-[41px] md:-left-[57px] -> -left-[45px] md:-left-[65px]
content = content.replace('-left-[41px] md:-left-[57px]', '-left-[45px] md:-left-[65px]')

# 5. Fix Padding on the Final CTA card for mobile
content = content.replace('rounded-[3rem] p-12 md:p-16', 'rounded-[2rem] md:rounded-[3rem] p-8 md:p-16')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Responsive classes applied!")

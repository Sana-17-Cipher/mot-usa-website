import os
import glob
import re

dir_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/locations'
files = glob.glob(f'{dir_path}/*.html')

menu_new = '''  <!-- Mobile Menu Fullscreen Overlay -->
  <div id="mobile-menu" class="hidden md:hidden fixed inset-0 bg-[#FBF6EC] z-40 flex-col pt-[120px] px-6 pb-8 gap-6 overflow-y-auto w-full h-screen">
    <a href="/about.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">About</a>
    <a href="/services.html" class="text-lg font-medium hover:text-marigold-dark text-[#C9862A] block">Services</a>
    <a href="/locations/new-jersey.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">Locations</a>
    <a href="/faq.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">FAQ</a>
    <a href="/pricing.html" class="text-lg font-medium hover:text-marigold-dark text-[#C9862A] block">Pricing</a>
    <a href="/contact.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">Contact</a>
    <div class="mt-auto pt-6 w-full">
      <a href="tel:+1XXXXXXXXXX" class="bg-[#E8A63C] text-center text-navy font-semibold px-5 py-4 rounded-full text-base block w-full hover:bg-[#C9862A] transition">Book Free Demo</a>
    </div>
  </div>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the entire mobile menu
    content = re.sub(
        r'<!-- Mobile Menu Dropdown -->.*?</div>\s*</header>',
        menu_new + '\n</header>',
        content,
        flags=re.DOTALL
    )

    # 2. Make Grid responsive
    content = content.replace(
        '<div style="display:grid; grid-template-columns:1fr 1.2fr 1fr; grid-template-rows:auto auto; gap:16px;">',
        '<div class="grid grid-cols-1 lg:grid-cols-[1fr_1.2fr_1fr] lg:grid-rows-[auto_auto] gap-4">'
    )

    # Card 1
    content = content.replace(
        'style="grid-column:1; grid-row:1; min-height:220px;"\n       class="bg-navy',
        'class="lg:col-start-1 lg:row-start-1 min-h-[220px] bg-navy'
    )
    # Card 2
    content = content.replace(
        'style="grid-column:2; grid-row:1/3; min-height:456px;"\n         class="rounded-3xl',
        'class="lg:col-start-2 lg:row-span-2 min-h-[456px] rounded-3xl'
    )
    # Card 3
    content = content.replace(
        'style="grid-column:3; grid-row:1; min-height:220px;"\n       class="bg-white',
        'class="lg:col-start-3 lg:row-start-1 min-h-[220px] bg-white'
    )
    # Card 4
    content = content.replace(
        'style="grid-column:1; grid-row:2;"\n         class="bg-marigold',
        'class="lg:col-start-1 lg:row-start-2 bg-marigold'
    )
    # Card 5
    content = content.replace(
        'style="grid-column:3; grid-row:2;"\n         class="bg-white',
        'class="lg:col-start-3 lg:row-start-2 bg-white'
    )
    
    # 3. Make hero responsive (-mt-24 overlap issue)
    content = content.replace(
        '<div class="max-w-6xl mx-auto px-6 relative z-20 -mt-24 mb-16">',
        '<div class="max-w-6xl mx-auto px-6 relative z-20 lg:-mt-24 mt-8 mb-16">'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {file}')

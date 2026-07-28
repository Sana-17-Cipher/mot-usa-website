import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Navbar width: change w-[calc(100%-48px)] to w-[calc(100%-24px)] for mobile
# Actually, it's better to just give it md:w-[calc(100%-48px)] w-[calc(100%-20px)]
content = content.replace(
    'w-[calc(100%-48px)]',
    'w-[calc(100%-20px)] md:w-[calc(100%-48px)]'
)

# 2. Navbar inner padding: py-1.5 px-1.5 pl-6 -> py-1.5 px-1.5 pl-4 md:pl-6
content = content.replace(
    'py-1.5 px-1.5 pl-6',
    'py-1.5 px-1.5 pl-4 md:pl-6'
)

# 3. Logo & Brand Text adjustments for mobile (make logo 32px instead of 36px, gap-1 instead of gap-2)
content = content.replace(
    '<a href="/" class="flex items-center gap-2 md:gap-2"><img src="images/logo.png" alt="Moms on Teaching logo" width="40" height="40" class="rounded-full w-9 h-9 md:w-10 md:h-10"><span class="font-display text-[13px] md:text-xl text-navy leading-tight">Moms on<br class="md:hidden"> Teaching <span class="md:hidden">USA</span></span></a>',
    '<a href="/" class="flex items-center gap-1.5 md:gap-2"><img src="images/logo.png" alt="Moms on Teaching logo" width="40" height="40" class="rounded-full w-8 h-8 md:w-10 md:h-10"><span class="font-display text-[11px] md:text-[13px] lg:text-xl text-navy leading-tight whitespace-nowrap">Moms on<br class="md:hidden"> Teaching <span class="md:hidden">USA</span></span></a>'
)

# 4. Button & Hamburger adjustments
content = content.replace(
    '<div class="flex items-center gap-2 md:gap-3">\n      <a href="tel:+1XXXXXXXXXX" class="inline-block bg-marigold hover:bg-marigold-dark text-navy font-bold md:font-semibold px-3 py-1.5 md:px-5 md:py-2.5 rounded-full text-[11px] md:text-sm transition whitespace-nowrap">Book Free Demo</a>\n      \n      <!-- Mobile menu button -->\n      <button id="mobile-menu-btn" class="md:hidden p-1.5 md:p-2 text-navy pr-3 md:pr-4" aria-label="Toggle Menu">\n        <svg class="w-6 h-6 md:w-7 md:h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>\n      </button>\n    </div>',
    '<div class="flex items-center gap-1.5 md:gap-3">\n      <a href="tel:+1XXXXXXXXXX" class="inline-block bg-marigold hover:bg-marigold-dark text-navy font-bold md:font-semibold px-2.5 py-1.5 md:px-5 md:py-2.5 rounded-full text-[10px] md:text-sm transition whitespace-nowrap">Book Free Demo</a>\n      \n      <!-- Mobile menu button -->\n      <button id="mobile-menu-btn" class="md:hidden p-1 text-navy pr-2 md:pr-4" aria-label="Toggle Menu">\n        <svg class="w-6 h-6 md:w-7 md:h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>\n      </button>\n    </div>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Navbar shrunk and adjusted for mobile!")

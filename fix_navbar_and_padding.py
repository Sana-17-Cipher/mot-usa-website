import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update logo area in the navbar
content = content.replace(
    '<a href="/" class="flex items-center gap-2"><img src="images/logo.png" alt="Moms on Teaching logo" width="40" height="40" class="rounded-full"><span class="font-display text-xl text-navy hidden sm:inline">Moms on Teaching</span></a>',
    '<a href="/" class="flex items-center gap-2 md:gap-2"><img src="images/logo.png" alt="Moms on Teaching logo" width="40" height="40" class="rounded-full w-9 h-9 md:w-10 md:h-10"><span class="font-display text-[13px] md:text-xl text-navy leading-tight">Moms on<br class="md:hidden"> Teaching <span class="md:hidden">USA</span></span></a>'
)

# 2. Update button area in the navbar
old_buttons = '''    <div class="flex items-center gap-3">
      <a href="tel:+1XXXXXXXXXX" class="hidden sm:inline-block bg-marigold hover:bg-marigold-dark text-navy font-semibold px-5 py-2.5 rounded-full text-sm transition">Book Free Demo</a>
      
      <!-- Mobile menu button -->
      <button id="mobile-menu-btn" class="md:hidden p-2 text-navy pr-4" aria-label="Toggle Menu">
        <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
      </button>
    </div>'''

new_buttons = '''    <div class="flex items-center gap-2 md:gap-3">
      <a href="tel:+1XXXXXXXXXX" class="inline-block bg-marigold hover:bg-marigold-dark text-navy font-bold md:font-semibold px-3 py-1.5 md:px-5 md:py-2.5 rounded-full text-[11px] md:text-sm transition whitespace-nowrap">Book Free Demo</a>
      
      <!-- Mobile menu button -->
      <button id="mobile-menu-btn" class="md:hidden p-1.5 md:p-2 text-navy pr-3 md:pr-4" aria-label="Toggle Menu">
        <svg class="w-6 h-6 md:w-7 md:h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
      </button>
    </div>'''

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons)
else:
    # Use regex if exact match fails
    content = re.sub(
        r'<div class="flex items-center gap-3">\s*<a href="tel:\+1XXXXXXXXXX" class="hidden sm:inline-block[^>]+>Book Free Demo</a>\s*<!-- Mobile menu button -->\s*<button id="mobile-menu-btn"[^>]+>\s*<svg[^>]+><path[^>]+></path></svg>\s*</button>\s*</div>',
        new_buttons,
        content
    )

# 3. Increase padding-top for mobile hero text to push it down further
content = content.replace(
    '.hero-section { min-height: auto; padding-top: 140px; padding-bottom: 0;',
    '.hero-section { min-height: auto; padding-top: 180px; padding-bottom: 0;'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Navbar updated and text moved down!")

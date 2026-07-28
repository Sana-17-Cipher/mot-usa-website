import os
import glob
import re

dir_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main'
files_root = glob.glob(f'{dir_path}/*.html')
files_locations = glob.glob(f'{dir_path}/locations/*.html')
all_files = files_root + files_locations

menu_new = '''  <!-- Mobile Menu Fullscreen Overlay -->
  <div id="mobile-menu" class="hidden md:hidden fixed inset-0 bg-[#FBF6EC] z-40 flex-col pt-[120px] px-6 pb-8 gap-6 overflow-y-auto w-full h-screen">
    <a href="/about.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">About</a>
    <a href="/services.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">Services</a>
    
    <div>
      <button id="mobile-locations-btn" class="text-lg font-medium hover:text-marigold-dark text-navy flex items-center justify-between w-full">
        Locations 
        <svg id="mobile-locations-icon" class="w-5 h-5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
      </button>
      <div id="mobile-locations-menu" class="hidden flex-col gap-4 mt-4 pl-4 border-l-2 border-marigold/30">
        <a href="/locations/new-jersey.html" class="text-base font-medium text-navy/80 hover:text-marigold-dark">New Jersey</a>
        <a href="/locations/california.html" class="text-base font-medium text-navy/80 hover:text-marigold-dark">California</a>
        <a href="/locations/texas.html" class="text-base font-medium text-navy/80 hover:text-marigold-dark">Texas</a>
        <a href="/locations/illinois.html" class="text-base font-medium text-navy/80 hover:text-marigold-dark">Illinois</a>
        <a href="/locations/new-york.html" class="text-base font-medium text-navy/80 hover:text-marigold-dark">New York</a>
        <a href="/locations/washington.html" class="text-base font-medium text-navy/80 hover:text-marigold-dark">Washington</a>
      </div>
    </div>

    <a href="/faq.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">FAQ</a>
    <a href="/pricing.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">Pricing</a>
    <a href="/contact.html" class="text-lg font-medium hover:text-marigold-dark text-navy block">Contact</a>
    <div class="mt-auto pt-6 w-full">
      <a href="tel:+1XXXXXXXXXX" class="bg-[#E8A63C] text-center text-navy font-semibold px-5 py-4 rounded-full text-base block w-full hover:bg-[#C9862A] transition">Book Free Demo</a>
    </div>
  </div>'''

script_addition = '''  // ====== Mobile menu toggle logic ======
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      mobileMenu.classList.toggle('flex');
    });
  }

  // ====== Mobile Locations Dropdown ======
  const mobLocBtn = document.getElementById('mobile-locations-btn');
  const mobLocMenu = document.getElementById('mobile-locations-menu');
  const mobLocIcon = document.getElementById('mobile-locations-icon');
  if (mobLocBtn && mobLocMenu) {
    mobLocBtn.addEventListener('click', () => {
      mobLocMenu.classList.toggle('hidden');
      mobLocMenu.classList.toggle('flex');
      mobLocIcon.classList.toggle('rotate-180');
    });
  }'''

for file in all_files:
    if os.path.basename(file) == 'index.html':
        continue # Already updated index.html manually
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the entire mobile menu (can be Mobile Menu Dropdown or Mobile Menu Fullscreen Overlay)
    content = re.sub(
        r'<!-- Mobile Menu (Dropdown|Fullscreen Overlay) -->.*?</div>\s*</header>',
        menu_new + '\n</header>',
        content,
        flags=re.DOTALL
    )

    # 2. Update the script part. Remove the old mobile logic and insert the new one
    content = re.sub(
        r'// Mobile menu toggle logic.*?\}\);[\s]*\}',
        script_addition.replace('// ====== Mobile menu toggle logic ======\n', ''),
        content,
        flags=re.DOTALL
    )
    
    # Also handles if the script was labelled differently
    content = re.sub(
        r'// ====== Mobile menu toggle logic ======.*?(?=</script>)',
        script_addition + '\n',
        content,
        flags=re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {file}')

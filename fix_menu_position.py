import os
import glob
import re

dir_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main'
files_root = glob.glob(f'{dir_path}/*.html')
files_locations = glob.glob(f'{dir_path}/locations/*.html')
all_files = files_root + files_locations

script_replacement = '''<script>
  // ====== Mobile menu toggle logic ======
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (mobileBtn && mobileMenu) {
    const iconPath = mobileBtn.querySelector('path');
    mobileBtn.addEventListener('click', () => {
      const isHidden = mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden');
      mobileMenu.classList.toggle('flex');
      if (isHidden) {
        // Menu is now open -> Show X
        if (iconPath) iconPath.setAttribute('d', 'M6 18L18 6M6 6l12 12');
      } else {
        // Menu is now closed -> Show Hamburger
        if (iconPath) iconPath.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');
      }
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
      if (mobLocIcon) mobLocIcon.classList.toggle('rotate-180');
    });
  }
</script>'''

for file in all_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move mobile menu out of header
    match = re.search(r'(<!-- Mobile Menu Fullscreen Overlay -->.*?)\s*</header>', content, flags=re.DOTALL)
    if match:
        menu_block = match.group(1)
        # Remove the menu_block from inside the header
        content = content.replace(menu_block, '')
        # Add it right after </header>
        content = content.replace('</header>', '</header>\n\n' + menu_block)

    # Replace the script block
    content = re.sub(
        r'<script>\s*// ====== Mobile menu toggle logic ======.*?</script>',
        script_replacement,
        content,
        flags=re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {file}')

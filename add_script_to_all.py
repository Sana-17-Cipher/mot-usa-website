import os
import glob
import re

dir_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main'
files_root = glob.glob(f'{dir_path}/*.html')
files_locations = glob.glob(f'{dir_path}/locations/*.html')
all_files = files_root + files_locations

script_addition = '''<script>
  // ====== Mobile menu toggle logic ======
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
  }
</script>
'''

for file in all_files:
    if os.path.basename(file) == 'index.html':
        continue # Already updated index.html manually
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing script that toggles the mobile menu
    # Be careful not to remove other scripts (like structured data, which is in <head>)
    # We'll just look for a script containing 'mobile-menu-btn'
    content = re.sub(
        r'<script>[^<]*mobile-menu-btn[^<]*</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Now insert the new script block right before </body>
    if '</body>' in content:
        content = content.replace('</body>', script_addition + '</body>')
    else:
        # If no </body> tag is found for some reason, append it
        content += '\n' + script_addition

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated script in {file}')

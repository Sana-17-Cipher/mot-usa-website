import glob

files = glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/*.html') + glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/locations/*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the 3 links from Resources
    links_to_remove = '''        <li><a href="/legal/privacy-policy.html" class="hover:text-marigold transition">Privacy Policy</a></li>
        <li><a href="/legal/terms.html" class="hover:text-marigold transition">Terms & Conditions</a></li>
        <li><a href="/sitemap.html" class="hover:text-marigold transition">Sitemap</a></li>\n'''
    
    content = content.replace(links_to_remove, '')

    # Also handle possible variations in newlines
    content = content.replace('<li><a href="/legal/privacy-policy.html" class="hover:text-marigold transition">Privacy Policy</a></li>\n', '')
    content = content.replace('<li><a href="/legal/terms.html" class="hover:text-marigold transition">Terms & Conditions</a></li>\n', '')
    content = content.replace('<li><a href="/sitemap.html" class="hover:text-marigold transition">Sitemap</a></li>\n', '')

    # 2. Separate footer from free demo CTA by changing its background and adding a top border
    # Previous footer opening tag: <footer class="bg-navy text-parchment/80 py-16 text-sm">
    # We will change it to bg-navy-dark and add a border-t border-white/10
    content = content.replace(
        '<footer class="bg-navy text-parchment/80 py-16 text-sm">',
        '<footer class="bg-navy-dark text-parchment/80 py-16 text-sm border-t border-white/10">'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")

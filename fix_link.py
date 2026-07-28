import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific link for the Meet Our Teacher Moms CTA
content = content.replace(
    'href="tel:+1XXXXXXXXXX" class="inline-flex items-center justify-center bg-marigold hover:bg-marigold-dark text-navy font-bold text-lg px-10 py-5 rounded-full transition-transform hover:-translate-y-1 shadow-xl">\n        Meet Our Teacher-Moms',
    'href="/contact.html" class="inline-flex items-center justify-center bg-marigold hover:bg-marigold-dark text-navy font-bold text-lg px-10 py-5 rounded-full transition-transform hover:-translate-y-1 shadow-xl">\n        Meet Our Teacher-Moms'
)
# Just in case whitespace is slightly different
content = re.sub(r'href="tel:\+1XXXXXXXXXX"([^>]+>[\s]*Meet Our Teacher-Moms)', r'href="/contact.html"\1', content)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Button link updated!")

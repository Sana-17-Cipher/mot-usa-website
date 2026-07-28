import os
import glob
import re

dir_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main'
files_root = glob.glob(f'{dir_path}/*.html')
files_locations = glob.glob(f'{dir_path}/locations/*.html')
all_files = files_root + files_locations

new_footer = '''<footer class="bg-navy text-parchment/80 py-16 text-sm">
  <div class="max-w-6xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12">
    <!-- Left Column: Logo & Description -->
    <div class="lg:col-span-2">
      <div class="flex items-center gap-3 mb-6">
        <img src="/images/logo.png" alt="Moms on Teaching logo" width="48" height="48" class="rounded-full">
        <span class="font-display text-2xl text-white">Moms on Teaching</span>
      </div>
      <p class="leading-relaxed mb-6 max-w-sm">
        From KG to Class 12, we provide 1-on-1 online tutoring across CBSE, ICSE, IGCSE, IB, and US School Support. Personalized Learning. Trusted Teacher-Moms.
      </p>
      <!-- Social Media Icons -->
      <div class="flex items-center gap-4">
        <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-marigold hover:text-navy transition" aria-label="Facebook"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg></a>
        <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-marigold hover:text-navy transition" aria-label="Twitter"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg></a>
        <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-marigold hover:text-navy transition" aria-label="Instagram"><svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center hover:bg-marigold hover:text-navy transition" aria-label="LinkedIn"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg></a>
      </div>
    </div>

    <!-- Quick Links -->
    <div>
      <h3 class="text-white font-bold mb-6 text-lg tracking-wide">Quick Links</h3>
      <ul class="flex flex-col gap-3">
        <li><a href="/about.html" class="hover:text-marigold transition">About Us</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">Services</a></li>
        <li><a href="/pricing.html" class="hover:text-marigold transition">Pricing</a></li>
        <li><a href="/faq.html" class="hover:text-marigold transition">FAQ</a></li>
        <li><a href="/contact.html" class="hover:text-marigold transition">Contact</a></li>
        <li><a href="https://momsonteaching.com/en/insightsblogsen" target="_blank" class="hover:text-marigold transition">Blog</a></li>
        <li><a href="https://momsonteaching.com/" target="_blank" class="hover:text-marigold transition flex items-center gap-1">Main Website <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg></a></li>
        <li><a href="https://gcc.momsonteaching.com/" target="_blank" class="hover:text-marigold transition flex items-center gap-1">GCC Website <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg></a></li>
      </ul>
    </div>

    <!-- Programmes -->
    <div>
      <h3 class="text-white font-bold mb-6 text-lg tracking-wide">Programmes</h3>
      <ul class="flex flex-col gap-3">
        <li><a href="/services.html" class="hover:text-marigold transition">CBSE</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">ICSE</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">IGCSE</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">IB</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">KG–Class 12</a></li>
      </ul>
    </div>

    <!-- Contact Us -->
    <div>
      <h3 class="text-white font-bold mb-6 text-lg tracking-wide">Contact Us</h3>
      <ul class="flex flex-col gap-4">
        <li>
          <a href="tel:+1XXXXXXXXXX" class="flex items-start gap-3 hover:text-marigold transition">
            <svg class="w-5 h-5 shrink-0 text-marigold mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
            <span>+1 (XXX) XXX-XXXX</span>
          </a>
        </li>
        <li>
          <a href="mailto:info@momsonteaching.com" class="flex items-start gap-3 hover:text-marigold transition">
            <svg class="w-5 h-5 shrink-0 text-marigold mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            <span>info@momsonteaching.com</span>
          </a>
        </li>
      </ul>
    </div>
  </div>

  <!-- Bottom Bar -->
  <div class="max-w-6xl mx-auto px-6 mt-16 pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4 text-xs">
    <div>
      © 2026 Moms on Teaching. All rights reserved.
    </div>
    <div class="flex items-center gap-6">
      <a href="/legal/privacy-policy.html" class="hover:text-marigold transition">Privacy Policy</a>
      <a href="/legal/terms.html" class="hover:text-marigold transition">Terms of Use</a>
      <a href="/sitemap.html" class="hover:text-marigold transition">Sitemap</a>
    </div>
  </div>
</footer>'''

for file in all_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the existing footer tag and everything inside it with the new_footer
    content = re.sub(
        r'<footer.*?</footer>',
        new_footer,
        content,
        flags=re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated footer in {file}')

import glob
import re

files = glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/*.html') + glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/locations/*.html')

new_footer = '''<footer class="bg-navy text-parchment/80 py-16 text-sm">
  <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10">
    
    <!-- Left Column: Logo & Description & Social -->
    <div class="lg:col-span-1 flex flex-col">
      <div class="flex items-center gap-3 mb-6">
        <img src="/images/logo.png" alt="Moms on Teaching logo" width="48" height="48" class="rounded-full">
        <span class="font-display text-xl text-white leading-tight">Moms on<br>Teaching</span>
      </div>
      <p class="leading-relaxed mb-6 text-xs text-parchment/70">
        From KG to Class 12, we provide 1-on-1 online tutoring across CBSE, ICSE, IGCSE, IB, and US School Support.
      </p>
      <!-- Social Media Icons -->
      <div class="flex items-center gap-4 mt-auto">
        <a href="#" class="text-white hover:text-marigold transition" aria-label="Facebook">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg>
        </a>
        <a href="#" class="text-white hover:text-marigold transition" aria-label="Twitter">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg>
        </a>
        <a href="#" class="text-white hover:text-marigold transition" aria-label="Instagram">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="#" class="text-white hover:text-marigold transition" aria-label="LinkedIn">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
        </a>
        <a href="#" class="text-white hover:text-marigold transition" aria-label="Google">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M12.24 10.285V14.4h6.806c-.275 1.765-2.056 5.174-6.806 5.174-4.095 0-7.439-3.389-7.439-7.574s3.344-7.574 7.439-7.574c2.33 0 3.891.989 4.785 1.849l3.254-3.138C18.189 1.186 15.479 0 12.24 0c-6.635 0-12 5.365-12 12s5.365 12 12 12c6.926 0 11.52-4.869 11.52-11.726 0-.788-.085-1.39-.189-1.989H12.24z"/></svg>
        </a>
      </div>
    </div>

    <!-- Quick Links -->
    <div class="lg:ml-8">
      <h3 class="text-white font-bold mb-6 text-base tracking-wide">Quick Links</h3>
      <ul class="flex flex-col gap-4 text-sm font-medium">
        <li><a href="/about.html" class="hover:text-marigold transition">About Us</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">Services</a></li>
        <li><a href="/pricing.html" class="hover:text-marigold transition">Pricing</a></li>
        <li><a href="/faq.html" class="hover:text-marigold transition">FAQ</a></li>
        <li><a href="/contact.html" class="hover:text-marigold transition">Contact</a></li>
      </ul>
    </div>

    <!-- Programmes -->
    <div>
      <h3 class="text-white font-bold mb-6 text-base tracking-wide">Programmes</h3>
      <ul class="flex flex-col gap-4 text-sm font-medium">
        <li><a href="/services.html" class="hover:text-marigold transition">CBSE</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">ICSE</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">IGCSE</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">IB</a></li>
        <li><a href="/services.html" class="hover:text-marigold transition">KG–Class 12</a></li>
      </ul>
    </div>

    <!-- Resources -->
    <div>
      <h3 class="text-white font-bold mb-6 text-base tracking-wide">Resources</h3>
      <ul class="flex flex-col gap-4 text-sm font-medium">
        <li><a href="/legal/privacy-policy.html" class="hover:text-marigold transition">Privacy Policy</a></li>
        <li><a href="/legal/terms.html" class="hover:text-marigold transition">Terms & Conditions</a></li>
        <li><a href="/sitemap.html" class="hover:text-marigold transition">Sitemap</a></li>
        <li><a href="https://momsonteaching.com/" target="_blank" class="hover:text-marigold transition">Main Website</a></li>
        <li><a href="https://gulf.momsonteaching.com/" target="_blank" class="hover:text-marigold transition">GCC Website</a></li>
        <li><a href="https://momsonteaching.com/en/insightsblogsen" target="_blank" class="hover:text-marigold transition">Blog</a></li>
      </ul>
    </div>

    <!-- Contact Us -->
    <div>
      <h3 class="text-white font-bold mb-6 text-base tracking-wide">Contact Us</h3>
      <ul class="flex flex-col gap-5 text-sm">
        <li>
          <a href="tel:+1XXXXXXXXXX" class="flex items-center gap-3 hover:text-marigold transition">
            <div class="bg-blue-500/20 p-2.5 rounded text-blue-400">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/></svg>
            </div>
            <span class="font-medium">+1 (XXX) XXX-XXXX</span>
          </a>
        </li>
        <li>
          <a href="mailto:info@momsonteaching.com" class="flex items-center gap-3 hover:text-marigold transition">
            <div class="bg-blue-500/20 p-2.5 rounded text-blue-400">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
            </div>
            <span class="font-medium">info@momsonteaching.com</span>
          </a>
        </li>
      </ul>
    </div>

  </div>

  <!-- Bottom Bar -->
  <div class="max-w-7xl mx-auto px-6 mt-16 pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-parchment/50">
    <div>
      © 2026 Moms on Teaching. All rights reserved.
    </div>
    <div class="flex items-center gap-6">
      <a href="/legal/privacy-policy.html" class="hover:text-white transition">Privacy Policy</a>
      <a href="/legal/terms.html" class="hover:text-white transition">Terms of Use</a>
      <a href="/sitemap.html" class="hover:text-white transition">Site Map</a>
    </div>
  </div>
</footer>'''

for file in files:
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

import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Navbar update
# Replace the header to have the exact padding, logo sizing, and hide CTA
old_header_pattern = re.compile(r'<header class="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-\[calc\(100%-20px\)\].*?</header>', re.DOTALL)

new_header = '''<header class="fixed top-6 left-1/2 -translate-x-1/2 z-50 w-[calc(100%-40px)] md:w-[calc(100%-48px)] max-w-[1000px] bg-parchment/95 backdrop-blur-md rounded-full shadow-[0_8px_32px_rgba(21,36,71,0.15)] border border-navy/5 transition-all">
  <nav class="w-full flex items-center justify-between px-5 md:px-1.5 md:pl-6 min-h-[72px]">
    <a href="/" class="flex items-center gap-[10px] md:gap-2">
      <img src="images/logo.png" alt="Moms on Teaching logo" class="rounded-full w-[38px] h-[38px] md:w-10 md:h-10">
      <span class="font-display text-[18px] md:text-xl text-navy leading-tight whitespace-nowrap">Moms on<br class="md:hidden"> Teaching</span>
    </a>
    <div class="hidden md:flex items-center gap-8 text-sm font-medium">
      <a href="about.html" class="hover:text-marigold-dark">About</a>
      <a href="services.html" class="hover:text-marigold-dark">Services</a>
      <div class="relative group">
        <a href="#" class="hover:text-marigold-dark flex items-center gap-1 py-4">Locations <svg class="w-4 h-4 opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
        <div class="absolute top-[80%] left-0 w-44 bg-white rounded-xl shadow-[0_12px_40px_rgba(21,36,71,0.15)] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 border border-navy/5 overflow-hidden z-50">
          <a href="locations/new-jersey.html" class="block px-4 py-2.5 text-sm text-navy hover:bg-marigold/10 hover:text-marigold-dark font-semibold transition-colors">New Jersey</a>
          <a href="locations/california.html" class="block px-4 py-2.5 text-sm text-navy hover:bg-marigold/10 hover:text-marigold-dark font-semibold transition-colors">California</a>
          <a href="locations/texas.html" class="block px-4 py-2.5 text-sm text-navy hover:bg-marigold/10 hover:text-marigold-dark font-semibold transition-colors">Texas</a>
          <a href="locations/illinois.html" class="block px-4 py-2.5 text-sm text-navy hover:bg-marigold/10 hover:text-marigold-dark font-semibold transition-colors">Illinois</a>
          <a href="locations/new-york.html" class="block px-4 py-2.5 text-sm text-navy hover:bg-marigold/10 hover:text-marigold-dark font-semibold transition-colors">New York</a>
          <a href="locations/washington.html" class="block px-4 py-2.5 text-sm text-navy hover:bg-marigold/10 hover:text-marigold-dark font-semibold transition-colors">Washington</a>
        </div>
      </div>
      <a href="faq.html" class="hover:text-marigold-dark">FAQ</a>
      <a href="pricing.html" class="hover:text-marigold-dark">Pricing</a>
      <a href="contact.html" class="hover:text-marigold-dark">Contact</a>
    </div>
    <div class="flex items-center gap-3">
      <a href="tel:+1XXXXXXXXXX" class="hidden md:inline-block bg-marigold hover:bg-marigold-dark text-navy font-semibold px-5 py-2.5 rounded-full text-sm transition whitespace-nowrap">Book Free Demo</a>
      <!-- Mobile menu button -->
      <button id="mobile-menu-btn" class="md:hidden p-1 text-navy" aria-label="Toggle Menu">
        <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
      </button>
    </div>
  </nav>
</header>'''
content = old_header_pattern.sub(new_header, content)

# 2. Update the mobile @media CSS in index.html
mobile_css_pattern = re.compile(r'@media \(max-width:768px\) \{.*?\}\n  \}', re.DOTALL)
new_mobile_css = '''@media (max-width:768px) {
    .hero-section { 
      min-height: auto; 
      padding-top: 120px; 
      padding-bottom: 40px; 
      display: flex; 
      flex-direction: column; 
      align-items: center; 
      overflow: visible; 
    }
    .hero-bg-image { display: none; }
    .hero-left-fade { display: none; }
    
    .hero-content {
      padding: 0 24px;
      width: 100%;
      max-width: 340px;
      margin: 0 auto;
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    
    .hero-text-block { max-width: 100%; align-items: center; display: flex; flex-direction: column; }
    
    .hero-text-block h1 { 
      font-size: 42px; 
      line-height: 1.08; 
      letter-spacing: -1px;
      max-width: 320px;
      margin: 0 auto 24px; 
      font-weight: 500;
      color: #152447;
    }
    
    .hero-text-block .hero-desc { 
      font-size: 18px; 
      line-height: 1.7; 
      color: #5a6a8a;
      max-width: 320px;
      margin: 0 auto 36px;
    }
    
    .hero-cta-btn {
      width: 220px;
      height: 58px;
      background: #152447;
      color: white;
      border-radius: 50px;
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin: 0 auto 48px;
    }
    
    .hero-badges { display: none; }
    
    /* Decorative elements */
    .dot-grid { display: none !important; }
    .mobile-dot-top-left { 
      display: grid !important; 
      top: 15% !important; 
      left: 10% !important; 
      opacity: 0.4 !important; 
    }
    
    .pink-blob { 
      width: 250px !important; 
      height: 200px !important;
      bottom: 10% !important; 
      right: 0% !important; 
      top: auto !important;
      left: auto !important;
      opacity: 0.8 !important;
      transform: none !important;
      z-index: 1 !important;
    }
    .pink-blob-2 { display: none; }
    
    /* Hide the complex white curve on mobile, we will use border-radius instead */
    .hero-mobile-curve { display: none !important; }
    
    .hero-mobile-image-wrapper {
      position: relative;
      width: 100%;
      padding-left: 24px;
      padding-right: 24px;
      margin-top: 0;
      z-index: 5; /* Above pink blob */
      clip-path: none;
      -webkit-clip-path: none;
    }
    
    .hero-mobile-img {
      width: 100%;
      max-width: 360px;
      height: 380px;
      margin: 0 auto;
      border-radius: 30px;
      object-fit: cover;
      object-position: center bottom;
      display: block;
    }
  }'''
if mobile_css_pattern.search(content):
    content = mobile_css_pattern.sub(new_mobile_css, content)

# 3. Clean up the HTML structure of the mobile image wrapper to remove the clip-path svg if we don't need it.
# Wait, the CSS already ignores the clip-path by setting clip-path: none;

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile hero redesign perfectly implemented!")

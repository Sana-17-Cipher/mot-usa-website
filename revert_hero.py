import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Put back the mobile image wrapper inside the hero section, before </section>
# Remove any existing mobile image block first if it exists
mobile_img_block_pattern = re.compile(r'<!-- Mobile Image Block.*?</div>', re.DOTALL)
content = mobile_img_block_pattern.sub('', content)

# Now, find the closing </section> of the hero section and insert the mobile image wrapper
hero_section_end_pattern = re.compile(r'(<!-- Hero Content -->.*?</section>)', re.DOTALL)
# Actually, it's easier to find </section> after <div class="hero-content">
# Let's do it by finding <section class="hero-section" id="hero"> and its closing tag.
# We'll just replace </section> (the first one)
new_mobile_image_block = '''  <!-- Mobile Image Block (Hidden on desktop) -->
  <div class="hero-mobile-image-wrapper md:hidden">
    <img src="images/hero.png" alt="Indian-American student learning on a tablet" class="hero-mobile-img">
  </div>
</section>'''

# Because I replaced </section> with wave divider stuff in the last script, let's be careful.
# Last script did:
# content = content.replace('<!-- Removed wave divider per user request -->', wave_divider)
# So </section> is intact.
content = content.replace('</section>', new_mobile_image_block, 1)

# 2. Add back the wave divider properly. The user wants the wave divider back!
# Let's ensure there's a proper wave divider after the hero section.
wave_divider = '''<!-- Wave Divider -->
<div class="wave-divider" style="position: relative; margin-top: -60px; z-index: 10; line-height: 0;">
  <svg viewBox="0 0 1440 120" fill="none" preserveAspectRatio="none" style="display: block; width: 100%; height: auto;">
    <path d="M0,60 C320,120 1120,0 1440,60 L1440,120 L0,120 Z" fill="#152447" />
  </svg>
</div>'''

# If it's already there from my last script, leave it. If not, add it.
if '<!-- Wave Divider -->' not in content:
    content = content.replace('<!-- PINNED CARDS SECTION -->', f'{wave_divider}\n\n<!-- PINNED CARDS SECTION -->')

# 3. Rewrite the entire mobile CSS back to the beautiful centered card-like layout
css_replacement = '''@media (max-width:768px) {
    .hero-section { 
      min-height: auto; 
      padding-top: 120px; 
      padding-bottom: 40px; 
      display: flex; 
      flex-direction: column; 
      align-items: center; 
      overflow: visible; 
    }
    .hero-bg-image { display: none !important; }
    .hero-left-fade { display: none !important; }
    
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
    
    .hero-text-block { max-width: 100%; align-items: center; display: flex; flex-direction: column; text-align: center; }
    
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
      display: block !important;
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
    
    .hero-mobile-curve { display: none !important; }
    
    .hero-mobile-image-wrapper {
      position: relative;
      width: 100%;
      padding-left: 24px;
      padding-right: 24px;
      margin-top: 0;
      z-index: 5;
      clip-path: none;
      -webkit-clip-path: none;
      display: block !important;
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
    
    .wave-divider { display: none; } /* Hide wave on mobile to keep it clean */
  }'''

pattern = re.compile(r'@media \(max-width:768px\) \{.*?\}\n  \}', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(css_replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted to the clean mobile layout and restored the wave divider!")

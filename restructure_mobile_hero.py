import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the `<div class="hero-mobile-image-wrapper md:hidden">...</div>` block
mobile_img_block = re.compile(r'<!-- Mobile Image Block.*?</div>', re.DOTALL)
content = mobile_img_block.sub('', content)

# 2. Add back the wave divider below the hero section
wave_divider = '''<!-- Wave Divider -->
<div class="wave-divider" style="position: relative; margin-top: -60px; z-index: 10; line-height: 0;">
  <svg viewBox="0 0 1440 120" fill="none" preserveAspectRatio="none" style="display: block; width: 100%; height: auto;">
    <path d="M0,60 C320,120 1120,0 1440,60 L1440,120 L0,120 Z" fill="#152447" />
  </svg>
</div>'''

# The pinned section has background #152447. So the wave should transition from #faf5ed (transparent) to #152447.
# Actually, the SVG path above is filled with #152447, which creates a wave that perfectly meets the next section!
# Let's insert it between </section> and <!-- PINNED CARDS SECTION -->
content = content.replace('<!-- Removed wave divider per user request -->', wave_divider)


# 3. Rewrite the entire mobile media query for the hero section
old_css_pattern = re.compile(r'@media \(max-width:768px\) \{.*?\.hero-mobile-img \{.*?\}\n  \}', re.DOTALL)

new_mobile_css = '''@media (max-width:768px) {
    .hero-section { 
      min-height: 700px; 
      padding-top: 120px; 
      position: relative;
      overflow: hidden;
      display: block; /* reset from flex */
    }
    
    /* Make the hero image peek in from bottom right */
    .hero-bg-image { 
      display: block !important;
      position: absolute;
      top: auto; /* override desktop top: 0 */
      bottom: 0;
      right: -70px;
      width: 320px;
      height: 440px; 
      object-fit: cover;
      object-position: 70% 30%; /* Crop to face, shoulders, tablet */
      opacity: 1 !important; /* override previous mobile opacity */
      z-index: 2; /* above blob, below wave and text */
    }
    
    .hero-left-fade { display: none; }
    
    .hero-content {
      padding: 0 24px;
      max-width: 280px;
      margin: 0; /* Left align */
      text-align: left;
      display: block;
      z-index: 10;
      position: relative;
    }
    
    .hero-text-block { 
      display: block; 
      text-align: left; 
    }
    
    .hero-text-block h1 { 
      font-size: clamp(2.6rem, 7vw, 4rem);
      line-height: .95; 
      letter-spacing: -1px;
      margin-bottom: 24px; 
      font-weight: 500;
      color: #152447;
    }
    
    .hero-text-block .hero-desc { 
      font-size: 16px; 
      line-height: 1.6; 
      color: #5a6a8a;
      margin-bottom: 36px;
    }
    
    .hero-cta-btn {
      background: #152447;
      color: white;
      padding: 14px 28px;
      border-radius: 50px;
      font-size: 15px;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      width: auto;
      margin: 0;
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
      width: 220px !important; 
      height: 180px !important;
      bottom: 10% !important; 
      right: -20px !important; 
      top: auto !important;
      left: auto !important;
      opacity: 0.8 !important;
      transform: none !important;
      z-index: 1 !important; /* Behind the image */
    }
    
    .pink-blob-2 { display: none; }
    
    /* Adjust wave for mobile if needed */
    .wave-divider { margin-top: -40px; }
  }'''

if old_css_pattern.search(content):
    content = old_css_pattern.sub(new_mobile_css, content)
else:
    print("Could not find mobile media query pattern to replace!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restructured mobile hero section applied!")

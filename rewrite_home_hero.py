import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We will insert the SVG clip-path definition at the very top of body
svg_clip = '''
<svg width="0" height="0" style="position:absolute;">
  <defs>
    <clipPath id="hero-curve-clip" clipPathUnits="objectBoundingBox">
      <path d="M 0,0.3 C 0.4,0.6 0.7,0.0 1,0.1 L 1,1 L 0,1 Z" />
    </clipPath>
  </defs>
</svg>
'''
content = content.replace('<body class="bg-parchment text-navy antialiased">', f'<body class="bg-parchment text-navy antialiased">\n{svg_clip}')

# 2. Modify the CSS for mobile @media (max-width:768px) inside the style tag
# We'll use regex to find the mobile media query and replace the hero section parts.
# Current CSS:
#   @media (max-width:768px) {
#     .hero-section { min-height: 75vh; }
#     .hero-bg-image { width: 100%; opacity: 0.2; }
#     .hero-left-fade { ... }
#     .hero-content { ... }
#     .hero-text-block { ... }
#     .hero-text-block h1 { font-size: 1.7rem; }
#     .hero-text-block .hero-desc { font-size: 14px; max-width: 100%; }
#     .hero-badges { ... }
#     .dot-grid { display: none; }
#   }

css_replacement = '''
  @media (max-width:768px) {
    .hero-section { min-height: auto; padding-top: 100px; padding-bottom: 0; display: flex; flex-direction: column; overflow: visible; }
    .hero-bg-image { display: none; }
    .hero-left-fade { display: none; }
    
    .hero-content {
      padding: 0 24px;
      min-height: auto;
      z-index: 10;
    }
    
    .hero-text-block { max-width: 100%; align-items: flex-start; }
    .hero-text-block h1 { 
      font-size: 2.8rem; 
      line-height: 1.15; 
      margin-bottom: 24px; 
      font-weight: 500;
      color: #152447;
    }
    .hero-text-block .hero-desc { 
      font-size: 16px; 
      line-height: 1.5; 
      color: #5a6a8a;
      max-width: 100%;
      margin-bottom: 32px;
    }
    .hero-cta-btn {
      background: #152447;
      color: white;
      padding: 16px 28px;
      border-radius: 50px;
      font-size: 16px;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 40px;
    }
    
    .hero-badges { display: none; /* Hide badges on mobile per new design */ }
    
    /* Reveal decorative elements on mobile and position them */
    .dot-grid { display: grid !important; }
    .mobile-dot-top-left { top: -20px !important; left: 24px !important; opacity: 0.4 !important; }
    .mobile-dot-bottom-left { bottom: 40px !important; left: 24px !important; opacity: 0.4 !important; }
    
    .pink-blob { 
      width: 300px !important; 
      height: 250px !important;
      top: 60% !important; 
      right: -50px !important; 
      left: auto !important;
      opacity: 0.8 !important;
      transform: translateY(-50%) !important;
      z-index: 1 !important;
    }
    .pink-blob-2 {
      position: absolute;
      width: 120px; height: 120px;
      top: 25%; left: -30px;
      background: #F9C4D2;
      border-radius: 50%;
      opacity: 0.5;
      z-index: 1;
      filter: blur(10px);
    }
    
    .hero-mobile-image-wrapper {
      position: relative;
      width: 100%;
      height: 400px;
      z-index: 5; /* Above pink blob */
      clip-path: url(#hero-curve-clip);
      -webkit-clip-path: url(#hero-curve-clip);
      margin-top: -80px; /* Overlap with content area slightly */
    }
    .hero-mobile-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 20%; /* Adjust to see the girl's face */
    }
'''

# We will inject this directly by replacing the mobile media query.
pattern = re.compile(r'@media \(max-width:768px\) \{[\s\S]*?\.dot-grid \{ display: none; \}\n  \}')
match = pattern.search(content)
if match:
    content = content.replace(match.group(0), css_replacement + '\n  }')

# 3. Add the mobile image block right before the closing </section> of hero
mobile_img_block = '''
  <!-- Mobile Image Block (Hidden on desktop) -->
  <div class="hero-mobile-image-wrapper md:hidden">
    <img src="images/hero.png" alt="Indian-American student learning on a tablet" class="hero-mobile-img">
  </div>
</section>
'''
content = content.replace('</section>', mobile_img_block, 1)

# 4. Modify the pink blob and dot grids to have specific mobile classes so we can target them
content = content.replace('class="dot-grid anim-pulse"', 'class="dot-grid anim-pulse mobile-dot-top-left"')
content = content.replace('class="dot-grid"', 'class="dot-grid mobile-dot-bottom-left"') # This will replace the second one

# Wait, replacing `class="dot-grid"` will also replace the first one if we're not careful.
# Let's do it directly:
content = content.replace(
    '<div class="dot-grid anim-pulse" style="top:28%;left:36%;animation-delay:.8s;">',
    '<div class="dot-grid anim-pulse mobile-dot-top-left" style="top:28%;left:36%;animation-delay:.8s;">'
)
content = content.replace(
    '<div class="dot-grid" style="bottom:28%;right:32%;opacity:.25;">',
    '<div class="dot-grid mobile-dot-bottom-left" style="bottom:28%;right:32%;opacity:.25;">'
)

# Also add the second pink blob for mobile (top left in screenshot)
pink_blob_2 = '<div class="pink-blob-2 md:hidden"></div>'
content = content.replace('<div class="hero-left-fade"></div>', f'<div class="hero-left-fade"></div>\n  {pink_blob_2}')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Rewrote index.html hero section for mobile.")

import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace everything between the mobile menu closing and the footer opening.
# Looking at the file, the mobile menu ends with:
#     <div class="mt-auto pt-6 w-full">
#       <a href="tel:+1XXXXXXXXXX" class="bg-[#E8A63C] text-center text-navy font-semibold px-5 py-4 rounded-full text-base block w-full hover:bg-[#C9862A] transition">Book Free Demo</a>
#     </div>
#   </div>
# 
# And then the old content starts with <section class="max-w-4xl mx-auto px-6 pt-8 pb-16">
# And the footer starts with <footer ...>

new_sections = '''
<!-- Hero Section -->
<section class="bg-parchment pt-12 pb-24 px-6 mt-6 relative overflow-hidden">
  <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-marigold/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
  <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-16 relative z-10">
    <div class="lg:w-1/2 flex flex-col items-start text-left">
      <div class="inline-flex items-center gap-2 bg-marigold/20 text-marigold-dark px-4 py-2 rounded-full text-xs font-bold tracking-wider mb-6">
        ABOUT MOMS ON TEACHING USA
      </div>
      <h1 class="font-display text-5xl md:text-6xl text-navy leading-[1.1] mb-6">
        Where Education Meets <span class="text-marigold-dark font-serif italic font-light">Motherly Care</span>
      </h1>
      <p class="text-lg md:text-xl text-navy/70 leading-relaxed mb-8">
        Moms on Teaching USA is a personalized one-on-one online tutoring platform connecting Indian-American families with experienced, verified Teacher-Moms who nurture confidence, curiosity, and academic success.
      </p>
    </div>
    <div class="lg:w-1/2 w-full">
      <div class="relative rounded-[2.5rem] overflow-hidden shadow-2xl border-[12px] border-white/50 backdrop-blur-sm">
        <img src="/images/hero.png" alt="Moms on Teaching Hero" class="w-full h-[500px] object-cover">
      </div>
    </div>
  </div>
</section>

<!-- Our Story -->
<section class="py-24 px-6 bg-white">
  <div class="max-w-7xl mx-auto flex flex-col lg:flex-row-reverse items-center gap-16">
    <div class="lg:w-1/2">
      <h2 class="font-display text-4xl md:text-5xl text-navy mb-6 leading-tight">A Global Community Built Around Every Child</h2>
      <div class="w-16 h-1.5 bg-marigold mb-8 rounded-full"></div>
      <p class="text-lg text-navy/70 leading-relaxed mb-6">
        Moms on Teaching began with a simple belief: every child deserves personalized guidance from educators who combine professional expertise with genuine care.
      </p>
      <p class="text-lg text-navy/70 leading-relaxed">
        What started as a successful tutoring initiative serving families across the Gulf has now expanded to the United States, supporting Indian-American families who seek the best of both educational worlds. Whether your child is following CBSE, ICSE, IGCSE, IB, or a US curriculum, we provide learning that adapts to their unique goals.
      </p>
    </div>
    <div class="lg:w-1/2 w-full">
      <div class="relative rounded-[2rem] overflow-hidden shadow-xl">
        <img src="/images/deepthi.jpeg" alt="Our Story" class="w-full h-[500px] object-cover object-top">
        <!-- Floating badge -->
        <div class="absolute bottom-8 -left-2 bg-marigold text-navy p-6 rounded-2xl shadow-xl hidden md:block border-4 border-white max-w-[280px]">
          <p class="font-bold text-2xl mb-1">Expanded to USA</p>
          <p class="text-sm font-medium">Supporting Indian-American families coast to coast</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Mission, Vision, Impact -->
<section class="py-24 px-6 bg-parchment relative overflow-hidden">
  <div class="max-w-7xl mx-auto relative z-10">
    <div class="grid lg:grid-cols-3 gap-8 items-stretch">
      <!-- Mission -->
      <div class="bg-white rounded-[2rem] p-10 shadow-lg border-b-4 border-marigold hover:-translate-y-2 transition-transform duration-300">
        <div class="w-14 h-14 bg-marigold/20 rounded-2xl flex items-center justify-center mb-6 text-marigold-dark">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        </div>
        <h3 class="font-display text-3xl text-navy mb-4">Our Mission</h3>
        <p class="text-navy/70 leading-relaxed text-lg">
          To provide every child with personalized one-on-one learning while creating meaningful work-from-home opportunities for qualified Teacher-Moms around the world.
        </p>
      </div>

      <!-- Vision -->
      <div class="bg-white rounded-[2rem] p-10 shadow-lg border-b-4 border-navy hover:-translate-y-2 transition-transform duration-300">
        <div class="w-14 h-14 bg-navy/10 rounded-2xl flex items-center justify-center mb-6 text-navy">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
        </div>
        <h3 class="font-display text-3xl text-navy mb-4">Our Vision</h3>
        <p class="text-navy/70 leading-relaxed text-lg">
          To build a global learning community where children thrive academically and educators empower families through compassionate, personalized teaching.
        </p>
      </div>

      <!-- Impact -->
      <div class="bg-navy-dark text-white rounded-[2rem] p-10 shadow-lg hover:-translate-y-2 transition-transform duration-300 flex flex-col justify-center relative overflow-hidden">
        <div class="absolute top-0 right-0 -mr-8 -mt-8 w-40 h-40 bg-white/5 rounded-full blur-2xl"></div>
        <h3 class="font-display text-3xl mb-8">Our Impact</h3>
        
        <div class="space-y-6">
          <div class="flex items-center gap-5">
             <div class="text-4xl font-display text-marigold font-bold w-20 counter" data-target="5000">0</div>
             <div class="text-sm text-parchment/80 font-medium leading-tight">tutoring hours delivered</div>
          </div>
          <div class="flex items-center gap-5">
             <div class="text-4xl font-display text-marigold font-bold w-20 counter" data-target="95">0</div>
             <div class="text-sm text-parchment/80 font-medium leading-tight">% students showed measurable improvement</div>
          </div>
          <div class="flex items-center gap-5">
             <div class="text-4xl font-display text-marigold font-bold w-20 counter" data-target="30">0</div>
             <div class="text-sm text-parchment/80 font-medium leading-tight">qualified Teacher-Moms</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Why Teacher-Moms -->
<section class="py-24 px-6 bg-white">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="font-display text-4xl md:text-5xl text-navy">Why Parents Choose Teacher-Moms</h2>
      <div class="w-20 h-1.5 bg-marigold mx-auto mt-6 rounded-full"></div>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
      <div class="group p-10 rounded-[2rem] border-2 border-parchment hover:border-marigold/50 hover:shadow-2xl hover:shadow-marigold/10 transition-all duration-300">
        <div class="w-16 h-16 bg-[#FBF6EC] rounded-2xl flex items-center justify-center mb-6 group-hover:bg-marigold/20 transition-colors">
          <svg class="w-8 h-8 text-marigold-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <h3 class="text-2xl font-bold text-navy mb-4">Patience That Builds Confidence</h3>
        <p class="text-navy/70 leading-relaxed text-lg">
          Teacher-Moms understand that every child learns at their own pace. They guide with encouragement, empathy, and consistency.
        </p>
      </div>

      <div class="group p-10 rounded-[2rem] border-2 border-parchment hover:border-marigold/50 hover:shadow-2xl hover:shadow-marigold/10 transition-all duration-300">
        <div class="w-16 h-16 bg-[#FBF6EC] rounded-2xl flex items-center justify-center mb-6 group-hover:bg-marigold/20 transition-colors">
          <svg class="w-8 h-8 text-marigold-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <h3 class="text-2xl font-bold text-navy mb-4">Experience Across Curricula</h3>
        <p class="text-navy/70 leading-relaxed text-lg">
          Many of our educators have experience teaching both Indian and international curricula, making transitions between education systems seamless.
        </p>
      </div>

      <div class="group p-10 rounded-[2rem] border-2 border-parchment hover:border-marigold/50 hover:shadow-2xl hover:shadow-marigold/10 transition-all duration-300">
        <div class="w-16 h-16 bg-[#FBF6EC] rounded-2xl flex items-center justify-center mb-6 group-hover:bg-marigold/20 transition-colors">
          <svg class="w-8 h-8 text-marigold-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        </div>
        <h3 class="text-2xl font-bold text-navy mb-4">Safe & Trusted</h3>
        <p class="text-navy/70 leading-relaxed text-lg">
          Every Teacher-Mom undergoes identity verification, background checks, and academic screening before joining our platform.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Our Vetting Process -->
<section class="py-24 px-6 bg-parchment">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="font-display text-4xl md:text-5xl text-navy">Our Vetting Process</h2>
      <p class="text-navy/60 mt-4 text-xl">We maintain the highest standards when bringing educators onto our platform.</p>
    </div>

    <div class="relative border-l-2 border-navy/10 pl-8 md:pl-12 ml-4 md:mx-auto max-w-2xl space-y-14 py-4">
      <!-- Step 1 -->
      <div class="relative">
        <div class="absolute -left-[41px] md:-left-[57px] bg-marigold w-6 h-6 md:w-8 md:h-8 rounded-full border-4 border-parchment shadow-md flex items-center justify-center"></div>
        <p class="text-marigold-dark font-bold text-sm tracking-widest uppercase mb-2">Step 1</p>
        <h4 class="font-bold text-2xl text-navy mb-3">Teaching Experience</h4>
        <p class="text-navy/70 leading-relaxed text-lg">Minimum three years of verified teaching or tutoring experience.</p>
      </div>

      <!-- Step 2 -->
      <div class="relative">
        <div class="absolute -left-[41px] md:-left-[57px] bg-navy w-6 h-6 md:w-8 md:h-8 rounded-full border-4 border-parchment shadow-md flex items-center justify-center"></div>
        <p class="text-marigold-dark font-bold text-sm tracking-widest uppercase mb-2">Step 2</p>
        <h4 class="font-bold text-2xl text-navy mb-3">Subject Assessment</h4>
        <p class="text-navy/70 leading-relaxed text-lg">Academic interview based on curriculum and specialization.</p>
      </div>

      <!-- Step 3 -->
      <div class="relative">
        <div class="absolute -left-[41px] md:-left-[57px] bg-marigold w-6 h-6 md:w-8 md:h-8 rounded-full border-4 border-parchment shadow-md flex items-center justify-center"></div>
        <p class="text-marigold-dark font-bold text-sm tracking-widest uppercase mb-2">Step 3</p>
        <h4 class="font-bold text-2xl text-navy mb-3">Background Verification</h4>
        <p class="text-navy/70 leading-relaxed text-lg">Identity verification and safety screening.</p>
      </div>

      <!-- Step 4 -->
      <div class="relative">
        <div class="absolute -left-[41px] md:-left-[57px] bg-navy w-6 h-6 md:w-8 md:h-8 rounded-full border-4 border-parchment shadow-md flex items-center justify-center"></div>
        <p class="text-marigold-dark font-bold text-sm tracking-widest uppercase mb-2">Step 4</p>
        <h4 class="font-bold text-2xl text-navy mb-3">Teaching Evaluation</h4>
        <p class="text-navy/70 leading-relaxed text-lg">Trial class reviewed by our academic team.</p>
      </div>

      <!-- Step 5 -->
      <div class="relative">
        <div class="absolute -left-[41px] md:-left-[57px] bg-marigold w-6 h-6 md:w-8 md:h-8 rounded-full border-4 border-parchment shadow-md flex items-center justify-center"></div>
        <p class="text-marigold-dark font-bold text-sm tracking-widest uppercase mb-2">Step 5</p>
        <h4 class="font-bold text-2xl text-navy mb-3">Continuous Quality Monitoring</h4>
        <p class="text-navy/70 leading-relaxed text-lg">Regular parent feedback and ongoing performance reviews.</p>
      </div>
    </div>
  </div>
</section>

<!-- Our Values -->
<section class="py-24 px-6 bg-white">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="font-display text-4xl md:text-5xl text-navy">Our Values</h2>
      <div class="w-20 h-1.5 bg-marigold mx-auto mt-6 rounded-full"></div>
    </div>
    
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-[#FBF6EC] p-8 rounded-3xl text-center shadow-sm">
        <div class="w-14 h-14 bg-white rounded-2xl shadow-sm flex items-center justify-center mx-auto mb-6 text-navy">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
        </div>
        <h4 class="font-bold text-navy text-xl mb-3">Personalized Learning</h4>
        <p class="text-base text-navy/70">Every lesson is tailored to each child's pace and goals.</p>
      </div>
      
      <div class="bg-[#FBF6EC] p-8 rounded-3xl text-center shadow-sm">
        <div class="w-14 h-14 bg-white rounded-2xl shadow-sm flex items-center justify-center mx-auto mb-6 text-navy">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        </div>
        <h4 class="font-bold text-navy text-xl mb-3">Trust</h4>
        <p class="text-base text-navy/70">Verified educators and transparent communication.</p>
      </div>
      
      <div class="bg-[#FBF6EC] p-8 rounded-3xl text-center shadow-sm">
        <div class="w-14 h-14 bg-white rounded-2xl shadow-sm flex items-center justify-center mx-auto mb-6 text-navy">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
        </div>
        <h4 class="font-bold text-navy text-xl mb-3">Compassion</h4>
        <p class="text-base text-navy/70">Learning built around encouragement and confidence.</p>
      </div>
      
      <div class="bg-[#FBF6EC] p-8 rounded-3xl text-center shadow-sm">
        <div class="w-14 h-14 bg-white rounded-2xl shadow-sm flex items-center justify-center mx-auto mb-6 text-navy">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
        </div>
        <h4 class="font-bold text-navy text-xl mb-3">Excellence</h4>
        <p class="text-base text-navy/70">Strong academic outcomes through structured one-on-one teaching.</p>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="max-w-5xl mx-auto px-6 pb-24 pt-10">
  <div class="bg-parchment rounded-[3rem] p-12 md:p-16 text-center shadow-xl border border-white/50 relative overflow-hidden">
    <div class="absolute top-0 right-0 w-64 h-64 bg-marigold/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
    <div class="relative z-10">
      <h2 class="font-display text-4xl md:text-5xl text-navy mb-6">Ready to Meet Your Child's Teacher-Mom?</h2>
      <p class="text-navy/70 text-lg md:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
        Let us help you find the right educator, learning plan, and schedule tailored to your child's academic journey.
      </p>
      <a href="tel:+1XXXXXXXXXX" class="inline-flex items-center justify-center bg-marigold hover:bg-marigold-dark text-navy font-bold text-lg px-10 py-5 rounded-full transition-transform hover:-translate-y-1 shadow-xl">
        Meet Our Teacher-Moms
      </a>
    </div>
  </div>
</section>
'''

# The JS for counters needs to be added just before </body>
js_counters = '''
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.counter');
    const speed = 100; 

    const animateCounters = () => {
      counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText.replace(/,/g, '');
        const inc = target / speed;

        if (count < target) {
          counter.innerText = Math.ceil(count + inc);
          setTimeout(animateCounters, 20);
        } else {
          // Format with + if it's not the percentage
          counter.innerText = target;
        }
      });
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounters();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
  });
</script>
'''

# Splitting logic
pattern = re.compile(r'(</div>\s*</div>\s*<section.*?>)(.*)(<footer)', re.DOTALL)
match = pattern.search(content)

if match:
    # First portion: everything up to the end of the mobile menu block
    # Actually wait. `</div>\s*</div>\s*<section.*?>` isn't foolproof because I added another section.
    # Let's use a simpler split: find the end of mobile menu overlay.
    # The mobile menu ends with `<!-- Mobile Menu Fullscreen Overlay -->... </div>`
    pass

# Better approach to find bounds:
# Top bound: find <!-- Mobile Menu Fullscreen Overlay --> block's end.
# Since mobile menu ends right before the first <section>
top_split = content.split('<section', 1)
top_half = top_split[0]

# Bottom bound: find <footer
bottom_split = top_split[1].rsplit('<footer', 1)
bottom_half = '<footer' + bottom_split[1]

# Now assemble
new_content = top_half + new_sections + '\\n' + bottom_half

# Add JS counters before </body>
new_content = new_content.replace('</body>', js_counters + '\\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated about.html!")

import re

file_path = 'c:/Ammu/SideQuest/usa-momsonteaching-main/about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_story = '''<!-- Our Story -->
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
</section>'''

new_story = '''<!-- Our Story -->
<section class="py-24 px-6 bg-white">
  <div class="max-w-4xl mx-auto text-center">
    <h2 class="font-display text-4xl md:text-5xl text-navy mb-6 leading-tight">A Global Community Built Around Every Child</h2>
    <div class="w-20 h-1.5 bg-marigold mb-8 rounded-full mx-auto"></div>
    <p class="text-lg text-navy/70 leading-relaxed mb-6">
      Moms on Teaching began with a simple belief: every child deserves personalized guidance from educators who combine professional expertise with genuine care.
    </p>
    <p class="text-lg text-navy/70 leading-relaxed">
      What started as a successful tutoring initiative serving families across the Gulf has now expanded to the United States, supporting Indian-American families who seek the best of both educational worlds. Whether your child is following CBSE, ICSE, IGCSE, IB, or a US curriculum, we provide learning that adapts to their unique goals.
    </p>
  </div>
</section>'''

# Using regex just in case formatting shifted slightly
pattern = re.compile(r'<!-- Our Story -->.*?</section>', re.DOTALL)
new_content = pattern.sub(new_story, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed image section!")

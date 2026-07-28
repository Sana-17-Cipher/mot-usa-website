import glob

files = glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/*.html') + glob.glob('c:/Ammu/SideQuest/usa-momsonteaching-main/locations/*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the main grid container to be more responsive (sm:grid-cols-2 lg:grid-cols-5)
    content = content.replace(
        '<div class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10">',
        '<div class="max-w-7xl mx-auto px-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-8 md:gap-10">'
    )

    # 2. Make the Logo column span full width on small/tablet screens
    content = content.replace(
        '<!-- Left Column: Logo & Description & Social -->\n    <div class="lg:col-span-1 flex flex-col">',
        '<!-- Left Column: Logo & Description & Social -->\n    <div class="sm:col-span-2 lg:col-span-1 flex flex-col mb-4 lg:mb-0">'
    )
    # in case of slightly different formatting:
    content = content.replace(
        '<div class="lg:col-span-1 flex flex-col">',
        '<div class="sm:col-span-2 lg:col-span-1 flex flex-col mb-4 lg:mb-0">'
    )

    # 3. Allow the bottom bar links to wrap so they don't overflow on very small devices
    content = content.replace(
        '<div class="flex items-center gap-6">',
        '<div class="flex items-center gap-4 sm:gap-6 flex-wrap justify-center">'
    )
    
    # 4. Center the copyright text on mobile just in case
    content = content.replace(
        '<div>\n      © 2026 Moms on Teaching. All rights reserved.\n    </div>',
        '<div class="text-center md:text-left">\n      © 2026 Moms on Teaching. All rights reserved.\n    </div>'
    )
    # Catching weird character encodings
    content = content.replace(
        '<div>\n       2026 Moms on Teaching. All rights reserved.\n    </div>',
        '<div class="text-center md:text-left">\n      © 2026 Moms on Teaching. All rights reserved.\n    </div>'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Made responsive updates to {file}")

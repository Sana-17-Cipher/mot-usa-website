const fs = require('fs');
const path = require('path');

function fixFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    const original = content;

    // We can detect if it's double-mojibaked by looking for typical sequences
    // like ÃƒÂ¢ which is 'â' (C3 A2) double encoded.
    // Actually, we can just repeatedly decode as long as we find 'Ã' (C3 83) or 'â' (E2 80 94 etc)
    // but it's safer to just decode based on a few known corrupted strings to avoid false positives.

    let fixed = content;
    
    // Triple mojibake of em-dash:
    fixed = fixed.replace(/ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â/g, '—');
    fixed = fixed.replace(/ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬â€œ/g, '–');
    
    // Double mojibake
    fixed = fixed.replace(/Ã¢â‚¬â€/g, '—');
    fixed = fixed.replace(/Ã¢â‚¬â€œ/g, '–');
    fixed = fixed.replace(/Ã¢â€šÂ¹/g, '₹');
    fixed = fixed.replace(/Ã‚Â·/g, '·');
    
    // Single mojibake
    fixed = fixed.replace(/â€”/g, '—');
    fixed = fixed.replace(/â€“/g, '–');
    fixed = fixed.replace(/â‚¹/g, '₹');
    fixed = fixed.replace(/Â·/g, '·');
    fixed = fixed.replace(/â‰ˆ/g, '≈');
    fixed = fixed.replace(/âœ“/g, '✓');
    fixed = fixed.replace(/â€’/g, '‒');
    fixed = fixed.replace(/â€˜/g, '‘');
    fixed = fixed.replace(/â€™/g, '’');
    fixed = fixed.replace(/â€œ/g, '“');
    fixed = fixed.replace(/â€/g, '”');
    fixed = fixed.replace(/â€¦/g, '…');
    // Also "KG?" where the question mark is actually a broken char. In services.html: "KG?"Plus Two"
    fixed = fixed.replace(/KG(\?|\?|"|â€")Plus Two/g, 'KG—Plus Two');
    fixed = fixed.replace(/KG(ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â)Plus Two/g, 'KG—Plus Two');
    fixed = fixed.replace(/KGÃ¢â‚¬â€Plus Two/g, 'KG—Plus Two');
    fixed = fixed.replace(/KGâ€”Plus Two/g, 'KG—Plus Two');
    
    // The screenshot also shows "ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â" in "Our Tutoring Programmes"
    // "syllabus ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â covering all"
    // So the replace above should catch it.

    // Another weird one from screenshot: "Classes 1 â€“ 5 Â· per hour"
    // We already have â€“ and Â· covered.

    if (fixed !== original) {
        fs.writeFileSync(filePath, fixed, 'utf8');
        console.log("Fixed: " + filePath);
    }
}

function walk(dir) {
    fs.readdirSync(dir).forEach(f => {
        if (f === 'usa-momsonteaching-main') return;
        const p = path.join(dir, f);
        if (fs.statSync(p).isDirectory()) walk(p);
        else if (p.endsWith('.html')) fixFile(p);
    });
}

walk(__dirname);

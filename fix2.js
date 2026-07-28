const fs = require('fs');
const path = require('path');

function fixFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    const original = content;

    // Fix the specific mojibake strings from services.html and locations
    content = content.replace(/ÃƒÂ¢Ã¢”šÂ¬“/g, '—');
    content = content.replace(/ÃƒÂ¢Ã¢”šÂ¬”\x9DÂ\x9D/g, '—');
    content = content.replace(/ÃƒÆ’”\x9DÅ¡Ãƒ”šÃ‚Â©/g, '©');
    content = content.replace(/Ãƒ”š·/g, '·');
    content = content.replace(/ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â/g, '—');
    content = content.replace(/ÃƒÂ¢Ã¢â€šÂ¬â€œ/g, '–');
    content = content.replace(/Ã¢â€šÂ¹/g, '₹');
    
    // Generic regex for blocks of non-ascii surrounded by specific text
    content = content.replace(/KG[^\x00-\x7F]+Plus Two/g, 'KG—Plus Two');
    content = content.replace(/syllabus [^\x00-\x7F]+ covering/g, 'syllabus — covering');
    content = content.replace(/DP [^\x00-\x7F]+ helping/g, 'DP — helping');

    content = content.replace(/10 [^\x00-\x7F]+ per hour/g, '10 · per hour');
    content = content.replace(/12 [^\x00-\x7F]+ per hour/g, '12 · per hour');
    content = content.replace(/5 [^\x00-\x7F]+ per hour/g, '5 · per hour');
    content = content.replace(/7 [^\x00-\x7F]+ per hour/g, '7 · per hour');

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('Fixed:', filePath);
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
walk('.');

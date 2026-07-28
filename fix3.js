const fs = require('fs');
const path = require('path');

function fixFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    const original = content;

    // We will aggressively replace between known boundaries.
    
    // KG...Plus Two
    content = content.replace(/KG.{1,15}Plus Two/g, (match) => {
        // If it's literally "KG through Plus Two", keep it or change it to KG—Plus Two
        return 'KG—Plus Two';
    });

    // syllabus...covering
    content = content.replace(/syllabus.{1,20}covering/g, 'syllabus — covering');

    // DP...helping
    content = content.replace(/DP.{1,20}helping/g, 'DP — helping');

    // All delivered 1-on-1 (in services.html)
    // "Plus Two A A A"sA"?A? all delivered"
    content = content.replace(/Plus Two.{1,30}all delivered/g, 'Plus Two — all delivered');

    // "Moms on Teaching A A A"sA"?A? CBSE" in meta description
    content = content.replace(/Moms on Teaching.{1,20}CBSE/g, 'Moms on Teaching — CBSE');

    // Any remaining A A A things
    content = content.replace(/ÃƒÂ¢Ã¢”šÂ¬“/g, '—');
    content = content.replace(/ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â/g, '—');

    // Middle dots
    content = content.replace(/10.{1,10}per hour/g, '10 · per hour');
    content = content.replace(/12.{1,10}per hour/g, '12 · per hour');
    content = content.replace(/5.{1,10}per hour/g, '5 · per hour');
    content = content.replace(/7.{1,10}per hour/g, '7 · per hour');
    
    // Classes 1...5
    content = content.replace(/Classes 1.{1,15}5/g, 'Classes 1 – 5');
    content = content.replace(/Classes 6.{1,15}7/g, 'Classes 6 – 7');
    content = content.replace(/Classes 8.{1,15}10/g, 'Classes 8 – 10');
    content = content.replace(/Classes 11.{1,15}12/g, 'Classes 11 – 12');

    // Rupees
    content = content.replace(/â‚¹/g, '₹');
    content = content.replace(/Ã¢â€šÂ¹/g, '₹');
    // If it has weird bytes before numbers
    content = content.replace(/[^\x00-\x7F]+200/g, '₹200');
    content = content.replace(/[^\x00-\x7F]+250/g, '₹250');
    content = content.replace(/[^\x00-\x7F]+300/g, '₹300');
    content = content.replace(/[^\x00-\x7F]+350/g, '₹350');
    content = content.replace(/[^\x00-\x7F]+400/g, '₹400');
    content = content.replace(/[^\x00-\x7F]+450/g, '₹450');
    content = content.replace(/[^\x00-\x7F]+500/g, '₹500');

    // Copyright
    content = content.replace(/[^\x00-\x7F]+ 2026 Moms/g, '© 2026 Moms');
    
    // Privacy policy dots
    content = content.replace(/[^\x00-\x7F]+ <a href="\/legal\/privacy/g, '· <a href="/legal/privacy');
    content = content.replace(/[^\x00-\x7F]+ <a href="\/sitemap/g, '· <a href="/sitemap');

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

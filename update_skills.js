const fs = require('fs');

let htmlContent = fs.readFileSync('index.html', 'utf-8');

// The outer container can just be `<div class="skill-tab-container">...</div>`
htmlContent = htmlContent.replace(/<div class="skill-list-container">/g, '<div class="skill-tab-container">');

const resultHtml = htmlContent.replace(
    /<div class="skill-item">[\s\S]*?<span class="skill-name">(.*?)<\/span>[\s\S]*?<\/div>\s*<\/div>/gi,
    (match, innerName) => {
        // innerName is like `<i class="fas fa-network-wired"></i> Network Security`
        return `<div class="skill-tab-item">${innerName}</div>`;
    }
);

if (resultHtml !== htmlContent) {
    fs.writeFileSync('index.html', resultHtml);
    console.log("Skills section updated to tabs successfully.");
} else {
    console.log("No changes made to skills section.");
}

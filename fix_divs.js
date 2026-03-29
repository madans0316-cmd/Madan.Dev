const fs = require('fs');
let txt = fs.readFileSync('index.html', 'utf-8');
const newTxt = txt.replace(/(<div class="skill-tab-item">.*?<\/div>)\s*<\/div>/g, '$1');
if(newTxt !== txt) {
    fs.writeFileSync('index.html', newTxt);
    console.log('Fixed extra divs!');
} else {
    console.log('No extra divs found.');
}

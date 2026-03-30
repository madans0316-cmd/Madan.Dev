const fs = require('fs');

const htmlContent = fs.readFileSync('index.html', 'utf-8');

// Regex to match a project card:
// <a href="(.*?)" target="_blank" rel="noopener" class="project-card.*?">
//   <div class="project-icon">.*?</div>
//   <div class="project-title">(.*?)</div>
//   ...
//   <div class="project-meta project-meta-styled">
//      ...
//      <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
//   </div>
// </a>

const resultHtml = htmlContent.replace(
    /<a href="([^"]+)" target="_blank" rel="noopener"\s*[\n\s]*class="project-card\s*project-card-clickable\s*project-card-link">([\s\S]*?)<div class="project-meta project-meta-styled">([\s\S]*?)<\/div>\s*<\/a>/gi,
    (match, githubUrl, cardInnerContent, metaInnerContent) => {
        // Find if there is a live link (some projects have them, some don't. By default we just use github pages or empty)
        let liveUrl = "";
        
        // Let's hardcode live URLs based on the repo name for the major ones in the user's Github
        const repoNameMatch = githubUrl.match(/github\.com\/madans0316-cmd\/([^/]+)/);
        const repoName = repoNameMatch ? repoNameMatch[1] : "";

        if (repoName === "India-Atlas-") {
            liveUrl = "https://india-atlas-eta.vercel.app";
        } else if (repoName === "student-to-do-list") {
            liveUrl = "https://madans0316-cmd.github.io/student-to-do-list/";
        } else if (repoName === "pulwama-memorial") {
            liveUrl = "https://madans0316-cmd.github.io/pulwama-memorial/";
        } else if (repoName === "SK.TYLERING") {
            liveUrl = "https://madans0316-cmd.github.io/SK.TYLERING/";
        } else if (repoName === "decode-every-expression") {
            liveUrl = "https://madans0316-cmd.github.io/decode-every-expression/";
        } else if (repoName === "Madan-kumar-S-portfolio") {
            liveUrl = "https://madans0316.github.io"; 
        } else {
            liveUrl = `https://madans0316-cmd.github.io/${repoName}/`; // Fallback github pages layout
        }

        // We replace the <a> tag with a div
        // We replace the inner .project-meta block with our custom links.
        return `<div class="project-card">
${cardInnerContent}<div class="project-actions">
                        <a href="${githubUrl}" target="_blank" rel="noopener" class="btn-action-icon" title="View Source on GitHub">
                            <i class="fab fa-github"></i>
                        </a>
                        <a href="${liveUrl}" target="_blank" rel="noopener" class="btn-action-live">
                            <i class="fas fa-external-link-alt"></i> Live Access to Website
                        </a>
                    </div>
                </div>`;
    }
);

if (resultHtml !== htmlContent) {
    fs.writeFileSync('index.html', resultHtml);
    console.log("Projects section updated successfully.");
} else {
    console.log("No changes made. Regex might not match.");
}

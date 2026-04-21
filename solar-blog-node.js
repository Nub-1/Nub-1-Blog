#!/usr/bin/env node
/**
 * Solar Blog Generator - Node.js version
 * Publishes solar articles to WordPress
 */

const fs = require('fs');
const path = require('path');
const { execSync, exec } = require('child_process');
const https = require('https');

// ========== CONFIG ==========
const BLOG_URL = 'https://blog.joe-data.uk';
const WP_USER = 'Mew';
const WP_APP_PASSWORD = 'CPkk 1ouF xZS4 KpaH nCVO Ay5R';
const WP_CATEGORY_ID = '24';

const GITHUB_REPO = '/root/.openclaw/workspace/Nub-1-Blog';
const IMAGES_DIR = path.join(GITHUB_REPO, 'images');
const ARTICLES_DIR = path.join(GITHUB_REPO, 'solar-articles');
const STATE_FILE = path.join(GITHUB_REPO, 'published-state.json');

// ========== ARTICLES ==========
const ARTICLES = {
    1: {
        title: 'ทำไมต้องสนใจโซลาร์ตอนนี้?',
        slug: 'why-solar-now-2026',
        prompt_image: 'Solar panels on rooftop with sun rays, modern house, Thailand scenery, 4:3 horizontal',
        content_path: '01-why-solar-now-2026.md'
    },
    2: {
        title: 'ต้องรู้อะไรก่อนติดโซลาร์?',
        slug: 'before-installing-solar',
        prompt_image: 'Checklist and notepad with solar panel background, Thailand house, 4:3',
        content_path: '02-before-installing-solar.md'
    },
    3: {
        title: 'โซลาร์ทำงานยังไง?',
        slug: 'how-solar-works-2026',
        prompt_image: 'Solar panel cross-section diagram showing photovoltaic cells, sunlight rays, electron flow, educational illustration, Thailand',
        content_path: '03-how-solar-works-2026.md'
    },
    4: {
        title: 'On-Grid vs Off-Grid vs Hybrid เลือกอันไหนดี?',
        slug: 'solar-on-grid-off-grid-hybrid-explained',
        prompt_image: 'Three solar system diagrams showing grid connection, battery storage, and hybrid setup, Thailand house, infographic style',
        content_path: '04-on-grid-off-grid-hybrid-2026.md'
    },
    5: {
        title: 'วิธีคำนวณขนาดระบบโซลาร์ที่เหมาะกับบ้านคุณ',
        slug: 'solar-system-size-calculation-guide',
        prompt_image: 'Solar calculator with house roof diagram, showing kWp calculation, Thailand home setting, practical illustration',
        content_path: '05-how-to-calculate-solar-size-2026.md'
    },
    6: {
        title: 'วิธีดูแลรักษาโซลาร์ให้อยู่ 25-30 ปี',
        slug: 'how-to-maintain-solar-2026',
        prompt_image: 'Solar panel maintenance checklist, cleaning solar panels on rooftop, Thailand house, 4:3 horizontal',
        content_path: '06-how-to-maintain-solar-2026.md'
    },
};

// ========== HELPERS ==========
function loadContent(contentPath) {
    const fullPath = path.join(ARTICLES_DIR, contentPath);
    try {
        return fs.readFileSync(fullPath, 'utf8');
    } catch (e) {
        console.error('❌ Cannot read file:', fullPath, e);
        return null;
    }
}

function generateImage(episode, title, outputPath) {
    console.log(`🎨 กำลังสร้างรูปปกสำหรับตอนที่ ${episode}...`);
    
    const episodeText = `ตอนที่ ${episode}`;
    
    // Escape quotes in title
    const safeTitle = title.replace(/'/g, "'\"'\"'");
    
    const cmd = `convert -size 1200x900 xc:#1a365d -fill white -gravity center -font Garuda -pointsize 72 -annotate +0-150 '${episodeText}' -font Garuda -pointsize 48 -annotate +0+50 '${safeTitle}' -font Garuda -pointsize 24 -annotate +0+200 'Nub-1 Channel | โซล่าเซลล์' -quality 90 ${outputPath}`;
    
    try {
        execSync(cmd, { stdio: 'pipe' });
        console.log(`✅ รูปภาพบันทึกที่: ${outputPath}`);
        return true;
    } catch (e) {
        console.error('❌ สร้างรูปไม่สำเร็จ:', e.message);
        return false;
    }
}

function mdToHtml(text) {
    // Simple markdown to HTML conversion
    let html = text;
    
    // Headers
    html = html.replace(/^#### (.+)$/gm, '<h4>$1</h4>');
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h4><strong>$1</strong></h4>');
    html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');
    
    // Bold
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    
    // Horizontal rule
    html = html.replace(/^---$/gm, '<hr>');
    
    // Lists
    const lines = html.split('\n');
    let inList = false;
    let result = [];
    for (const line of lines) {
        const listMatch = line.match(/^[-*] (.+)$/);
        if (listMatch) {
            if (!inList) {
                result.push('<ul>');
                inList = true;
            }
            result.push('<li>' + listMatch[1] + '</li>');
        } else {
            if (inList) {
                result.push('</ul>');
                inList = false;
            }
            result.push(line);
        }
    }
    if (inList) result.push('</ul>');
    html = result.join('\n');
    
    // Paragraphs
    const paragraphs = [];
    let currentPara = [];
    const specialTags = ['<h', '<ul', '<li', '<pre', '<hr', '<code', '<strong'];
    
    for (const line of html.split('\n')) {
        const stripped = line.trim();
        const isSpecial = specialTags.some(tag => stripped.startsWith(tag));
        
        if (stripped === '' || isSpecial) {
            if (currentPara.length > 0) {
                paragraphs.push('<p>' + currentPara.join('<br>\n') + '</p>');
                currentPara = [];
            }
            if (isSpecial) paragraphs.push(stripped);
        } else {
            currentPara.push(stripped);
        }
    }
    if (currentPara.length > 0) {
        paragraphs.push('<p>' + currentPara.join('<br>\n') + '</p>');
    }
    
    html = paragraphs.join('\n');
    html = html.replace(/<p><\/p>/g, '');
    
    return html;
}

function uploadWordpress(episode, title, content, imagePath, slug) {
    return new Promise((resolve, reject) => {
        const htmlContent = mdToHtml(content);
        const boundary = '----WordPressBoundary' + Date.now();
        
        // Read image as base64
        let imageData;
        try {
            imageData = fs.readFileSync(imagePath);
        } catch (e) {
            console.error('❌ Cannot read image:', imagePath);
            resolve(null);
            return;
        }
        
        // Build multipart body
        const payload = [
            `--${boundary}`,
            `Content-Disposition: form-data; name="title"`,
            '',
            title,
            `--${boundary}`,
            `Content-Disposition: form-data; name="content"`,
            '',
            htmlContent,
            `--${boundary}`,
            `Content-Disposition: form-data; name="categories"`,
            '',
            WP_CATEGORY_ID,
            `--${boundary}`,
            `Content-Disposition: form-data; name="status"`,
            '',
            'publish',
            `--${boundary}`,
            `Content-Disposition: form-data; name="slug"`,
            '',
            slug,
            `--${boundary}`,
            `Content-Disposition: form-data; name="file"; filename="${path.basename(imagePath)}"`,
            'Content-Type: image/jpeg',
            '',
            imageData.toString('binary'),
            `--${boundary}--`
        ].join('\r\n');
        
        const url = new URL('/wp-json/wp/v2/posts', BLOG_URL);
        
        const options = {
            hostname: url.hostname,
            path: url.pathname,
            method: 'POST',
            headers: {
                'Authorization': 'Basic ' + Buffer.from(WP_USER + ':' + WP_APP_PASSWORD).toString('base64'),
                'Content-Type': 'multipart/form-data; boundary=' + boundary,
                'Content-Length': Buffer.byteLength(payload)
            }
        };
        
        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    const json = JSON.parse(data);
                    if (res.statusCode === 200 || res.statusCode === 201) {
                        console.log('✅ อัปโหลดสำเร็จ:', json.link);
                        resolve(json.link);
                    } else {
                        console.error('❌ อัปโหลดล้มเหลว:', res.statusCode, json);
                        resolve(null);
                    }
                } catch (e) {
                    console.error('❌ Parse error:', data.substring(0, 200));
                    resolve(null);
                }
            });
        });
        
        req.on('error', (e) => {
            console.error('❌ Request error:', e.message);
            resolve(null);
        });
        
        req.write(payload, 'binary');
        req.end();
    });
}

function pushToGithub(episode) {
    try {
        execSync('git add .', { cwd: GITHUB_REPO, stdio: 'pipe' });
        execSync(`git commit -m "บทความตอนที่ ${episode}"`, { cwd: GITHUB_REPO, stdio: 'pipe' });
        execSync('git push', { cwd: GITHUB_REPO, stdio: 'pipe' });
        console.log('✅ Push ขึ้น GitHub สำเร็จ');
        return true;
    } catch (e) {
        console.error('❌ Git push ล้มเหลว:', e.message);
        return false;
    }
}

function saveMarkdown(episode, content) {
    const article = ARTICLES[episode];
    const filepath = path.join(ARTICLES_DIR, `${String(episode).padStart(2,'0')}-${article.slug}.md`);
    fs.writeFileSync(filepath, content, 'utf8');
    console.log('✅ บันทึกไฟล์:', filepath);
}

async function generateArticle(episode) {
    const article = ARTICLES[episode];
    if (!article) {
        console.error('❌ ไม่พบตอนที่', episode);
        return false;
    }
    
    console.log(`\n📝 กำลังสร้างบทความตอนที่ ${episode}: ${article.title}`);
    
    // Ensure directories exist
    if (!fs.existsSync(IMAGES_DIR)) fs.mkdirSync(IMAGES_DIR, { recursive: true });
    
    // 1. Create cover image
    const imagePath = path.join(IMAGES_DIR, `${String(episode).padStart(2,'0')}-${article.slug}.jpg`);
    generateImage(episode, article.title, imagePath);
    
    // 2. Load content
    const content = loadContent(article.content_path);
    if (!content) return false;
    
    // 3. Save markdown
    saveMarkdown(episode, content);
    
    // 4. Upload to WordPress
    const postUrl = await uploadWordpress(episode, article.title, content, imagePath, article.slug);
    
    // 5. Push to GitHub
    pushToGithub(episode);
    
    // 6. Update state
    let state = {};
    if (fs.existsSync(STATE_FILE)) {
        try {
            state = JSON.parse(fs.readFileSync(STATE_FILE, 'utf8'));
        } catch (e) {}
    }
    
    state[String(episode)] = {
        title: article.title,
        slug: article.slug,
        url: postUrl,
        published_at: new Date().toISOString()
    };
    
    fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2), 'utf8');
    
    console.log(`✅ ตอนที่ ${episode} เผยแพร่แล้ว!`);
    return postUrl;
}

async function generateAll() {
    let state = {};
    if (fs.existsSync(STATE_FILE)) {
        try {
            state = JSON.parse(fs.readFileSync(STATE_FILE, 'utf8'));
        } catch (e) {}
    }
    
    for (const episode of Object.keys(ARTICLES).map(Number).sort((a,b) => a-b)) {
        const episodeStr = String(episode);
        if (state[episodeStr]) {
            console.log(`⏭️ ตอนที่ ${episode} เผยแพร่แล้ว ข้าม...`);
        } else {
            console.log('\n' + '='.repeat(50));
            console.log(`📝 กำลังสร้างบทความตอนที่ ${episode}...`);
            await generateArticle(episode);
        }
    }
}

// ========== MAIN ==========
const args = process.argv.slice(2);

if (args.includes('--auto')) {
    generateAll().then(() => {
        console.log('\n✅ All done!');
        process.exit(0);
    }).catch(e => {
        console.error('❌ Error:', e);
        process.exit(1);
    });
} else if (args.includes('--episode')) {
    const idx = args.indexOf('--episode');
    const episode = parseInt(args[idx + 1]);
    if (episode && ARTICLES[episode]) {
        generateArticle(episode).then(url => {
            if (url) {
                console.log('\n✅ Published:', url);
            }
            process.exit(0);
        }).catch(e => {
            console.error('❌ Error:', e);
            process.exit(1);
        });
    } else {
        console.error('❌ Invalid episode. Available:', Object.keys(ARTICLES));
        process.exit(1);
    }
} else {
    console.log('Usage:');
    console.log('  node solar-blog-node.js --auto          (publish all unpublished)');
    console.log('  node solar-blog-node.js --episode 1     (publish specific episode)');
    process.exit(0);
}
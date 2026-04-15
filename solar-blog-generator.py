#!/usr/bin/env python3
"""
Solar Blog Generator - Nub-1 Blog
ผลิตบทความโซล่าเซลล์ ทุกวัน 11:30 น.
"""

import os
import sys
import json
import argparse
import subprocess
import requests
from datetime import datetime
from pathlib import Path

# ========== CONFIG ==========
BLOG_URL = "https://blog.joe-data.uk"
WP_USER = "Mew"
WP_APP_PASSWORD = "CPkk 1ouF xZS4 KpaH nCVO Ay5R"
WP_CATEGORY_ID = 24  # โซล่าเซลล์

GITHUB_REPO = "/root/.openclaw/workspace/Nub-1-Blog"
IMAGES_DIR = f"{GITHUB_REPO}/images"
ARTICLES_DIR = f"{GITHUB_REPO}/solar-articles"
STATE_FILE = f"{GITHUB_REPO}/published-state.json"

# ========== AFFILIATE LINKS (placeholder - will update later) ==========
AFFILIATE_LINKS = {
    # จะอัปเดตภายหลังจากเจ้านาย
}

# ========== ARTICLE TEMPLATES ==========

SCRIPT_DIR = Path(__file__).parent.absolute()
ARTICLE_FILES_DIR = SCRIPT_DIR / "solar-articles"

ARTICLES = {
    1: {
        "title": "ทำไมต้องสนใจโซลาร์ตอนนี้?",
        "slug": "why-solar-now-2026",
        "prompt_image": "Solar panels on rooftop with sun rays, modern house, Thailand scenery, 4:3 horizontal",
        "content": """# ทำไมต้องสนใจโซลาร์ตอนนี้? ☀️

## 🔥 สิ่งที่จะได้เรียนรู้
- ทำไมโซลาร์ถึงเป็นเรื่องที่ต้องรู้ตอนนี้
- ตัวเลขจริงที่น่าตกใจเกี่ยวกับค่าไฟ
- โอกาสที่หลายคนมองข้าม

---

## 🌞 เรื่องมันเริ่มต้นที่... บิลค่าไฟ!

ลองนึกภาพตามนะครับ...

คุณเปิดบิลค่าไฟเดือนที่แล้ว เจอตัวเลข **3,500 บาท** สำหรับครอบครัวเล็กๆ 4 คน คุณบอกตัวเองว่า "เยอะหว่า..." แต่ก็จ่ายไป

แล้วเดือนนี้ บิลมา **5,200 บาท!**

อ๋อ... คุณนึกออก ลูกเพิ่งเทิร์นอินสำคัญ ทีวีเปิดทั้งวัน แอร์ทำงานหนักขึ้น เครื่องซักผ้าก็หมุนบ่อยขึ้น

**นี่คือปัญหาที่ทุกบ้านกำลังเผชิญ**

---

## 💡 แล้วโซลาร์มาช่วยยังไง?

ลองนึกภาพว่า... หลังคาบ้านคุณเป็น "โรงงานผลิตไฟฟ้า" ขนาดเล็กๆ

☀️ **แดดทุกวัน** → โซลาร์แผงแปลงเป็นไฟฟ้า
⚡ **ไฟฟ้าที่ผลิตได้** → ใช้ในบ้านทันที
💰 **เจ็บตัวน้อยลง** → ค่าไฟลดลง 50-80%

มันเหมือนกับการติดตั้งเครื่องปั่นไฟขนาดเล็กบนหลังคา แต่ใช้พลังแดดฟรีๆ ไม่ต้องเติมน้ำมัน

---

## 📊 ตัวเลขที่หลายคนไม่รู้

**ค่าไฟไทยในปี 2569:**
- เฉลี่ยครัวเรือน: **3,000-5,000 บาท/เดือน**
- อัตราการขึ้นราคา: **ปีละ 5-10%**
- ค่าไฟต่อหน่วย: **4.18 บาท** (ยังไม่รวมFt)

**แล้วถ้าติดโซลาร์?**
- ลดค่าไฟได้: **1,500-4,000 บาท/เดือน**
- คืนทุน: **5-7 ปี**
- อายุการใช้งาน: **25-30 ปี**

นั่นหมายความว่า... **กำไร 18-25 ปี หลังจากคืนทุน!**

---

## 🏠 บ้านแบบไหนติดโซลาร์ได้?

คุณอาจคิดว่า "บ้านฉันคงติดไม่ได้"

ความจริง:
- ✅ บ้านเดี่ยว → ติดได้เลย!
- ✅ ทาวน์เฮาส์ → ถ้าหลังคาเอื้ออำนวย
- ✅ คอนโด → มีโซลูชันสำหรับคนอยู่คอนโด
- ✅ โรงงาน/อาคาร → ยิ่งคุ้มค่า!

**ข้อแม้เดียว:** ต้องมีพื้นที่หลังคาที่รับแดดได้อย่างน้อย 4-6 ชั่วโมง/วัน

---

## 🔑 สิ่งที่คุณจะได้จากซีรีย์นี้

ในซีรีย์ 20 ตอนนี้ ผมจะพาคุณ:

1. **เข้าใจโซลาร์เบื้องต้น** - มันทำงานยังไง
2. **คำนวณให้เป็น** - ขนาดระบบที่เหมาะกับบ้านคุณ
3. **เลือกให้ถูก** - อุปกรณ์ ช่าง บริษัท
4. **รู้ทันกฎหมาย** - ขออนุญาตยังไง สิทธิอะไรบ้าง
5. **ดูแลให้คุ้ม** - ให้โซลาร์อยู่ 25-30 ปี

**ไม่ต้องมีความรู้เรื่องไฟฟ้ามาก่อน** ผมจะอธิบายทุกอย่างเป็นเรื่องเล่า เปรียบเทียบให้เข้าใจง่าย

---

## ⚠️ ความเชื่อผิดๆ ที่ต้องลบล้าง

**ผิด:** "โซลาร์แพงมาก คนทั่วไปติดไม่ได้"
**จริง:** ราคาลดลง 70% ใน 10 ปี ตอนนี้เข้าถึงได้ง่าย

**ผิด:** "แดดบ้านเราไม่แรงพอ"
**จริง:** ประเทศไทยอยู่ในเขตที่แดดจัดที่สุดในโลก

**ผิด:** "ติดแล้วดูแลยุ่งยาก"
**จริง:** โซลาร์แทบไม่ต้องดูแล ทำความสะอาดปีละ 2-4 ครั้ง

---

## 📌 บทความตอนต่อไป

ในตอนที่ 2 เราจะมาว่ากันว่า **"ต้องรู้อะไรก่อนติดโซลาร์?"** — สิ่งที่หลายคนมองข้ามก่อนตัดสินใจ

---

## 🛒 สินค้าที่เกี่ยวข้อง

| รายการ | รายละเอียด | ลิงก์ |
|--------|-------------|-------|
| หนังสือพลังงานทดแทนสำหรับมือใหม่ | ความรู้พื้นฐานโซลาร์และพลังงานสะอาด | [ดูสินค้า](affiliate_link) |
| เครื่องคำนวณค่าไฟ Smart | วัดและติดตามการใช้ไฟฟ้าในบ้าน | [ดูสินค้า](affiliate_link) |

---

*บทความนี้เป็นส่วนหนึ่งของซีรีย์ "โซลาร์เบื้องต้น - จากมือใหม่สู่ผู้เชี่ยวชาญ" | [ดูตอนอื่นๆ](/)*
"""
    },
    2: {
        "title": "ต้องรู้อะไรก่อนติดโซลาร์?",
        "slug": "before-installing-solar",
        "prompt_image": "Checklist and notepad with solar panel background, Thailand house, 4:3",
        "content": """# ต้องรู้อะไรก่อนติดโซลาร์? 📋

## 🔥 สิ่งที่จะได้เรียนรู้
- สิ่งที่ต้องเช็คก่อนติดโซลาร์
- เอกสารที่ต้องเตรียม
- คำถามสำคัญที่ต้องถามบริษัท

---

## 🤔 เรื่องที่ไม่มีใครบอกคุณก่อนติดตั้ง

ก่อนจะโทรเรียกบริษัทมาติดตั้งโซลาร์... มีสิ่งที่คุณควรรู้ก่อน

เหมือนกับการซื้อรถยนต์คันใหม่ — คุณไม่ได้ซื้อแค่รถ แต่ซื้อ **บริการหลังการขาย อะไหล่ และความสบายใจ**

โซลาร์ก็เหมือนกัน...

---

## 📝 5 สิ่งที่ต้องเช็คก่อนตัดสินใจ

### 1️⃣ หลังคาบ้านคุณพร้อมไหม?

ลองถามตัวเอง:
- หลังคาโดนแดดเที่ยงกี่ชั่วโมง?
- มีต้นไม้หรืออาคารบังแดดไหม?
- หลังคาเก่าแค่ไหน? ต้องซ่อมก่อนไหม?

**วิธีง่ายๆ:** ถ่ายรูปหลังคาตอนเที่ยงวัน แล้วดูว่าแดดเต็มที่ไหม

---

### 2️⃣ ค่าไฟเฉลี่ยต่อเดือนเท่าไหร่?

ดูจากบิลค่าไฟ 3-6 เดือนล่าสุด

- ต่ำกว่า 2,000 บาท → ระบบเล็ก 3-5 kWp ก็เพียงพอ
- 2,000-4,000 บาท → ระบบกลาง 5-8 kWp
- 4,000-6,000 บาท → ระบบใหญ่ 8-10 kWp
- มากกว่า 6,000 บาท → ระบบพิเศษ ต้องคำนวณเพิ่ม

---

### 3️⃣ งบประมาณที่พร้อม?

**ราคาโซลาร์ต่อ 1 kWp (พร้อมติดตั้ง):**
- ระบบดี: 25,000-35,000 บาท
- ระบบกลาง: 20,000-25,000 บาท
- ระบบประหยัด: 15,000-20,000 บาท

**ตัวอย่าง:** บ้านใช้ไฟ 3,500 บาท/เดือน ต้องติดระบบ ~5 kWp
- ค่าใช้จ่าย: 5 kWp × 25,000 = **125,000 บาท**
- คืนทุน: 5-7 ปี

---

### 4️⃣ ทำบ้านหรือยัง?

ถ้าบ้านใหม่หรือกำลังสร้าง → **ติดตอนนี้เลย!**
- เดินสายไฟให้เรียบร้อยก่อน
- ประหยัดค่าใช้จ่ายตอนติดทีหลัง

ถ้าบ้านเก่า → ตรวจเช็คสภาพหลังคาและสายไฟก่อน

---

### 5️⃣ มีพื้นที่ว่างบนหลังคาเท่าไหร่?

**สูตรคร่าวๆ:**
- 1 kWp ต้องพื้นที่ ~7-8 ตร.ม.
- บ้าน 2 ชั้น หลังคาเฉลี่ย 60-80 ตร.ม.
- ติดได้สูงสุด ~8-10 kWp

---

## 📋 เอกสารที่ต้องเตรียม

| เอกสาร | ทำที่ไหน |
|--------|---------|
| สำเนาบัตรประชาชน | - |
| สำเนาทะเบียนบ้าน | - |
| สำเนาโฉนด/น.ส.3 | - |
| บิลค่าไฟ 3 เดือนล่าสุด | การไฟฟ้า |
| แบบแปลนบ้าน (ถ้ามี) | - |

---

## ❓ คำถามที่ต้องถามบริษัทก่อนติดตั้ง

1. **ใช้แผงโซลาร์ยี่ห้ออะไร?** → เลือกยี่ห้อดังๆ มีมาตรฐาน
2. **รับประกันกี่ปี?** → อย่างน้อย 10 ปี
3. **Inverter ยี่ห้ออะไร?** → เป็นหัวใจของระบบ
4. **มีศูนย์บริการที่ไหน?** → ดูว่าใกล้บ้านคุณไหม
5. **ทำงานให้กี่ปีแล้ว?** → เลือกบริษัทที่มีประสบการณ์

---

## ⚠️ สัญญาณเตือนที่ต้องระวัง

🚩 บริษัทที่:
- บอกว่า "ติดเร็วมาก 3 วันเสร็จ"
- ไม่มีสำนักงานให้ไปดู
- ไม่ยอมให้ดูผลงานจริง
- ราคาถูกกว่าท้องตลาดมากๆ

---

## 📌 บทความตอนต่อไป

ตอนที่ 3: **"โซลาร์ทำงานยังไง?"** — มาเข้าใจการทำงานของโซลาร์กัน

---

## 🛒 สินค้าที่เกี่ยวข้อง

| รายการ | รายละเอียด | ลิงก์ |
|--------|-------------|-------|
| มัลติมิเตอร์ดิจิตอล | วัดกระแสไฟฟ้า ตรวจสอบระบบไฟ | [ดูสินค้า](affiliate_link) |
| เครื่องวัดความเข้มแสงโซลาร์ | วัดว่าหลังคาคุณได้แสงเท่าไหร่ | [ดูสินค้า](affiliate_link) |
| Smart Meter | ติดตามการใช้ไฟฟ้าแบบเรียลไทม์ | [ดูสินค้า](affiliate_link) |

---

*บทความนี้เป็นส่วนหนึ่งของซีรีย์ "โซลาร์เบื้องต้น - จากมือใหม่สู่ผู้เชี่ยวชาญ" | [ดูตอนอื่นๆ](/)*
"""
    },
    3: {
        "title": "โซลาร์ทำงานยังไง?",
        "slug": "how-solar-works-2026",
        "prompt_image": "Solar panel cross-section diagram showing photovoltaic cells, sunlight rays, electron flow, educational illustration, Thailand",
        "content": f"file:{ARTICLE_FILES_DIR}/03-how-solar-works-2026.md"
    },
    4: {
        "title": "On-Grid vs Off-Grid vs Hybrid เลือกอันไหนดี?",
        "slug": "solar-on-grid-off-grid-hybrid-explained",
        "old_slug": "on-grid-off-grid-hybrid-2026",
        "prompt_image": "Three solar system diagrams showing grid connection, battery storage, and hybrid setup, Thailand house, infographic style",
        "content": f"file:{ARTICLE_FILES_DIR}/04-on-grid-off-grid-hybrid-2026.md"
    },
    5: {
        "title": "วิธีคำนวณขนาดระบบโซลาร์ที่เหมาะกับบ้านคุณ",
        "slug": "solar-system-size-calculation-guide",
        "old_slug": "how-to-calculate-solar-size-2026",
        "prompt_image": "Solar calculator with house roof diagram, showing kWp calculation, Thailand home setting, practical illustration",
        "content": f"file:{ARTICLE_FILES_DIR}/05-how-to-calculate-solar-size-2026.md"
    },
}


def load_article_content(article):
    """โหลด content จากไฟล์ ถ้า content เป็น path (เริ่มต้นด้วย 'file:')"""
    content = article.get('content', '')
    if content.startswith('file:'):
        filepath = content[5:].strip()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"❌ ไม่สามารถอ่านไฟล์ {filepath}: {e}")
            return content
    return content


def generate_image(episode, prompt, output_path):
    """สร้างรูปภาพปกด้วย ImageMagick"""
    print(f"🎨 กำลังสร้างรูปปกสำหรับตอนที่ {episode}...")

    # ข้อความบนรูป
    episode_text = f"ตอนที่ {episode}"
    title_text = ARTICLES[episode]["title"]

    # สร้างรูปด้วย ImageMagick (1200x900 = 4:3)
    cmd = f"""
    convert -size 1200x900 xc:#1a365d \
        -fill white -gravity center \
        -font Garuda -pointsize 72 \
        -annotate +0-150 '{episode_text}' \
        -font Garuda -pointsize 48 \
        -annotate +0+50 '{title_text}' \
        -font Garuda -pointsize 24 \
        -annotate +0+200 'Nub-1 Channel | โซล่าเซลล์' \
        -quality 90 {output_path}
    """

    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True)
        print(f"✅ รูปภาพบันทึกที่: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ สร้างรูปไม่สำเร็จ: {e}")
        return False


def save_markdown(episode, content):
    """บันทึกไฟล์ .md """
    filepath = f"{ARTICLES_DIR}/{episode:02d}-{ARTICLES[episode]['slug']}.md"
    Path(ARTICLES_DIR).mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ บันทึกไฟล์: {filepath}")
    return filepath


def upload_wordpress(episode, title, content, image_path, slug):
    """อัปโหลดบทความขึ้น WordPress"""
    # แปลง markdown เป็น HTML (แบบง่าย)
    html_content = content.replace('\n', '<br>\n')
    html_content = html_content.replace('# ', '<h2>').replace(' #', '</h2>')
    html_content = html_content.replace('## ', '<h3>').replace(' ##', '</h3>')
    html_content = html_content.replace('**', '<strong>').replace('**', '</strong>')

    url = f"{BLOG_URL}/wp-json/wp/v2/posts"
    files = {
        'file': open(image_path, 'rb')
    }
    data = {
        'title': title,
        'content': html_content,
        'categories': WP_CATEGORY_ID,
        'status': 'publish',
        'slug': slug
    }

    try:
        response = requests.post(url, auth=(WP_USER, WP_APP_PASSWORD), files=files, data=data, timeout=30)
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"✅ อัปโหลดสำเร็จ: {result.get('link', '')}")
            return result.get('link', '')
        else:
            print(f"❌ อัปโหลดล้มเหลว: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        return None


def push_to_github(episode):
    """Push ขึ้น GitHub"""
    try:
        subprocess.run(['git', 'add', '.'], cwd=GITHUB_REPO, check=True)
        subprocess.run(['git', 'commit', '-m', f'บทความตอนที่ {episode}'], cwd=GITHUB_REPO, check=True)
        subprocess.run(['git', 'push'], cwd=GITHUB_REPO, check=True)
        print('\u2705 Push ขึ้น GitHub สำเร็จ')
        return True
    except subprocess.CalledProcessError as e:
        print(f'\u274c Git push ล้มเหลว: {e}')
        return False


def generate_article(episode, use_ai=False):
    """สร้างและเผยแพร่บทความตอนที่กำหนด"""
    if episode not in ARTICLES:
        print(f"❌ ไม่พบตอนที่ {episode}")
        return False

    article = ARTICLES[episode]
    print(f"\n📝 กำลังสร้างบทความตอนที่ {episode}: {article['title']}")

    # 1. สร้างรูป
    image_path = f"{IMAGES_DIR}/{episode:02d}-{article['slug']}.jpg"
    Path(IMAGES_DIR).mkdir(parents=True, exist_ok=True)
    generate_image(episode, article['prompt_image'], image_path)

    # 2. โหลด content (จากไฟล์หรือ inline)
    content = load_article_content(article)

    # 3. บันทึก .md
    save_markdown(episode, content)

    # 4. อัปโหลด WordPress
    post_url = upload_wordpress(episode, article['title'], content, image_path, article['slug'])

    # 5. Push GitHub
    push_to_github(episode)

    # 6. อัปเดต state
    state = {}
    if Path(STATE_FILE).exists():
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)

    state[str(episode)] = {
        'title': article['title'],
        'slug': article['slug'],
        'url': post_url,
        'published_at': datetime.now().isoformat()
    }

    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    print(f"✅ ตอนที่ {episode} เผยแพร่แล้ว!")
    return True


def generate_all():
    """สร้างและเผยแพร่บทความทุกตอนที่ยังไม่เผยแพร่"""
    state = {}
    if Path(STATE_FILE).exists():
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)

    for episode in sorted(ARTICLES.keys()):
        episode_str = str(episode)
        if episode_str not in state:
            print(f"\n{'='*50}")
            print(f"📝 กำลังสร้างบทความตอนที่ {episode}...")
            generate_article(episode)
        else:
            print(f"⏭️ ตอนที่ {episode} เผยแพร่แล้ว ข้าม...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solar Blog Generator')
    parser.add_argument('--episode', type=int, help='สร้างบทความตอนที่ต้องการ')
    parser.add_argument('--auto', action='store_true', help='สร้างทุกตอนที่ยังไม่เผยแพร่')
    parser.add_argument('--force', action='store_true', help='สร้างใหม่ทั้งหมด')
    args = parser.parse_args()

    if args.episode:
        generate_article(args.episode)
    elif args.auto:
        generate_all()
    else:
        print("ใช้งาน: python solar-blog-generator.py --episode 1")
        print("   หรือ: python solar-blog-generator.py --auto  (สร้างทุกตอนที่ยังไม่เผยแพร่)")

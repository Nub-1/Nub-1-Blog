# WordPress Solar Article Template
# ใช้สำหรับบทความโซลาร์ทุกตอนบน WordPress

## ⚠️ สำคัญ: รูปแบบที่ต้องจำ

### 1. Header Section (Gradient Banner)
```html
<div style="background: linear-gradient(135deg, #1a365d 0%, #2d3748 100%); color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px;">
<h2 style="color: #ffd700; margin: 0;">[หัวข้อหลัก]</h2>
<p style="color: #e2e8f0; margin-top: 10px;">ตอนที่ X | ระดับ: [พื้นฐาน/กลาง/ขั้นสูง] | เวลาอ่าน: XX-XXX นาที</p>
</div>
```

### 2. Table of Contents (ถ้ายาวมาก)
```html
<div style="border-left: 4px solid #4299e1; padding-left: 20px; margin: 20px 0;">
<strong style="color: #2d3748;">📋 สารบัญ</strong>
<ol style="color: #4a5568; line-height: 1.8;">
<li><a href="#section1">ชื่อ section 1</a></li>
...
</ol>
</div>
```

### 3. Section Headers
```html
<h2 id="sectionX" style="color: #2d3748; border-bottom: 3px solid #COLORCODE; padding-bottom: 10px;">X. 📌 หัวข้อหลัก</h2>
```

### 4. Content Blocks

**แบบ Info Box:**
```html
<div style="background: #ebf8ff; padding: 20px; border-radius: 10px; margin: 15px 0; border-left: 4px solid #4299e1;">
<strong style="color: #2b6cb0;">💡 คำแนะนำ</strong>
<p style="color: #4a5568; margin-bottom: 0;">เนื้อหา...</p>
</div>
```

**แบบ Warning:**
```html
<div style="background: #fff5f5; padding: 20px; border-radius: 10px; margin: 15px 0; border-left: 4px solid #f56565;">
<strong style="color: #c53030;">⚠️ คำเตือน</strong>
<p style="color: #4a5568; margin-bottom: 0;">เนื้อหา...</p>
</div>
```

**แบบ Success/Highlight:**
```html
<div style="background: #f0fff4; padding: 20px; border-radius: 10px; margin: 15px 0; border-left: 4px solid #48bb78;">
<strong style="color: #276749;">✅ สรุป</strong>
<p style="color: #4a5568; margin-bottom: 0;">เนื้อหา...</p>
</div>
```

**แบบ Stats/Data:**
```html
<div style="background: #f7fafc; padding: 20px; border-radius: 10px; margin: 15px 0;">
• <strong>รายการ 1:</strong> ค่า<br>
• <strong>รายการ 2:</strong> ค่า
</div>
```

**แบบ 3-Column Flex:**
```html
<div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 20px 0;">
<div style="flex: 1; min-width: 200px; background: #ebf8ff; padding: 15px; border-radius: 10px; border-left: 4px solid #4299e1;">
<strong style="color: #2b6cb0;">หัวข้อ 1</strong>
<p style="color: #4a5568; margin: 5px 0;">เนื้อหา...</p>
</div>
<div style="flex: 1; min-width: 200px; background: #f0fff4; padding: 15px; border-radius: 10px; border-left: 4px solid #48bb78;">
<strong style="color: #276749;">หัวข้อ 2</strong>
<p style="color: #4a5568; margin: 5px 0;">เนื้อหา...</p>
</div>
</div>
```

**แบบ Checklist:**
```html
<div style="background: #f7fafc; padding: 20px; border-radius: 10px; margin: 15px 0;">
☐ รายการที่ 1<br>
☐ รายการที่ 2<br>
☐ รายการที่ 3
</div>
```

### 5. Footer Sections

**Author Box:**
```html
<hr style="border: none; border-top: 2px solid #e2e8f0; margin: 30px 0;">
<div style="background: linear-gradient(135deg, #1a365d 0%, #2d3748 100%); color: white; padding: 25px; border-radius: 15px; margin-top: 30px;">
<h3 style="color: #ffd700; margin-top: 0;">✏️ เกี่ยวกับผู้เขียน</h3>
<p style="margin-bottom: 0;">
<strong>Nub-1 Channel | โจ้ พัฒนากร</strong><br>
<span style="color: #e2e8f0;">นักวิชาการพัฒนาชุมชนชำนาญการ | ผู้เชี่ยวชาญด้านพลังงานทดแทน</span><br>
<span style="color: #a0aec0; font-size: 0.9em;">
📧 Contact | 🔗 Website | 📱 Social Media<br>
<a href="https://blog.joe-data.uk" style="color: #63b3ed;">blog.joe-data.uk</a>
</span>
</p>
</div>
```

**References Section:**
```html
<hr style="border: none; border-top: 2px solid #e2e8f0; margin: 30px 0;">
<div style="background: #f7fafc; padding: 25px; border-radius: 10px; margin: 20px 0;">
<h3 style="color: #2d3748; margin-top: 0;">📚 แหล่งอ้างอิงและข้อมูลที่ใช้</h3>

<p style="color: #4a5568; font-weight: bold;">แหล่งที่มาหลัก:</p>
<ol style="color: #4a5568; line-height: 1.8;">
<li><strong>การไฟฟ้าฝ่ายผลิตแห่งประเทศไทย (EGAT)</strong> - ข้อมูลการผลิตไฟฟ้า<br>
<a href="https://www.egat.co.th" style="color: #3182ce;">https://www.egat.co.th</a></li>

<li><strong>การไฟฟ้าส่วนภูมิภาค (PEA)</strong> - ข้อมูลโซลาร์ภาคประชาชน<br>
<a href="https://www.pea.co.th" style="color: #3182ce;">https://www.pea.co.th</a></li>

<li><strong>สำนักงานคณะกรรมการกำกับกิจการพลังงาน (กกพ.)</strong> - มาตรฐานและกฎหมาย<br>
<a href="https://www.energy.go.th" style="color: #3182ce;">https://www.energy.go.th</a></li>

<li><strong>กรมพัฒนาพลังงานทดแทน (DEDE)</strong> - สถิติพลังงานทดแทน<br>
<a href="https://www.dede.go.th" style="color: #3182ce;">https://www.dede.go.th</a></li>
</ol>

<p style="color: #4a5568; font-weight: bold; margin-top: 20px;">มาตรฐานที่อ้างอิง:</p>
<ul style="color: #4a5568; line-height: 1.8;">
<li><strong>IEC 61215</strong> - มาตรฐานแผงโซลาร์เซลล์</li>
<li><strong>IEC 61730</strong> - มาตรฐานความปลอดภัยแผงโซลาร์</li>
<li><strong>IEC 62109</strong> - มาตรฐานอินเวอร์เตอร์</li>
<li><strong>TIS 2214</strong> - มาตรฐานผลิตภัณฑ์อุตสาหกรรมไทยสำหรับโซลาร์</li>
</ul>

<p style="color: #718096; font-size: 0.9em; margin-top: 20px; padding-top: 15px; border-top: 1px solid #e2e8f0;">
<em>* ข้อมูลอ้างอิง ณ วันที่ [DD MMMM YYYY] ราคาและเงื่อนไขอาจมีการเปลี่ยนแปลง ควรตรวจสอบข้อมูลล่าสุดกับแหล่งที่มาทางการก่อนตัดสินใจ</em>
</p>
</div>
```

**CTA Section:**
```html
<div style="background: #f0fff4; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
<p style="color: #276749; font-weight: bold; margin-bottom: 10px;">📢 ต้องการติดตามบทความต่อไป?</p>
<p style="color: #4a5568; margin-bottom: 0;">
<a href="https://blog.joe-data.uk" style="background: #48bb78; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">ดูบทความทั้งหมด</a>
</p>
</div>
```

---

## 🎨 รหัสสีที่ใช้บ่อย

| สี | Hex | ใช้สำหรับ |
|----|-----|-----------|
| เขียวเข้ม | #276749 | Success, CTA |
| เขียวอ่อน | #48bb78 | Success border |
| น้ำเงินเข้ม | #2b6cb0 | Info, Links |
| น้ำเงินอ่อน | #4299e1 | Info border |
| แดงเข้ม | #c53030 | Warning |
| แดงอ่อน | #f56565 | Warning border |
| เหลืองทอง | #ffd700 | Highlight, Title |
| เทาเข้ม | #2d3748 | Text headers |
| เทาอ่อน | #4a5568 | Body text |
| Background | #f7fafc | Light boxes |

---

## 📝 Checklist ก่อน Publish

- [ ] หัวข้อ H2 มี emoji + หมายเลข section
- [ ] มี Table of Contents (ถ้ายาว > 2000 คำ)
- [ ] ใช้ styled boxes แทนตาราง
- [ ] มี Author Box ท้ายบทความ
- [ ] มี References Section พร้อมลิงก์
- [ ] มี CTA Section
- [ ] เช็คว่าลิงก์ถูกต้อง
- [ ] Featured Image ขนาด 1200x630
- [ ] Category: โซล่าเซลล์ (ID: 24)
- [ ] slug: solar-episode-X-[topic]

---

## 📅 ตอนที่ต้องทำ

| ตอน | หัวข้อ | สถานะ |
|-----|--------|-------|
| 1 | ทำไมต้องสนใจโซลาร์ตอนนี้? | ✅ เสร็จแล้ว |
| 2 | ต้องรู้อะไรก่อนติดโซลาร์? | ⏳ รอพรุ่งนี้ 11:30 |
| 3 | โซลาร์ทำงานยังไง? | 📋 ต้องเขียน |
| ... | ... | ... |
| 20 | เทคโนโลยีอนาคต + สรุป | 📋 ต้องเขียน |

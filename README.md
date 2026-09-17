# A Date with Death — Thai Localization Mod

ม็อดแปลภาษาไทยสำหรับเกม **A Date with Death** (Ren'Py 8.2.1, Steam PC)

Thai localization mod for *A Date with Death*.

## วิธีติดตั้ง (Installation)

1. แตกไฟล์ `thai_mod.zip` — จะได้ไฟล์ `game/thai_mod.rpa`
2. คัดลอก `thai_mod.rpa` ไปวางในโฟลเดอร์ `game\` ของเกม

   ```
   A Date with Death\game\thai_mod.rpa
   ```

   (หรือแตก zip ลงในโฟลเดอร์เกมโดยตรง — ไฟล์จะไปอยู่ที่ถูกต้องเอง)

3. เปิดเกม — ครั้งแรกจะมีหน้าเลือกภาษา **English / ไทย / 日本語**
4. สลับภาษาได้ตลอดผ่านปุ่ม **EN / ไทย** ที่มุมซ้ายบน หรือในเมนู Preferences → Text Language

## วิธีถอน (Uninstall)

- ลบไฟล์ `thai_mod.rpa` ออกจากโฟลเดอร์ `game\`

## ข้อกำหนด (Requirements)

- เกม A Date with Death — Steam PC build (Ren'Py 8.2.1) **เวอร์ชันเดียวกันเท่านั้น**
  - `thai_mod.rpa` เก็บ `.rpyc` compiled — ถ้าเกมอัปเดต Ren'Py version ต้อง rebuild ม็อด
- ไม่ต้องแตะ `archive.rpa` เดิม — ม็อดทำงานแบบ overlay ไฟล์แยก

## สิ่งที่แปล (Coverage)

- เนื้อเรื่องครบทุกวัน Day 1–7, room exploration, bad end, endings 1–2, DLC ending
- UI ทั้งหมด, หน้าสร้างตัวละคร, pronouns, หนังสือในเกม, ข้อความแชท/DM, contacts
- ฟอนต์ไทยครบทุกชุด (composite fonts รักษาสไตล์ตัวอักษรเดิม)
- ตัดบรรทัดภาษาไทยถูกต้อง (zero-width-space word segmentation)

## หมายเหตุ (Notes)

- Lingo minigame คงเป็นภาษาอังกฤษ (สระ/วรรณยุกต์ไทยไม่เข้ากับตารางตัวอักษร)
- ชื่อผู้ใช้, ชื่อเกม, ชื่อ DLC "Beyond the Bet" คงเป็นภาษาอังกฤษตามเจตนา

## เครดิต (Credits)

- เกมต้นฉบับ: *A Date with Death* by Two and a Half Studios
- ฟอนต์: Noto Sans Thai, PlainPixel (OFL/Apache)
- แปลและสร้างม็อดด้วย [Devin](https://devin.ai)

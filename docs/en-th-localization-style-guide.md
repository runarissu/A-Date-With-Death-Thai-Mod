# English → Thai Localization Style Guide
## A Date with Death (Ren'Py 8.2.1)

> มาตรฐานการแปลวิดีโอเกมจากภาษาอังกฤษเป็นภาษาไทย สำหรับใช้กับเกม *A Date with Death*
> อ้างอิงหลักการแปลเกมมืออาชีพ (IGDA Localization SIG, SEAMEO RELC, ราชบัณฑิตยสถาน)
> และบทเรียนจาก Japanese localization ที่มีอยู่ในเกม (`tl/japanese/`)

---

## 1. หลักการพื้นฐาน (Core Principles)

| หลักการ | คำอธิบาย |
|---|---|
| **Meaning over Literal** | แปลความหมายและอารมณ์เป็นหลัก ไม่แปลคำต่อคำจนแข็ง |
| **Tone Preservation** | รักษาน้ำเสียงของตัวละคร — Grim โอ่อ่า/น่าขนลุก, ผู้เล่น ขี้เล่น/ตลก |
| **Character Voice Consistency** | ตัวละครแต่ละตัวมี "เสียง" คงเส้นคงวา ดูตารางที่ 3 |
| **Context-Aware** | แปลตามบริบทฉาก — คำเดียวกันอาจแปลต่างกันใน chat vs call vs narrator |
| **Idiomatic Thai** | ภาษาไทยมาตรฐานราชบัณฑิตยสถาน + ภาษาพูดธรรมชาติตามตัวละคร |
| **No Over-Localization** | proper nouns ที่เป็นเอกลักษณ์คงไว้/ทับศัพท์ ไม่แปล |

---

## 2. โครงสร้างเกมที่ต้องรู้ (Game Structure)

เกมนี้เป็น **chat-based VN** — ผู้เล่นคุยกับยมทูตผ่านโปรแกรมแชทในคอม มี 2 โหมดแสดงผล:

| โหมด | ตัวละคร Ren'Py | ลักษณะ |
|---|---|---|
| **NVL / Chat** (`gametype = "NVL"`) | `GR`, `player`, `nv`, `O` | แชทตัวอักษรเต็มจอ คล้ายโปรแกรมแชทจริง |
| **ADV / Call & Room** (`gametype = "ADV"`) | `GRC`, `playerc`, `other`, `O_ip` | หน้าจอโทรศัพท์ / คลิกสำรวจห้อง |
| **Narrator** | `narrator` (italic) | ผู้เล่นคิดในใจ |
| **Center text** | `center_text` | ข้อความกลางจอ (dramatic reveal) |

### ไฟล์ script หลัก

| ไฟล์ | เนื้อหา |
|---|---|
| `script.rpy` | flow หลัก, นิยามตัวละคร/ตัวแปร |
| `chapters/1_day.rpy` … `6_day.rpy`, `7_roomexplore.rpy` | เนื้อเรื่องรายวัน |
| `chapters/*_roomexplore.rpy` | สำรวจห้อง (คลิกของ) |
| `chapters/bad_end.rpy`, `end_1.rpy`, `end_2.rpy`, `dlc_end.rpy` | endings |
| `books.rpy` | หนังสืออ่านได้ในเกม (เนื้อความยาว) |
| `call_messages.rpy` | ข้อความประกอบสายโทร |
| `computer.rpy`, `contacts.rpy` | UI คอม/รายชื่อ |
| `pronoun selection.rpy` | หน้าเลือก pronouns/เพศ/descriptors |
| `charactercreator.rpy`, `roomcreation.rpy` | หน้าสร้างตัวละคร/ห้อง |
| `lingo.rpy` | มินิเกม Wordle-like (ดูข้อ 16.6) |
| `pong.rpy` | มินิเกม Pong |
| `kinetic_text_tags.rpy` | custom text effects |

---

## 3. เสียงตัวละคร (Character Voice Profile)

| ตัวละคร | บุคลิก EN | สรรพนามตัวเอง (TH) | สรรพนามผู้ฟัง (TH) | น้ำเสียงไทย |
|---|---|---|---|---|
| **Grim** (`GR`/`GRC`, ชื่อ `[grim_reaper_name!t]`) | ยมทูต โอ่อ่า พูด **Title Case ทุกคำ** เชิงข่มขู่แต่ค่อยๆ อ่อนลง | **ข้า** | **เจ้า** | ดูข้อ 3.1 — สำคัญที่สุดของเกมนี้ |
| **Player** (`player`/`playerc`, ชื่อ `[playername!t]`) | วิญญาณคนเป็นๆ ขี้แกล้ง ชอบพูนสยอง (death puns) | ฉัน | เธอ/นาย | ภาษาพูด casual แซว Grim |
| **Narration** (`center_text`) | บรรยายบุคคลที่สอง ("you") | คุณ | — | ภาษาบรรยาย ไม่มีคำสุภาพ — ดูข้อ 10 |
| **Nobody** (`O`) | สถานะ "ไม่มีใคร" ในแชท | — | — | แปลชื่อเป็น "ว่างเปล่า" / คง "Nobody" ตามบริบท |
| **Other Reaper** (`O_ip`, ชื่อ `[other_reaper_name]`) | ยมทูตอีกตน (DLC) ชื่อเริ่มจาก "???" | ข้า | เจ้า | โทนเดียวกับ Grim หรือแยกตามบุคลิกเมื่อเปิดเผย |

> ⚠️ ชื่อทุกตัวเป็น **dynamic** — ผู้เล่นเปลี่ยนชื่อ Grim/ตัวเองได้ ห้าม hardcode ชื่อในประโยค ต้องใช้ `[grim_reaper_name!t]`, `[playername!t]` เสมอ

### 3.1 ปัญหา Title Case ของ Grim — การตัดสินใจเชิงสร้างสรรค์

Grim พูดแบบ `"I Shall Make It As Painful As I Can For You."` — **ทุกคำขึ้นต้นตัวพิมพ์ใหญ่** เพื่อสื่อความโบราณ สูงส่ง น่าเกรงขาม

**ภาษาไทยไม่มีตัวพิมพ์** → ต้องใช้ register แทน:

- สรรพนาม **"ข้า"** (I) และ **"เจ้า"** (you) — archaic, น่าเกรงขาม, เทียบเท่า "貴様" ที่ Japanese TL ใช้
- โครงประโยคกระชับ หนักแน่น ท้ายประโยคไม่ใส่ particle เบาๆ (ไม่ใช้ "นะ", "จ้ะ")
- ใช้คำโบราณ/วรรณกรรมตามบริบท: "จง", "มิ", "บัดนี้", "หมายมั่น" — อย่าเยอะจนอ่านไม่รู้เรื่อง
- เมื่อ Grim **อ่อนลง/ใกล้ชิด** ผู้เล่นในภาคหลัง ให้ค่อยๆ ผ่อน register ลง (ใช้ "เจ้า" ต่อ แต่ประโยคนุ่มขึ้น) — สะท้อน character arc เดียวกับต้นฉบับ

| EN (Grim) | TH ✅ | TH ❌ |
|---|---|---|
| "Know This." | "จงรู้ไว้" | "รู้ไว้นะ" |
| "I Shall Make It As Painful As I Can For You." | "ข้าจะมอบความเจ็บปวดให้เจ้ามากที่สุดเท่าที่ข้าทำได้" | "ฉันจะทำให้เจ็บที่สุดเลย" |
| "Stupid Mortal." | "มนุษย์โง่เขลา" | "คนโง่" |

---

## 4. ระบบ Pronoun แบบ Dynamic — จัดการผ่าน `translate thai strings`

### 4.1 ตัวแปรทั้งหมด (จาก `pronoun selection.rpy`)

ทุกค่า pronoun ครอบด้วย `__()` อยู่แล้ว → **แปลผ่าน translate strings ได้เลย ไม่ต้องเขียน Python override** (วิธีเดียวกับที่ Japanese TL ทำ)

| ตัวแปร | EN (she/he/they) | ค่าไทยแนะนำ | บริบท |
|---|---|---|---|
| `she` / `She` | she / he / they | **เขา** | pronoun หลัก — "[She] [is] waiting" |
| `her` / `Her` | her / him / them | **เขา** | object/possessive — "give [her] time" |
| `her2` / `Her2` | her / his / their | **ของเขา** | possessive ชัดเจน |
| `she2` / `She2` | she / he / they | **เขา** | variant ตัวที่สอง |
| `gender` | female / male / nb | **เพศ** *(ดูหมายเหตุ)* | ใช้ใน UI/logic |
| `girl` / `Girl` | girl / guy / person | **คน** / ผู้หญิง / ผู้ชาย | "[girl] like you" |
| `women` | women / men / people | **ผู้คน** | |
| `woman` | woman / man / person | **คน** | |
| `wife` | wife / husband / spouse | **คู่สมรส** | |
| `pretty` | pretty / cute / captivating | **น่ารัก** | descriptor เบา |
| `beautiful` | beautiful / handsome / divine | **งดงาม** | descriptor หนัก |
| `custom_She` / `custom_Her` | (ผู้เล่นพิมพ์เอง) | **เขา** (default ไทย) | custom pronoun |
| `custom_pretty` / `custom_beautiful` | (ผู้เล่นพิมพ์เอง) | **น่ารัก** / **งดงาม** | custom descriptor |

### 4.2 หลักการแปล

```renpy
translate thai strings:
    old "she"
    new "เขา"

    old "her"
    new "เขา"

    old "Girl"
    new "คน"
```

- ภาษาไทยไม่มี gendered pronoun ระดับคำ → ใช้คำกลางเพศทุกกรณี คล้ายกลยุทธ์ของ reference project
- หน้า **pronoun selection** เองต้องแปล label ปุ่มด้วย ("She/Her", "He/Him", "They/Them", "Custom") — ให้แปลเป็นคำอธิบายไทย ไม่ใช่ค่าที่จะ inject
- ⚠️ **Custom pronouns**: ผู้เล่นพิมพ์ pronoun เองได้ — ค่า custom จะ inject ดิบๆ เข้าประโยค ประโยคไทยต้องออกแบบให้รองรับคำแปลกได้ (หลีกเลี่ยงโครงที่ต้อง agreement)
- ⚠️ เช็คทุกประโยคที่มี `[she]`/`[her]`/`[pretty]` ว่าอ่านเป็นธรรมชาติหลังแทน "เขา"/"น่ารัก" — ถ้าแปลกให้แปลทั้งประโยคใหม่

| ต้นฉบับ | แปลตรง (ไม่ดี) | แปลใหม่ (ดี) |
|---|---|---|
| `[She] said [she]'d wait for me.` | "เขา พูดว่าเขาจะรอฉัน" | "เขาบอกว่าจะรอฉัน" |
| `You look [pretty] today.` | "เธอดูน่ารัก วันนี้" | "วันนี้เธอดูน่ารักจัง" |

---

## 5. การรักษา Tag และ Variable — ห้ามแตะเด็ดขาด

### 5.1 Ren'Py standard tags

| Tag | ตัวอย่าง |
|---|---|
| Formatting | `{b}` `{/b}` `{i}` `{/i}` `{size=}` `{color=}` `{font=}` |
| Interpolation | `[playername!t]` `[grim_reaper_name!t]` `[she]` `[pretty]` |
| Wait/control | `{w}` `{p}` `{nw}` `{fast}` `{clear}` `{cps=}` |
| Escape | `{{` `[[` `\\` |

### 5.2 Custom tags ของเกมนี้ (Kinetic Text Tags — `kinetic_text_tags.rpy`)

| Tag | Effect | ตัวอย่างจริงในเกม |
|---|---|---|
| `{bt=...}` `{/bt}` | ตัวอักษรเด้ง | `{bt=10}`, `{bt=h5-p2.0-s0.5}` |
| `{fi=...}` `{/fi}` | fade in ทีละตัว | `{fi=0-0.5}` |
| `{sc=...}` `{/sc}` | ตัวอักษรสั่น/น่ากลัว | `{sc=2}`, `{sc=[range]}` |
| `{chaos}` `{/chaos}` | ตัวอักษรกระจายวุ่นวาย | `{chaos}` |
| `{rotat=...}` `{/rotat}` | หมุน | `{rotat=[speed]}` |
| `{swap=...}` `{/swap}` | สลับข้อความ | `{swap=Text@Four@0.5}` |
| `{move}` `{/move}` | เคลื่อนไหว | `{move}` |
| `{omega=...}` `{/omega}` | composite effect | `{omega=BT=[bt_arg]@SC=[sc_arg]@...}` |
| `{para}` | paragraph (self-closing) | `{para}` |

> ⚠️ `{omega}` รับ argument ที่เป็น **ตัวแปร** — `{omega=BT=[bt_arg]@SC=[sc_arg]@FI=...}` ห้ามแปล parameter names และห้ามแปลข้อความที่ถูก `swap` (มันคือ text ID)
> ⚠️ `{swap=Text@Four@0.5}` — `Text@Four` คือ string reference ห้ามแปล

### 5.3 `{font=...}` inline tags

เกมใช้ `{font=gui/8bitOperatorPlusSC-Regular.ttf}` กับข้อความ glitch (WARNING/ERROR/SYSTEM MALFUNCTION) และ `{font=gui/PixelMplus12-Regular.ttf}` สำหรับญี่ปุ่น

- **คง tag ไว้** แต่ระวัง: font pixel ไม่มี glyph ไทย → ข้อความไทยใน `{font=...}` จะเป็น `□□□`
- วิธีแก้: ใช้ `config.font_replacement_map` map `8bitOperatorPlusSC` → composite Thai font (แนวทางเดียวกับ `replace_font.rpy` ของ reference)

### 5.4 ตัวอย่างถูก/ผิด

```renpy
# ต้นฉบับ
GR "{sc=2}Stupid Mortal.{/sc} You Would Quiver Under My Gaze."

# ✅
GR "{sc=2}มนุษย์โง่เขลา{/sc} เจ้าคงตัวสั่นอยู่ใต้สายตาข้า ก่อนที่ข้าจะประทานความตายให้"

# ❌ ลบ tag
GR "มนุษย์โง่เขลา เจ้าคงตัวสั่นอยู่ใต้สายตาข้า"

# ❌ แปลชื่อตัวแปร
GR "มนุษย์โง่เขลา [ชื่อผู้เล่น]"
```

---

## 6. การทับศัพท์ vs การแปล

### 6.1 คงเดิม / ทับศัพท์

| หมวด | ตัวอย่าง | เหตุผล |
|---|---|---|
| ชื่อเกม | A Date with Death | proper noun |
| ชื่อตัวละคร dynamic | `[grim_reaper_name!t]`, `[playername!t]` | ผู้เล่นตั้งเอง — ผ่านตัวแปรเท่านั้น |
| ชื่อ default | "Grim Reaper", "Grim", "Soul#8129" | ดูตาราง Glossary (ข้อ 14) — แปลได้แบบ JP (`魂＃8129`) หรือคง EN |
| ศัพท์เกม | soul, reaping, reaper (เมื่อเป็นคำทั่วไป) | แปล: วิญญาณ, เก็บเกี่ยววิญญาณ, ยมทูต |
| คำ tech/UI | Save, Load, Steam, DLC | คนคุ้น |
| มินิเกม | Pong, lingo (wordle) | ชื่อเกม |

### 6.2 ทับศัพท์เมื่อคุ้นกว่า

| EN | TH |
|---|---|
| meme | มีม |
| spoiler | สปอยล์ |
| chat / DM | แชท / DM |
| streamer mode | โหมดสตรีมเมอร์ |
| plush(ie) | ตุ๊กตา (Casper plush → ตุ๊กตา Casper) |

---

## 7. วรรคตอนและเครื่องหมาย

- ไทยไม่ใช้ `.` จบประโยค — แต่ถ้าต้นฉบับมี `.` ท้ายบรรทัด ให้**คงไว้** (engine ใช้ตรวจ end-of-line บางจุด)
- `...` สำหรับ hesitation, `—` สำหรับ interruption — คงตามต้นฉบับ
- วรรณยุกต์ใส่ครบ: ่ ้ ๊ ๋ ั ี ื ็ ฯ — ยกเว้นแชท (ข้อ 11)
- เว้นวรรคระหว่างประโยค ไม่เว้นหน้าสระ/วรรณยุกต์
- ห้ามลบ `\n`

### 7.1 รูปแบบ Choice — `"1. <ข้อความ>"`

ตัวเลือกของเกมนี้มี format เฉพาะ: `"1. <Hey...>"` (เลข + preview ใน `<>`)

```renpy
# ต้นฉบับ
menu:
    "1. <Make a killing? :)>":
        player "Make a killing? :)"

# ✅ — คงโครง "N. <...>" แปลเฉพาะข้างใน
menu:
    "1. <ทำเอาตายไปเลยสิ? :)>":
        player "ทำเอาตายไปเลยสิ? :)"
```

> Japanese TL เปลี่ยนเป็น `１.《…》` (fullwidth + angle quotes) — ทำตามได้ถ้าต้องการสไตล์ แต่ต้องทำให้ **consistent ทั้งเกม** ค่า default ที่ปลอดภัยคือคง `1. <…>` เดิม

---

## 8. ความยาวข้อความ

- English → Thai เฉลี่ย 1.0–1.3 เท่า
- ⚠️ **NVL chat** ของเกมนี้มีพื้นที่จำกัดกว่า ADV ทั่วไป — ข้อความยาวจะล้น bubble ทดสอบในเกมจริงบ่อย
- UI/ปุ่มต้องสั้นมาก (โปรแกรมคอมในเกมจำลอง OS — พื้นที่น้อย)
- Grim พูดสั้น หนักแน่น — อย่าแปลให้ยาวพล่าม

---

## 9. การแปล UI / Menu

| EN | TH | หมายเหตุ |
|---|---|---|
| Start | เริ่มเกม | |
| Continue | เล่นต่อ | |
| Save / Load | บันทึก / โหลด | |
| Preferences / Options | การตั้งค่า | |
| Text Language | ภาษาข้อความ | มีอยู่แล้วในเกม (EN/JP) — เพิ่ม TH |
| Voice Language | ภาษาเสียง | |
| History | ประวัติ | |
| Skip | ข้าม | |
| Auto | ออโต้ | |
| Main Menu | เมนูหลัก | |
| Quit | ออกจากเกม | |
| New Character | สร้างตัวละครใหม่ | character creator |
| Pronouns | สรรพนาม | |
| Customize | ปรับแต่ง | |
| CALL ENDED | สายสิ้นสุด | glitch screen — คง font tag |
| Day N | วันที่ N | |
| Ending | ตอนจบ | |

---

## 10. การแปล Narration (`center_text`) — Second Person

- เกมนี้บรรยายแบบ **บุคคลที่สอง** ("you") ผ่าน `center_text` — JP TL ใช้ あなた
- ใช้ **"คุณ"** — กลางเพศ ตรง design ที่ผู้เล่นเลือกเพศเอง
- ภาษาบรรยาย, ไม่มีคำสุภาพ; tense ใช้ "แล้ว/เคย/กำลัง" บอกเวลา
- (`narrator` ตัว italic ถูก define ไว้แต่แทบไม่ถูกใช้ — narration จริงคือ `center_text`)

```renpy
# ต้นฉบับ
center_text "You've been here before, haven't you?"

# ✅
center_text "คุณเคยอยู่ที่นี่มาก่อน ไม่ใช่เหรอ?"
```

---

## 11. การแปลแชท (Chat Register) — หัวใจของเกมนี้

ผู้เล่นคุยกับ Grim ผ่าน **โปรแกรมแชท** — register ต่างจากบทพูดปกติ:

- ผู้เล่น: ภาษาแชทจริง สั้น กระชับ emoticon/emoticon text (`:)`, `>.<`) คงไว้
- death puns / wordplay: **แปลแบบสร้างสรรค์** — หา pun ไทยที่เทียบอารมณ์ อย่าแปลตรงจนเสียมุก

| EN (pun) | แปลตรง ❌ | แนวทาง ✅ |
|---|---|---|
| "Make a killing? :)" | "ฆ่าคนได้กำไร?" | "ทำเอาตายไปเลยสิ?" / เล่นคำ "ตาย" สองนัย |
| "dying to meet you" | "กำลังตายอยากเจอ" | "ตั้งตารอจนแทบตาย" (คงนัยตายไว้) |

- ถ้า pun แปลไม่ได้เลย → แปลความหมาย + เก็บ tone ขี้เล่น ยอมเสีย pun ดีกว่าเขียนประโยคไม่เป็นธรรมชาติ

---

## 12. การแปลหน้าจอพิเศษ

| หน้าจอ | ไฟล์ | ข้อควรระวัง |
|---|---|---|
| Pronoun selection | `pronoun selection.rpy` | ปุ่ม She/Her, He/Him, They/Them, Custom — แปล label; ช่อง custom input ให้ผู้เล่นพิมพ์ไทยได้ (Ren'Py input รองรับ Unicode) แต่ค่าที่พิมพ์จะ inject ตรงๆ — เตือนใน QA |
| Character creator | `charactercreator.rpy` | label ปุ่มสั้นๆ |
| Computer/OS UI | `computer.rpy` | จำลอง desktop — ข้อความสั้นมาก, เทคนิค |
| Books | `books.rpy` | เนื้อความยาว fiction ในเกม — แปลภาษาบรรยายเต็มรูป |
| Call messages | `call_messages.rpy` | ข้อความสถานะสาย — สั้น กะทัดรัด |
| Lingo minigame | `lingo.rpy` + `sgb-words.txt` | word list เป็นภาษาอังกฤษ 5 ตัวอักษร — **เก็บเป็นอังกฤษ** (grid เช็คตัวอักษร ไทยมีสระ/วรรณยุกต์จะพัง) แปลเฉพาะคำอธิบาย UI |
| Credits | `credits.rpy` | แปล role descriptions คงชื่อคน |

---

## 13. Glitch / Error / Special Text

- ข้อความระบบจำลองพัง (`WARNING!`, `ERROR!`, `SYSTEM MALFUNCTION!`, `FORCE... RESTART...`) — ใช้ `{font=gui/8bitOperatorPlusSC-Regular.ttf}` + `animated_glitch` transform
- **แปลเนื้อความได้** แต่ต้องคง `{font=...}` tag และใช้ composite font ที่มี glyph ไทยใน style pixel — หรือคง EN ถ้าเป็นส่วนหนึ่งของ aesthetic
- binary/hex/glitch strings ดิบๆ → คงไว้ ไม่แปล

---

## 14. Glossary — คำศัพท์เฉพาะเกม

| EN | TH | หมายเหตุ |
|---|---|---|
| A Date with Death | คงไว้ | ชื่อเกม |
| Grim Reaper | ยมทูต / คง "Grim Reaper" | ชื่อ default ของ GR — แนะนำ "ยมทูต" เพื่อให้ผู้เล่นไทยเข้าใจทันที (JP แปล "Nobody"→"虚" แสดงว่าแปลชื่อได้) |
| Grim | กริม / ยมราช | ชื่อย่อหลัง rename — ทับศัพท์ "กริม" อ่านง่าย |
| Soul#8129 | วิญญาณ#8129 | default player name — JP ใช้ "魂＃8129" ไทยใช้ "วิญญาณ#8129" |
| Nobody | ว่างเปล่า / ไม่มีใคร | สถานะแชท — JP ใช้ "虚" |
| reaper / reaping | ยมทูต / เก็บเกี่ยววิญญาณ | คำทั่วไปแปลได้ |
| soul | วิญญาณ | |
| afterlife | ชาติหน้า / โลกหลังความตาย | เลือกตามบริบท — ให้ consistent |
| Day (N) | วันที่ N | |
| Beyond the Bet | คงไว้ | ชื่อ DLC |
| Casper | คงไว้ | ตุ๊กตา/reference (casperplush) |
| streamer mode | โหมดสตรีมเมอร์ | |
| soulbaby | เบบี๋วิญญาณ / ลูกวิญญาณ | ending name (DLC) — แปลให้น่ารัก |
| NSFW patch | แพตช์ NSFW | |

---

## 15. Quality Assurance Checklist

- [ ] ทุก tag `{...}` ครบ ไม่หาย ไม่เพิ่ม — โดยเฉพาะ kinetic tags (`bt`, `sc`, `chaos`, `omega`, `swap`)
- [ ] `{omega=...}`/`{swap=...}` parameters ไม่ถูกแปล
- [ ] ทุก variable `[...]` ครบ ไม่แปลชื่อ (`[grim_reaper_name!t]`, `[she]`, `[pretty]`)
- [ ] `{font=...}` text มี glyph ไทยจริง (ทดสอบ ไม่ใช่ `□□□`)
- [ ] Grim ใช้ ข้า/เจ้า + register น่าเกรงขาม consistent ทั้งเกม
- [ ] แปล pronoun variables ครบใน `translate thai strings` (`she/her/her2/girl/woman/wife/pretty/beautiful` + capitalized + custom)
- [ ] ทดสอบ pronoun ทุกแบบ (she/he/they/custom) — ประโยคยังอ่านได้
- [ ] ทดสอบพิมพ์ custom pronoun/ชื่อเป็นภาษาไทย
- [ ] ข้อความไม่ล้น NVL chat bubble
- [ ] Choice format `N. <...>` consistent
- [ ] ไม่มี EN ตกค้าง (ยกเว้นทับศัพท์ตาม glossary)
- [ ] lingo wordle เล่นได้ (คง word list EN)

---

## 16. ข้อยกเว้นเฉพาะเกมนี้

1. **Title Case → register โบราณ** — Grim ใช้ ข้า/เจ้า + โทนสั่งการ แทนการพิมพ์ใหญ่
2. **Pronouns ผ่าน `__()`** — แปลใน `translate thai strings` ได้เลย ไม่ต้อง override Python (ต่างจาก reference ที่ต้อง wrap `refresh_pronouns()`)
3. **Dynamic names** — `grim_reaper_name`, `playername`, `other_reaper_name` ผู้เล่นแก้ได้ ใช้ตัวแปรเท่านั้น คง `!t` flag
4. **Kinetic text tags** — 9 custom tags ห้ามแตะ ระวัง `{omega}`/`{swap}` ที่มี args เป็นตัวแปร
5. **`{font=...}` inline** — font ต้องมี Thai glyph ผ่าน `config.font_replacement_map`
6. **lingo wordle** — `sgb-words.txt` เป็นคำ EN 5 ตัวอักษร คงไว้ (Thai มี combining marks ทำ grid พัง)
7. **Japanese coexistence** — เกมมี `tl/japanese` อยู่แล้ว + `_preferences.language == "japanese"` checks ใน `screens.rpy` กระจายหลายจุด (font PixelMplus12 ฯลฯ) — Thai ต้องเพิ่มเงื่อนไขแยกของตัวเอง ห้ามแตะ branch ญี่ปุ่น
8. **DLC detection** — `persistent.DLC_installed`/`BTBDLC_installed` — ไฟล์ `dlc_end.rpy`/`beyond the bet/` แปลครบถ้าผู้เล่นมี DLC

---

## 17. Workflow

1. Extract `archive.rpa` → เอา `.rpy` มาทำ temp project (Ren'Py SDK **8.2.1** เท่านั้น)
2. `translate thai` สร้าง `game/tl/thai/*.rpy`
3. เขียน `replace_font.rpy` — `config.font_replacement_map` map ทุก font ใน `game/gui/` → composite Noto Sans Thai + fontเดิม (ใช้ script merge จาก reference ได้)
4. แปล `translate thai strings` ก่อน: pronouns, ชื่อ default, UI
5. แปล `common.rpy` (Ren'Py UI) → ทดสอบ UI แสดงผล
6. แปล chapters ตามลำดับ Day 1→7 → endings → books/call_messages → DLC
7. เพิ่มปุ่ม "ไทย" ใน language screen (`language_choose_firstlaunch` + preferences `Text Language` ที่ `screens.rpy` ~line 2129) — ทำผ่านไฟล์ mod ใน `tl/thai/` (replace screen) ไม่แก้ archive
8. PyICU → `game/python-packages` สำหรับตัดบรรทัดไทย
9. QA ตาม checklist (ข้อ 15) — ทีละ day จบก่อนข้าม
10. Pack เป็น `thai_mod.rpa` หรือวาง `tl/thai/` loose ใน `game/`

---

> หมายเหตุ: Guide นี้เฉพาะ *A Date with Death* — เผด็จการ register ของ Grim, pronouns ผ่าน `__()`, และ kinetic tags เป็นเอกลักษณ์เกมนี้ อ้างอิง workflow/เครื่องมือเพิ่มได้จาก `X:\14DaysWithYou-5.5-pc\docs\`

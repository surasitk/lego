#!/usr/bin/env python3
"""Generate schema.sql (Supabase) and figures.json from the canonical dataset."""
import json

BL = "https://img.bricklink.com/ItemImage/MN/0/{}.png"

# name_th, name_en, series, release_date, sort, category, bricklink_id, confidence, emoji
FIGS = [
    ("บัซ ไลต์เยียร์", "Buzz Lightyear", "LEGO Toy Story", "2010", 20100101, "licensed", "toy004", "fair", "🚀"),
    ("วู้ดดี้", "Woody", "LEGO Toy Story", "2010", 20100102, "licensed", "toy003", "sure", "🤠"),
    ("ฟาโรห์", "Pharaoh", "Series 2", "2010", 20100901, "fantasy", "col032", "fair", "🏺"),
    ("แกลดิเอเตอร์", "Gladiator", "Series 5", "2011", 20110901, "fantasy", "col066", "fair", "⚔️"),
    ("ราชาสมุทร", "Ocean King", "Series 7", "พ.ค. 2012", 20120501, "fantasy", "col101", "sure", "🔱"),
    ("ชุดไก่", "Chicken Suit Guy", "Series 9", "ม.ค. 2013", 20130101, "animal", "col135", "sure", "🐔"),
    ("พ่อมด", "Wizard", "Series 12", "2014", 20140101, "fantasy", "col179", "sure", "🧙"),
    ("ชุดฮอตดอก", "Hot Dog Man", "Series 13", "ม.ค. 2015", 20150101, "food", "col208", "sure", "🌭"),
    ("ราชาคลาสสิก", "Classic King", "Series 13", "ม.ค. 2015", 20150102, "fantasy", "col195", "sure", "👑"),
    ("ชุดฉลาม", "Shark Suit Guy", "Series 15", "ม.ค. 2016", 20160101, "animal", "col240", "sure", "🦈"),
    ("อัศวินสยอง", "Frightening Knight", "Series 15", "ม.ค. 2016", 20160102, "fantasy", "col230", "fair", "🛡️"),
    ("ชุดกล้วย", "Banana Guy", "Series 16", "ก.ย. 2016", 20160901, "food", "col258", "sure", "🍌"),
    ("เด็กชุดเพนกวิน", "Penguin Boy", "Series 16", "ก.ย. 2016", 20160902, "animal", "col253", "fair", "🐧"),
    ("แบทแมน", "Batman", "The LEGO Batman Movie", "2017", 20170101, "licensed", None, "guess", "🦇"),
    ("ชุดข้าวโพด", "Corn Cob Guy", "Series 17", "พ.ค. 2017", 20170501, "food", "col289", "sure", "🌽"),
    ("ชุดมังกรแดง", "Dragon Suit Guy", "Series 18", "เม.ย. 2018", 20180401, "fantasy", "col318", "sure", "🐉"),
    ("ชุดพลุ (BANG)", "Firework Guy", "Series 18", "เม.ย. 2018", 20180402, "fantasy", "col316", "sure", "🎆"),
    ("ชุดกระบองเพชร", "Cactus Girl", "Series 18", "เม.ย. 2018", 20180403, "food", "col322", "sure", "🌵"),
    ("ชุดยีราฟ", "Giraffe Guy", "The LEGO Movie 2", "ก.พ. 2019", 20190201, "animal", "tlm151", "sure", "🦒"),
    ("ชุดสีเทียน", "Crayon Girl", "The LEGO Movie 2", "ก.พ. 2019", 20190202, "craft", "tlm152", "sure", "🖍️"),
    ("ชุดแตงโม", "Watermelon Dude", "The LEGO Movie 2", "ก.พ. 2019", 20190203, "food", "tlm155", "sure", "🍉"),
    ("ชุดพิซซ่า", "Pizza Costume Guy", "Series 19", "ก.ย. 2019", 20190901, "food", "col351", "sure", "🍕"),
    ("ชุดถั่วลันเตา", "Peapod Costume Girl", "Series 20", "2020", 20200101, "food", "col360", "sure", "🫛"),
    ("ชุดลามา", "Llama Costume Girl", "Series 20", "2020", 20200102, "animal", "col364", "sure", "🦙"),
    ("ชุดไก่งวง", "Turkey Costume", "Series 23", "ก.ย. 2022", 20220901, "animal", "col406", "sure", "🦃"),
    ("ชุดมังกรเขียว", "Green Dragon Costume", "Series 23", "ก.ย. 2022", 20220902, "fantasy", "col409", "sure", "🐲"),
    ("ชุดป๊อปคอร์น", "Popcorn Costume", "Series 23", "ก.ย. 2022", 20220903, "food", "col404", "sure", "🍿"),
    ("ชุดนกยูง", "Peacock Costume", "Series 28", "ม.ค. 2026", 20260101, "animal", "col461", "sure", "🦚"),
]

# Unidentified / needs close-up. name_th(desc), guess(note), emoji
UNSURE = [
    ("ชุดลูกเจี๊ยบ/ปลาทอง (เหลือง)", "อาจเป็น Goldfish/Chick — เทียบ Series 28 (2026)", "🐥"),
    ("เงือกชาย (อกทอง หางเข้ม)", "ยังระบุซีรีส์ไม่ได้ — อาจเป็นไลน์ Atlantis/คัสตอม", "🧜"),
    ("อัศวิน/ราชาน้ำเงิน (โล่ลายม้า)", "น่าจะไลน์ Castle — ต้องดูตราโล่ใกล้ๆ", "🐴"),
    ("ตัวดำหัวเปลวไฟ นั่งบนสัตว์ดำ", "เดาว่าธีมไฟ/Ninjago หรือคัสตอม", "🔥"),
    ("นักรบนก/อินทรี (แขนขนนก)", "อาจเป็นไลน์ Chima หรือชุดนก", "🦅"),
    ("สาวชุดสตรอว์เบอร์รี + ลูกอมแท่ง", "ดูเป็นธีมหวาน/เทศกาล — ยังไม่พบรุ่นตรง", "🍓"),
    ("ชายปกแหลมน้ำตาล มีหนวด", "คล้ายชุดสิงโต/มนุษย์หมาป่า — ไม่ชัด", "🦁"),
    ("ชายชุดทักซิโด้ผูกโบว์", "อาจเป็น Magician (Series 1) หรือเจ้าบ่าว/นักธุรกิจ", "🎩"),
    ("นักธุรกิจถือแซกโซโฟนทอง", "คล้าย Saxophone Player แต่ชุดต่าง — ไม่ชัด", "🎷"),
    ("ชายหัวล้าน เสื้อกล้ามดำ", "ดูเป็นลูกน้อง/วายร้ายจากเซ็ต — ไม่ชัด", "👤"),
    ("ชายผมบลอนด์ชุดขาวล้วน", "อาจเป็นนักกีฬา/เจ้าบ่าว/ตัวเฉพาะเซ็ต", "🤍"),
]

rows = []
for n_th, n_en, series, date, sort, cat, bl, conf, emoji in FIGS:
    rows.append({
        "name_th": n_th, "name_en": n_en, "series": series, "release_date": date,
        "release_sort": sort, "category": cat, "bricklink_id": bl,
        "image_url": BL.format(bl) if bl else None,
        "confidence": conf, "emoji": emoji, "identified": True, "note": None,
    })
for desc, guess, emoji in UNSURE:
    rows.append({
        "name_th": desc, "name_en": None, "series": None, "release_date": None,
        "release_sort": 99990000, "category": None, "bricklink_id": None,
        "image_url": None, "confidence": "guess", "emoji": emoji,
        "identified": False, "note": guess,
    })

# --- figures.json (fallback data for the app) ---
with open("figures.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

# --- schema.sql ---
def sql_str(v):
    if v is None:
        return "NULL"
    return "'" + str(v).replace("'", "''") + "'"

lines = []
lines.append("-- LEGO Minifigures collection — Supabase schema + seed")
lines.append("-- Run this in the Supabase SQL Editor.\n")
lines.append("create table if not exists public.minifigures (")
lines.append("  id            bigserial primary key,")
lines.append("  name_th       text not null,")
lines.append("  name_en       text,")
lines.append("  series        text,")
lines.append("  release_date  text,")
lines.append("  release_sort  integer not null default 99990000,")
lines.append("  category      text,")
lines.append("  bricklink_id  text,")
lines.append("  image_url     text,")
lines.append("  confidence    text,")
lines.append("  emoji         text,")
lines.append("  identified    boolean not null default true,")
lines.append("  note          text,")
lines.append("  created_at    timestamptz not null default now()")
lines.append(");\n")
lines.append("alter table public.minifigures enable row level security;\n")
lines.append("drop policy if exists \"public read\" on public.minifigures;")
lines.append("create policy \"public read\" on public.minifigures for select to anon, authenticated using (true);\n")
lines.append("truncate table public.minifigures restart identity;\n")
cols = "name_th, name_en, series, release_date, release_sort, category, bricklink_id, image_url, confidence, emoji, identified, note"
lines.append(f"insert into public.minifigures ({cols}) values")
vals = []
for r in rows:
    vals.append("  (" + ", ".join([
        sql_str(r["name_th"]), sql_str(r["name_en"]), sql_str(r["series"]),
        sql_str(r["release_date"]), str(r["release_sort"]), sql_str(r["category"]),
        sql_str(r["bricklink_id"]), sql_str(r["image_url"]), sql_str(r["confidence"]),
        sql_str(r["emoji"]), "true" if r["identified"] else "false", sql_str(r["note"]),
    ]) + ")")
lines.append(",\n".join(vals) + ";")
with open("schema.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Wrote figures.json ({len(rows)} rows) and schema.sql")
print(f"Identified: {sum(1 for r in rows if r['identified'])}, Unidentified: {sum(1 for r in rows if not r['identified'])}")

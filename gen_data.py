#!/usr/bin/env python3
"""Generate schema.sql (Supabase) and figures.json from the canonical dataset."""
import json

BL = "https://qmmopgyevfuztpqaynww.supabase.co/storage/v1/object/public/minifigs/{}.png"

# dict keys: th, en, series, set_no, date, sort, cat, bl, conf, emoji
FIGS = [
    dict(th="บัซ ไลต์เยียร์", en="Buzz Lightyear", series="LEGO Toy Story", set_no=None, date="2010", sort=20100101, cat="licensed", bl="toy004", conf="fair", emoji="🚀"),
    dict(th="วู้ดดี้", en="Woody", series="LEGO Toy Story", set_no=None, date="2010", sort=20100102, cat="licensed", bl="toy003", conf="sure", emoji="🤠"),
    dict(th="ฟาโรห์", en="Pharaoh", series="Series 2", set_no="8684", date="2010", sort=20100901, cat="fantasy", bl="col032", conf="fair", emoji="🏺"),
    dict(th="ราชาสมุทร / โพไซดอน", en="Ocean King (Poseidon)", series="Series 7", set_no="8831", date="May 2012", sort=20120501, cat="fantasy", bl="col101", conf="sure", emoji="🔱"),
    dict(th="ชุดไก่", en="Chicken Suit Guy", series="Series 9", set_no="71000", date="Jan 2013", sort=20130101, cat="animal", bl="col135", conf="sure", emoji="🐔"),
    dict(th="พ่อมด", en="Wizard", series="Series 12", set_no="71007", date="2014", sort=20140101, cat="fantasy", bl="col179", conf="sure", emoji="🧙"),
    dict(th="ชุดฮอตดอก", en="Hot Dog Man", series="Series 13", set_no="71008", date="Jan 2015", sort=20150101, cat="food", bl="col208", conf="sure", emoji="🌭"),
    dict(th="ราชาคลาสสิก", en="Classic King", series="Series 13", set_no="71008", date="Jan 2015", sort=20150102, cat="fantasy", bl="col195", conf="sure", emoji="👑"),
    dict(th="ชุดฉลาม", en="Shark Suit Guy", series="Series 15", set_no="71011", date="Jan 2016", sort=20160101, cat="animal", bl="col240", conf="sure", emoji="🦈"),
    dict(th="ชุดกล้วย", en="Banana Guy", series="Series 16", set_no="71013", date="Sep 2016", sort=20160901, cat="food", bl="col258", conf="sure", emoji="🍌"),
    dict(th="เด็กชุดเพนกวิน", en="Penguin Boy", series="Series 16", set_no="71013", date="Sep 2016", sort=20160902, cat="animal", bl="col253", conf="fair", emoji="🐧"),
    dict(th="แบทแมน (Batman Returns 1992)", en="Batman — Batman Returns 1992", series="DC Super Heroes", set_no="30653", date="1992 (LEGO 2023)", sort=20230101, cat="licensed", bl="sh0880", conf="sure", emoji="🦇"),
    dict(th="แคทแมน", en="Catman", series="The LEGO Batman Movie Series 1", set_no="71017", date="2017", sort=20170201, cat="licensed", bl="coltlbm16", conf="sure", emoji="🐱"),
    dict(th="เฮดีส", en="Hades", series="Disney Series 2", set_no="71024", date="2019", sort=20190210, cat="licensed", bl="dis036", conf="sure", emoji="🔥"),
    dict(th="เพรซิเดนต์ บิสเนส", en="President Business", series="The LEGO Movie Series 1", set_no="71004", date="2014", sort=20140110, cat="licensed", bl="tlm002", conf="sure", emoji="🎷"),
    dict(th="เจมส์ บอนด์ 007", en="James Bond (007)", series="Speed Champions", set_no="76911", date="2022", sort=20220110, cat="licensed", bl="sc102", conf="sure", emoji="🎩"),
    dict(th="โดมินิค โทเร็ตโต้", en="Dominic Toretto", series="Speed Champions", set_no="76912", date="2022", sort=20220120, cat="licensed", bl="sc103", conf="sure", emoji="👤"),
    dict(th="ไบรอัน โอคอนเนอร์", en="Brian O'Conner", series="Speed Champions", set_no="76917", date="2023", sort=20230110, cat="licensed", bl="sc104", conf="sure", emoji="🤍"),
    dict(th="ชุดข้าวโพด", en="Corn Cob Guy", series="Series 17", set_no="71018", date="May 2017", sort=20170501, cat="food", bl="col289", conf="sure", emoji="🌽"),
    dict(th="ชุดมังกรแดง", en="Dragon Suit Guy", series="Series 18", set_no="71021", date="Apr 2018", sort=20180401, cat="fantasy", bl="col318", conf="sure", emoji="🐉"),
    dict(th="ชุดพลุ (BANG)", en="Firework Guy", series="Series 18", set_no="71021", date="Apr 2018", sort=20180402, cat="fantasy", bl="col316", conf="sure", emoji="🎆"),
    dict(th="ชุดกระบองเพชร", en="Cactus Girl", series="Series 18", set_no="71021", date="Apr 2018", sort=20180403, cat="food", bl="col322", conf="sure", emoji="🌵"),
    dict(th="ชุดยีราฟ", en="Giraffe Guy", series="The LEGO Movie 2", set_no="71023", date="Feb 2019", sort=20190201, cat="animal", bl="tlm151", conf="sure", emoji="🦒"),
    dict(th="ชุดสีเทียน", en="Crayon Girl", series="The LEGO Movie 2", set_no="71023", date="Feb 2019", sort=20190202, cat="craft", bl="tlm152", conf="sure", emoji="🖍️"),
    dict(th="ชุดแตงโม", en="Watermelon Dude", series="The LEGO Movie 2", set_no="71023", date="Feb 2019", sort=20190203, cat="food", bl="tlm155", conf="sure", emoji="🍉"),
    dict(th="ชุดพิซซ่า", en="Pizza Costume Guy", series="Series 19", set_no="71025", date="Sep 2019", sort=20190901, cat="food", bl="col351", conf="sure", emoji="🍕"),
    dict(th="ชุดถั่วลันเตา", en="Peapod Costume Girl", series="Series 20", set_no="71027", date="2020", sort=20200101, cat="food", bl="col360", conf="sure", emoji="🫛"),
    dict(th="ชุดลามา", en="Llama Costume Girl", series="Series 20", set_no="71027", date="2020", sort=20200102, cat="animal", bl="col364", conf="sure", emoji="🦙"),
    dict(th="เด็กชุดไก่ (ส้ม)", en="Chicken Suit Boy", series="Build-A-Minifigure", set_no="BAM 2022", date="2022", sort=20220101, cat="animal", bl="hol299", conf="sure", emoji="🐥"),
    dict(th="ชุดไก่งวง", en="Turkey Costume", series="Series 23", set_no="71034", date="Sep 2022", sort=20220901, cat="animal", bl="col406", conf="sure", emoji="🦃"),
    dict(th="ชุดมังกรเขียว", en="Green Dragon Costume", series="Series 23", set_no="71034", date="Sep 2022", sort=20220902, cat="fantasy", bl="col409", conf="sure", emoji="🐲"),
    dict(th="ชุดป๊อปคอร์น", en="Popcorn Costume", series="Series 23", set_no="71034", date="Sep 2022", sort=20220903, cat="food", bl="col404", conf="sure", emoji="🍿"),
    dict(th="อัศวินแวมไพร์", en="Vampire Knight", series="Series 25", set_no="71045", date="2024", sort=20240101, cat="fantasy", bl="col426", conf="sure", emoji="🧛"),
    dict(th="ราชาอัศวินม้า", en="Horse Knight King", series="Castle (set 31168)", set_no="31168", date="2025", sort=20250801, cat="fantasy", bl="cas592", conf="sure", emoji="🐎"),
    dict(th="แบทแมนเงือก", en="Mermaid Batman", series="The LEGO Batman Movie Series 2", set_no="71020", date="2018", sort=20180105, cat="licensed", bl="coltlbm29", conf="sure", emoji="🧜"),
    dict(th="สาวชุดสตรอว์เบอร์รีเค้ก", en="Strawberry Shortcake Girl", series="Build-A-Minifigure", set_no="BAM 2023", date="2023", sort=20230601, cat="food", bl="hol355x", img="https://qmmopgyevfuztpqaynww.supabase.co/storage/v1/object/public/minifigs/strawberry.jpg", conf="sure", emoji="🍓"),
    dict(th="เฮอร์คิวลิส", en="Hercules", series="Disney Series 2", set_no="71024", date="2019", sort=20190215, cat="licensed", bl="dis037", conf="sure", emoji="🏛️"),
    dict(th="ชุดสีเทียนม่วงแดง", en="Magenta Crayon Costume Guy", series="Build-A-Minifigure", set_no="BAM 2023", date="2023", sort=20230610, cat="craft", bl=None, img="https://qmmopgyevfuztpqaynww.supabase.co/storage/v1/object/public/minifigs/magenta-crayon.webp", conf="sure", emoji="🖍️"),
    dict(th="นายกฯ ชุดข้าวโพด (Solomon Fleck)", en="Mayor Solomon Fleck (Corn Cob)", series="LEGO City", set_no="cty1222", date="2020", sort=20200601, cat="food", bl="cty1222", conf="sure", emoji="🌽"),
    dict(th="ชุดเค้ก/พาย", en="Cake / Pie Costume Guy", series="Build-A-Minifigure", set_no="BAM 2022", date="2022", sort=20220115, cat="food", bl="hol296", conf="sure", emoji="🥧"),
    dict(th="ปาร์ตี้ บานาน่า", en="Party Banana Guy", series="Party Banana Juice Bar", set_no="5005250", date="2018", sort=20181001, cat="food", bl="col330", conf="sure", emoji="🍌"),
    dict(th="ราชินีอียิปต์", en="Egyptian Queen", series="Series 5", set_no="8805", date="2011", sort=20110902, cat="myth", bl="col078", conf="sure", emoji="🐍"),
    dict(th="ราชินี", en="Queen", series="Series 15", set_no="71011", date="Jan 2016", sort=20160103, cat="castle", bl="col243", conf="sure", emoji="👸"),
    dict(th="กัปตันโจรสลัด (Redbeard)", en="Pirate Captain (Redbeard)", series="Pirates", set_no=None, date="1989", sort=19890101, cat="pirate", bl="pi055", conf="sure", emoji="🏴‍☠️"),
    dict(th="ทหารอิมพีเรียล (Bluecoat)", en="Imperial Soldier", series="Pirates", set_no=None, date="1996", sort=19960101, cat="pirate", bl="pi061", conf="sure", emoji="🪖"),
    dict(th="ชุดนกยูง", en="Peacock Costume", series="Series 28", set_no="71051", date="Jan 2026", sort=20260101, cat="animal", bl="col461", conf="sure", emoji="🦚"),
]

# Unidentified / needs close-up. th(desc), note, emoji
UNSURE = []

rows = []
for f in FIGS:
    rows.append({
        "name_th": f["th"], "name_en": f["en"], "series": f["series"], "set_no": f["set_no"],
        "release_date": f["date"], "release_sort": f["sort"], "category": f["cat"],
        "bricklink_id": f["bl"], "image_url": (f["img"] if "img" in f else (BL.format(f["bl"]) if f["bl"] else None)),
        "confidence": f["conf"], "emoji": f["emoji"], "identified": True, "note": None,
    })
for desc, guess, emoji in UNSURE:
    rows.append({
        "name_th": desc, "name_en": None, "series": None, "set_no": None,
        "release_date": None, "release_sort": 99990000, "category": None,
        "bricklink_id": None, "image_url": None, "confidence": "guess",
        "emoji": emoji, "identified": False, "note": guess,
    })

# --- Category remap (content-based, grounded in LEGO theme structure) ---
CATMAP = {
    "animal": ["Chicken Suit Guy","Penguin Boy","Shark Suit Guy","Giraffe Guy","Llama Costume Girl","Turkey Costume","Chicken Suit Boy","Peacock Costume"],
    "food":   ["Banana Guy","Hot Dog Man","Corn Cob Guy","Cactus Girl","Watermelon Dude","Pizza Costume Guy","Peapod Costume Girl","Popcorn Costume","Strawberry Shortcake Girl","Cake / Pie Costume Guy","Party Banana Guy","Mayor Solomon Fleck (Corn Cob)"],
    "castle": ["Classic King","Horse Knight King","Vampire Knight"],
    "myth":   ["Pharaoh","Wizard","Ocean King (Poseidon)","Hercules","Hades","Dragon Suit Guy","Green Dragon Costume"],
    "pop":    ["Buzz Lightyear","Woody","Batman — Batman Returns 1992","Catman","Mermaid Batman","James Bond (007)","Dominic Toretto","Brian O'Conner","President Business"],
    "other":  ["Firework Guy","Crayon Girl","Magenta Crayon Costume Guy"],
}
_n2c = {n: c for c, ns in CATMAP.items() for n in ns}
for r in rows:
    if r["name_en"] in _n2c:
        r["category"] = _n2c[r["name_en"]]

# --- History & Inspiration (shown in the popup) ---
HIST = {
 "Buzz Lightyear": ("Part of the LEGO Toy Story line (2010), released alongside the Toy Story 3 sets.", "Buzz Lightyear, the Space Ranger action figure from Pixar's Toy Story."),
 "Woody": ("Released in 2010 with LEGO's Toy Story theme.", "Sheriff Woody, the pull-string cowboy doll and Andy's favourite toy."),
 "Pharaoh": ("Collectible Minifigures Series 2 (2010), an early CMF wave.", "An ancient Egyptian pharaoh in golden ceremonial regalia."),
 "Ocean King (Poseidon)": ("Collectible Minifigures Series 7 (2012).", "A merman sea-king echoing Poseidon/Neptune, ruler of the oceans."),
 "Chicken Suit Guy": ("CMF Series 9 (set 71000, 2013); one of LEGO's most beloved costume figures.", "A super-fan wearing a full chicken mascot suit."),
 "Wizard": ("CMF Series 12 (71007, 2014).", "A classic fantasy wizard with a star-and-moon robe and crystal staff."),
 "Hot Dog Man": ("CMF Series 13 (71008, 2015); an instant collector favourite.", "A cheerful man dressed as a hot dog in a bun."),
 "Classic King": ("CMF Series 13 (71008, 2015).", "A medieval king with golden crown and ermine cape, nodding to LEGO Castle."),
 "Shark Suit Guy": ("CMF Series 15 (71011, 2016).", "A goofy guy poking out of a foam shark costume."),
 "Banana Guy": ("CMF Series 16 (71013, 2016).", "A man in a giant banana suit."),
 "Penguin Boy": ("CMF Series 16 (71013, 2016).", "A child bundled up in a penguin costume."),
 "Batman — Batman Returns 1992": ("LEGO DC polybag 30653 (2023), a tribute build.", "Michael Keaton's Batman from Tim Burton's 1992 film Batman Returns."),
 "Catman": ("The LEGO Batman Movie CMF Series 1 (71017, 2017).", "Catman, a campy clawed DC villain spoofed in the movie."),
 "Hades": ("LEGO Disney CMF Series 2 (71024, 2019).", "Hades, the blue-flamed lord of the Underworld from Disney's Hercules."),
 "President Business": ("The LEGO Movie CMF Series (71004, 2014).", "Lord/President Business, the order-obsessed villain of The LEGO Movie."),
 "James Bond (007)": ("LEGO Speed Champions 007 Aston Martin DB5 (76911, 2022).", "James Bond (Daniel Craig) in his tuxedo, from No Time to Die."),
 "Dominic Toretto": ("Speed Champions 1970 Dodge Charger R/T (76912, 2022).", "Dom Toretto, the family-first street racer of Fast & Furious."),
 "Brian O'Conner": ("Speed Champions 2 Fast 2 Furious Nissan Skyline GT-R (76917, 2023).", "Brian O'Conner, ex-cop turned racer in the Fast & Furious saga."),
 "Corn Cob Guy": ("CMF Series 17 (71018, 2017).", "A man dressed as an ear of corn on the cob."),
 "Dragon Suit Guy": ("CMF Series 18 (71021, 2018), the 40th-anniversary 'party' wave.", "A festive dragon costume."),
 "Firework Guy": ("CMF Series 18 (71021, 2018).", "A 'BANG!' firework-rocket costume for celebrations."),
 "Cactus Girl": ("CMF Series 18 (71021, 2018).", "A prickly cactus costume."),
 "Giraffe Guy": ("The LEGO Movie 2 CMF (71023, 2019).", "A tall giraffe onesie costume."),
 "Crayon Girl": ("The LEGO Movie 2 CMF (71023, 2019).", "A colourful crayon costume."),
 "Watermelon Dude": ("The LEGO Movie 2 CMF (71023, 2019).", "A juicy watermelon-slice costume."),
 "Pizza Costume Guy": ("CMF Series 19 (71025, 2019).", "A man dressed as a slice of pizza."),
 "Peapod Costume Girl": ("CMF Series 20 (71027, 2020).", "A girl tucked inside a pea-pod costume."),
 "Llama Costume Girl": ("CMF Series 20 (71027, 2020).", "A fluffy llama costume."),
 "Chicken Suit Boy": ("LEGO Build-A-Minifigure (BAM) station exclusive, 2022.", "A kid in a bright orange chick/chicken suit."),
 "Turkey Costume": ("CMF Series 23 (71034, 2022).", "A Thanksgiving turkey costume."),
 "Green Dragon Costume": ("CMF Series 23 (71034, 2022).", "A green dragon costume, companion to earlier dragon suits."),
 "Popcorn Costume": ("CMF Series 23 (71034, 2022).", "A movie-night popcorn-bucket costume."),
 "Vampire Knight": ("CMF Series 25 (71045, 2024).", "A vampiric knight with bat-wing helm, bat shield and axe."),
 "Horse Knight King": ("LEGO Creator 3-in-1 Medieval Horse Knight Castle (31168, 2025).", "King of the new Horse Knights faction, reviving the Castle theme."),
 "Mermaid Batman": ("The LEGO Batman Movie CMF Series 2 (71020, 2018).", "A gag 'merman' Batman from the movie's wacky costume line-up."),
 "Strawberry Shortcake Girl": ("LEGO Build-A-Minifigure exclusive, 2023.", "A girl in a strawberry-shortcake slice costume with tie-dye shirt."),
 "Hercules": ("LEGO Disney CMF Series 2 (71024, 2019).", "Hercules, the demigod hero of Disney's Hercules."),
 "Magenta Crayon Costume Guy": ("LEGO Build-A-Minifigure exclusive, 2023.", "A bright magenta crayon costume."),
 "Mayor Solomon Fleck (Corn Cob)": ("LEGO Hidden Side / City figure (cty1222).", "Mayor Solomon Fleck in a corn-cob mascot suit from Hidden Side's town of Newbury."),
 "Cake / Pie Costume Guy": ("LEGO Build-A-Minifigure exclusive, 2022.", "A sweet slice-of-cake / pie costume."),
 "Party Banana Guy": ("Party Banana Juice Bar promo set (5005250, 2018).", "A dancing banana-suit guy with a boombox."),
 "Egyptian Queen": ("CMF Series 5 (set 8805, 2011).", "An Egyptian queen in the spirit of Cleopatra, complete with a pet snake."),
 "Queen": ("CMF Series 15 (71011, 2016).", "A regal castle queen with crown and ermine-trimmed cape."),
 "Pirate Captain (Redbeard)": ("A classic LEGO Pirates captain, from the original 1989 Pirates theme.", "A swashbuckling pirate captain with skull-and-crossbones hat, hook hand and peg leg."),
 "Imperial Soldier": ("LEGO Pirates 'Bluecoats' Imperial Soldiers faction (mid-1990s).", "A Napoleonic-style naval soldier who pursued LEGO's pirates."),
 "Peacock Costume": ("CMF Series 28 (71051, 2026), the latest wave.", "A proud peacock costume with a fanned tail of feathers."),
}
for r in rows:
    _h = HIST.get(r["name_en"])
    r["history"] = _h[0] if _h else None
    r["inspiration"] = _h[1] if _h else None

with open("figures.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

def sql_str(v):
    return "NULL" if v is None else "'" + str(v).replace("'", "''") + "'"

L = []
L.append("-- LEGO Minifigures collection — Supabase schema + seed")
L.append("create table if not exists public.minifigures (")
L.append("  id bigserial primary key, name_th text not null, name_en text, series text,")
L.append("  set_no text, release_date text, release_sort integer not null default 99990000,")
L.append("  category text, bricklink_id text, image_url text, confidence text, emoji text,")
L.append("  identified boolean not null default true, note text, history text, inspiration text, created_at timestamptz not null default now()")
L.append(");")
L.append("alter table public.minifigures add column if not exists set_no text;")
L.append("alter table public.minifigures add column if not exists history text;")
L.append("alter table public.minifigures add column if not exists inspiration text;")
L.append("alter table public.minifigures enable row level security;")
L.append('drop policy if exists "public read" on public.minifigures;')
L.append('create policy "public read" on public.minifigures for select to anon, authenticated using (true);')
L.append("truncate table public.minifigures restart identity;")
cols = "name_th, name_en, series, set_no, release_date, release_sort, category, bricklink_id, image_url, confidence, emoji, identified, note, history, inspiration"
L.append(f"insert into public.minifigures ({cols}) values")
vals = []
for r in rows:
    vals.append("  (" + ", ".join([
        sql_str(r["name_th"]), sql_str(r["name_en"]), sql_str(r["series"]), sql_str(r["set_no"]),
        sql_str(r["release_date"]), str(r["release_sort"]), sql_str(r["category"]),
        sql_str(r["bricklink_id"]), sql_str(r["image_url"]), sql_str(r["confidence"]),
        sql_str(r["emoji"]), "true" if r["identified"] else "false", sql_str(r["note"]),
        sql_str(r.get("history")), sql_str(r.get("inspiration")),
    ]) + ")")
L.append(",\n".join(vals) + ";")
with open("schema.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")

print(f"rows={len(rows)} identified={sum(1 for r in rows if r['identified'])} unsure={sum(1 for r in rows if not r['identified'])}")

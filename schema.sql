-- LEGO Minifigures collection — Supabase schema + seed
-- Run this in the Supabase SQL Editor.

create table if not exists public.minifigures (
  id            bigserial primary key,
  name_th       text not null,
  name_en       text,
  series        text,
  release_date  text,
  release_sort  integer not null default 99990000,
  category      text,
  bricklink_id  text,
  image_url     text,
  confidence    text,
  emoji         text,
  identified    boolean not null default true,
  note          text,
  created_at    timestamptz not null default now()
);

alter table public.minifigures enable row level security;

drop policy if exists "public read" on public.minifigures;
create policy "public read" on public.minifigures for select to anon, authenticated using (true);

truncate table public.minifigures restart identity;

insert into public.minifigures (name_th, name_en, series, release_date, release_sort, category, bricklink_id, image_url, confidence, emoji, identified, note) values
  ('บัซ ไลต์เยียร์', 'Buzz Lightyear', 'LEGO Toy Story', '2010', 20100101, 'licensed', 'toy004', 'https://img.bricklink.com/ItemImage/MN/0/toy004.png', 'fair', '🚀', true, NULL),
  ('วู้ดดี้', 'Woody', 'LEGO Toy Story', '2010', 20100102, 'licensed', 'toy003', 'https://img.bricklink.com/ItemImage/MN/0/toy003.png', 'sure', '🤠', true, NULL),
  ('ฟาโรห์', 'Pharaoh', 'Series 2', '2010', 20100901, 'fantasy', 'col032', 'https://img.bricklink.com/ItemImage/MN/0/col032.png', 'fair', '🏺', true, NULL),
  ('แกลดิเอเตอร์', 'Gladiator', 'Series 5', '2011', 20110901, 'fantasy', 'col066', 'https://img.bricklink.com/ItemImage/MN/0/col066.png', 'fair', '⚔️', true, NULL),
  ('ราชาสมุทร', 'Ocean King', 'Series 7', 'พ.ค. 2012', 20120501, 'fantasy', 'col101', 'https://img.bricklink.com/ItemImage/MN/0/col101.png', 'sure', '🔱', true, NULL),
  ('ชุดไก่', 'Chicken Suit Guy', 'Series 9', 'ม.ค. 2013', 20130101, 'animal', 'col135', 'https://img.bricklink.com/ItemImage/MN/0/col135.png', 'sure', '🐔', true, NULL),
  ('พ่อมด', 'Wizard', 'Series 12', '2014', 20140101, 'fantasy', 'col179', 'https://img.bricklink.com/ItemImage/MN/0/col179.png', 'sure', '🧙', true, NULL),
  ('ชุดฮอตดอก', 'Hot Dog Man', 'Series 13', 'ม.ค. 2015', 20150101, 'food', 'col208', 'https://img.bricklink.com/ItemImage/MN/0/col208.png', 'sure', '🌭', true, NULL),
  ('ราชาคลาสสิก', 'Classic King', 'Series 13', 'ม.ค. 2015', 20150102, 'fantasy', 'col195', 'https://img.bricklink.com/ItemImage/MN/0/col195.png', 'sure', '👑', true, NULL),
  ('ชุดฉลาม', 'Shark Suit Guy', 'Series 15', 'ม.ค. 2016', 20160101, 'animal', 'col240', 'https://img.bricklink.com/ItemImage/MN/0/col240.png', 'sure', '🦈', true, NULL),
  ('อัศวินสยอง', 'Frightening Knight', 'Series 15', 'ม.ค. 2016', 20160102, 'fantasy', 'col230', 'https://img.bricklink.com/ItemImage/MN/0/col230.png', 'fair', '🛡️', true, NULL),
  ('ชุดกล้วย', 'Banana Guy', 'Series 16', 'ก.ย. 2016', 20160901, 'food', 'col258', 'https://img.bricklink.com/ItemImage/MN/0/col258.png', 'sure', '🍌', true, NULL),
  ('เด็กชุดเพนกวิน', 'Penguin Boy', 'Series 16', 'ก.ย. 2016', 20160902, 'animal', 'col253', 'https://img.bricklink.com/ItemImage/MN/0/col253.png', 'fair', '🐧', true, NULL),
  ('แบทแมน', 'Batman', 'The LEGO Batman Movie', '2017', 20170101, 'licensed', NULL, NULL, 'guess', '🦇', true, NULL),
  ('ชุดข้าวโพด', 'Corn Cob Guy', 'Series 17', 'พ.ค. 2017', 20170501, 'food', 'col289', 'https://img.bricklink.com/ItemImage/MN/0/col289.png', 'sure', '🌽', true, NULL),
  ('ชุดมังกรแดง', 'Dragon Suit Guy', 'Series 18', 'เม.ย. 2018', 20180401, 'fantasy', 'col318', 'https://img.bricklink.com/ItemImage/MN/0/col318.png', 'sure', '🐉', true, NULL),
  ('ชุดพลุ (BANG)', 'Firework Guy', 'Series 18', 'เม.ย. 2018', 20180402, 'fantasy', 'col316', 'https://img.bricklink.com/ItemImage/MN/0/col316.png', 'sure', '🎆', true, NULL),
  ('ชุดกระบองเพชร', 'Cactus Girl', 'Series 18', 'เม.ย. 2018', 20180403, 'food', 'col322', 'https://img.bricklink.com/ItemImage/MN/0/col322.png', 'sure', '🌵', true, NULL),
  ('ชุดยีราฟ', 'Giraffe Guy', 'The LEGO Movie 2', 'ก.พ. 2019', 20190201, 'animal', 'tlm151', 'https://img.bricklink.com/ItemImage/MN/0/tlm151.png', 'sure', '🦒', true, NULL),
  ('ชุดสีเทียน', 'Crayon Girl', 'The LEGO Movie 2', 'ก.พ. 2019', 20190202, 'craft', 'tlm152', 'https://img.bricklink.com/ItemImage/MN/0/tlm152.png', 'sure', '🖍️', true, NULL),
  ('ชุดแตงโม', 'Watermelon Dude', 'The LEGO Movie 2', 'ก.พ. 2019', 20190203, 'food', 'tlm155', 'https://img.bricklink.com/ItemImage/MN/0/tlm155.png', 'sure', '🍉', true, NULL),
  ('ชุดพิซซ่า', 'Pizza Costume Guy', 'Series 19', 'ก.ย. 2019', 20190901, 'food', 'col351', 'https://img.bricklink.com/ItemImage/MN/0/col351.png', 'sure', '🍕', true, NULL),
  ('ชุดถั่วลันเตา', 'Peapod Costume Girl', 'Series 20', '2020', 20200101, 'food', 'col360', 'https://img.bricklink.com/ItemImage/MN/0/col360.png', 'sure', '🫛', true, NULL),
  ('ชุดลามา', 'Llama Costume Girl', 'Series 20', '2020', 20200102, 'animal', 'col364', 'https://img.bricklink.com/ItemImage/MN/0/col364.png', 'sure', '🦙', true, NULL),
  ('ชุดไก่งวง', 'Turkey Costume', 'Series 23', 'ก.ย. 2022', 20220901, 'animal', 'col406', 'https://img.bricklink.com/ItemImage/MN/0/col406.png', 'sure', '🦃', true, NULL),
  ('ชุดมังกรเขียว', 'Green Dragon Costume', 'Series 23', 'ก.ย. 2022', 20220902, 'fantasy', 'col409', 'https://img.bricklink.com/ItemImage/MN/0/col409.png', 'sure', '🐲', true, NULL),
  ('ชุดป๊อปคอร์น', 'Popcorn Costume', 'Series 23', 'ก.ย. 2022', 20220903, 'food', 'col404', 'https://img.bricklink.com/ItemImage/MN/0/col404.png', 'sure', '🍿', true, NULL),
  ('ชุดนกยูง', 'Peacock Costume', 'Series 28', 'ม.ค. 2026', 20260101, 'animal', 'col461', 'https://img.bricklink.com/ItemImage/MN/0/col461.png', 'sure', '🦚', true, NULL),
  ('ชุดลูกเจี๊ยบ/ปลาทอง (เหลือง)', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🐥', false, 'อาจเป็น Goldfish/Chick — เทียบ Series 28 (2026)'),
  ('เงือกชาย (อกทอง หางเข้ม)', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🧜', false, 'ยังระบุซีรีส์ไม่ได้ — อาจเป็นไลน์ Atlantis/คัสตอม'),
  ('อัศวิน/ราชาน้ำเงิน (โล่ลายม้า)', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🐴', false, 'น่าจะไลน์ Castle — ต้องดูตราโล่ใกล้ๆ'),
  ('ตัวดำหัวเปลวไฟ นั่งบนสัตว์ดำ', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🔥', false, 'เดาว่าธีมไฟ/Ninjago หรือคัสตอม'),
  ('นักรบนก/อินทรี (แขนขนนก)', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🦅', false, 'อาจเป็นไลน์ Chima หรือชุดนก'),
  ('สาวชุดสตรอว์เบอร์รี + ลูกอมแท่ง', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🍓', false, 'ดูเป็นธีมหวาน/เทศกาล — ยังไม่พบรุ่นตรง'),
  ('ชายปกแหลมน้ำตาล มีหนวด', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🦁', false, 'คล้ายชุดสิงโต/มนุษย์หมาป่า — ไม่ชัด'),
  ('ชายชุดทักซิโด้ผูกโบว์', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🎩', false, 'อาจเป็น Magician (Series 1) หรือเจ้าบ่าว/นักธุรกิจ'),
  ('นักธุรกิจถือแซกโซโฟนทอง', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🎷', false, 'คล้าย Saxophone Player แต่ชุดต่าง — ไม่ชัด'),
  ('ชายหัวล้าน เสื้อกล้ามดำ', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '👤', false, 'ดูเป็นลูกน้อง/วายร้ายจากเซ็ต — ไม่ชัด'),
  ('ชายผมบลอนด์ชุดขาวล้วน', NULL, NULL, NULL, 99990000, NULL, NULL, NULL, 'guess', '🤍', false, 'อาจเป็นนักกีฬา/เจ้าบ่าว/ตัวเฉพาะเซ็ต');

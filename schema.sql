-- LEGO Minifigures collection — Supabase schema + seed
create table if not exists public.minifigures (
  id bigserial primary key, name_th text not null, name_en text, series text,
  set_no text, release_date text, release_sort integer not null default 99990000,
  category text, bricklink_id text, image_url text, confidence text, emoji text,
  identified boolean not null default true, note text, created_at timestamptz not null default now()
);
alter table public.minifigures add column if not exists set_no text;
alter table public.minifigures enable row level security;
drop policy if exists "public read" on public.minifigures;
create policy "public read" on public.minifigures for select to anon, authenticated using (true);
truncate table public.minifigures restart identity;
insert into public.minifigures (name_th, name_en, series, set_no, release_date, release_sort, category, bricklink_id, image_url, confidence, emoji, identified, note) values
  ('บัซ ไลต์เยียร์', 'Buzz Lightyear', 'LEGO Toy Story', NULL, '2010', 20100101, 'licensed', 'toy004', 'https://img.bricklink.com/ItemImage/MN/0/toy004.png', 'fair', '🚀', true, NULL),
  ('วู้ดดี้', 'Woody', 'LEGO Toy Story', NULL, '2010', 20100102, 'licensed', 'toy003', 'https://img.bricklink.com/ItemImage/MN/0/toy003.png', 'sure', '🤠', true, NULL),
  ('ฟาโรห์', 'Pharaoh', 'Series 2', '8684', '2010', 20100901, 'fantasy', 'col032', 'https://img.bricklink.com/ItemImage/MN/0/col032.png', 'fair', '🏺', true, NULL),
  ('ราชาสมุทร / โพไซดอน', 'Ocean King (Poseidon)', 'Series 7', '8831', 'พ.ค. 2012', 20120501, 'fantasy', 'col101', 'https://img.bricklink.com/ItemImage/MN/0/col101.png', 'sure', '🔱', true, NULL),
  ('ชุดไก่', 'Chicken Suit Guy', 'Series 9', '71000', 'ม.ค. 2013', 20130101, 'animal', 'col135', 'https://img.bricklink.com/ItemImage/MN/0/col135.png', 'sure', '🐔', true, NULL),
  ('พ่อมด', 'Wizard', 'Series 12', '71007', '2014', 20140101, 'fantasy', 'col179', 'https://img.bricklink.com/ItemImage/MN/0/col179.png', 'sure', '🧙', true, NULL),
  ('ชุดฮอตดอก', 'Hot Dog Man', 'Series 13', '71008', 'ม.ค. 2015', 20150101, 'food', 'col208', 'https://img.bricklink.com/ItemImage/MN/0/col208.png', 'sure', '🌭', true, NULL),
  ('ราชาคลาสสิก', 'Classic King', 'Series 13', '71008', 'ม.ค. 2015', 20150102, 'fantasy', 'col195', 'https://img.bricklink.com/ItemImage/MN/0/col195.png', 'sure', '👑', true, NULL),
  ('ชุดฉลาม', 'Shark Suit Guy', 'Series 15', '71011', 'ม.ค. 2016', 20160101, 'animal', 'col240', 'https://img.bricklink.com/ItemImage/MN/0/col240.png', 'sure', '🦈', true, NULL),
  ('ชุดกล้วย', 'Banana Guy', 'Series 16', '71013', 'ก.ย. 2016', 20160901, 'food', 'col258', 'https://img.bricklink.com/ItemImage/MN/0/col258.png', 'sure', '🍌', true, NULL),
  ('เด็กชุดเพนกวิน', 'Penguin Boy', 'Series 16', '71013', 'ก.ย. 2016', 20160902, 'animal', 'col253', 'https://img.bricklink.com/ItemImage/MN/0/col253.png', 'fair', '🐧', true, NULL),
  ('แบทแมน (Batman Returns 1992)', 'Batman — Batman Returns 1992', 'DC Super Heroes', '30653', '1992 (LEGO 2023)', 20230101, 'licensed', 'sh0880', 'https://img.bricklink.com/ItemImage/MN/0/sh0880.png', 'sure', '🦇', true, NULL),
  ('แคทแมน', 'Catman', 'The LEGO Batman Movie Series 1', '71017', '2017', 20170201, 'licensed', 'coltlbm16', 'https://img.bricklink.com/ItemImage/MN/0/coltlbm16.png', 'sure', '🐱', true, NULL),
  ('เฮดีส', 'Hades', 'Disney Series 2', '71024', '2019', 20190210, 'licensed', 'dis036', 'https://img.bricklink.com/ItemImage/MN/0/dis036.png', 'sure', '🔥', true, NULL),
  ('เพรซิเดนต์ บิสเนส', 'President Business', 'The LEGO Movie Series 1', '71004', '2014', 20140110, 'licensed', 'tlm002', 'https://img.bricklink.com/ItemImage/MN/0/tlm002.png', 'sure', '🎷', true, NULL),
  ('เจมส์ บอนด์ 007', 'James Bond (007)', 'Speed Champions', '76911', '2022', 20220110, 'licensed', 'sc102', 'https://img.bricklink.com/ItemImage/MN/0/sc102.png', 'sure', '🎩', true, NULL),
  ('โดมินิค โทเร็ตโต้', 'Dominic Toretto', 'Speed Champions', '76912', '2022', 20220120, 'licensed', 'sc103', 'https://img.bricklink.com/ItemImage/MN/0/sc103.png', 'sure', '👤', true, NULL),
  ('ไบรอัน โอคอนเนอร์', 'Brian O''Conner', 'Speed Champions', '76917', '2023', 20230110, 'licensed', 'sc104', 'https://img.bricklink.com/ItemImage/MN/0/sc104.png', 'sure', '🤍', true, NULL),
  ('ชุดข้าวโพด', 'Corn Cob Guy', 'Series 17', '71018', 'พ.ค. 2017', 20170501, 'food', 'col289', 'https://img.bricklink.com/ItemImage/MN/0/col289.png', 'sure', '🌽', true, NULL),
  ('ชุดมังกรแดง', 'Dragon Suit Guy', 'Series 18', '71021', 'เม.ย. 2018', 20180401, 'fantasy', 'col318', 'https://img.bricklink.com/ItemImage/MN/0/col318.png', 'sure', '🐉', true, NULL),
  ('ชุดพลุ (BANG)', 'Firework Guy', 'Series 18', '71021', 'เม.ย. 2018', 20180402, 'fantasy', 'col316', 'https://img.bricklink.com/ItemImage/MN/0/col316.png', 'sure', '🎆', true, NULL),
  ('ชุดกระบองเพชร', 'Cactus Girl', 'Series 18', '71021', 'เม.ย. 2018', 20180403, 'food', 'col322', 'https://img.bricklink.com/ItemImage/MN/0/col322.png', 'sure', '🌵', true, NULL),
  ('ชุดยีราฟ', 'Giraffe Guy', 'The LEGO Movie 2', '71023', 'ก.พ. 2019', 20190201, 'animal', 'tlm151', 'https://img.bricklink.com/ItemImage/MN/0/tlm151.png', 'sure', '🦒', true, NULL),
  ('ชุดสีเทียน', 'Crayon Girl', 'The LEGO Movie 2', '71023', 'ก.พ. 2019', 20190202, 'craft', 'tlm152', 'https://img.bricklink.com/ItemImage/MN/0/tlm152.png', 'sure', '🖍️', true, NULL),
  ('ชุดแตงโม', 'Watermelon Dude', 'The LEGO Movie 2', '71023', 'ก.พ. 2019', 20190203, 'food', 'tlm155', 'https://img.bricklink.com/ItemImage/MN/0/tlm155.png', 'sure', '🍉', true, NULL),
  ('ชุดพิซซ่า', 'Pizza Costume Guy', 'Series 19', '71025', 'ก.ย. 2019', 20190901, 'food', 'col351', 'https://img.bricklink.com/ItemImage/MN/0/col351.png', 'sure', '🍕', true, NULL),
  ('ชุดถั่วลันเตา', 'Peapod Costume Girl', 'Series 20', '71027', '2020', 20200101, 'food', 'col360', 'https://img.bricklink.com/ItemImage/MN/0/col360.png', 'sure', '🫛', true, NULL),
  ('ชุดลามา', 'Llama Costume Girl', 'Series 20', '71027', '2020', 20200102, 'animal', 'col364', 'https://img.bricklink.com/ItemImage/MN/0/col364.png', 'sure', '🦙', true, NULL),
  ('เด็กชุดไก่ (ส้ม)', 'Chicken Suit Boy', 'Build-A-Minifigure', 'BAM 2022', '2022', 20220101, 'animal', 'hol299', 'https://img.bricklink.com/ItemImage/MN/0/hol299.png', 'sure', '🐥', true, NULL),
  ('ชุดไก่งวง', 'Turkey Costume', 'Series 23', '71034', 'ก.ย. 2022', 20220901, 'animal', 'col406', 'https://img.bricklink.com/ItemImage/MN/0/col406.png', 'sure', '🦃', true, NULL),
  ('ชุดมังกรเขียว', 'Green Dragon Costume', 'Series 23', '71034', 'ก.ย. 2022', 20220902, 'fantasy', 'col409', 'https://img.bricklink.com/ItemImage/MN/0/col409.png', 'sure', '🐲', true, NULL),
  ('ชุดป๊อปคอร์น', 'Popcorn Costume', 'Series 23', '71034', 'ก.ย. 2022', 20220903, 'food', 'col404', 'https://img.bricklink.com/ItemImage/MN/0/col404.png', 'sure', '🍿', true, NULL),
  ('อัศวินแวมไพร์', 'Vampire Knight', 'Series 25', '71045', '2024', 20240101, 'fantasy', 'col426', 'https://img.bricklink.com/ItemImage/MN/0/col426.png', 'sure', '🧛', true, NULL),
  ('ราชาอัศวินม้า', 'Horse Knight King', 'Castle (set 31168)', '31168', '2025', 20250801, 'fantasy', 'cas592', 'https://img.bricklink.com/ItemImage/MN/0/cas592.png', 'sure', '🐎', true, NULL),
  ('แบทแมนเงือก', 'Mermaid Batman', 'The LEGO Batman Movie Series 2', '71020', '2018', 20180105, 'licensed', 'coltlbm29', 'https://img.bricklink.com/ItemImage/MN/0/coltlbm29.png', 'sure', '🧜', true, NULL),
  ('สาวชุดสตรอว์เบอร์รีเค้ก', 'Strawberry Shortcake Girl', 'Build-A-Minifigure', 'BAM 2023', '2023', 20230601, 'food', 'hol355x', 'https://img.bricklink.com/ItemImage/MN/0/hol355x.png', 'sure', '🍓', true, NULL),
  ('เฮอร์คิวลิส', 'Hercules', 'Disney Series 2', '71024', '2019', 20190215, 'licensed', 'dis037', 'https://img.bricklink.com/ItemImage/MN/0/dis037.png', 'sure', '🏛️', true, NULL),
  ('ชุดสีเทียนม่วงแดง', 'Magenta Crayon Costume Guy', 'Build-A-Minifigure', 'BAM 2023', '2023', 20230610, 'craft', NULL, NULL, 'sure', '🖍️', true, NULL),
  ('นายกฯ ชุดข้าวโพด (Solomon Fleck)', 'Mayor Solomon Fleck (Corn Cob)', 'LEGO City', 'cty1222', '2020', 20200601, 'food', 'cty1222', 'https://img.bricklink.com/ItemImage/MN/0/cty1222.png', 'sure', '🌽', true, NULL),
  ('ชุดเค้ก/พาย', 'Cake / Pie Costume Guy', 'Build-A-Minifigure', 'BAM 2022', '2022', 20220115, 'food', 'hol296', 'https://img.bricklink.com/ItemImage/MN/0/hol296.png', 'sure', '🥧', true, NULL),
  ('ปาร์ตี้ บานาน่า', 'Party Banana Guy', 'Party Banana Juice Bar', '5005250', '2018', 20181001, 'food', 'col330', 'https://img.bricklink.com/ItemImage/MN/0/col330.png', 'sure', '🍌', true, NULL),
  ('ชุดนกยูง', 'Peacock Costume', 'Series 28', '71051', 'ม.ค. 2026', 20260101, 'animal', 'col461', 'https://img.bricklink.com/ItemImage/MN/0/col461.png', 'sure', '🦚', true, NULL);

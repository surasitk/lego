# 🧱 LEGO Minifigures Collection

เว็บแสดงคอลเลกชันมินิฟิกเกอร์ LEGO ส่วนตัว เรียงตามปีวางจำหน่าย พร้อม **รูปทางการ** ดึงจาก BrickLink Image CDN แสดงในตารางทันที (ไม่ต้องคลิกไปหา)

🔗 **Live:** _(ดูใน Vercel หลัง deploy)_

## ฟีเจอร์
- ตารางสวยๆ พร้อมรูป thumbnail ในแถว + มุมมองแกลเลอรี (toggle)
- ค้นหา (ชื่อ / ซีรีส์ / รหัส BrickLink) และกรองตามหมวด (สัตว์ / อาหาร / แฟนตาซี / ลิขสิทธิ์ / อื่นๆ)
- เรียงตามปี / ชื่อ / ซีรีส์
- คลิกดูรูปใหญ่ (lightbox) + ลิงก์ไปแคตตาล็อก BrickLink
- ข้อมูลดึงสดจาก **Supabase** (มี fallback เป็น `figures.json` เผื่อออฟไลน์)

## โครงสร้าง
| ไฟล์ | หน้าที่ |
|---|---|
| `index.html` | ทั้งเว็บในไฟล์เดียว (HTML/CSS/JS) — static deploy ได้เลย |
| `figures.json` | ข้อมูลมินิฟิกเกอร์ (fallback + seed) |
| `schema.sql` | สร้างตาราง + RLS + insert ข้อมูลลง Supabase |
| `gen_data.py` | สคริปต์สร้าง `schema.sql` และ `figures.json` จาก dataset เดียว |

## Setup
1. รัน `schema.sql` ใน Supabase SQL Editor (โปรเจกต์ `qmmopgyevfuztpqaynww`)
2. ใส่ `anon` key ของโปรเจกต์ในตัวแปร `SUPABASE_ANON_KEY` ใน `index.html`
3. Deploy โฟลเดอร์นี้บน Vercel (static, zero config)

## ข้อมูล
รูปจาก BrickLink Image CDN (`img.bricklink.com/ItemImage/MN/0/{id}.png`) · ข้อมูลซีรีส์/วันวางจำหน่ายอ้างอิง LEGO.com, BrickLink, Brickset

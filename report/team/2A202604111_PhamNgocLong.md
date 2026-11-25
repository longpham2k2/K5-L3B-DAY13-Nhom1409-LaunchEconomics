# Báo cáo cá nhân — Phạm Ngọc Long · 2A202604111

## 1. Thông tin thành viên

- Họ tên: Phạm Ngọc Long
- MSSV: 2A202604111
- Email:
- Vai trong nhóm: người viết code (CP1, CP2, CP4); nhóm trưởng, chủ repo nhóm.

## 2. Phần việc phụ trách

- Chuẩn bị: tạo repo nhóm, cài môi trường `src/.venv`, chạy thử file khởi đầu, chia vai trong `TEAM.md`.
- CP1–CP2: viết `src/lab13.py` cho nhiệm vụ A (A1–A4) và B (B1–B4).
- CP4: viết phần cỡ mẫu D1 và tỉ lệ mở lại hiện tại trong `src/lab13.py`.
- Rà soát số liệu các thành viên khác đẩy lên so với đầu ra của `src/lab13.py`.
- CP5: viết ba chỉ số và danh sách event trong `report/team/chi_so.md`; bảo vệ hồ sơ tại Gate 2a; commit và push bài nộp.

## 3. Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: hàm `mo_hinh()`. Tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`: 4.472 đ/việc thành công, gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ) [simulated].
- A3, A4: tách theo `loai` (quoc_te 22.515 đ = 1,88× mốc 12.000 đ; lần thử 1/2/3 đúng 30% / 11,4% / 2,2%) và cộng chi phí cố định cho phạm vi noi_dia + hang_nang: 4.599 đ (0,38×) [simulated].
- B1–B4: 9 kịch bản độ nhạy kèm tự kiểm tra "giảm một nửa = nửa mức tăng" (in ĐẠT); cặp token + xem lại 6.543 đ (+46,3%); giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ); xem lại 100% 11.743 đ (0,98×) [simulated].
- D1: cỡ mẫu 1.251/nhóm theo yêu cầu; theo nhân viên DE 2,48 cần 84 người > 40; 20 người mỗi nhóm tối đa 1.000; mức chênh 6 điểm cần m ≥ 299 (DE 6,96); power còn 0,64 nếu tác động thật 5 điểm. Tỉ lệ mở lại 7 ngày hiện tại 4,25%, phạm vi pilot 3,97%.
- Hồ sơ launch: bổ sung con số cho mục 1 và mục 3 (toàn mẫu 5.865 đ/yêu cầu = 0,49× khi tính cả 222 yêu cầu nhân viên làm thay), đồng tác giả với Minh [simulated].

## 4. Bằng chứng

- `0129a02`: điền `TEAM.md` (thông tin nhóm, vai trò).
- `94a40ba`: CP1, nhiệm vụ A trong `src/lab13.py`.
- `6d941fb`: CP2, nhiệm vụ B trong `src/lab13.py`.
- `49f24f5`: CP4, D1 và tỉ lệ mở lại trong `src/lab13.py`.
- `1fa2d3f`: mục 1 và 3 trong `report/team/ho_so_launch_v0.md`.
- Chạy lại: `cd src && python lab13.py` in toàn bộ số ở mục 3.

## 5. Công cụ AI đã dùng

- Claude Code (Claude Opus): viết code cho A1–A4, B1–B4, D1 trong `src/lab13.py`; cài môi trường; rà soát commit của các thành viên khác so với đầu ra của code.
- Tự kiểm tra: chạy `python lab13.py`; ba phép thử A1 và phép thử "giảm một nửa" ở B1 đều in ĐẠT; đối chiếu từng con số A2, A3, A4, B1–B4, D1 với số tự kiểm tra trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, tất cả trùng (lệch dưới 2%). Tính tay kiểm lại tỉ lệ toàn mẫu: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ.

## 6. Tự đánh giá

- Giải thích được vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, và vì sao giờ nhân viên (xem lại + làm lại, 92,5% tổng chi phí) quyết định kết quả chứ không phải giá token.
- Cần tự luyện thêm phần cỡ mẫu theo cụm (hệ số thiết kế, giới hạn c ÷ ICC) vì phần code D1 được AI hỗ trợ viết.

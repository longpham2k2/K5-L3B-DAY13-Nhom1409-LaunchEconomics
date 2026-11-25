# Báo cáo cá nhân — Phạm Ngọc Long · 2A202604111

## 1. Thông tin thành viên

- Họ tên: Phạm Ngọc Long
- MSSV: 2A202604111
- Email:
- Vai trong nhóm: người viết code (CP1, CP2, CP4, CP5 · E1); nhóm trưởng, chủ repo nhóm.

## 2. Phần việc phụ trách

- Chuẩn bị: tạo repo nhóm, cài môi trường `src/.venv`, chạy thử file khởi đầu, chia vai trong `TEAM.md`.
- CP1–CP2: viết `src/lab13.py` cho nhiệm vụ A (A1–A4) và B (B1–B4).
- CP4: viết phần cỡ mẫu D1 và tỉ lệ mở lại hiện tại trong `src/lab13.py`.
- Rà soát số liệu các thành viên khác đẩy lên so với đầu ra của `src/lab13.py`.
- CP5: tính ba chỉ số E1 trong `src/lab13.py`; viết đặc tả chỉ số, danh sách event và kiểm tra chéo trong `report/team/chi_so.md`.
- Gate 2a: tham gia hội đồng chấm nhóm Economics (L3B); commit và push bài nộp.

## 3. Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: hàm `mo_hinh()`. Tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`: 4.472 đ/việc thành công, gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ) [simulated].
- A3, A4: tách theo `loai` (quoc_te 22.515 đ = 1,88× mốc 12.000 đ; lần thử 1/2/3 đúng 30% / 11,4% / 2,2%) và cộng chi phí cố định cho phạm vi noi_dia + hang_nang: 4.599 đ (0,38×) [simulated].
- B1–B4: 9 kịch bản độ nhạy kèm tự kiểm tra "giảm một nửa = nửa mức tăng" (in ĐẠT); cặp token + xem lại 6.543 đ (+46,3%); giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ); xem lại 100% 11.743 đ (0,98×) [simulated].
- D1: cỡ mẫu 1.251/nhóm theo yêu cầu; theo nhân viên DE 2,48 cần 84 người > 40; 20 người mỗi nhóm tối đa 1.000; mức chênh 6 điểm cần m ≥ 299 (DE 6,96); power còn 0,64 nếu tác động thật 5 điểm. Tỉ lệ mở lại 7 ngày hiện tại 4,25%, phạm vi pilot 3,97%.
- E1: thêm phần tính ba chỉ số vào `src/lab13.py`. Chỉ số trong đợt chạy thử: chính (đóng trong 24 giờ, không mở lại 7 ngày) 82,83% (994/1.200); bỏ qua gợi ý (sua + bo) 27,12% (48/177); mở lại trong 7 ngày 4,25% (51/1.200), phạm vi pilot 3,97% (39/982). Ghi rõ đợt chạy thử không có đối chứng nên không kết luận về tác động.
- E1 (đề xuất): thêm một chỉ số dùng (% yêu cầu nhóm trợ lý được mở bằng trợ lý) và một chỉ số an toàn (% đơn hoàn sai tiền qua kiểm tra mẫu 100 đơn/tuần, bắt lỗi ngầm như ca 5 và 17), mỗi chỉ số có công thức.
- Danh sách event: 10 event, mỗi event có `trace_id` (từ `refund_request_created` tới `audit_sample_checked`), có `arm` để tách nhóm trợ lý / đối chứng, phút xem lại và làm lại đo thật để thay cột simulated, `idempotency_key` để phát hiện hoàn trùng. Kiểm tra chéo: mỗi chỉ số trong E1, chi phí mỗi việc thành công và luật dừng hoàn trùng đều chỉ ra được event dùng để tính.
- Gate 2a: đặt câu hỏi duy nhất của hội đồng cho nhóm Economics, về cách chọn chia theo yêu cầu, theo nhân viên hay theo depot: "Tôi tò mò về cách nhóm bạn chọn cách chia này, nhóm bạn có số liệu nào ủng hộ cách chọn này không?". Nhóm trả lời chủ yếu bằng nội dung đã có trong slide (bảng so sánh ba cách chia: 1.251 mỗi nhóm theo yêu cầu, trần 1.000 theo nhân viên, trần 300 theo depot), chưa đưa thêm lập luận hay số liệu ngoài slide.
- Hồ sơ launch: bổ sung con số cho mục 1 và mục 3 (toàn mẫu 5.865 đ/yêu cầu = 0,49× khi tính cả 222 yêu cầu nhân viên làm thay), đồng tác giả với Minh [simulated].

## 4. Bằng chứng

- `0129a02`: điền `TEAM.md` (thông tin nhóm, vai trò).
- `94a40ba`: CP1, nhiệm vụ A trong `src/lab13.py`.
- `6d941fb`: CP2, nhiệm vụ B trong `src/lab13.py`.
- `49f24f5`: CP4, D1 và tỉ lệ mở lại trong `src/lab13.py`.
- `1fa2d3f`: mục 1 và 3 trong `report/team/ho_so_launch_v0.md`.
- `74e586f`: CP5, phần E1 trong `src/lab13.py`; đặc tả chỉ số, danh sách event và kiểm tra chéo trong `report/team/chi_so.md`.
- Gate 2a: câu hỏi cho nhóm Economics ghi ở mục 3; slide của nhóm được chấm (bảng so sánh ba cách chia).
- Chạy lại: `cd src && python lab13.py` in toàn bộ số ở mục 3.

## 5. Công cụ AI đã dùng

- Claude Code (Claude Opus): viết code cho A1–A4, B1–B4, D1, E1 trong `src/lab13.py`; soạn nháp đặc tả chỉ số, danh sách event và kiểm tra chéo trong `chi_so.md`; cài môi trường; rà soát commit của các thành viên khác so với đầu ra của code.
- Tự kiểm tra: chạy `python lab13.py`; ba phép thử A1 và phép thử "giảm một nửa" ở B1 đều in ĐẠT; đối chiếu từng con số A2, A3, A4, B1–B4, D1, E1 với số tự kiểm tra trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, tất cả trùng (lệch dưới 2%). Tính tay kiểm lại tỉ lệ toàn mẫu: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ.

## 6. Tự đánh giá

- Hiểu và tự giải thích được mô hình chi phí: tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm việc thành công; giờ nhân viên chiếm 92,5% tổng chi phí nên quyết định kết quả, không phải giá token [simulated].
- Hiểu vì sao giới hạn rẻ nhất cho công ty (2 lần, 6.901.220 đ) khác giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần): tối ưu riêng chỉ số này đẩy thêm 85 yêu cầu sang nhân viên [simulated].
- Làm tốt: code chạy đúng toàn bộ số đối chiếu (lệch < 2%), có tự kiểm tra tự động (A1, "giảm một nửa"); rà soát commit của cả nhóm và phát hiện sớm lỗi nhãn CP3 do AI gợi ý.
- Ở Gate 2a, nhận ra một hồ sơ trình bày đủ số liệu vẫn có thể chưa giải thích được vì sao chọn một phương án; cách chia nên được bảo vệ bằng hai tiêu chí cùng lúc: đủ mẫu (trần c ÷ ICC) và tách được tác động (ít nhất 20 cụm, không tràn sang đối chứng).
- Chưa tốt: phân công vai trò ban đầu bị lệch so với thực tế (Huy làm phần của Đạt ở CP4), và nhóm chưa xử lý dứt điểm việc gắn nhãn độc lập ở CP3 trước giờ nộp.
- Cần luyện thêm: cỡ mẫu theo cụm (hệ số thiết kế 1 + (m − 1) × ICC, giới hạn c ÷ ICC) vì phần code D1 được AI hỗ trợ viết; cần tự tính tay lại câu e (m ≥ 299).
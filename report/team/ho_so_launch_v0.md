# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhóm1409 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: 4.472 đ/việc thành công, gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại 51,8% và xem lại 40,7% tổng chi phí. Phạm vi `noi_dia` + `hang_nang`: 3.414 đ/việc, 4.599 đ khi cộng chi phí cố định 40 triệu đ/tháng | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8%; xem lại ×2: +40,7%; lương +25%: +23,1% chi phí mỗi việc thành công | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Toàn mẫu, tính cả 222 yêu cầu nhân viên làm thay: 5.865 đ/yêu cầu (0,49× mốc 12.000 đ). Pilot `noi_dia` + `hang_nang`: 4.599 đ/việc (0,38×) ở 45.000 yêu cầu/tháng; 5.784 đ (0,48×) ở nửa khối lượng. Loại `quoc_te` (22.515 đ; 1,88×; thành công 27,3%) và `doi_tac` (10.215 đ; 0,85× nhưng điều khoản riêng) để giữ phạm vi dễ diễn giải | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chạy thử: chính 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại trong 7 ngày 4,25% (51/1.200), phạm vi pilot 3,97% (39/982). Không có đối chứng nên chưa kết luận tác động | Giả lập | Người viết chỉ số |
| 5 · Bảng lỗi và cách khắc phục | 18/20 ca đồng thuận ban đầu (90%); ca 2 và 8 được nhóm thống nhất nhãn cuối là Hệ thống; có biện pháp cho đủ 5 loại lỗi | Xong, có bằng chứng | Người gắn nhãn 2 |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, phân tầng depot: 20/40 người mỗi nhánh; 299 yêu cầu/người (5.980/nhánh), phát hiện mức chênh 6 điểm. Đánh đổi: power khoảng 64% nếu tác động thật chỉ 5 điểm; an toàn: mở lại ≤6% và không cao hơn đối chứng ≥2 điểm | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2: CPS +51,8% lên 6.787 đ; xem lại 100%: 11.743–12.415 đ/việc (0,98–1,03× mốc 12.000 đ); khối lượng giảm nửa: 5.784 đ/việc | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** — Gate 2a chỉ duyệt kế hoạch pilot.

- Trước bắt đầu 30/11/2026, Giám đốc vận hành xác nhận phân bổ ngẫu nhiên 20 nhân viên mỗi nhánh, phân tầng theo depot, quyền truy cập tách biệt và log đủ event có `trace_id`.
- Trước chuyển sang bước tiếp theo, PM trợ lý kiểm tra cỡ mẫu/luật dừng; không mở rộng nếu an toàn chưa đạt hoặc giao dịch hoàn trùng chưa được xử lý.
- Ngày 12/01/2027, hội đồng chỉ xem xét mở rộng nếu có đủ 20 cụm mỗi nhánh, 299 yêu cầu đủ theo dõi mỗi cụm, mức tăng ước tính ≥5 điểm phần trăm so với đối chứng (mục tiêu đề bài; MDE 6 điểm chỉ dùng để tính cỡ mẫu), p < 0,05 và các ngưỡng vận hành đạt; nếu thiếu điều kiện thì chưa mở rộng.

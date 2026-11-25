# Báo cáo nhóm

Lab 13 · Đánh giá kế hoạch pilot trợ lý hoàn phí LogiX-VN tại Gate 2a.

## 1. Thông tin nhóm

- Tên nhóm: Nhóm1409
- Lớp: L3B
- Thành viên: Phạm Ngọc Long, Nguyễn Công Huy, Trần Trọng Đạt và Đặng Khắc Hoàng Minh. [Phân công nhóm](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí, rủi ro và cách đo hiệu quả của trợ lý hoàn phí. Nhóm dùng dữ liệu giả lập của đợt chạy thử gồm **1.200 yêu cầu và 1.624 lượt chạy**, sau đó thiết kế pilot có đối chứng để đo tác động.

## 3. Giải pháp

- **A–B.** Cộng token, tool, xem lại và làm lại trên mọi lượt chạy và yêu cầu liên quan rồi chia cho số việc thành công. Tách theo loại yêu cầu, phân bổ chi phí cố định và so sánh các kịch bản độ nhạy. [Bảng chi phí](bang_chi_phi.md)
- **C.** Đối chiếu 20 ca theo năm loại lỗi Google PAIR và chọn một ca mỗi loại để đề xuất cách phát hiện, khắc phục và vai trò phụ trách. [Bảng lỗi](bang_loi.md)
- **D.** Chia ngẫu nhiên theo nhân viên, phân tầng theo depot, với đối chứng cùng thời gian. Mỗi nhóm có 20 người, tối thiểu 299 yêu cầu/người để phát hiện chênh lệch 6 điểm phần trăm. Kế hoạch có bốn luật dừng. [Kế hoạch pilot](pilot_plan.yaml)
- **E.** Đặc tả chỉ số kết quả, sử dụng và an toàn, thiết kế 10 event có `trace_id` và lập bảng ba rủi ro kinh tế. [Chỉ số và rủi ro](chi_so.md)

## 4. Kết quả

- **Chi phí [simulated].** Toàn mẫu tốn **4.472 đ/việc thành công**. Phạm vi `noi_dia` và `hang_nang` tốn **4.599 đ/việc thành công** sau khi cộng chi phí cố định ở mức 45.000 yêu cầu/tháng. Nếu xem lại mọi yêu cầu có lượt chạy `ok` trong 5 phút/ca, chi phí tăng lên **11.743–12.415 đ/việc thành công**, tùy thời gian làm lại. [Bảng chi phí](bang_chi_phi.md)
- **Vận hành.** Hai bộ nhãn trùng **18/20 ca (90%)** ban đầu. Nhóm chốt ca 2 và 8 là **Hệ thống**. Trên dữ liệu chạy thử giả lập, **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày, **27,12%** số yêu cầu được xem lại có gợi ý bị sửa hoặc bỏ, và **4,25%** yêu cầu mở lại trong 7 ngày. [Bảng lỗi](bang_loi.md) · [Chỉ số](chi_so.md)
- **Đề xuất Gate 2a.** Nhóm đề xuất **Go có điều kiện** cho pilot `noi_dia` và `hang_nang`. Trước khi khởi động, Giám đốc vận hành xác nhận đủ 40 nhân viên, khả năng thu mẫu và ghi event có `trace_id`. Kế hoạch yêu cầu việc tắt trợ lý có hiệu lực trong 30 phút kể từ khi luật an toàn kích hoạt. Ngày quyết định dự kiến là **12/01/2027**. [Hồ sơ launch v0](ho_so_launch_v0.md) · [Kế hoạch pilot](pilot_plan.yaml)
- **Duyệt chéo.** Repo hiện chưa có điểm hoặc nhận xét hội đồng gửi cho Nhóm1409. [Phiếu chấm](phieu_cham.md)

## 5. Khó khăn và cách xử lý

- Giới hạn 1 lượt chạy cho chi phí mỗi việc thành công thấp nhất nhưng để lại thêm **85 yêu cầu** cho nhân viên so với giới hạn 2 lượt. Nhóm tính thêm phần nhân viên làm thay để so chi phí toàn hệ thống [simulated]. [B3](bang_chi_phi.md#b3--giới-hạn-chạy-lại-có-thật-sự-rẻ-hơn)
- Với 40 nhân viên, chia theo cụm không đủ mẫu cho mức chênh 5 điểm phần trăm. Nhóm chọn thiết kế phát hiện 6 điểm và ghi rõ power chỉ khoảng **64%** nếu tác động thật là 5 điểm. [Kế hoạch pilot](pilot_plan.yaml)
- Hồ sơ launch và kế hoạch pilot từng lệch về ngưỡng mở rộng (6 và 5 điểm). Nhóm đã thống nhất: mở rộng khi mức tăng ước tính ít nhất **5 điểm phần trăm** theo mục tiêu đề bài, p < 0,05; **6 điểm** chỉ là MDE dùng để tính cỡ mẫu. [Kế hoạch pilot](pilot_plan.yaml) · [Hồ sơ launch v0](ho_so_launch_v0.md)

## 6. Tổng hợp đóng góp

- **Phạm Ngọc Long:** Viết mô hình chi phí, kịch bản độ nhạy, phép tính cỡ mẫu và đặc tả E1.
- **Nguyễn Công Huy:** Kiểm số và điền bảng chi phí, rà soát CP3, hoàn thiện kế hoạch pilot, viết E2 và báo cáo nhóm.
- **Trần Trọng Đạt:** Gắn nhãn bộ 1, phối hợp đối chiếu nhãn, bổ sung phân tích B3 và cập nhật kế hoạch pilot.
- **Đặng Khắc Hoàng Minh:** Chuẩn bị bộ nhãn 2 có hỗ trợ AI, đối chiếu hai bộ nhãn, bổ sung B4 và cập nhật hồ sơ launch. [Chi tiết đóng góp](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Dữ liệu chạy thử là giả lập và thiếu đối chứng, nên mức **82,83%** chỉ mô tả mẫu. Trong pilot, nhóm cần đo phút xem lại và làm lại thực tế, đồng thời kiểm tra mẫu giao dịch hằng tuần để phát hiện hoàn sai tiền.

## 8. Tài liệu tham khảo

- [Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) và [hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) và [mã tính toán](../../src/lab13.py).

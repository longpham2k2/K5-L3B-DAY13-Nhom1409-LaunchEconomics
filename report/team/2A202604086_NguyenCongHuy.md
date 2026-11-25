# Báo cáo cá nhân — Nguyễn Công Huy · 2A202604086

## 1. Thông tin thành viên

- Họ tên: Nguyễn Công Huy
- MSSV: 2A202604086
- Email: conghuycr@gmail.com
- Vai trong nhóm: Người kiểm số ở CP1–CP2, người viết code sau giờ giải lao.

## 2. Phần việc phụ trách

- CP1–CP2: Đối chiếu chi phí tính từ trace, điền bảng chi phí và phân tích độ nhạy.
- CP4: Tính cỡ mẫu D1 trong `src/lab13.py`.
- CP5: Tổng hợp rủi ro kinh tế từ bảng độ nhạy, viết báo cáo nhóm và tham gia bảo vệ hồ sơ tại Gate 2a.

## 3. Đóng góp cụ thể

- CP1: Hoàn thiện bảng A1–A4. Ở A4, trình bày cách dự báo số việc thành công và phân bổ 40 triệu đồng chi phí cố định mỗi tháng. Chi phí sau khi cộng khoản cố định là 4.599 đ và 5.784 đ mỗi việc thành công ở hai mức 45.000 và 22.500 yêu cầu/tháng [simulated].
- CP2: Điền 9 kịch bản độ nhạy, tính kịch bản kết hợp ở B2 và lập bảng so sánh ba giới hạn chạy ở B3. Khi giá token và tỉ lệ xem lại cùng gấp đôi, chi phí tăng 46,3% lên 6.543 đ mỗi việc thành công [simulated].

## 4. Bằng chứng

- CP1: Commit `7980daf`, phần A1–A4 trong [bảng chi phí](bang_chi_phi.md).
- CP2: Commit `e35180e`, phần B1, B2 và bảng B3 trong [bảng chi phí](bang_chi_phi.md).

## 5. Công cụ AI đã dùng

- Dùng Codex để hỗ trợ điền và rà soát bảng chi phí, đồng thời giải thích cách tính tay B2. Kết quả được đối chiếu với đầu ra của `src/lab13.py`. Phép tính tay B2 lấy (245.585 + 1.780.000) ÷ 4.373.585 × 100, ra mức tăng khoảng 46,3% [simulated].

## 6. Tự đánh giá

- Có thể giải thích cách phân bổ chi phí cố định theo sản lượng và tính lại mức tăng chi phí ở B2 từ các khoản gốc trong A2.
- Khi đọc kết quả B3, cần ghi rõ đang so chi phí của cả hệ thống hay chi phí trên mỗi việc trợ lý hoàn thành, vì hai chỉ tiêu cho hai giới hạn chạy tối ưu khác nhau.

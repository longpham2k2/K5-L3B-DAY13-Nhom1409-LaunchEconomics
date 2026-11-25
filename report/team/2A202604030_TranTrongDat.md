# Báo cáo cá nhân — Trần Trọng Đạt — 2A202604030

## 1. Thông tin thành viên

- Họ tên: Trần Trọng Đạt.
- MSSV: 2A202604030.
- Email:
- Vai trong nhóm: Người gắn nhãn 1; theo dõi điều kiện hoàn thành các checkpoint và phụ trách điền kế hoạch pilot theo phân công.

## 2. Phần việc phụ trách

- CP1–CP2: Đọc đề và kiểm tra điều kiện hoàn thành; đối chiếu bảng chi phí, phân tích độ nhạy với kết quả chạy chương trình; kiểm tra nhãn `simulated`.
- CP3: Gắn nhãn 20 ca lỗi ở cột người 1, đối chiếu hai bộ nhãn, rà soát và thống nhất lại nhãn với người gán nhãn 2.
- CP4: Hoàn thiện phần kế hoạch trong `pilot_plan.yaml` dựa trên kết quả cỡ mẫu của nhóm, rà soát phạm vi, cách chia nhóm, luật dừng và phương án quay về luồng nhân viên tự làm.

## 3. Đóng góp cụ thể

### CP1 — Kiểm tra mô hình chi phí

- Đối chiếu ba phép thử A1 với kết quả 1,20; 1,25; 1,25 và thông báo ĐẠT khi chạy code.
- Kiểm tra A2 đủ 9 dòng, A3 đủ 4 loại yêu cầu, A4 có phân bổ chi phí cố định 40 triệu đ/tháng; các khoản suy ra từ thời gian giả lập có nhãn `simulated`.
- Làm rõ hai mẫu số: 274,7 đ là tiền token và tool trên mỗi yêu cầu; 4.472 đ là tổng chi phí trợ lý, xem lại và làm lại trên mỗi việc thành công [simulated]. Khi tính thêm nhân viên xử lý yêu cầu không thành công, chi phí toàn hệ thống là khoảng 5.865 đ/yêu cầu, chưa gồm cố định [simulated].

### CP2

- Rà soát 9 kịch bản B1, bảng đổi một cặp B2 và quy tắc mức giảm khi giảm một nửa bằng nửa mức tăng khi gấp đôi, tính trước khi làm tròn.
- Điền và chỉnh câu trả lời B3: giới hạn 2 lần chạy có tổng chi phí hệ thống thấp nhất, 6.901.220 đ, giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất, 4.111 đ, nhưng để lại thêm 85 yêu cầu cho nhân viên so với giới hạn 2 lần [simulated].

### CP3

- Điền bộ nhãn người 1 cho 20 ca theo 5 loại: Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm..
- Kiểm tra, đối chiếu và thống nhất nhãn của người gán 2 và chọn ra nhãn lỗi cuối cùng.

### CP4

- Phối hợp hoàn thiện kế hoạch theo cách chia ngẫu nhiên theo nhân viên, phân tầng theo depot, 20 nhân viên dùng trợ lý và 20 nhân viên đối chứng.
- Dùng kết quả D1 do nhóm tính để điền kế hoạch: chấp nhận MDE 6 điểm, cỡ mẫu hiệu dụng 859 mỗi nhóm, 299 yêu cầu/nhân viên và 5.980 yêu cầu thực tế mỗi nhóm. Phân biệt MDE 6 điểm với mục tiêu cải thiện ít nhất 5 điểm của đề.
- Rà soát bốn luật dừng về mở lại, hoàn trùng, chi phí và mức độ sử dụng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ, làm rõ người chịu trách nhiệm, thời hạn và việc không được phép làm khi chưa khắc phục.
- Kiểm tra đúng cho file yaml.
- Đối chiếu với `chi_so.md` để nhận diện điểm cần đồng bộ về cửa sổ mở lại, cách đếm yêu cầu được xem lại và chính sách xem lại.

## 4. Bằng chứng

| Phần việc | Bằng chứng |
| --- | --- |
| Kiểm tra CP1–CP2, câu trả lời B3 | [Bảng chi phí](bang_chi_phi.md); commit `eb99a82`, `b697341` về B3. Code tính toán do thành viên phụ trách code thực hiện trong [lab13.py](../../src/lab13.py). |
| Bộ nhãn người 1 | [Bảng lỗi](bang_loi.md); commit `96173af` về nhãn người 1 và `5a5c051` cập nhật bảng lỗi. |
| Hợp nhất bảng bị conflict | Merge commit `385990a`; giữ hai cột nhãn ban đầu và kết quả đối chiếu 18/20 ca. |
| Hoàn thiện pilot | [Kế hoạch pilot](pilot_plan.yaml); commit `34d104d`. |

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Công cụ: ChatGPT/Codex.
- Cách dùng: giải thích đề, giải thích sự khác nhau giữa chi phí mỗi việc thành công và chi phí cả hệ thống, hỗ trợ xử lý conflict, rà soát YAML, đề xuất sửa luật dừng và soạn báo cáo này.
- Cách kiểm tra: đối chiếu câu trả lời với đề, `CHECKPOINTS.md`, `RUBRIC.md` và kết quả `src/lab13.py`. Nhờ codex so và sửa lại kết quả pilot nếu có khác biệt với file chi_so.md.

## 6. Tự đánh giá

- Đã thực hiện phần gắn nhãn người 1, tham gia kiểm tra số liệu, câu trả lời B3 và hoàn thiện kế hoạch pilot. Hiểu rằng chi phí mỗi việc thành công thấp chưa đủ chứng minh tổng chi phí công ty thấp; cần tính cả phần nhân viên xử lý việc không thành công và chi phí cố định.
- Hiểu đánh đổi cỡ mẫu khi chia theo nhân viên: tăng số yêu cầu không khắc phục được giới hạn số cụm để phát hiện mức chênh 5 điểm với nguồn lực đã cho, cần nêu rõ việc chấp nhận thiết kế 6 điểm và power giảm nếu tác động thật nhỏ hơn.
- Hiểu được các mức dừng khác nhau tùy vào chi phí và rủi ro của vấn đề.

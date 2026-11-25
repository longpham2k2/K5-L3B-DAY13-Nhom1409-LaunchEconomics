# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Trọng Đạt · Người gắn nhãn 2: Đặng Khắc Hoàng Minh (AI gợi ý nhưng đã kiểm tra lại và đồng ý).

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Ngầm | Hệ thống | Không | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận ban đầu:** 18 / 20 = 90% (đạt ngưỡng 80%).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 2: Nhóm thống nhất nhãn cuối là **Hệ thống** vì tool dùng sai tham số và khoản hoàn thiếu đã lộ qua phản ánh/mở lại của khách; giữ nguyên nhãn độc lập ban đầu.
- Ca 8: Nhóm thống nhất nhãn cuối là **Hệ thống** vì trợ lý viện dẫn điều khoản không tồn tại; lỗi thể hiện trong câu trả lời dù số tiền hoàn đúng.
- Hai ca bất đồng được thống nhất là Hệ thống; nhãn độc lập ban đầu không bị sửa.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng* | Theo dõi event `refund_bank_reject`; cảnh báo khi tỷ lệ lỗi tăng trên 2% trong ngày | Kiểm tra định dạng/số kiểm tra tài khoản trước khi gửi; yêu cầu khách xác nhận thông tin không khớp | Người vận hành hoàn phí |
| 7 | Hệ thống* | Đối chiếu `ledger_write_status` với `customer_refund_notice`; cảnh báo mọi thông báo thành công khi chưa có xác nhận sổ cái | Chỉ báo thành công sau ACK; lỗi 503 thì giữ trạng thái chờ và chuyển nhân viên, không retry mù | Kỹ sư tích hợp |
| 3 | Ngữ cảnh* | Theo dõi `refund_destination` và event mở lại/phản ánh; rà soát hàng tuần nếu có khách hiểu sai phương thức nhận | Nêu rõ tiền về ví LogiX, thời gian dự kiến và lựa chọn/kênh hỗ trợ trước khi khách xác nhận | Thiết kế trải nghiệm khách hàng |
| 11 | Giới hạn hệ thống* | Ghi `unsupported_input_type`; báo cáo hàng tuần số/tỷ lệ tin nhắn thoại không xử lý được | Báo rõ giới hạn, cung cấp chuyển giọng nói thành văn bản hoặc chuyển nhân viên kèm transcript | Chủ sản phẩm trợ lý |
| 5 | Ngầm* | Đối soát hàng tuần giá trị hoàn với giá sau giảm; cảnh báo mọi chênh lệch khác 0 và tổng tiền vượt ngưỡng kiểm soát | Sửa công thức dùng giá thực trả sau giảm; rà soát hồi tố các giao dịch từ lần cập nhật gần nhất và hoàn phần chênh | Chủ chính sách hoàn phí |

\* Nhãn thống nhất cho ca 2 và 8 là Hệ thống; hai nhãn độc lập ban đầu vẫn được lưu riêng để tính đúng tỷ lệ đồng thuận.

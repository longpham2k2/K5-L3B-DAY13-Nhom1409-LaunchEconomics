# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Trọng Đạt · Người gắn nhãn 2: Đặng Khắc Hoàng Minh. Cột nhãn người 2 dưới đây là **bản gợi ý do AI soạn, chưa được Minh xác nhận độc lập**; không dùng làm kết quả CP3 cho tới khi Minh tự rà nhãn. Chưa có bộ nhãn của Đạt.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Chờ nhãn độc lập | Do người dùng (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 2 | Chờ nhãn độc lập | Hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 3 | Chờ nhãn độc lập | Ngữ cảnh (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 4 | Chờ nhãn độc lập | Giới hạn hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 5 | Chờ nhãn độc lập | Ngầm (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 6 | Chờ nhãn độc lập | Do người dùng (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 7 | Chờ nhãn độc lập | Hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 8 | Chờ nhãn độc lập | Hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 9 | Chờ nhãn độc lập | Do người dùng (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 10 | Chờ nhãn độc lập | Ngữ cảnh (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 11 | Chờ nhãn độc lập | Giới hạn hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 12 | Chờ nhãn độc lập | Ngầm (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 13 | Chờ nhãn độc lập | Giới hạn hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 14 | Chờ nhãn độc lập | Do người dùng (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 15 | Chờ nhãn độc lập | Hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 16 | Chờ nhãn độc lập | Ngữ cảnh (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 17 | Chờ nhãn độc lập | Ngầm (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 18 | Chờ nhãn độc lập | Ngữ cảnh (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 19 | Chờ nhãn độc lập | Giới hạn hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |
| 20 | Chờ nhãn độc lập | Hệ thống (gợi ý AI) | Chưa đối chiếu | Chờ đối chiếu |

**Tỉ lệ đồng thuận:** Chưa tính — cần hai bộ nhãn độc lập đã được người gắn nhãn xác nhận.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chưa có danh sách ca bất đồng. Sau khi có hai bộ nhãn: phân biệt **Do người dùng** (nhập/chọn sai) với **Hệ thống** (xử lý sai so với thiết kế); **Ngữ cảnh** là xử lý đúng thiết kế nhưng không khớp kỳ vọng/hoàn cảnh; **Giới hạn hệ thống** là ngoài phạm vi hoặc thiếu khả năng/dữ liệu; **Ngầm** là sai sót không được người dùng hay hệ thống phát hiện trong vận hành thông thường.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng* | Theo dõi event `refund_bank_reject`; cảnh báo khi tỷ lệ lỗi tăng trên 2% trong ngày | Kiểm tra định dạng/số kiểm tra tài khoản trước khi gửi; yêu cầu khách xác nhận thông tin không khớp | Người vận hành hoàn phí |
| 7 | Hệ thống* | Đối chiếu `ledger_write_status` với `customer_refund_notice`; cảnh báo mọi thông báo thành công khi chưa có xác nhận sổ cái | Chỉ báo thành công sau ACK; lỗi 503 thì giữ trạng thái chờ và chuyển nhân viên, không retry mù | Kỹ sư tích hợp |
| 3 | Ngữ cảnh* | Theo dõi `refund_destination` và event mở lại/phản ánh; rà soát hàng tuần nếu có khách hiểu sai phương thức nhận | Nêu rõ tiền về ví LogiX, thời gian dự kiến và lựa chọn/kênh hỗ trợ trước khi khách xác nhận | Thiết kế trải nghiệm khách hàng |
| 11 | Giới hạn hệ thống* | Ghi `unsupported_input_type`; báo cáo hàng tuần số/tỷ lệ tin nhắn thoại không xử lý được | Báo rõ giới hạn, cung cấp chuyển giọng nói thành văn bản hoặc chuyển nhân viên kèm transcript | Chủ sản phẩm trợ lý |
| 5 | Ngầm* | Đối soát hàng tuần giá trị hoàn với giá sau giảm; cảnh báo mọi chênh lệch khác 0 và tổng tiền vượt ngưỡng kiểm soát | Sửa công thức dùng giá thực trả sau giảm; rà soát hồi tố các giao dịch từ lần cập nhật gần nhất và hoàn phần chênh | Chủ chính sách hoàn phí |

\* Phân loại và biện pháp ở bảng này là bản dự thảo dựa trên ca chính thức; cần nhóm xác nhận sau khi so hai bộ nhãn.

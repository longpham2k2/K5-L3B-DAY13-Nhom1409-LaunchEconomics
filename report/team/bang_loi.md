# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Trọng Đạt · Người gắn nhãn 2: Đặng Khắc Hoàng Minh.

**Lưu ý:** Nhãn người 1 được giữ nguyên từ bản của Đạt. Cột người 2 là bản gợi ý do AI soạn, chưa được Minh xác nhận độc lập. Cột Trùng? so sánh tên loại, bỏ qua ghi chú nguồn AI. Nhãn thống nhất dưới đây là đề xuất đối chiếu tài liệu, cần Đạt và Minh xác nhận; chưa phải kết quả thảo luận của hai người.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng (gợi ý AI) | Có | Do người dùng (đề xuất) |
| 2 | Ngầm | Hệ thống (gợi ý AI) | Không | Hệ thống (đề xuất) |
| 3 | Ngữ cảnh | Ngữ cảnh (gợi ý AI) | Có | Ngữ cảnh (đề xuất) |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống (gợi ý AI) | Có | Giới hạn hệ thống (đề xuất) |
| 5 | Ngầm | Ngầm (gợi ý AI) | Có | Ngầm (đề xuất) |
| 6 | Do người dùng | Do người dùng (gợi ý AI) | Có | Do người dùng (đề xuất) |
| 7 | Hệ thống | Hệ thống (gợi ý AI) | Có | Hệ thống (đề xuất) |
| 8 | Ngầm | Hệ thống (gợi ý AI) | Không | Hệ thống (đề xuất) |
| 9 | Do người dùng | Do người dùng (gợi ý AI) | Có | Do người dùng (đề xuất) |
| 10 | Ngữ cảnh | Ngữ cảnh (gợi ý AI) | Có | Ngữ cảnh (đề xuất) |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống (gợi ý AI) | Có | Giới hạn hệ thống (đề xuất) |
| 12 | Ngầm | Ngầm (gợi ý AI) | Có | Ngầm (đề xuất) |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống (gợi ý AI) | Có | Giới hạn hệ thống (đề xuất) |
| 14 | Do người dùng | Do người dùng (gợi ý AI) | Có | Do người dùng (đề xuất) |
| 15 | Hệ thống | Hệ thống (gợi ý AI) | Có | Hệ thống (đề xuất) |
| 16 | Ngữ cảnh | Ngữ cảnh (gợi ý AI) | Có | Ngữ cảnh (đề xuất) |
| 17 | Ngầm | Ngầm (gợi ý AI) | Có | Ngầm (đề xuất) |
| 18 | Ngữ cảnh | Ngữ cảnh (gợi ý AI) | Có | Ngữ cảnh (đề xuất) |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống (gợi ý AI) | Có | Giới hạn hệ thống (đề xuất) |
| 20 | Hệ thống | Hệ thống (gợi ý AI) | Có | Hệ thống (đề xuất) |

**Tỉ lệ đồng thuận (đối chiếu tạm):** 18 / 20 = 90%. Hai bộ nhãn khác nhau ở ca 2 và 8. Đây chưa phải tỉ lệ đồng thuận giữa hai người gắn nhãn độc lập; cần Minh tự rà và xác nhận bộ nhãn người 2 trước khi dùng làm kết quả CP3.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 2: Đề xuất Hệ thống; lỗi xử lý đã biểu hiện trong vận hành, khác Ngầm là sai sót chưa được nhận ra cho tới khi kiểm tra.
- Ca 8: Đề xuất Hệ thống; sai trích dẫn đã nhìn thấy được, không thuộc lỗi Ngầm.
- Hai quy tắc trên là đề xuất dựa trên tài liệu hướng dẫn, cần hai người xác nhận; không thay đổi nhãn độc lập ban đầu.

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

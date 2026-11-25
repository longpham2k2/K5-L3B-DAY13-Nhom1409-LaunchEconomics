# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Số tính bằng `src/lab13.py` (phần E1). Đây là chỉ số trong đợt chạy thử 2 tuần ở 6 depot; đợt chạy thử không có nhóm đối chứng nên không dùng để kết luận về tác động của trợ lý.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); phạm vi `noi_dia` + `hang_nang` 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được mở bằng trợ lý | Số yêu cầu nhóm trợ lý có `agent_suggestion_shown` và nhân viên mở gợi ý, chia số yêu cầu `refund_request_created` có `arm` = trợ lý, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm, ví dụ ca 5 và 17 trong `bang_loi.md`) | Số đơn trong mẫu 100 đơn/tuần có `so_tien_da_hoan` khác `so_tien_dung`, chia 100 | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent (`logix_runs.csv` đã có cột `trace_id`).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm (trợ lý / đối chứng), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, opened (có / không), trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | request_id, staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | request_id, phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | request_id, reason (thieu_du_lieu / ngoai_pham_vi / het_lan_chay), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua (ok / loi), trace_id | Khi ghi sổ cái hoàn tiền |
| `ticket_closed` | Hệ thống ticket | request_id, created_at, closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, bang_gia_version, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`; tách theo `arm`.
- Dùng (bỏ qua gợi ý): `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`.
- An toàn (mở lại): `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia số `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown` có opened = có, chia `refund_request_created` có arm = trợ lý.
- An toàn (tự đề xuất): `audit_sample_checked` có so_tien_da_hoan khác so_tien_dung, chia số đơn trong mẫu.
- Chi phí mỗi việc thành công trong pilot: `agent_run_completed` (token, tool), `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho cột simulated), chia số yêu cầu thành công. Hoàn trùng (luật dừng): hai `refund_ledger_write` ok cùng request_id.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

# Báo cáo cá nhân — Đặng Khắc Hoàng Minh

## 1. Thông tin thành viên

- Họ tên: Đặng Khắc Hoàng Minh
- MSSV: Chưa được ghi trong `TEAM.md`; cần bổ sung để đổi tên file theo quy định.
- Email: Chưa được ghi trong `TEAM.md`.
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ.

## 2. Phần việc phụ trách

- Cập nhật `report/team/ho_so_launch_v0.md` xuyên suốt các checkpoint.
- CP3: rà soát bộ nhãn người gắn nhãn 2, cùng người gắn nhãn 1 thống nhất các ca bất đồng; góp phần hoàn thiện quy tắc phân biệt và bảng khắc phục trong `report/team/bang_loi.md`.
- CP4: kiểm tra `report/team/pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?` ngoài chú thích.
- CP5: hoàn thiện hồ sơ launch v0 và tham gia chấm nhóm kế tiếp trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- Cập nhật hồ sơ launch với số liệu chi phí, so sánh phạm vi pilot, chỉ số, rủi ro và thiết kế pilot; đề xuất Go có điều kiện kèm tiêu chí và ngày quyết định.
- CP3: rà soát nhãn của 20 ca; hai ca bất đồng (2 và 8) được nhóm thống nhất nhãn cuối là Hệ thống. Đồng thuận ban đầu là 18/20 (90%).
- Hoàn thiện bảng khắc phục cho năm loại lỗi, gồm cách phát hiện, biện pháp và vai trò phụ trách.
- Xác nhận YAML đọc được và không có dấu `?` ngoài chú thích.

## 4. Bằng chứng

- `report/team/ho_so_launch_v0.md`: bảy mục hồ sơ launch, đề xuất Go có điều kiện, các ngưỡng vận hành và ngày quyết định 12/01/2027.
- `report/team/bang_loi.md`: 20 ca, tỷ lệ đồng thuận 18/20 = 90%, kết luận hai ca bất đồng và bảng khắc phục năm loại.
- `report/team/pilot_plan.yaml`: kế hoạch chia theo nhân viên, 20 cụm mỗi nhánh, 299 yêu cầu mỗi cụm và các luật dừng.
- Kiểm tra CP4 bằng `yaml.safe_load`: đọc thành công; rà các dòng ngoài chú thích không tìm thấy dấu `?`.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT để hỗ trợ tính/đối chiếu một số số liệu từ bảng chi phí, soạn nháp nội dung hồ sơ và gợi ý nhãn/biện pháp khắc phục.
- Tự rà nội dung với `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml` và đề bài; xác nhận với nhóm rằng ca 2 và 8 có nhãn thống nhất là Hệ thống.
- Nhãn CP3 có AI hỗ trợ; không coi phần gợi ý AI là một phép gắn nhãn độc lập. Tỷ lệ 18/20 được tính từ hai bộ nhãn độc lập đã ghi trong `bang_loi.md`.

## 6. Tự đánh giá

- Hoàn thành phần giữ hồ sơ, kiểm tra YAML và phối hợp chốt nhãn/biện pháp CP3.
- Cần bổ sung MSSV, email và thông tin/ bằng chứng thực tế về phần chấm chéo nhóm trước khi nộp bản cuối.

# Team

## Thông tin nhóm

- Tên nhóm: Nhom1409
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom1409-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/longpham2k2/K5-L3B-DAY13-Nhom1409-LaunchEconomics · nhánh `main` · commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Ngọc Long | 2A202604111 |       | longpham2k2 | Người viết code (CP1–CP2) |
|   2 | Nguyễn Công Huy | 2A202604086 | conghuycr@gmail.com | HyperSyst | Người kiểm số (CP1–CP2), người viết code sau giờ giải lao (CP3–CP5) |
|   3 | Trần Trọng Đạt |      |       | dtr-uep | Người gắn nhãn 1 |
|   4 | Đặng Khắc Hoàng Minh |      |       | dangkhacm-a11y | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## PhamNgocLong-2A202604111

### Phần việc phụ trách

- Người viết code CP1–CP2: cài môi trường, viết ba hàm A1 và `mo_hinh()` trong `src/lab13.py`, tính theo từng `loai` (A3), cộng chi phí cố định (A4).
- Viết các kịch bản độ nhạy B1–B4 trong `src/lab13.py`.
- CP3: cùng Huy hoàn thiện CP2 trong lúc hai người gắn nhãn làm việc; CP4: kiểm số cỡ mẫu.
- CP5: viết ba chỉ số và danh sách event trong `report/team/chi_so.md`; bảo vệ hồ sơ tại Gate 2a; commit và push bài nộp.

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenCongHuy-2A202604086

### Phần việc phụ trách

- CP1–CP2: Kiểm số từ trace, đối chiếu phép tính với `src/lab13.py` và cập nhật bảng chi phí, phân tích độ nhạy.
- CP3: Hỗ trợ rà soát bảng lỗi và kết quả đối chiếu hai bộ nhãn của Đạt và Minh.
- CP4: Kiểm tra kết quả D1 trong `src/lab13.py`, hoàn thiện và kiểm tra `report/team/pilot_plan.yaml`.
- CP5: viết các dòng rủi ro kinh tế (lấy số từ bảng độ nhạy) trong `report/team/chi_so.md`; bảo vệ hồ sơ tại Gate 2a; viết `report/team/group_report.md`.

### Đóng góp cụ thể

- CP1: Hoàn thiện bảng A1–A4 và giải thích cách phân bổ 40 triệu đ chi phí cố định mỗi tháng. Chi phí sau khi cộng khoản cố định là 4.599 đ và 5.784 đ mỗi việc thành công ở hai mức khối lượng [simulated].
- CP2: Điền 9 kịch bản B1, giải thích cách tính và xếp hạng yếu tố ở B2, lập bảng so sánh ba giới hạn chạy ở B3.
- CP3: Kiểm tra tỉ lệ trùng nhãn 18/20 (90%), xác định hai ca khác nhãn (2 và 8) và rà soát bảng khắc phục đủ năm loại lỗi.
- CP4: Điền D1–D2, đối chiếu tỉ lệ mở lại 3,97% trong dữ liệu giả lập và chọn cách chia ngẫu nhiên theo nhân viên với 20 người mỗi nhóm, tối thiểu 299 yêu cầu mỗi người. Viết bốn luật dừng, làm rõ điều kiện chuyển bước rollout và yêu cầu tắt trợ lý chậm nhất 30 phút sau khi xác minh sự cố.

### Bằng chứng

- CP1 và CP2: Commit `7980daf` và `e35180e` trong [bảng chi phí](report/team/bang_chi_phi.md).
- CP3: [Bảng lỗi dùng để đối chiếu](report/team/bang_loi.md).
- CP4: Commit `5d1345a` trong [kế hoạch pilot](report/team/pilot_plan.yaml). Phép tính D1 lấy từ `src/lab13.py`, commit `49f24f5` của Long.
- [Báo cáo cá nhân](report/team/2A202604086_NguyenCongHuy.md).

## TranTrongDat-MSSV

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" của từng checkpoint (A2 đủ 9 dòng có nhãn `simulated`, A3 đủ 4 dòng, quy tắc "giảm một nửa").
- CP3: gắn nhãn độc lập 20 ca lỗi; cùng Minh so nhãn, tính tỉ lệ đồng thuận, viết quy tắc phân biệt và bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- CP4: điền mọi dấu `?` và ít nhất ba luật dừng trong `report/team/pilot_plan.yaml`.
- CP5: kiểm tra không còn từ "production"; chấm nhóm n + 1 vào `report/team/phieu_cham.md`.

### Đóng góp cụ thể

-

### Bằng chứng

-

## DangKhacHoangMinh-MSSV

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` từ đầu buổi, cập nhật số sau mỗi checkpoint.
- CP3: gắn nhãn độc lập 20 ca lỗi; cùng Đạt so nhãn, tính tỉ lệ đồng thuận, viết quy tắc phân biệt và bảng khắc phục trong `report/team/bang_loi.md`.
- CP4: kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?`.
- CP5: hoàn thiện hồ sơ launch v0 (một trang, bảy mục, dòng cuối là đề xuất Go / Go có điều kiện / No-go); chấm nhóm n + 1 vào `report/team/phieu_cham.md`.

### Đóng góp cụ thể

-

### Bằng chứng

-

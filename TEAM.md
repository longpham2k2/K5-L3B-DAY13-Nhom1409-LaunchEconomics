# Team

## Thông tin nhóm

- Tên nhóm: Nhom1409
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom1409-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/longpham2k2/K5-L3B-DAY13-Nhom1409-LaunchEconomics · nhánh `main` · commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Ngọc Long | 2A202604111 |       | longpham2k2 | Người viết code (CP1, CP2, CP4, CP5 · E1), nhóm trưởng |
|   2 | Nguyễn Công Huy | 2A202604086 | conghuycr@gmail.com | HyperSyst | Người kiểm số (CP1–CP2), người viết code sau giờ giải lao (CP3–CP5) |
|   3 | Trần Trọng Đạt | 2A202604030 |       | dtr-uep | Người gắn nhãn 1 |
|   4 | Đặng Khắc Hoàng Minh | 2A202604082 |       | dangkhacm-a11y | Người gắn nhãn 2, kiêm giữ hồ sơ |

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

- Chuẩn bị: tạo repo nhóm, cài môi trường, chạy thử file khởi đầu, chia vai trong `TEAM.md`.
- Người viết code CP1, CP2, CP4 và E1 (CP5) trong `src/lab13.py`.
- CP5: đặc tả chỉ số, danh sách event và kiểm tra chéo trong `report/team/chi_so.md`.
- Gate 2a: tham gia hội đồng chấm nhóm Economics; commit và push bài nộp.

### Đóng góp cụ thể

- CP1–CP2: ba hàm A1 (ba phép thử ĐẠT), `mo_hinh()` (4.472 đ/việc thành công, gấp 16,3× hoá đơn token chia số yêu cầu [simulated]), tách theo loại, chi phí cố định, 9 kịch bản độ nhạy kèm tự kiểm tra, B2–B4.
- CP4: cỡ mẫu D1 (1.251 theo yêu cầu; 84 người > 40 khi chia theo nhân viên; m ≥ 299 cho mức chênh 6 điểm; power 0,64 ở 5 điểm) và tỉ lệ mở lại hiện tại 4,25%.
- CP5: ba chỉ số trong đợt chạy thử (82,83% · 27,12% · 4,25%), hai chỉ số đề xuất, 10 event có `trace_id` và kiểm tra chéo chỉ số ↔ event.
- Hồ sơ launch: con số cho mục 1 và mục 3 (toàn mẫu 5.865 đ/yêu cầu = 0,49× [simulated]).
- Gate 2a: đặt câu hỏi của hội đồng cho nhóm Economics về lựa chọn cách chia (theo yêu cầu, nhân viên hay depot).

### Bằng chứng

- Commit `0129a02` (`TEAM.md`), `94a40ba` (CP1), `6d941fb` (CP2), `49f24f5` (CP4), `74e586f` (CP5 · E1, `chi_so.md`), `1fa2d3f` (hồ sơ launch).
- [Báo cáo cá nhân](report/team/2A202604111_PhamNgocLong.md).

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

## TranTrongDat-2A202604030

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" của từng checkpoint, kiểm tra nhãn `simulated`.
- CP2: câu trả lời B3 trong `report/team/bang_chi_phi.md`.
- CP3: gắn nhãn người 1 cho 20 ca lỗi; cùng Minh đối chiếu và thống nhất nhãn trong `report/team/bang_loi.md`.
- CP4: hoàn thiện `report/team/pilot_plan.yaml` (luật dừng, điều kiện chuyển bước, quy tắc quyết định).

### Đóng góp cụ thể

- CP1–CP2: kiểm tra A1 (1,20 · 1,25 · 1,25), A2 đủ 9 dòng, A3 đủ 4 loại, A4 có chi phí cố định, nhãn `simulated`; rà soát B1, B2 và quy tắc "giảm một nửa = nửa mức tăng".
- B3: giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ), giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) nhưng để lại thêm 85 yêu cầu cho nhân viên [simulated].
- CP3: bộ nhãn người 1 cho 20 ca theo năm loại Google PAIR; xử lý conflict khi hợp nhất bảng lỗi, giữ nguyên hai cột nhãn ban đầu.
- CP4: sửa bốn luật dừng (mở lại, hoàn trùng, chi phí, mức độ sử dụng) để vế KHÔNG THÌ ghi rõ việc bị cấm; thêm quy tắc không gộp mẫu trước và sau khi đổi phạm vi; phân biệt MDE 6 điểm với mục tiêu 5 điểm của đề; kiểm tra YAML đọc được.

### Bằng chứng

- Commit `bf7dc1e`, `b697341`, `eb99a82` (B3); `96173af`, `385990a`, `5a5c051` (nhãn người 1 và hợp nhất bảng lỗi); `34d104d` (kế hoạch pilot); `4996340`, `ae7a9c4` (báo cáo cá nhân).
- [Báo cáo cá nhân](report/team/2A202604030_TranTrongDat.md).

## DangKhacHoangMinh-2A202604082

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` qua các checkpoint.
- CP2: câu trả lời B4 trong `report/team/bang_chi_phi.md`.
- CP3: bộ nhãn người 2 và bảng khắc phục trong `report/team/bang_loi.md`.
- CP5 và Gate 2a: hoàn thiện hồ sơ launch v0; điền phiếu chấm nhóm Economics trong `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Hồ sơ launch: điền thông tin nhóm, mục 1–7 (chi phí, độ nhạy, so với nhân viên tự làm, chỉ số, bảng lỗi, pilot plan, rủi ro kinh tế) và đề xuất Go có điều kiện kèm điều kiện, người phụ trách và ngày quyết định 12/01/2027.
- B4: xem lại 100% ở `noi_dia` + `hang_nang` tốn 11.743 đ (0,98×) hoặc 12.415 đ (1,03×) mỗi việc thành công; hoà vốn khi xem lại ≤ 5,12 hoặc ≤ 4,80 phút/ca [simulated].
- CP3: bộ nhãn người 2 có AI gợi ý, Minh rà lại và đồng ý (đã ghi rõ trong `bang_loi.md` và báo cáo cá nhân, nên chưa phải gắn nhãn độc lập thuần túy); đồng thuận ban đầu với nhãn người 1 là 18/20 (90%); cùng Đạt thống nhất ca 2 và 8 là Hệ thống; bảng khắc phục 5 ca đủ năm loại.
- Kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?`.
- Gate 2a: điền phiếu chấm nhóm Economics (25/30, Go có điều kiện).

### Bằng chứng

- Commit `4be046c`, `ec58d4b`, `8be7e2e`, `b200582` (hồ sơ launch, B4, phiếu chấm); `42fec18`, `992fdc6`, `81d607d` (nhãn người 2, đối chiếu nhãn, ghi chú AI); `4fa3b55` (báo cáo cá nhân).
- [Báo cáo cá nhân](report/team/2A202604082_DangKhacHoangMinh.md).

# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 lần giá một lần chạy |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, token và tool của lần chạy thứ 2 và 3 | 93.804 | `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 | 890 phút từ `phut_xem_lai_simulated` × 2.000 đ/phút | simulated |
| Làm lại | 2.264.000 | 1.132 phút từ `phut_lam_lai_simulated` × 2.000 đ/phút | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua = thanh_cong` | |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (Token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,3 lần hoá đơn chia cho số yêu cầu [simulated].
- Làm lại chiếm 51,8% tổng chi phí, cao nhất trong các khoản [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22x |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69x |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88x |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85x |

- Nên để nhân viên xử lý `quoc_te`: trợ lý chỉ đạt 27,3% thành công và tốn 22.515 đ mỗi việc thành công, bằng 1,88 lần mức 12.000 đ [simulated].
- Ở `quoc_te`, giới hạn 1, 2 và 3 lần chạy lần lượt cho 32, 41 và 41 việc thành công. Tỉ lệ `ok` trong số lượt thực hiện ở từng lần là 30,0%, 11,4% và 2,2%.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

1. **Ước tính số việc thành công mỗi tháng.** Trong 1.200 yêu cầu của toàn mẫu, có 783 việc thành công thuộc `noi_dia` và 117 việc thành công thuộc `hang_nang`. Giả sử cơ cấu yêu cầu và tỉ lệ thành công giữ nguyên, nhân tổng khối lượng tháng với (783 + 117) ÷ 1.200 = 75,0%.
2. **Tính chi phí biến đổi mỗi việc thành công.** Trong phạm vi hai loại, tổng token, tool, xem lại và làm lại là 3.072.513 đ. Chia cho 900 việc thành công được khoảng 3.414 đ/việc [simulated].
3. **Phân bổ chi phí cố định.** Chia 40.000.000 đ/tháng cho số việc thành công ước tính mỗi tháng. Cộng kết quả với chi phí biến đổi ở bước 2, rồi chia cho 12.000 đ để so sánh. Các kết quả trong bảng được làm tròn sau khi tính.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 45.000 × 75,0% = 33.750 | 40.000.000 ÷ 33.750 ≈ 1.185 đ | 4.599 đ | 0,38x |
| 22.500 yêu cầu/tháng | 22.500 × 75,0% = 16.875 | 40.000.000 ÷ 16.875 ≈ 2.370 đ | 5.784 đ | 0,48x |

- Khi khối lượng giảm một nửa, chi phí cố định mỗi việc tăng gấp đôi, từ 1.185 đ lên 2.370 đ. Tổng chi phí mỗi việc thành công vẫn dưới mốc 12.000 đ ở cả hai mức, lần lượt là 4.599 đ và 5.784 đ [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...

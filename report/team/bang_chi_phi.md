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
- Theo công thức B3, chi phí cả hệ thống là 5.865 đ/yêu cầu, bằng 0,49 lần mức 12.000 đ nếu nhân viên tự làm [simulated].

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

Với 40 triệu đ chi phí cố định mỗi tháng, lấy 900 việc thành công thuộc phạm vi pilot trên 1.200 yêu cầu toàn mẫu để quy đổi theo tổng khối lượng tháng. Chi phí biến đổi trong phạm vi này là 3.414 đ mỗi việc thành công [simulated].

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38x |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48x |

- Sau khi cộng chi phí cố định, cả hai mức 4.599 đ và 5.784 đ mỗi việc thành công đều thấp hơn mốc 12.000 đ [simulated].

## B1 · Đổi từng yếu tố

Mốc so sánh là 4.472 đ mỗi việc thành công ở A2 [simulated]. Phần trăm thay đổi được tính trước khi làm tròn chi phí.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có `attempt > 2`. Yêu cầu có `so_lan_chay > 2` chuyển sang nhân viên, phút xem lại và làm lại của trợ lý bằng 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi đưa chi phí lên 6.543 đ mỗi việc thành công, tăng 46,3% (5,6% + 40,7%) [simulated].
- Ba yếu tố ảnh hưởng mạnh nhất theo các kịch bản B1 là số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%) và lương nhân viên (+23,1%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công, theo giả định nhân viên xử lý các yêu cầu đó.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ (rẻ nhất) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn 2 lần có chi phí cả hệ thống thấp nhất (6.901.220 đ). Giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) và để lại thêm 85 yêu cầu cho nhân viên so với giới hạn 2 lần [simulated].

## B4 · Nếu phải xem lại tất cả

Trong 982 yêu cầu `noi_dia` và `hang_nang`, xem lại 948 yêu cầu có lượt chạy `ok` trong 5 phút mỗi ca, tính thời gian làm lại cho 48 ca và cộng 224.513 đ tiền token và tool. Chia tổng chi phí cho 900 việc thành công.

| Thời gian làm lại mỗi ca | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] | Thời gian xem lại tối đa để hoà vốn [simulated] |
| --- | ---: | ---: | ---: |
| 9 phút theo đề | 11.743 đ | 0,98x | khoảng 5,12 phút/ca |
| 15,3 phút trung bình toàn mẫu [simulated] | 12.415 đ | 1,03x | khoảng 4,80 phút/ca |

- Khi xem lại 100% trong 5 phút mỗi ca, chi phí nằm sát mốc 12.000 đ [simulated]. Pilot cần xác định có thể giảm tỉ lệ xem lại đến mức nào mà vẫn an toàn và có thể rút thời gian xem lại xuống dưới 5 phút mỗi ca hay không.

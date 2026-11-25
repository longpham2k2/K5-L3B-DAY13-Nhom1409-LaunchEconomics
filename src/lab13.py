"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Cắt các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn sẽ chuyển cho nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai

    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('inf'),
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f"{'gap_lan':12s} {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:>14,.1f}  (cps / hoá đơn mỗi yêu cầu)")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  ti trong {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:6.1%}")

    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\nA3 · Theo loại [cps: simulated]')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps':>8s} {'/12000':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {m['thanh_cong'] / len(r):9.1%} {so_chay / len(r):8.2f} "
              f"{m['cps']:8,.0f} {m['cps'] / BASELINE:6.2f}x")

    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['ok'] = (runs_loai['status'] == 'ok').astype(float)
    print('\nTỉ lệ ok theo lần thử (attempt):')
    print(runs_loai.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---------- Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    CO_DINH = 40_000_000   # đồng / tháng
    YC_THANG = 45_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    m_pv = mo_hinh(runs, pham_vi)
    print(f"\nA4 · Phạm vi noi_dia + hang_nang: {m_pv['thanh_cong']} việc thành công / {len(reqs)} yêu cầu mẫu, "
          f"cps = {m_pv['cps']:,.0f} đ [simulated]")
    for ten, kl in [('45.000 yc/tháng', YC_THANG), ('một nửa', YC_THANG / 2)]:
        tc_thang = kl * m_pv['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = CO_DINH / tc_thang
        tong_moi_viec = m_pv['cps'] + co_dinh_moi_viec
        print(f"  {ten:16s} tc/tháng {tc_thang:>8,.0f} · cố định/việc {co_dinh_moi_viec:>6,.0f} đ · "
              f"cps + cố định {tong_moi_viec:>6,.0f} đ · {tong_moi_viec / BASELINE:.2f}x")
    # ---------- Nhiệm vụ B1 · Đổi từng yếu tố ----------
    goc = ket_qua['cps']
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    print(f'\nB1 · Độ nhạy [simulated] · gốc {goc:,.0f} đ')
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = cps / goc - 1
        print(f'  {ten:24s} {cps:8,.0f} đ {thay_doi[ten]:+7.1%}')

    # Tự kiểm tra: "giảm một nửa" = nửa mức tăng của "gấp đôi" (mô hình tuyến tính)
    for x2, x05 in [('Giá token gấp đôi', 'Giá token giảm một nửa'),
                    ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
                    ('Làm lại gấp đôi', 'Làm lại giảm một nửa')]:
        assert abs(thay_doi[x05] + thay_doi[x2] / 2) < 1e-9, f'{x05} phải bằng -1/2 của {x2}'
    print('  Tự kiểm tra "giảm một nửa = nửa mức tăng": ĐẠT')

    # ---------- Nhiệm vụ B2 · Đổi một cặp và xếp hạng ----------
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'\nB2 · Token ×2 + xem lại ×2: {cps_cap:,.0f} đ {cps_cap / goc - 1:+.1%} '
          f'(tổng hai tác động riêng {tong_rieng:+.1%}) [simulated]')
    yeu_to = {'Số ca làm lại': thay_doi['Làm lại gấp đôi'],
              'Tỉ lệ xem lại': thay_doi['Xem lại gấp đôi'],
              'Lương nhân viên (+25%)': thay_doi['Lương tăng 25%'],
              'Giá token': thay_doi['Giá token gấp đôi']}
    xep_hang = sorted(yeu_to.items(), key=lambda kv: -abs(kv[1]))
    print('  Xếp hạng: ' + ' · '.join(f'{i}. {t} ({v:+.1%})' for i, (t, v) in enumerate(xep_hang[:3], 1)))

    # ---------- Nhiệm vụ B3 · Giới hạn chạy lại có thật sự rẻ hơn ----------
    # Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay)
    print('\nB3 · Giới hạn số lần chạy [simulated]')
    print(f"  {'giới hạn':>8s} {'tổng trợ lý':>12s} {'không tc':>9s} {'cả hệ thống':>12s} {'cps':>7s}")
    b3 = {}
    for k in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        he_thong = m['tong'] + BASELINE * khong_tc
        b3[k] = (he_thong, m['cps'], khong_tc)
        print(f"  {k:>8d} {m['tong']:>12,.0f} {khong_tc:>9d} {he_thong:>12,.0f} {m['cps']:>7,.0f}")
    re_nhat_ht = min(b3, key=lambda k: b3[k][0])
    re_nhat_cps = min(b3, key=lambda k: b3[k][1])
    print(f'  Rẻ nhất cho công ty: {re_nhat_ht} lần · cps thấp nhất: {re_nhat_cps} lần · '
          f'chênh {b3[re_nhat_cps][2] - b3[re_nhat_ht][2]} yêu cầu chuyển nhân viên')

    # ---------- Nhiệm vụ B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ----------
    PHUT_XEM_LAI = 5      # phút xem lại mỗi yêu cầu có lần chạy ok
    PHUT_LAM_LAI = 9      # phút làm lại mỗi ca lam_lai (theo đề)
    pv_runs = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_yc_ok = pv_runs.loc[pv_runs['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = m_pv['token'] + m_pv['tool']
    tc_pv = m_pv['thanh_cong']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()  # simulated
    print(f'\nB4 · Xem lại 100% · {len(pham_vi)} yêu cầu, {so_yc_ok} có lần chạy ok, '
          f'{so_lam_lai} ca làm lại, token+tool {token_tool_pv:,.0f} đ, {tc_pv} việc thành công [simulated]')
    for nhan, phut_ll in [('9 phút theo đề', PHUT_LAM_LAI),
                          (f'{phut_lam_lai_tb:.1f} phút TB toàn mẫu', phut_lam_lai_tb)]:
        tien_ll = so_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = so_yc_ok * PHUT_XEM_LAI * LUONG_PHUT + tien_ll + token_tool_pv
        cps_b4 = tong_b4 / tc_pv
        # Hoà vốn: số phút xem lại tối đa để cps = 12.000 đ
        phut_hoa_von = (BASELINE * tc_pv - tien_ll - token_tool_pv) / (so_yc_ok * LUONG_PHUT)
        print(f'  làm lại {nhan:22s} cps {cps_b4:>7,.0f} đ · {cps_b4 / BASELINE:.2f}x · '
              f'hoà vốn khi xem lại ≤ {phut_hoa_von:.2f} phút/ca')

    # ---------- Nhiệm vụ D1 · Cỡ mẫu theo ba cách chia ----------
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    P1, ALPHA, POWER, ICC = 0.70, 0.05, 0.80, 0.02

    def co_mau(p1, p2, alpha=ALPHA, power=POWER):
        """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức z, z chính xác)."""
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    def he_so_thiet_ke(m, icc=ICC):
        return 1 + (m - 1) * icc

    n5 = co_mau(P1, P1 + 0.05)
    n6 = co_mau(P1, P1 + 0.06)
    de75 = he_so_thiet_ke(75)
    n_nv = math.ceil(n5 * de75)
    nv_moi_nhom = math.ceil(n_nv / 75)
    # e) 20 cụm: 20m / (1 + (m-1)·ICC) >= n6  →  m >= n6·(1-ICC) / (20 - n6·ICC)
    m_can = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    # Power thật nếu tác động chỉ là 5 điểm mà cỡ mẫu tính cho 6 điểm
    es5 = abs(proportion_effectsize(P1 + 0.05, P1))
    power_thuc = NormalIndPower().power(effect_size=es5, nobs1=n6, alpha=ALPHA)

    print('\nD1 · Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02)')
    print(f'  a) Theo yêu cầu, +5 điểm:          {n5:,} yêu cầu mỗi nhóm')
    print(f'  b) Theo nhân viên, m = 75:         DE {de75:.2f} → {n_nv:,} mỗi nhóm = {nv_moi_nhom} người/nhóm, '
          f'tổng {2 * nv_moi_nhom} > 40 → không đủ người')
    print(f'  c) 20 nhân viên mỗi nhóm:          tối đa 20 / ICC = {20 / ICC:,.0f} < {n5:,} → không đạt')
    print(f'  d) 6 depot mỗi nhóm:               tối đa 6 / ICC = {6 / ICC:,.0f}')
    print(f'  e) +6 điểm ({n6:,}/nhóm), 20 người: m ≥ {m_can} yêu cầu mỗi người '
          f'(DE {he_so_thiet_ke(m_can):.2f})')
    print(f'  Power nếu tác động thật chỉ 5 điểm với n = {n6:,}: {power_thuc:.2f}')

    # ---------- Nhiệm vụ D3 · Tỉ lệ mở lại hiện tại (trước khi đặt luật an toàn) ----------
    mo_lai = reqs['mo_lai_trong_7_ngay'].astype(int)
    mo_lai_pv = pham_vi['mo_lai_trong_7_ngay'].astype(int)
    print(f'\nD3 · mo_lai_trong_7_ngay hiện tại: {mo_lai.mean():.2%} ({mo_lai.sum()}/{len(reqs)}); '
          f'phạm vi noi_dia + hang_nang: {mo_lai_pv.mean():.2%} ({mo_lai_pv.sum()}/{len(pham_vi)})')

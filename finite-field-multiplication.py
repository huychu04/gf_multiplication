
"""
Phep nhan trong truong huu han GF(2^4) va GF(2^8).

GF(2^4): p(x) = x^4 + x + 1       -> 0x13
GF(2^8): p(x) = x^8 + x^4 + x^3 + x + 1 -> 0x11B
"""


def gf_multiply(a: int, b: int, m: int, modulus: int) -> int:
    """
    Nhan hai phan tu a, b trong GF(2^m).

    a, b: cac phan tu duoc bieu dien bang so nguyen
    m: bac cua truong
    modulus: da thuc bat kha quy, bao gom bit x^m
    """
    if m < 1:
        raise ValueError("m phai lon hon hoac bang 1")

    if modulus < (1 << m) or modulus >= (1 << (m + 1)):
        raise ValueError("Da thuc modulus khong hop le voi bac m")

    if not (0 <= a < (1 << m) and 0 <= b < (1 << m)):
        raise ValueError(f"a va b phai nam trong [0, {((1 << m) - 1)}]")

    result = 0

    while b > 0:
        # Neu bit thap nhat cua b bang 1, cong a vao ket qua.
        if b & 1:
            result ^= a

        # Nhan a voi x bang phep dich trai.
        a <<= 1

        # Neu bac cua a dat den m, rut gon theo modulus.
        if a & (1 << m):
            a ^= modulus

        # Xet bit tiep theo cua b.
        b >>= 1

    return result


def multiply_gf16(a: int, b: int) -> int:
    """Phep nhan trong GF(2^4), voi p(x) = x^4 + x + 1."""
    return gf_multiply(a, b, 4, 0x13)


def multiply_gf256(a: int, b: int) -> int:
    """Phep nhan trong GF(2^8), voi p(x) = x^8 + x^4 + x^3 + x + 1."""
    return gf_multiply(a, b, 8, 0x11B)


def run_tests():
    # Kiem tra cac tinh chat co ban trong GF(2^4).
    assert multiply_gf16(0x0, 0x7) == 0x0
    assert multiply_gf16(0x1, 0x7) == 0x7
    assert multiply_gf16(0x5, 0x3) == multiply_gf16(0x3, 0x5)

    # Kiem tra cac tinh chat co ban trong GF(2^8).
    assert multiply_gf256(0x00, 0xA5) == 0x00
    assert multiply_gf256(0x01, 0xA5) == 0xA5
    assert multiply_gf256(0x57, 0x83) == 0xC1
    assert multiply_gf256(0x12, 0x34) == multiply_gf256(0x34, 0x12)

    # Kiem tra ket qua luon nam trong mien bieu dien.
    for a in range(16):
        for b in range(16):
            assert 0 <= multiply_gf16(a, b) < 16

    for a in range(256):
        for b in range(256):
            assert 0 <= multiply_gf256(a, b) < 256

    print("Tat ca cac test deu thanh cong!")


def main():
    print("=== Phep nhan trong GF(2^4) ===")
    a4 = int(input("Nhap a (0..15, co the nhap 0x...): "), 0)
    b4 = int(input("Nhap b (0..15, co the nhap 0x...): "), 0)
    result4 = multiply_gf16(a4, b4)
    print(f"Ket qua: 0x{result4:X} ({result4})")

    print("\n=== Phep nhan trong GF(2^8) ===")
    a8 = int(input("Nhap a (0..255, co the nhap 0x...): "), 0)
    b8 = int(input("Nhap b (0..255, co the nhap 0x...): "), 0)
    result8 = multiply_gf256(a8, b8)
    print(f"Ket qua: 0x{result8:02X} ({result8})")


if __name__ == "__main__":
    run_tests()
    main()

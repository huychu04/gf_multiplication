# Thuật toán nhân trong trường hữu hạn GF(2⁴) và GF(2⁸)

## 1. Mục tiêu
Cài đặt thuật toán nhân hai phần tử trong trường hữu hạn GF(2⁴) và GF(2⁸) bằng Python, sử dụng đa thức bất khả quy tương ứng.

## 2. Đa thức bất khả quy

- **GF(2⁴):** P(x)=x^4+x+1, biểu diễn `0x13`.
- **GF(2⁸):** P(x)=x^8+x^4+x^3+x+1, biểu diễn `0x11B`.

## 3. Thuật toán
Sử dụng phép dịch bit, XOR và rút gọn đa thức theo đa thức bất khả quy để tính tích của hai phần tử trong trường hữu hạn.

## 4. Cấu trúc dự án

```text
finite-field-multiplication/
├── gf_multiplication.py
└── README.md
```

## 5. Hướng dẫn chạy

Yêu cầu: Python 3.8 trở lên, không cần thư viện ngoài.

```bash
python gf_multiplication.py
```

Chương trình thực hiện kiểm thử trước khi cho phép nhập dữ liệu để tính phép nhân.

## 6. Kiểm thử

- GF(2⁴): kiểm tra các trường hợp cơ bản và tính giao hoán.
- GF(2⁸): kiểm tra các trường hợp cơ bản và phép nhân `0x57 × 0x83 = 0xC1`.
- Kiểm tra kết quả nằm trong phạm vi biểu diễn của từng trường.

## 7. Thông tin dự án

- Ngôn ngữ: Python
- Mã nguồn: [GitHub Repository](https://github.com/huychu04/finite-field-multiplication)

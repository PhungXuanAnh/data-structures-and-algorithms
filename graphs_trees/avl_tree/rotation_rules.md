### 1. Quy tắc cốt lõi: "Ngoài bám chặt, Giữa sang tay"

Bất kể xoay trái hay xoay phải, hãy nhìn vào 2 nút đang thực hiện xoay (Cha và Con sắp lên làm Cha):

1. **Con Ngoài (Outer):** Luôn **trung thành**, dính chặt lấy cha hiện tại của nó (không đổi cha).
2. **Con Giữa (Inner):** Luôn **đổi chủ**, chuyển sang làm con của "ông kia" (nút còn lại trong cặp xoay).

> *Lưu ý:* Khi "đổi chủ", nó luôn đổi sang phía **đối diện** (đang là nhánh Phải thì sang làm nhánh Trái của chủ mới, và ngược lại).

---

### 2. Minh họa siêu ngắn gọn

Hãy tưởng tượng trục số ngang: `Nhỏ (P) --- [Giữa] --- Lớn (Q)`

**Khi Xoay Phải (P trồi lên, Q tụt xuống):**

* **Con Ngoài (của P):** Vẫn ở bên trái P.
* **Con Giữa (nhánh phải của P):** Đang nằm giữa P và Q. Khi P và Q tách ra, thằng Giữa này bị đẩy sang làm con trái của Q.

**Khi Xoay Trái (Q trồi lên, P tụt xuống):**

* **Con Ngoài (của Q):** Vẫn ở bên phải Q.
* **Con Giữa (nhánh trái của Q):** Đang nằm giữa P và Q. Nó bị đẩy sang làm con phải của P.

### 3. Áp dụng

Áp dụng với Cặp xoay: **40 (P)** và **60 (Q)** trong 2 ví dụ sau.

**Ví dụ con ngoài:**

```
     20  (Hệ số cân bằng: -2 -> Lệch PHẢI)
    /  \
  10    60  (Hệ số cân bằng: +1 -> Lệch TRÁI)
       /  \
     40    80
    /
   35
```

* Nút **35**: Là con trái của 40  Nó nằm ngoài cùng bên trái  Là **Con Ngoài**.
* *Kết quả:* **Bám chặt 40** (40 đi đâu 35 theo đó).

```
      20
     /  \
   10    40   <-- (40 lên)
        /  \
      35    60
              \
               80

```

**Ví dụ con giữa:**

```
     20  (Hệ số cân bằng: -2 -> Mất cân bằng về bên PHẢI)
    /  \
  10    60  (Hệ số cân bằng: +1 -> Lệch TRÁI)
       /  \
     40    80
      \
       50 (con phải của 40)
```

* Nút **50**: Là con phải của 40  Nó nằm kẹp giữa 40 và 60  Là **Con Giữa**.
* *Kết quả:* **Sang tay**. Từ con phải 40 Thành con trái 60.

```
                     20
                    /  \
                  10    40   <-- (40 đã lên thay 60)
                         \
                         60
                        /  \
    (con trái của 60) 50    80
```

**Túm lại, chỉ cần nhớ 1 câu thần chú:**

> **"Con ngoài giữ nguyên, con giữa đổi cha."**
import pytest

# Khai báo hàm movie_ticket (đã được ghi nhận)
def movie_ticket(age: int, time: int) -> int:
    # Kiểm tra đầu vào hợp lệ
    if not (0 <= age <= 120):
        raise ValueError("Tuổi không hợp lệ, phải trong khoảng [0,120]")
    if not (0 <= time <= 23):
        raise ValueError("Giờ chiếu không hợp lệ, phải trong khoảng [0,23]")

    # Xác định giá vé cơ bản theo tuổi
    if age < 12:
        base = 50000
    elif age < 60:
        base = 100000
    else:
        base = 70000

    # Giảm giá 20% nếu suất chiếu muộn (từ 22h trở đi)
    if time >= 22:
        base *= 0.8

    return int(round(base))

# ==============================================================================
# 1. KIỂM THỬ ALL-USES COVERAGE VÀ GIÁ TRỊ BIÊN HỢP LỆ
# ==============================================================================

@pytest.mark.parametrize("age, time, expected_price, tc_id", [
    # --- All-Uses Coverage (Phủ các cặp (Def, Use) của biến 'base') ---
    # TC1: d3, u7 (age < 12, time >= 22 - Giảm giá)
    (10, 22, 40000, "TC1"),
    # TC2: d3, u8 (age < 12, time < 22 - Không giảm giá)
    (5, 15, 50000, "TC2"),
    # TC3: d4, u7 (12 <= age < 60, time >= 22 - Giảm giá)
    (30, 23, 80000, "TC3"),
    # TC4: d4, u8 (12 <= age < 60, time < 22 - Không giảm giá)
    (45, 10, 100000, "TC4"),
    # TC5: d5, u7 (age >= 60, time >= 22 - Giảm giá)
    (70, 22, 56000, "TC5"),
    # TC6: d5, u8 (age >= 60, time < 22 - Không giảm giá)
    (80, 20, 70000, "TC6"),
    
    # --- Kiểm tra Giá trị Biên Hợp lệ ---
    (11, 21, 50000, "Bound_Age_11"),  # age biên: dưới 12
    (12, 21, 100000, "Bound_Age_12"), # age biên: >= 12
    (59, 21, 100000, "Bound_Age_59"), # age biên: dưới 60
    (60, 21, 70000, "Bound_Age_60"),  # age biên: >= 60
    (30, 21, 100000, "Bound_Time_21"),# time biên: dưới 22 (Không giảm giá)
    (30, 22, 80000, "Bound_Time_22"), # time biên: >= 22 (Có giảm giá)
])
def test_all_uses_and_boundaries(age, time, expected_price, tc_id):
    assert movie_ticket(age, time) == expected_price

# ==============================================================================
# 2. KIỂM THỬ LỖI ĐẦU VÀO (VALIDATION)
# ==============================================================================

def test_value_errors():
    # Tuổi không hợp lệ (Age < 0)
    with pytest.raises(ValueError, match="Tuổi không hợp lệ"):
        movie_ticket(-1, 10)
    
    # Tuổi không hợp lệ (Age > 120)
    with pytest.raises(ValueError, match="Tuổi không hợp lệ"):
        movie_ticket(121, 10)
        
    # Giờ chiếu không hợp lệ (Time > 23)
    with pytest.raises(ValueError, match="Giờ chiếu không hợp lệ"):
        movie_ticket(30, 24)
        
    # Giờ chiếu không hợp lệ (Time < 0)
    with pytest.raises(ValueError, match="Giờ chiếu không hợp lệ"):
        movie_ticket(30, -1)
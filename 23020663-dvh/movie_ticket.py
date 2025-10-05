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
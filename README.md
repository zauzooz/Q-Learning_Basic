# Q-LEARNING CƠ BẢN

Các thư viện yêu cầu:

- numpy
- pandas

**Bước 1**: chạy `generate_parameter.py` để tạo các tham số cần thiết cho hàm Q-Learning.

```
python3 generate_parameter.py
```

Tạo ra cá file lưu trong thư mục `parameter`:

- `ACTION`: lưu danh sách các action.
- `STATE`: lưu danh sách các state.
- `REWARD.csv`: bảng REWARD, với `REWARD[state][action]` sẽ trả về một giá trị. Nếu giá trị là -1 thì thức là `state` không có `action`, nếu lớn hơn -1 thì là nó là `reward`.
- `TRANSITION.csv`: bảng TRANSITION, với `TRANSITION[state][action]` sẽ trả về `state` tiếp theo. Nếu giá trị là -1 thì tức là `action` không giúp chuyển sang `state` khác, nếu giá trị là khác -1 thì tức là `action` đưa đến `state` mới là giá trị đó.

**Bước 2**: chạy `q-learning.py` để thực hiện training. Kết quả xuất ra là file `Q_TABLE.csv` lưu trong thư mục `parameter`:

```
python3 q-learning.py
```

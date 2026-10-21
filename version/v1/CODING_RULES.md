# CODING_RULES.md — Hướng dẫn lập trình và quy trình sửa code cho Agent

File này định nghĩa các nguyên tắc lập trình thực tế, quy trình viết code an toàn và cơ chế tự kiểm chứng của agent trong project nghiên cứu khoa học. Bộ quy tắc này kế thừa nguyên lý cẩn trọng của CLAUDE.md và kiến trúc Harness dài hạn (Planner-Generator-Evaluator).

---

## 1. Nguyên tắc cốt lõi: Cẩn trọng & Tối giản (CLAUDE.md style)

### 1.1. Suy nghĩ kỹ trước khi code (Think Before Coding)
* **Không giả định:** Nếu có bất kỳ điểm nào không rõ về logic vật lý, kiểu dữ liệu, hay thiết kế thí nghiệm, agent phải dừng lại và hỏi người dùng.
* **Nêu rõ giả định:** Khi có nhiều phương án triển khai, phải liệt kê ưu/nhược điểm từng phương án trước khi triển khai, không âm thầm lựa chọn.
* **Không giấu sự bối rối:** Nếu code hoặc công thức cũ quá khó hiểu, agent phải nêu tên điểm gây bối rối thay vì viết đè code đoán mò.

### 1.2. Đơn giản là trên hết (Simplicity First)
* **Chỉ viết đủ:** Không viết thêm tính năng hay tham số tùy biến nếu người dùng không yêu cầu.
* **Tránh trừu tượng hóa sớm:** Không tạo thêm class, helper function phức tạp, hoặc abstraction layer nếu code đó chỉ được gọi một lần.
* **Giới hạn số dòng code:** Nếu một logic có thể viết ngắn gọn và tường minh trong 50 dòng, tuyệt đối không viết thành 200 dòng.

### 1.3. Sửa đổi mang tính phẫu thuật (Surgical Changes)
* **Chỉ sửa phần cần thiết:** Khi sửa lỗi hoặc thêm tính năng, chỉ chạm vào đúng các dòng code liên quan.
* **Không tiện tay dọn dẹp:** Không tự ý format lại code adjacent, sửa comment cũ không liên quan, hoặc refactor các hàm đang chạy ổn định.
* **Tuân thủ style có sẵn:** Viết code theo đúng phong cách và quy chuẩn đặt tên biến/hàm hiện tại của file (ngay cả khi agent muốn viết theo kiểu khác).

---

## 2. Quy trình kiểm chứng dài hạn: Generator - Evaluator Loop

Để tránh việc code chạy được nhưng cho ra kết quả khoa học bị sai hoặc lỗi logic ngầm, agent phải tự vận hành theo mô hình phân tách vai trò:

### 2.1. Hợp đồng Sprint (Sprint Contract)
Trước khi viết code/sửa file (trừ các lỗi cú pháp hiển nhiên):
1. **Đề xuất Contract:** Agent đề xuất một bản "Sprint Contract" ngắn gọn ghi rõ:
   * **Mục tiêu:** Tính năng hoặc hàm cần sửa.
   * **Mô tả thay đổi:** Sửa đổi cụ thể ở file nào, hàm nào.
   * **Cách kiểm chứng (Validation Tests):** Các bước kiểm tra chạy thử để chứng minh code hoạt động đúng (ví dụ: in ra shape, kiểm tra NoData, assert kết quả).
2. **User xác nhận:** Chờ người dùng duyệt Contract trước khi tiến hành code.

### 2.2. Generator (Viết code từng phần)
* Thực hiện code chính xác theo phạm vi của Sprint Contract.
* Viết code tới đâu tự kiểm tra cú pháp và logic cơ bản tới đó.
* Ghi lại chi tiết log/output sau khi chạy thử.

### 2.3. Evaluator (Đánh giá độc lập)
Sau khi Generator hoàn thành code, agent phải tự chuyển sang vai trò Evaluator để "phản biện" lại chính code mình vừa viết theo các tiêu chuẩn:
* **Tính đúng đắn (Functionality):** Code chạy không lỗi cú pháp, xử lý đúng dữ liệu biên, không gây crash pipeline.
* **Tính khoa học (Evidence & Physics):** (Nếu sửa công thức/vật lý) Phép tính có đúng thứ nguyên/đơn vị không? Có bịa tham số không? Có thay đổi baseline vật lý mà chưa kiểm chứng không?
* **Code quality:** Spacing đồng nhất, comment rõ ràng, dễ đọc.

Nếu bất kỳ tiêu chuẩn nào không đạt, Generator phải thực hiện sửa lại ở vòng lặp tiếp theo.

---

## 3. Lệnh chạy và môi trường (Build & Test Commands)

Agent cần ưu tiên sử dụng các lệnh chuẩn của hệ thống:
* **Kiểm tra Python/Cú pháp:** `python -m py_compile <file_path>` hoặc chạy test nhanh bằng script hỗ trợ.
* **Môi trường:** Sử dụng `uv` hoặc `pip` khi cần cài đặt/quản lý dependency (cần hỏi ý kiến user trước khi thay đổi package).
* **Workspace:** Mọi thao tác ghi log, tạo file tạm thời phải nằm trong thư mục workspace hiện tại.

---

## 4. Quản lý Context & Tránh quá tải cửa sổ ngữ cảnh

* **Tự thu gọn (Compaction):** Khi chat dài, agent chủ động tóm tắt các bước đã làm, kết quả đã thống nhất để giải phóng context window, tránh model bị "context anxiety" (lo sợ đầy context dẫn đến code vội vã, wraps up thiếu chi tiết).
* **Đọc file chọn lọc:** Không load toàn bộ file nếu chỉ cần kiểm tra một hàm. Sử dụng tool `view_file` với line range cụ thể.

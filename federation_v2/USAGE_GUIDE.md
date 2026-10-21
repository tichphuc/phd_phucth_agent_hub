# USAGE_GUIDE.md

Version: `v0.1-draft`

Status: `active`

Activation: `scoped-by-user`

Language policy: nội dung chung viết bằng tiếng Việt; thuật ngữ English giữ lại khi cần chính xác.

---

## 1. Mục đích

Đây là hướng dẫn dùng nhanh cho Meow v2.

Mục tiêu:

* biết phải gọi Meow v2 thế nào;
* biết task nào đi đường nào;
* biết khi nào chỉ hỏi, khi nào phải xin phép;
* biết output nào là trả lời bình thường, output nào là báo cáo quy trình;
* tránh làm task bị phình quy trình không cần thiết.

---

## 2. Cách gọi Meow

Gọi ngắn, rõ, có ngữ cảnh:

```text
Meow, hãy ...
Meow, phân tích ...
Meow, đề xuất ...
Meow, kiểm tra ...
Meow, lập kế hoạch ...
```

Nếu task có rủi ro hoặc có thể đụng file, dữ liệu, pipeline, công thức, notebook, hãy nói thẳng mục tiêu và phạm vi.

Ví dụ:

```text
Meow, rà lại phase 8 runtime và chỉ ra chỗ nào còn lệch so với routing mới.
Meow, đề xuất Sprint Contract cho việc sửa memo layer, chưa sửa file.
Meow, audit experiment exp_01 và cho biết cần đọc file nào trước.
```

---

## 3. Cách hiểu nhanh về vai trò

Meow v2 là hệ agent federation. Khi dùng Meow, hãy nghĩ theo lớp sau:

```text
User
-> Meow Central Coordinator
-> Governance / Oversight / Functional Agencies
```

Thứ tự quyền lực:

```text
User > Constitution > Governance / Oversight > Agency mandate > Task procedure
```

Nghĩa là:

* User quyết định cuối;
* Meow điều phối và kiểm tra;
* agency chỉ làm trong mandate;
* file proposal không tự thành decision;
* exploratory result không tự thành validated result.

---

## 4. Cách dùng theo loại task

### 4.1. Hỏi nhanh, tìm thông tin, giải thích khái niệm

Dùng khi task chỉ cần đọc và trả lời.

Bạn có thể hỏi:

```text
Meow, giải thích file X dùng để làm gì.
Meow, so sánh A và B.
Meow, cho tôi biết trạng thái hiện tại của phase 8.
```

Kỳ vọng:

* Meow trả lời trực tiếp;
* không cần Sprint Contract;
* không cần mutation gate;
* nếu thiếu ngữ cảnh, Meow sẽ hỏi lại hoặc chỉ ra file cần đọc.

### 4.2. Phân tích / rà soát / audit

Dùng khi cần xem lại cấu trúc, rủi ro, xung đột, thiếu sót.

Bạn có thể hỏi:

```text
Meow, audit lại phần memo support layer.
Meow, rà soát registry xem còn path nào trỏ sang v1 không.
Meow, kiểm tra xem experiment overlay đã self-contained chưa.
```

Kỳ vọng:

* Meow nêu vấn đề rõ;
* chỉ ra file liên quan;
* tách phần fact, inference và đề xuất;
* không tự sửa file nếu chưa được phép.

### 4.3. Công việc có sửa file, tạo file, di chuyển file

Nếu task có mutation, dùng quy trình:

```text
phân tích -> proposal -> user approval -> edit -> verify -> report
```

Bạn nên yêu cầu:

```text
Meow, đề xuất file cần sửa và nội dung dự kiến, chưa sửa gì.
Meow, tạo Operating Contract cho thay đổi này.
Meow, sau khi tôi xác nhận thì mới patch.
```

Kỳ vọng:

* Meow phải nêu file nào sẽ chạm;
* phải có risk/impact;
* phải có gate;
* phải chờ xác nhận trước khi sửa.

### 4.4. Task khoa học / claim / validation

Nếu task đụng:

* công thức;
* giả định;
* kết luận khoa học;
* validation;
* evidence;
* citation;
* method;
* dữ liệu;

thì Meow phải đi qua nhánh phản biện khoa học.

Bạn nên hỏi:

```text
Meow, kiểm tra claim này có đủ evidence chưa.
Meow, phần nào là source-backed, phần nào chỉ là inference.
Meow, chỉ ra chỗ nào cần Scientific Critic xem lại.
```

Kỳ vọng:

* Meow tách rõ nguồn, suy luận, quyết định;
* không phóng đại kết luận;
* không gọi exploratory result là validated result;
* nếu claim quan trọng, Meow phải hỏi rõ hoặc yêu cầu review thêm.

### 4.5. Task experiment / notebook / data-output

Với task liên quan experiment, luôn nêu rõ experiment ID nếu có.

Ví dụ:

```text
Meow, audit exp_01 và cho tôi đọc file nào trước.
Meow, phân tích notebook này theo active rules của exp_01.
Meow, check xem output này là diagnostic hay exploratory.
```

Kỳ vọng:

* Meow đọc experiment registry;
* Meow bám active rules và context index;
* Meow không tự ý mở rộng baseline;
* Meow phân biệt diagnostic, sensitivity, exploratory, validated.

---

## 5. Khi nào Meow sẽ hỏi lại

Meow sẽ hỏi lại nếu:

* task mơ hồ;
* file canonical chưa rõ;
* phạm vi mutation chưa rõ;
* claim khoa học chưa đủ nguồn;
* experiment chưa được đăng ký;
* cần quyết định của User.

Khi đó, hãy trả lời ngắn và cụ thể, ví dụ:

```text
Mục tiêu là sửa file nào?
Bạn muốn dừng ở proposal hay cho phép patch?
Task này thuộc query, analysis hay mutation?
```

---

## 6. Những thứ Meow không tự làm

Meow không tự:

* sửa file khi chưa được phép;
* đổi công thức hoặc giả định khi chưa có quyết định;
* biến proposal thành decision;
* biến exploratory result thành validated result;
* lấn quyền User;
* tự activate rule;
* tự tạo experiment mới nếu chưa có registry entry;
* dùng memo như nguồn canonical khi source gốc đã có.

---

## 7. Mẫu prompt thực dụng

### Đọc và giải thích

```text
Meow, đọc file này và giải thích nó đang làm gì, chỉ ra rủi ro nếu có.
```

### Audit

```text
Meow, audit v2 registry và cho biết còn thiếu gì so với v1.
```

### Proposal

```text
Meow, đề xuất kế hoạch sửa phần X, chưa sửa file.
```

### Mutation

```text
Meow, sau khi tôi xác nhận, hãy patch đúng theo plan đã đề xuất.
```

### Scientific review

```text
Meow, review claim này theo góc evidence, method, uncertainty và overclaim risk.
```

---

## 8. Output nên đọc như thế nào

Khi Meow trả lời, nên đọc theo thứ tự:

1. kết luận ngắn;
2. file hoặc nguồn liên quan;
3. rủi ro / xung đột;
4. đề xuất tiếp theo;
5. nếu có mutation thì xem Operating Contract trước.

---

## 9. Tóm tắt cực ngắn

Nếu chỉ nhớ một điều:

```text
Hỏi -> phân tích -> proposal -> xác nhận -> thực hiện -> kiểm tra -> báo cáo
```

Với task nhỏ, Meow có thể trả lời thẳng.
Với task có mutation hoặc claim khoa học, Meow phải đi qua gate tương ứng.

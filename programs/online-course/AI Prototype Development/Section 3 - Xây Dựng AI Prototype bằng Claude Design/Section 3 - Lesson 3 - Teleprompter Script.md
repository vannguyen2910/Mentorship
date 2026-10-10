# Teleprompter — Lesson 3: Xây Dựng Design Token Bằng AI

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 16 — Lesson 3 divider]**

Sang Lesson 3: xây dựng design token bằng AI.

Đây là bước đầu tiên trong chuỗi ba bước dựng lại prototype pattern từ file thật: token, rồi component inventory, rồi template.

Chạy một lần, mọi màn hình sau đó dùng đúng màu và chữ của bạn, không phải màu mặc định của AI.

**[Slide 17 — Vì sao token quan trọng]**

Một nghiên cứu năm 2025 của NN/g, Nielsen Norman Group, về các công cụ AI prototyping ghi nhận: khi không có chỉ định cụ thể về màu sắc, kiểu chữ, hay khoảng cách, AI có xu hướng mặc định về những thư viện component phổ biến nhất trong dữ liệu huấn luyện của nó.

Kết quả là giao diện trông "sạch" nhưng chung chung, không có bản sắc riêng.

Nhiều công cụ AI khác nhau lại cho ra kết quả trông na ná nhau.

Xây token bằng AI chính là bước ngăn điều đó xảy ra.

Nó là lý do prototype của bạn trông giống sản phẩm của bạn, chứ không giống một template có sẵn nào đó.

**[Slide 18 — Trích xuất token. Tạo CSS variables.]**

Prompt để AI đọc file Figma của bạn.

Trích xuất design token: giá trị màu sắc, kiểu chữ, và khoảng cách.

Tạo ra một file CSS variables từ những token này, để mọi màn hình sau đó dùng đúng giá trị từ hệ thống của bạn.

Prompt này chỉ cần chạy một lần.

Sau bước này, mọi màn hình bạn build ở các bước sau đều tự động dùng đúng màu và chữ thật của bạn, thay vì để AI tự đoán.

Tài liệu chính thức của Figma về MCP cũng khuyến nghị đúng nguyên tắc này.

Dùng Figma variables cho token thay vì giá trị gõ tay, vì đây là cách trực tiếp nhất để AI đọc đúng ý định thiết kế, thay vì đoán.

Nếu token trong file Figma của bạn chưa được set up dưới dạng variable, bước dọn dẹp file lúc trước là thời điểm tốt để chuyển chúng thành variable, trước khi chạy prompt này.

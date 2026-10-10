# Teleprompter — Lesson 5: Xây Dựng Design Template Bằng AI

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 22 — Lesson 5 divider]**

Sang Lesson 5: xây dựng design template bằng AI.

Bản đồ chỉ đường, dựng từ đúng component inventory vừa tạo.

**[Slide 23 — Template: bản đồ của toàn bộ journey]**

Prompt dựa trên component inventory ở trên.

Map template cho prototype của tôi: những màn hình nào tồn tại, cái gì kết nối chúng, và điều gì kích hoạt mỗi lần chuyển màn hình.

Dùng component inventory làm tham chiếu.

Cũng như component inventory, nếu bản cũ và bản đọc ở đây khác nhau, bản mới luôn thắng vì nó phản ánh đúng file thật.

Kết thúc lesson này, bạn sẽ có component inventory và design template sẵn sàng cho bước build.

**[Slide 24 — Một file. Toàn bộ Design System.]**

Giờ cả ba layer, token, component inventory, và template, đã có đủ.

Đây là lúc tạo ra một file duy nhất để nhìn thấy toàn bộ hệ thống bằng mắt, thay vì chỉ đọc mô tả bằng chữ.

Prompt dựa trên token, component inventory, và template ở trên.

Tạo một file design_system.html duy nhất, hiển thị trực quan: bảng màu, thang chữ, spacing, và preview thật của từng component, đủ variant và state.

File này sẽ là nguồn tham chiếu hình ảnh cho mọi màn hình bạn build sau này.

Lưu file này vào local folder đã tạo trước đó, và cập nhật rules file để trỏ tới nó, đúng như đã chuẩn bị.

Từ giờ, mỗi khi build một màn hình mới, bạn có thể mở file này cạnh màn hình đang build để so sánh trực tiếp, thay vì chỉ tin vào mô tả bằng chữ.

**[Slide 25 — Đừng build cả journey. Test 1 component trước.]**

Trước khi bắt đầu build main journey, đừng vội viết prompt cho cả journey.

Một nghiên cứu năm 2025 của NN/g, đánh giá AI prototyping trên dự án thật, ghi nhận: ngay cả với prompt chi tiết nhất, output AI vẫn thường "tốt từ xa, chưa tốt khi nhìn gần".

Sai ở token màu, tên component, hay state khi nhìn kỹ.

Bắt lỗi này càng sớm càng rẻ.

Rẻ nhất là ngay sau khi ba layer vừa xong, không phải sau khi đã build xong cả journey.

Chọn một thứ đơn giản nhất có thể, không phải cả màn hình.

Ví dụ, một component với vài state, nút CTA ở default, hover, disabled.

Build component đó, dùng đúng token và component inventory ở trên, đối chiếu với design_system.html.

Kiểm tra ba điều trên kết quả: đúng token màu và chữ, đúng tên component, đúng state.

Nếu sai, quay lại sửa bước dọn dẹp file, hoặc phần token, component inventory, template trước.

Đừng mang lỗi này sang build cả main journey, vì lúc đó chi phí sửa đã cao hơn nhiều.

Kết quả cần có trước khi build main journey: một component inventory, một template, và một file design_system.html đã được xác nhận, khớp với main journey bạn đã chọn từ trước, và đã pass bước test nhỏ này.

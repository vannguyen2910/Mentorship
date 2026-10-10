# Teleprompter — Lesson 4: Xây Dựng Component Inventory Bằng AI

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 19 — Lesson 4 divider]**

Sang Lesson 4: xây dựng component inventory bằng AI.

Trước đó, bạn đã tự tay viết component inventory, dựa trên các screen bạn thiết kế trong Figma.

Đó là bản kế hoạch.

Giờ file Figma của bạn đã được dọn dẹp, đây là lúc tạo ra bản chính thức, đọc trực tiếp từ file thật.

Để AI coding tool build dựa trên đúng những gì thực sự tồn tại, chứ không phải những gì bạn nhớ là mình đã thiết kế.

**[Slide 20 — AI chỉ dùng những component đã tồn tại]**

Prompt để AI đọc file Figma của bạn.

Generate một component inventory: liệt kê từng component với tên, chức năng, và toàn bộ state của nó, default, hover, loading, error.

Gắn cờ bất kỳ thứ gì trông chưa hoàn chỉnh hoặc không nhất quán.

Đọc kỹ output.

Sửa lại tên hoặc state nào bị sai.

Đây sẽ là nguồn tham chiếu chính cho toàn bộ phần build phía sau.

Nếu bước dọn dẹp file trước đó đã được làm kỹ, danh sách này sẽ ngắn gọn và sạch.

Nếu output ở đây dài và lộn xộn, đó là dấu hiệu nên quay lại hoàn thiện bước dọn dẹp trước khi build tiếp.

Đừng cố build trên một inventory bạn không tin tưởng.

**[Slide 21 — File thật luôn thắng trí nhớ của bạn]**

So sánh với bản viết tay trước đó.

Nếu bản cũ và bản đọc ở đây khác nhau, chẳng hạn AI phát hiện thêm một state bạn quên nhắc tới lúc mô tả bằng lời, hoặc một component đã đổi tên trong lúc dọn dẹp, thì bản đọc từ file thật luôn thắng.

Nó phản ánh file thật, không phải trí nhớ của bạn về file đó.

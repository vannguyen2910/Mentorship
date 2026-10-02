---
title: "Section 4: Xây Dựng AI Prototype bằng Figma Make"
subtitle: "Cùng một prototype pattern, một tool khác — từ Figma Make kit đến prototype chia sẻ được"
course: Systematic AI Prototyping for Product Designers
section: 4
source-lesson: Library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-08-17
language: vi
---

## Tổng Quan Section

> **Section mới (2026-08-17):** Trước đây folder này là "Mở Rộng Quy Mô Prototype" (build các journey còn lại, mở rộng design system). Nội dung đó đã chuyển sang phần Practice chung, nằm giữa section này và phần kế tiếp. Folder này giờ là track tool thứ hai của khoá học: build prototype pattern bằng Figma Make, song song với track Claude Design. Bạn chỉ cần học 1 trong 2 track để tiếp tục — chọn tool nào bạn sẽ thực sự dùng.

Track Claude Design đã đi qua toàn bộ quy trình build: setup, dựng lại token/component inventory/template, build main journey, và chia sẻ. Section này đi qua đúng quy trình đó, nhưng bằng Figma Make.

Vì Figma Make sống ngay trong Figma, một vài bước ở track Claude Design không cần lặp lại ở đây. Không cần setup design system sang một tool khác, không cần MCP, không cần dựng lại template như một bước riêng. Figma Make đọc trực tiếp file Figma của bạn qua "Make kit", bundle sẵn component, token, và style. Vì vậy phần này gọn hơn nhiều. Phần lý thuyết đã học rồi, ở đây chỉ học thao tác khác biệt.

**Kết thúc section này, bạn sẽ có thể:**
1. Chuẩn bị Make kit và viết Guidelines.md để Figma Make build đúng theo design system của bạn
2. Viết prompt build prototype trên Figma Make, dựa trên prototype pattern đã chuẩn bị từ trước
3. Tinh chỉnh bằng prompt lặp lại, đúng cách Figma Make được thiết kế để làm việc
4. Chia sẻ prototype từ Figma Make bằng tính năng publish có sẵn

**Nội dung section:**
- 4 lesson: 3 lesson nội dung và 1 lesson chia sẻ
- Cần có: file Figma đã thiết kế và dọn dẹp từ trước, tài khoản Figma có quyền dùng Figma Make (Full seat, gói trả phí)

---

## Nội Dung Lesson

### Lesson 1: Chuẩn Bị Make Kit & Guidelines.md
*Một Make kit, gồm cả design system thật và rule cho AI trong cùng 1 chỗ.*

**Make kit là gì:** một file Figma Make riêng, đóng gói style/component từ design system đã publish, cộng với guidelines hướng dẫn AI dùng đúng. Publish kit xong, cả team chọn dùng lại trong bất kỳ project Make nào, không cần add lại context từ đầu mỗi lần.

**Trước khi bắt đầu:** design system đã chuẩn bị từ trước cần được publish thành library trong Figma Design trước (tab Assets, chọn Publish). Make kit chỉ lấy style và component từ library đã publish, không đọc được file còn ở dạng nháp.

**Các bước tạo Make kit:**
1. Mở 1 file Figma Make mới, vào Settings ở góc trên phải, chọn Create a kit.
2. Chọn Assemble your kit để dùng library đã publish, rồi chọn đúng library của bạn.
3. Figma Make tự tạo 1 folder guidelines kèm file Guidelines.md, để bạn viết rule cho AI (xem phần dưới).
4. Test kit: prompt Make build thử 1 màn hình, xem component hay token có lệch không, chỉnh lại guidelines nếu cần.
5. Publish kit: bấm Publish kit ở góc trên phải, đặt tên và thumbnail rõ ràng, rồi Publish. Kit cần nằm trong 1 folder, không publish được nếu còn ở Drafts.

Khi bắt đầu 1 project Make mới, bấm Select a Make kit ngay trong ô prompt, chọn đúng kit vừa publish. Có thể chọn cùng lúc nhiều kit nếu cần. Đây là bước tương đương việc Claude Design đọc file qua MCP, chỉ khác là gói gọn ngay trong Figma.

**Guidelines.md: gộp rules + template vào 1 file**

Ở track Claude Design, rules cho AI và bản đồ template là 2 việc tách biệt: rules file cấp project, và 1 prompt riêng để dựng template. Với Figma Make, cả 2 gộp vào 1 file duy nhất: `Guidelines.md`, được tạo sẵn ngay khi bạn tạo Make kit.

**Guidelines.md nên có:**
- Token: bảng màu, thang chữ, spacing, radius (tham chiếu tới token thật trong file Figma)
- Quy tắc component: ưu tiên tái sử dụng component có sẵn, không tạo mới nếu đã có biến thể tương tự
- Quy tắc layout: dùng responsive layout (flexbox/grid), tránh positioning tuyệt đối trừ khi thật sự cần
- Micro-interaction và hành vi component không thấy được bằng mắt (giống annotation đã chuẩn bị từ trước)
- Quy tắc code: giữ code sạch, refactor khi cần, giữ file size nhỏ

Figma Make không tự đọc toàn bộ flow giữa các màn hình từ file Figma. Mỗi lần build, bạn vẫn mô tả flow context ngay trong prompt: đến từ màn hình nào, dẫn tới màn hình nào (cách viết cụ thể ở lesson sau). Vì vậy Guidelines.md không cần vẽ lại bản đồ toàn bộ chuỗi màn hình như một bước riêng, chỉ cần củng cố rule cho component, token, và layout.

**Kết quả tối thiểu:** 1 Make kit đã publish, chứa đúng library design system của bạn, cùng 1 file `Guidelines.md` phản ánh đúng token, component, và rule.

---

### Lesson 2: Viết Prompt Build Prototype Trên Figma Make
*Cùng mindset pattern-first, chỉ khác cách gõ ra thành lời.*

Khung 5 thành phần đã học trước đó (Goal, Layout, Content, Audience, Flow context) áp dụng y hệt ở đây. Figma Make không cần một cú pháp prompt khác, nó cần cùng một lượng thông tin cụ thể để không phải đoán.

**Prompt build 1 màn hình, ví dụ:**

> "Build màn hình [tên màn hình]. Goal: [user đang cố làm gì]. Layout: [cách sắp xếp cụ thể]. Content: [dữ liệu mẫu thật]. Audience: [ai đang dùng]. Flow context: đến từ [màn hình trước], dẫn tới [màn hình sau]. Dùng đúng component và token từ Make kit, theo đúng Guidelines.md. Không tạo component mới nếu đã có biến thể tương tự."

**Khác biệt khi build:** Figma Make trả về cả preview trực quan lẫn code, xem song song ngay trong 1 cửa sổ. Bạn không cần mở file khác để đối chiếu, giống việc mở `design_system.html` cạnh màn hình khi làm với Claude Design.

**Kỳ vọng đúng cho lần build đầu tiên:** Figma Make thường tạo ra bản đầu khoảng 80% hoàn chỉnh. Đây là điểm khởi đầu để tinh chỉnh, không phải bản cuối cùng. Cùng nguyên tắc "build → review → tiếp tục" đã học trước đó vẫn áp dụng: build 1 màn hình, review, sửa những gì cần thiết, rồi mới sang màn hình tiếp theo. Đừng build cả main journey trong 1 prompt.

**Kết quả tối thiểu:** main journey 2-4 màn hình, chạy được trong Figma Make, dùng đúng component và token từ Make kit.

---

### Lesson 3: Tinh Chỉnh Bằng Prompt Lặp Lại
*Figma Make được thiết kế để bạn sửa bằng câu, không phải chỉnh tay từng pixel.*

Sau khi có bản build đầu tiên, tinh chỉnh trên Figma Make chủ yếu qua prompt lặp lại (follow-up prompt), ngay trong cùng cuộc trò chuyện đã build ra màn hình đó.

**Ví dụ prompt tinh chỉnh:**
- "Làm gọn phần hero section lại, đang chiếm quá nhiều không gian so với nội dung bên dưới."
- "Thêm 1 card testimonial vào giữa section này, dùng đúng Card component đã có."
- "Spacing giữa các item trong list này không đều, chỉnh lại theo đúng token spacing."

Nguyên tắc review vẫn giống track Claude Design: đối chiếu với file Figma gốc, tự hỏi đúng 6 câu hỏi đã học (mục tiêu, định hướng, ưu tiên thông tin, nhất quán component, next action, kết nối journey). Khác biệt duy nhất là cách sửa: thay vì chọn giữa 3 chế độ tinh chỉnh của Claude Design, ở đây bạn chỉ cần tiếp tục cuộc trò chuyện bằng câu tiếp theo.

**Lỗi lặp lại ở nhiều màn hình?** Cùng nguyên tắc "sửa 1 chỗ" đã học: nếu lỗi nằm ở token hoặc component dùng chung, cập nhật Guidelines.md hoặc component gốc trong Make kit, không sửa riêng từng màn hình.

**Kết quả tối thiểu:** main journey đã tinh chỉnh, nhất quán component và token, sẵn sàng để chia sẻ.

---

### Lesson 4: Chia Sẻ Prototype Từ Figma Make
*Figma Make publish trực tiếp, không cần GitHub hay hosting riêng.*

Khác với Claude Design, nơi bạn cần đẩy code lên GitHub rồi kết nối hosting để có link sống, Figma Make có tính năng publish tích hợp sẵn.

**Cách publish:**
1. Trong Figma Make, tìm nút Publish trên project của bạn
2. Xác nhận nội dung sẵn sàng công khai, đặt tên nếu cần
3. Publish để có 1 URL riêng, chạy được ngay trên web, không cần setup gì thêm

**Kiểm soát quyền xem:** giống chia sẻ file Figma thông thường, bạn chọn giữa "bất kỳ ai có link", "chỉ người được mời vào file", hoặc "chỉ người trong tổ chức". Chọn đúng mức độ trước khi gửi link cho stakeholder.

**Nếu bạn chỉ cần demo nhanh, chưa muốn publish công khai:** dùng chế độ Present (giống prototype link thông thường của Figma) để có link xem trước, không cần publish chính thức. Link dạng này phù hợp cho demo nội bộ, không phải link chia sẻ lâu dài.

**Dù chọn cách nào, luôn xác nhận trước khi gửi:**
- Link mở được ở chế độ ẩn danh hoặc trên thiết bị khác, không riêng máy bạn
- 1 câu mô tả ngắn đi kèm link: prototype này thể hiện user goal gì, gồm những màn hình nào

**Kết quả tối thiểu:** 1 link prototype đã publish hoặc present, xác nhận mở được, sẵn sàng gửi cho stakeholder.

---

*Khóa học: Systematic AI Prototyping for Product Designers · Section 4 — Xây Dựng AI Prototype bằng Figma Make*
*Thực hiện bởi Winnie Nguyen · Cập nhật lần cuối tháng 8/2026*

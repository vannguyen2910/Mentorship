# Slide Outline: Practice - Xây Dựng Prototype Bằng AI

> **Nguồn nội dung:** `practice-lesson.md` (cùng thư mục). Outline cho slide đi kèm 4 lesson (3 nội dung + 1 bài tập tổng), chưa build thành deck HTML, chỉ là bản kế hoạch để duyệt trước khi build (theo Rule WF-5).
> **Vị trí trong khoá học:** Giữa Section 4 (Xây Dựng AI Prototype bằng Figma Make) và Section 5 (Stitching Prototype). Không đánh số Section riêng, theo quyết định restructure khóa học tháng 8/2026.
> **Nguồn gốc nội dung:** Gộp từ `section 4-slide-outline.md` cũ (Lesson 1 "Xây Dựng Các Journey Còn Lại" + Lesson 3 "Mở Rộng Design System Đúng Cách", giữ nguyên toàn bộ slide) và `section 5-slide-outline.md` cũ (Lesson 2 "Phản Tư..." → đổi tên "Nhìn Lại Quá Trình..." + Lesson 3 "Bài Tập Về Nhà & Prompt Library"). Lesson "Chia Sẻ Prototype" (Section 5 cũ, Lesson 1) đã chuyển sang cuối Section 3, không lặp lại ở đây. 2 slide PRACTICE cũ (Practice 1 của Section 4 + bài tập về nhà của Section 5) đã gộp thành 1 slide PRACTICE cuối duy nhất, khớp với `practice-lesson.md`.
> **Cấu trúc:** 1 deck liền mạch, có slide "divider" đánh dấu ranh giới mỗi lesson.

---

## Prompt để build (khi đã duyệt outline)

```
Dùng outline trong file này, build slide deck HTML cho Practice - Xây Dựng Prototype Bằng AI
(khóa Systematic AI Prototyping for Product Designers, bản tiếng Việt).

Theo đúng rule trong _Config/rules/SLIDE_DECK_RULES.md.
Copy tokens.css và deck-stage.js vào thư mục này để deck tự chứa (self-contained).

Kiểm tra dòng "Loại visual" của từng slide trước khi build - nếu chưa chọn, dừng lại và hỏi
Winnie trước khi build slide đó.

Giữ tiếng Anh cho thuật ngữ chuyên môn ngay trong câu tiếng Việt.
Dòng "Ghi chú thuyết trình" đưa vào speaker notes của HTML deck, không hiển thị trên slide chính.
```

---

## Thống kê

**19 slide tổng cộng:** 1 cover + 1 roadmap + 4 lesson-divider + 11 slide nội dung (Lesson 1: 5, Lesson 2: 3, Lesson 3: 2, Lesson 4: 1) + 1 practice tổng + 1 end.

| Phần | Số slide |
|---|---|
| Cover + Roadmap | 2 |
| Lesson 1: Build Các Journey Còn Lại | 1 divider + 5 = 6 |
| Lesson 2: Mở Rộng Design System Đúng Cách | 1 divider + 3 = 4 |
| Lesson 3: Nhìn Lại Quá Trình Cộng Tác Với AI | 1 divider + 2 = 3 |
| Lesson 4: Bài Tập & Prompt Library | 1 divider + 1 = 2 |
| Practice tổng + Kết thúc | 2 |
| **Tổng** | **19** |

---

## 1. Cover & Roadmap

---

### COVER
- Kicker: Practice · Khóa Systematic AI Prototyping for Product Designers
- Title: Xây Dựng\nPrototype Bằng AI
- Subtitle: Build các journey còn lại, mở rộng design system đúng lúc, nhìn lại quá trình cộng tác với AI, và nộp bài
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Mở đầu bằng đúng câu trong lesson: phần trước để lại main journey đã chạy được nhưng chưa hoàn hảo, và bạn đã biết cách chia sẻ nó. Nhấn: phần này áp dụng được dù bạn build bằng Claude Design (Section 3) hay Figma Make (Section 4), tuỳ tool bạn đã chọn.

---

### PROCESS - Lộ trình Practice
- Kicker: Wrap-up Phase
- Title: Từ 1 journey. *Đến 1 hệ thống, đã được nhìn lại.*
- Nội dung: 4 ô ngang nối tiếp: "Lesson 1: Build các journey còn lại" → "Lesson 2: Mở rộng design system đúng cách" → "Lesson 3: Nhìn lại quá trình cộng tác với AI" → "Lesson 4: Bài tập & Prompt Library" → dẫn tới ô cuối "Practice tổng: build, nhìn lại, nộp bài."
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Giới thiệu nhanh 4 lesson ngắn dẫn tới 1 practice tổng duy nhất ở cuối. Nhấn đây là phần "hạ cánh" sau Section 3/4 dày đặc, trước khi bước sang Section 5 (Stitching).

---

## 2. Lesson 1: Build Các Journey Còn Lại

---

### SECTION - Lesson 1
- Title: Lesson 1\nBuild các\njourney còn lại
- Sub: Cùng một quy trình. Nhưng lần này, bạn không còn bắt đầu từ số 0.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Câu mở lesson: "không có kỹ thuật mới ở đây, chỉ là lặp lại quy trình build/review đã học ở Section 3 hoặc 4 cho các user goal còn lại." Nhấn với học viên: khác biệt duy nhất là lần này họ mang theo bài học, lỗi đã gặp và cách sửa, từ main journey đầu tiên.

---

### PROCESS - Build từng journey một
- Kicker: Đừng build mọi thứ cùng lúc
- Title: Hoàn thành một journey. *Rồi mới chuyển sang journey tiếp theo.*
- Lead:
  · Bắt đầu với màn hình đầu tiên của journey
  · Build và review kết quả
  · Sửa những gì chưa đúng
  · Tiếp tục sang màn hình tiếp theo
  · Hoàn thành toàn bộ journey trước khi bắt đầu journey mới
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nguyên tắc giống hệt phần build main journey trước đó, chỉ đổi cấp độ: màn hình → journey. Nhắc 3 bước lesson yêu cầu cho mỗi journey: viết build prompt 5 thành phần (nêu rõ flow context nối journey trước) → build/review cạnh file Figma gốc → sửa trước khi qua màn hình tiếp theo.

---

### STATEMENT - Đừng dồn hết vào 1 prompt
- Kicker: Prompt Overload
- Title: Đừng dồn hết vào 1 prompt.
- Lead:
  · Đã có Design Tokens, Components, Template
  · Giờ còn có cả main journey đầu tiên làm tham chiếu
  · Càng nhiều thứ có sẵn, càng dễ bị cám dỗ dồn hết vào 1 prompt
  · Input càng dài, AI càng dễ bỏ sót chi tiết ("context rot")
  · Build tuần tự vẫn luôn đúng, dù có sẵn bao nhiêu tài liệu
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn: đến bước này học viên có sẵn Design Tokens, Components, Template, cả main journey đầu, thậm chí PRD và Wireframe. Càng nhiều thứ có sẵn càng dễ bị cám dỗ dồn hết vào 1 prompt cho nhanh. Insight cần nhớ: có sẵn không có nghĩa nên dùng hết cùng lúc.

---

### STATEMENT - Lỗi lặp lại, sửa 1 chỗ
- Kicker: Lợi ích cụ thể của pattern-first
- Title: Lỗi lặp lại? *Sửa 1 chỗ, không sửa từng màn hình.*
- Lead:
  · Đừng sửa riêng lẻ từng màn hình
  · Sửa đúng 1 chỗ: component inventory hoặc token
  · Mọi màn hình tự động đúng theo
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Slide quan trọng nhất lesson. Ví dụ: main journey lỡ sai spacing hay sai token màu, kiểm tra ngay lỗi đó có lặp ở journey tiếp theo không, vì cả hai build từ cùng 1 component inventory. Nếu có, sửa 1 lần ở component inventory hoặc token, không sửa từng màn hình.

---

### STATEMENT - Review là công việc của Designer, ở mọi journey
- Kicker: Không chỉ áp dụng cho journey đầu tiên
- Title: Đẹp không có nghĩa là đúng.
- Lead: Sau mỗi lần build, hãy review:
  · Màn hình có đúng mục tiêu không?
  · Người dùng có biết mình đang ở đâu không?
  · Thông tin có được ưu tiên đúng không?
  · Component và pattern có nhất quán không?
  · Hành động tiếp theo có rõ ràng không?
  · Màn hình có kết nối đúng với journey không?
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đúng 6 câu hỏi review đã dùng ở main journey đầu tiên, đây là lúc nhắc học viên nhớ lại chứ không dạy lại. Cảnh báo: dễ chủ quan bỏ review ở journey thứ 2, 3 vì đã quen tay.

---

### STATEMENT - Kiểm tra tính nhất quán
- Kicker: Consistency Check
- Title: Mở tất cả journey cạnh nhau.
- Lead:
  · Button, màu sắc, khoảng cách có nhất quán giữa các journey không?
  · Nếu có, đó là bằng chứng pattern-first đã hoạt động, không phải may mắn
  · Mở design_system.html cạnh các journey để đối chiếu, thay vì tự nhớ
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Bước chốt lesson. Kết quả tối thiểu học viên cần đạt: toàn bộ journey đã chọn chạy được, nhất quán component và token.

---

## 3. Lesson 2: Mở Rộng Design System Đúng Cách

---

### SECTION - Lesson 2
- Title: Lesson 2\nMở rộng design system\nđúng cách
- Sub: Không phải màn hình mới nào cũng cần component mới
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Câu mở lesson: càng build nhiều màn hình, càng dễ rơi vào 1 trong 2 thái cực, ép mọi thứ dùng lại component cũ dù không còn hợp, hoặc tạo mới cho từng biến thể nhỏ khiến inventory phình to.

---

### TABLE - 3 câu hỏi trước khi thêm mới
- Kicker: Trước khi tạo mới
- Title: Cái này thật sự mới. *Hay chỉ là 1 biến thể?*
- Bảng 3 dòng: Component tương tự đã có chưa (chỉ khác state/size/nội dung) · Nên là 1 biến thể hay 1 component riêng · Template mới tái dùng được component cũ, hay cần layout khác.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: 3 câu hỏi lấy nguyên từ lesson. Đây cũng là quy tắc chính thức của Figma MCP: ưu tiên dùng lại trước khi tạo mới.

---

### STATEMENT - Dùng design_system.html làm căn cứ
- Kicker: Không dùng trí nhớ
- Title: Tra cứu design_system.html. *Đừng dùng trí nhớ.*
- Lead:
  · File này bạn đã tạo trước đó, hiển thị trực quan toàn bộ token, component, template hiện có
  · Mở nó, đối chiếu màn hình mới cần build với những gì đã hiển thị
  · Rồi mới quyết định: dùng lại, tạo biến thể, hay tạo mới hoàn toàn
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đọc luôn prompt kiểm tra trong lesson file cho học viên nghe: đính kèm design_system.html, mô tả màn hình cần build, hỏi AI component nào dùng lại được.

---

### STATEMENT - Cập nhật lại sau khi mở rộng
- Kicker: Kết quả tối thiểu
- Title: Mở rộng xong. *Cập nhật lại ngay.*
- Lead:
  · Mỗi lần thêm component hoặc template mới, generate lại design_system.html
  · Bỏ qua bước này, file lỗi thời
  · Mất luôn giá trị làm căn cứ cho lần build tiếp theo
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Chốt lại đúng "kết quả tối thiểu" của lesson: mọi màn hình mới đều đối chiếu với design_system.html trước khi build, inventory chỉ tăng khi thật sự cần.

---

## 4. Lesson 3: Nhìn Lại Quá Trình Cộng Tác Với AI

---

### SECTION - Lesson 3
- Title: Lesson 3\nNhìn lại quá trình\ncộng tác với AI
- Sub: "Tôi thấy nó hay" không phải một lần nhìn lại quá trình
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn ngay từ đầu: lesson này không phải thủ tục cho có, mà là bước biến kinh nghiệm build vừa xong thành hiểu biết mang theo sang những prototype tiếp theo.

---

### PROCESS - 3 câu hỏi nhìn lại quá trình
- Kicker: Nhật Ký Review
- Title: AI làm đúng gì. AI bỏ sót gì. *Nếu không có pattern thì sao?*
- Nội dung (3 câu hỏi, mỗi câu có gợi ý trả lời ngắn): AI làm đúng điều gì nhanh hơn nếu tự làm tay; AI bỏ sót điều gì bạn phải tự sửa (lấy ví dụ từ nhật ký review); Nếu không có prototype pattern từ Section 2, build hôm nay sẽ khác thế nào.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn học viên mở lại đúng Build & Journey Worksheet để trả lời câu 2 bằng ví dụ thật, không phải đoán lại từ trí nhớ.

---

### STATEMENT - Nghịch lý AI hạ thấp rào cản
- Kicker: Nghịch Lý Đáng Nhớ (NN/g, 2025)
- Title: AI hứa hẹn thu hẹp khoảng cách kỹ năng. *Nhưng lại tốt nhất trong tay người đã giỏi.*
- Lead: Để ra lệnh chính xác cho AI, bạn cần hiểu bố cục, kiểu chữ, cách đặt tên component, luồng người dùng, đúng kiến thức bạn đã học trước khoá này. AI không thay thế kiến thức thiết kế, nó khuếch đại khoảng cách giữa kết quả tạm ổn và kết quả thực sự tốt.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Slide triết lý quan trọng nhất của phần này, đọc chậm. Nhấn: đây chính là lý do khoá học không dạy "prompt để AI tự thiết kế thay bạn", mà dạy bạn định nghĩa hệ thống trước.

---

## 5. Lesson 4: Bài Tập & Prompt Library

---

### SECTION - Lesson 4
- Title: Lesson 4\nBài tập\n& Prompt Library
- Sub: Mở rộng prototype của bạn, và biết nơi tra cứu lại mọi prompt đã học
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Lesson cuối trước practice tổng, vừa giới thiệu bài tập, vừa để lại 1 tài liệu tra cứu học viên sẽ cần dùng lại ở Section 5 (Stitching).

---

### TABLE - Prompt Library tham chiếu nhanh
- Kicker: Tra Cứu Khi Cần
- Title: 5 nhóm prompt bạn dùng lại xuyên suốt khoá học.
- Bảng 2 cột (Mục đích / Khi nào dùng), 5 dòng: Generate token/inventory/template từ file thật; Build 1 màn hình (khung 5 thành phần); Review output; Chọn chế độ tinh chỉnh; Sửa lỗi có cấu trúc.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn: đây không phải nội dung học mới, toàn bộ đã xuất hiện ở Section 3/4, đây chỉ là bản tổng hợp để tra cứu. Nhắc học viên sẽ dùng lại đúng những prompt này ở Section 5 (Stitching).

---

## 6. Practice Tổng & Kết Thúc

---

### PRACTICE - Build Journey Còn Lại, Nhìn Lại Quá Trình & Nộp Bài
- Kicker: Practice khép lại phần này
- Title: Lần này, không ai build mẫu cho bạn.
- Nội dung (gộp từ 2 practice cũ):
  1. Chọn 1 user goal khác, tự viết build prompt, tự build, đối chiếu với main journey
  2. Review bằng 6 câu hỏi (Lesson 1), fix những gì cần thiết
  3. Mở rộng thêm ít nhất 2 màn hình, dùng đúng component inventory đã có (áp dụng quy trình Lesson 2 nếu cần component/template mới)
  4. Ghi lại 1 lỗi AI đã làm và cách bạn sửa
  5. Nhìn lại quá trình: trả lời 3 câu hỏi ở Lesson 3
  6. Nộp bài: 1 link (live/repo, đã học cách tạo ở cuối Section 3) + đoạn nhìn lại quá trình
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đây là practice duy nhất, gộp "build thêm 1 journey" và "nộp bài + nhìn lại quá trình" thành 1 bài khép lại phần này, không phải 2 bài nộp riêng như cấu trúc cũ. Không có ai build mẫu — đây là lúc kiểm tra xem quy trình đã thực sự "dính" thành workflow của học viên chưa. Nhắc prototype này sẽ được dùng lại ở Section 5 (Stitching).

---

### END - Kết thúc Practice (chuyển sang Section 5)
- Kicker: Một điều mang theo
- Title: "Bạn không còn prototype rời rạc. *Bạn có một hệ thống biết tự lắp ráp."*
- Lead: Section 5 (Stitching Prototype) sẽ dạy bạn cách nối nhiều prototype, của bạn và có thể của cả nhóm, thành một hành trình người dùng hoàn chỉnh để demo cho stakeholder.
- Sign: Winnie Nguyen
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Slide chốt cả phần này, đọc chậm và trang trọng. Preview ngắn gọn Section 5, không đi sâu chi tiết.

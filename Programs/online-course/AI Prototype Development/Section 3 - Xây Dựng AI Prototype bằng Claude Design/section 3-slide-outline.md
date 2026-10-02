# Slide Outline: Section 3 - Xây Dựng AI Prototype bằng Claude Design

> **Nguồn nội dung:** `section 3-lesson.md` (cùng thư mục). Outline cho slide đi kèm 10 lesson của Section 3, chưa build thành deck HTML, chỉ là bản kế hoạch để duyệt trước khi build (theo Rule WF-5).
> **Cấu trúc:** 1 deck liền mạch cho cả section (không tách deck riêng theo từng lesson), có slide "divider" đánh dấu ranh giới mỗi lesson, cùng convention với các section trước.
> **Ngôn ngữ:** Tiếng Việt, giữ nguyên tiếng Anh cho thuật ngữ chuyên môn (prototype pattern, component inventory, template, token, Design System, Pages, Templates, CLAUDE.md, Claude Design...), và cho một số câu chốt/punchline ngắn trong Ghi chú thuyết trình khi đó là cách nói tự nhiên nhất.
> **Loại visual:** mỗi slide có dòng "Loại visual" riêng (Diagram / Illustration / Real image), để trống nếu chưa quyết định.
> **Ghi chú thuyết trình:** viết theo văn nói thật, ngôi "mình", nhịp staccato, để Winnie đọc lướt khi trình bày trực tiếp, không phải nội dung bắt buộc đọc nguyên văn.
> **Cập nhật cấu trúc (2026-08-18):** Viết lại toàn bộ outline theo đúng cơ chế thật của Claude Design, thay khung generic "AI coding tool / AI design tool" trước đó. Bỏ 2 slide-group cũ (Local Folder & Rules File, Thiết lập MCP), thay bằng 4 slide-group mới: Đưa Design System Từ Figma, Pages, Templates, CLAUDE.md. Thêm 1 slide-group mới "Review & Refine Prototype". Tổng slide: 42.
> **Cập nhật giọng văn (2026-08-18, pass 2):** Winnie viết lại toàn bộ Ghi chú thuyết trình và một phần Lead/Nội dung theo đúng giọng thật của mình — ngôi "mình" nhất quán trong Ghi chú thuyết trình (không chỉ khi tự kể kinh nghiệm), nhịp staccato dày hơn, numbered step dùng dạng "01 · Nhãn" cho mọi danh sách bước/checklist kể cả ở Section 3 (không đợi tới Section 4), so sánh 2 track viết bằng dữ liệu thật song song thay vì phạm trù trừu tượng, và cho phép một câu punchline tiếng Anh ngắn trong Ghi chú thuyết trình khi đó là cách nói tự nhiên nhất (ví dụ "Garbage in, garbage out."). Đã cập nhật `writing-style-guide.md` để ghi lại các pattern này.

---

## Prompt để build (khi đã duyệt outline)

```
Dùng outline trong file này, build slide deck HTML cho Section 3 - Xây Dựng AI Prototype bằng Claude Design
(khóa Systematic AI Prototyping for Product Designers, bản tiếng Việt).

Theo đúng rule trong _System/rules/SLIDE_DECK_RULES.md.
Copy tokens.css và deck-stage.js vào thư mục Section 3 để deck tự chứa (self-contained).

Kiểm tra dòng "Loại visual" của từng slide trước khi build - nếu chưa chọn, dừng lại và hỏi
Winnie trước khi build slide đó.
```

---

## Thống kê

**42 slide tổng cộng:** 1 cover + 1 roadmap + 2 mini-intro + 37 slide lesson/practice + 1 end.

| Lesson | Số slide |
|---|---|
| Cover + Roadmap | 2 |
| Trước khi vào bài học | 2 |
| L1 Đưa Design System từ Figma | 4 |
| L2 Pages | 3 |
| L3 Templates | 3 |
| L4 CLAUDE.md | 4 |
| L5 Practice 1 | 1 |
| L6 Viết build prompt | 6 |
| L7 Xây main journey | 6 |
| L8 Practice 2 | 1 |
| L9 Review & Refine | 5 |
| L10 Chia sẻ prototype | 4 |
| End | 1 |
| **Tổng** | **42** |

---

## 1. Cover & Roadmap

---

### COVER
- Kicker: Section 3 · Systematic AI Prototyping for Product Designers
- Title: Xây Dựng AI Prototype\nbằng Claude Design
- Subtitle: Từ file Figma đến một prototype có Design System đứng phía sau
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Ở những phần trước, mình đã chuẩn bị file Figma và làm rõ prototype pattern.
  · Giờ mới đến phần thú vị hơn: đưa tất cả những thứ đó vào Claude Design và bắt đầu build.
  · Không phải prompt một câu rồi hy vọng AI tự hiểu.
  · Mình sẽ chuẩn bị context trước, rồi mới build prototype.

---

### PROCESS - Lộ trình Section 3
- Kicker: Build Phase
- Title: Từ Figma đến prototype chạy được
- Nội dung:
  **01 · Design System**
  Đưa system từ Figma sang Claude Design.
  **02 · Pages & Templates**
  Tổ chức system để Claude biết tìm gì ở đâu.
  **03 · CLAUDE.md**
  Đặt những rule cần giữ xuyên suốt project.
  **04 · Build**
  Dùng framework 5 thành phần để build từng màn hình.
  **05 · Review & Refine**
  Build xong chưa phải hết. Review rồi sửa đúng chỗ.
  **06 · Share**
  Đưa prototype ra khỏi Claude Design và gửi cho người khác.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Có một điều bạn sẽ thấy xuyên suốt section này: mình không bắt đầu bằng build.
  · Mình chuẩn bị system trước, sau đó mới build.
  · Đây cũng là lý do section này dài hơn Figma Make. Claude Design cho mình nhiều lớp context hơn để kiểm soát prototype.

---

## 1b. Trước Khi Vào Bài Học (không tính lesson)

---

### STATEMENT - Cùng một công thức. Một cái bếp khác.
- Kicker: Trước khi vào bài học
- Title: Cùng một công thức.\nMột cái bếp *khác.*
- Lead:
  Prototype pattern vẫn là pattern mình đã học. Nhưng trong section này, mình sẽ làm mọi thứ trực tiếp trong Claude Design.

  Bạn sẽ thấy những khái niệm mới như: Design System file · Pages · Templates · CLAUDE.md. Đây là cách Claude Design tổ chức context cho prototype.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Mình muốn nói rõ điều này trước để tránh một hiểu lầm.
  · Bạn không học lại một cách làm prototype mới.
  · Bạn đang học cách đưa cùng một cách nghĩ vào một tool cụ thể.

---

### COMPARE - Mindset không đổi. Tool thì có.
- Kicker: Mindset vs Tool
- Title: Mindset không đổi.\nTool thì *có.*
- Không đổi: Design System nên có trước khi build · AI cần nguồn tham chiếu rõ ràng · Build từng màn hình, review trước khi tiếp tục · Pattern nên được reuse thay vì tạo lại
- Claude Design: Design System file · Pages · Templates · CLAUDE.md · Chat / Comment / Edit / Draw · Export hoặc chia sẻ theo tổ chức
- Figma Make: Make kit · Guidelines.md · Prompt build · Follow-up prompt · Publish
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Hai track sẽ có vài cái tên khác nhau.
  · Nhưng đừng để những cái tên đó làm mình nghĩ đây là hai phương pháp khác nhau.
  · Pattern là nền tảng. Tool chỉ là cách mình thực hiện nó.

---

## 2. Lesson 1: Đưa Design System Từ Figma Sang Claude Design

---

### SECTION - Lesson 1
- Title: Lesson 1\nĐưa Design System\ntừ Figma sang Claude Design
- Sub: Đừng bắt Claude đoán design system của bạn. Cho nó một nguồn để đọc.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là bước đầu tiên trước khi build.
  · Mình sẽ lấy Design System đã chuẩn bị trong Figma và đưa nó vào Claude Design.
  · Mục tiêu không phải chỉ để Claude biết màu nào đẹp.
  · Mục tiêu là để Claude biết: "Đây là system mà prototype này phải tuân theo."

---

### DIAGRAM - Figma → Design System file
- Kicker: Input → System
- Title: Một Design System file.\nClaude đọc lại *mỗi khi build.*
- Nội dung: Figma → Design System file → Token + Component + Pattern → Claude dùng làm reference khi build
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình:
  · Mình tạo một Design System file trong Claude Design rồi đưa file Figma vào.
  · Claude có thể extract những thứ như: color, typography, component, design pattern.
  · Nhưng có một việc mình vẫn phải làm: đọc lại output và đối chiếu với Figma gốc.
  · Đừng mặc định AI import đúng 100%.

---

### STATEMENT - File Figma càng sạch, system càng dễ đọc
- Kicker: Input matters
- Title: File Figma càng sạch.\nClaude càng ít phải *đoán.*
- Lead: Nếu token của bạn đã được setup bằng Figma Variables, Claude có cơ hội hiểu đúng design intent tốt hơn thay vì chỉ nhìn thấy một loạt giá trị rời rạc. Vì vậy bước dọn file Figma ở phần trước không chỉ để file nhìn gọn hơn. Nó ảnh hưởng trực tiếp đến chất lượng input cho AI.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là lý do mình bắt bạn dọn file trước khi đưa vào Claude.
  · Không phải vì mình thích file Figma sạch.
  · Mà vì: garbage in, garbage out. Input càng rõ thì output càng dễ kiểm soát.

---

### COMPARE - Use this system hay Published?
- Kicker: Một project hay cả tổ chức?
- Title: Dùng cho một project.\nHay dùng cho cả *team?*
- Cá nhân, Pro / Max: "Use this system" — gắn Design System vào project hiện tại.
- Team / Enterprise: "Published" → "Set as org default" — đặt system thành mặc định cho các project mới trong tổ chức.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Với khóa học này, nếu bạn dùng tài khoản cá nhân thì "Use this system" là đủ.
  · Phần Team / Enterprise chỉ cần biết để hiểu cách workflow này có thể scale lên trong một tổ chức.

---

## 3. Lesson 2: Pages

---

### SECTION - Lesson 2
- Title: Lesson 2\nPages\nTổ chức Design System
- Sub: Một Design System tốt không chỉ có đủ thứ. Nó còn phải dễ tìm.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Bây giờ mình đã có Design System file.
  · Nhưng nếu mọi thứ nằm chung một chỗ thì vẫn chưa đủ tốt.
  · Claude cần biết: token nằm ở đâu, template nằm ở đâu?
  · Đó là lúc Pages trở nên hữu ích.

---

### DIAGRAM - Cấu trúc Pages
- Kicker: Bên trong Design System file
- Title: Chia nhỏ để dễ tìm.\nKhông phải *để cho đẹp.*
- Ví dụ: Readme (giải thích system này dùng cho sản phẩm nào) · Colors (Grey scale, Primary, Semantic) · Templates (Checkout, Detail, Home Feed, Tab Directory)
- Có thể thêm: Typography · Components · Patterns
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình:
  · Cấu trúc này không phải công thức bắt buộc.
  · Bạn có thể tổ chức Pages khác.
  · Điều quan trọng là khi mình cần một thứ, mình biết nó nằm ở đâu.

---

### STATEMENT - Pages không chỉ để file gọn
- Kicker: Why it matters
- Title: Claude không cần đọc tất cả.\nNó cần *tìm đúng chỗ.*
- Lead: Cần token màu? → Colors. Cần pattern cho một loại màn hình? → Templates. Cần hiểu system? → Readme. Pages giúp Design System trở thành một nguồn tham chiếu có cấu trúc, thay vì một đống thông tin nằm chung với nhau.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là điểm mình muốn bạn nhớ nhất ở lesson này.
  · Organize để giảm guessing.
  · Không phải organize chỉ để nhìn đẹp.

---

## 4. Lesson 3: Templates

---

### SECTION - Lesson 3
- Title: Lesson 3\nTemplates
- Sub: Cho Claude một bản mẫu để tham chiếu trước khi nó tự tạo một màn hình mới.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Templates là phần rất dễ hiểu nhầm.
  · Đây không phải màn hình thật trong prototype.
  · Nó là bản mẫu để Claude biết: "Một màn hình thuộc loại này nên được tổ chức như thế nào?"

---

### STATEMENT - Nếu không có template
- Kicker: Một pattern, nhiều màn hình
- Title: Cùng một loại màn hình.\nNhưng mỗi lần build *một kiểu.*
- Lead: Ví dụ bạn có hai màn hình dạng feed. Nếu Claude build từng màn hình độc lập, rất dễ xảy ra: spacing khác nhau, card khác nhau, hierarchy khác nhau, vị trí action khác nhau, state khác nhau. Có một Template chung giúp mình định nghĩa pattern trước.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là lúc mình bắt đầu chuyển từ "AI build màn hình cho tôi" sang "AI build màn hình theo pattern tôi đã định nghĩa."
  · Hai cách này khác nhau rất nhiều.

---

### PROMPT - Xây một Template
- Kicker: Template ≠ màn hình thật
- Title: Một bản mẫu để Claude *tham chiếu.*
- Prompt card:
  "Dựa trên các component đã có trong Design System này, tạo một page Template cho pattern [loại màn hình]. Template cần thể hiện: layout tổng thể, component được sử dụng, thứ tự ưu tiên thông tin, và các state chính (loading, empty, có dữ liệu). Đây là bản mẫu tham chiếu, không phải màn hình thật trong prototype."
- Loại visual: AI chat bot (mockup giao diện chat AI hiển thị prompt) — không thuộc 3 loại chuẩn
- Ghi chú thuyết trình:
  · Không cần tạo Template cho mọi màn hình.
  · Chỉ cần tạo cho những pattern lặp lại nhiều lần, hoặc đủ phức tạp để đáng chuẩn hóa.
  · Sau này khi build màn hình thật, mình chỉ cần nói cho Claude biết: "Dùng Template này."

---

## 5. Lesson 4: CLAUDE.md

---

### SECTION - Lesson 4
- Title: Lesson 4\nĐặt rule bằng\nCLAUDE.md
- Sub: Những điều Claude cần nhớ, nhưng bạn không muốn phải nhắc lại trong từng prompt.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đến đây mình có: Design System, Pages, Templates.
  · Nhưng vẫn còn một vấn đề: có những rule mình muốn Claude nhớ xuyên suốt project.
  · Không thể mỗi lần build lại nhắc một lần.
  · Đó là việc của CLAUDE.md.

---

### STATEMENT - CLAUDE.md là file sống
- Kicker: Project rules
- Title: Không phải viết một lần *rồi bỏ đó.*
- Lead: CLAUDE.md chứa những rule Claude cần tuân theo khi làm việc với project. Và nó có thể thay đổi. Nếu hôm nay mình phát hiện một lỗi lặp lại: sửa rule, lần build sau Claude sẽ có rule mới.

  Một dấu hiệu rất đơn giản: nếu bạn phải nhắc Claude cùng một điều 3 lần, có lẽ điều đó nên trở thành một rule.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Mình rất thích cách nghĩ này.
  · CLAUDE.md không phải một tài liệu mình viết cho đủ bài.
  · Nó lớn lên cùng prototype. Prototype càng lớn, mình càng phát hiện những rule cần giữ.

---

### STATEMENT - CLAUDE.md nên có gì?
- Kicker: Keep it useful
- Title: 4 điều là *đủ để bắt đầu.*
- Lead:
  **01 · Reference**
  Trỏ tới Design System và Templates.
  **02 · Naming**
  Quy tắc đặt tên component và page.
  **03 · Reuse first**
  Luôn kiểm tra component hoặc Template có sẵn trước khi tạo mới.
  **04 · Repeated instructions**
  Bất kỳ điều gì bạn phải nhắc Claude nhiều lần.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Không cần viết một file dài 10 trang.
  · Nếu rule không giúp Claude build tốt hơn thì bỏ.
  · Mình muốn một file: ngắn, rõ, dùng được.

---

### STATEMENT - Ví dụ CLAUDE.md
- Kicker: Một file ngắn
- Title: Claude cần nhớ gì?\nViết đúng *những thứ đó.*
- Blockquote ví dụ CLAUDE.md (project Travel Buddy):
  "Design System — Use the Travel Buddy Design System as the primary source for all UI decisions.
  Components — Always reuse existing components before creating new ones.
  Templates — Check Templates before creating a new screen pattern.
  Naming — Use PascalCase for component names and match the names used in the Design System.
  Content — Use realistic sample content. Do not use lorem ipsum."
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là một ví dụ mình muốn bạn có thể lấy về và chỉnh lại cho project của mình.
  · Không cần copy nguyên xi.
  · Chỉ cần giữ nguyên tư duy: những gì cần nhớ lâu dài, đưa vào rule.

---

## 6. Lesson 5: Practice 1

---

### PRACTICE - Set up Design System của bạn
- Kicker: Practice 1
- Title: Đến lượt bạn setup.
- Checklist:
  **01** Import file Figma vào Design System file.
  **02** Kiểm tra Pages và tạo ít nhất một folder cho token.
  **03** Tạo ít nhất một Template cho pattern xuất hiện nhiều nhất trong main journey.
  **04** Viết CLAUDE.md với ít nhất 4 rule.
- Kết quả cần có: một Design System file đã sẵn sàng để Claude dùng khi build prototype.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đừng vội build màn hình.
  · Nếu bạn làm Practice này nghiêm túc, phần build phía sau sẽ nhẹ hơn rất nhiều.
  · Setup tốt một lần. Dùng lại nhiều lần.

---

## 7. Lesson 6: Những Lưu Ý Khi Viết Build Prompt

---

### SECTION - Lesson 6
- Title: Lesson 6\nViết build prompt
- Sub: Bạn không cần prompt dài. Bạn cần prompt có đủ context.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đến đây mới bắt đầu build màn hình thật.
  · Và mình muốn thay đổi một thói quen rất phổ biến.
  · Đừng hỏi: "Prompt thế nào để AI làm đẹp?"
  · Hãy hỏi: "AI cần biết gì để hiểu đúng màn hình này?"

---

### TABLE - 5 thành phần
- Kicker: Một màn hình cần nhiều hơn UI
- Title: Goal. Layout. Content. Audience. *Flow context.*
- Bảng 5 dòng:

| Thành phần | Câu hỏi cần trả lời |
|---|---|
| **Goal** | User đang cố làm gì? |
| **Layout** | Nội dung được sắp xếp thế nào? |
| **Content** | User thực sự nhìn thấy dữ liệu gì? |
| **Audience** | Ai đang dùng màn hình này? |
| **Flow context** | User đến từ đâu và sẽ đi đâu tiếp? |

- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình:
  · Đây không phải một công thức để làm prompt nghe "xịn" hơn.
  · Đây thực ra là 5 câu hỏi mà Product Designer vốn đã phải tự hỏi khi thiết kế.
  · Chỉ khác là: bây giờ mình nói chúng cho Claude biết.

---

### STATEMENT - Flow context là phần dễ quên nhất
- Kicker: Đừng để màn hình đứng một mình
- Title: Một màn hình *không sống một mình.*
- Lead: Bạn có thể mô tả một màn hình rất chi tiết. Nhưng nếu Claude không biết user vừa làm gì, đến từ đâu, đang ở bước nào, và sau đó sẽ đi đâu, thì nó rất dễ build một màn hình đúng riêng lẻ nhưng sai trong cả journey.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là lý do flow context quan trọng.
  · CLAUDE.md có thể giữ những rule chung.
  · Nhưng flow context là context riêng của từng màn hình. Nó vẫn cần nằm trong build prompt.

---

### STATEMENT - Dùng một khung cho mọi màn hình
- Title: Đừng viết lại từ đầu.\nGiữ cùng *một khung.*
- Lead: Mỗi màn hình vẫn dùng Goal → Layout → Content → Audience → Flow context. Sang màn hình tiếp theo thì chỉ thay nội dung. Cách này giúp không bỏ sót context, dễ review, dễ so sánh các màn hình, giữ flow context xuyên suốt journey, dễ phát hiện màn hình nào đang thiếu thông tin. Nếu đã có Template phù hợp, nhắc Claude dùng lại.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Bạn sẽ không phải nghĩ lại: "Prompt màn hình tiếp theo nên viết thế nào?"
  · Khung đã có. Bạn chỉ tập trung vào màn hình.

---

### STATEMENT - Có PRD, wireframe hoặc user flow rồi?
- Kicker: Đừng bắt đầu từ trang trắng
- Title: Tài liệu có sẵn giúp bạn viết prompt *nhanh hơn.*
- Lead: Bạn có thể dùng PRD, user flow, wireframe, solution list để điền vào framework nhanh hơn. Nhưng đừng đưa cả đống tài liệu vào một prompt chỉ vì "AI có càng nhiều context càng tốt". Context không liên quan cũng có thể trở thành noise. Lấy đúng phần Claude cần cho màn hình đang build.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là điểm mình muốn học viên tránh.
  · Nhiều context không đồng nghĩa với context tốt.
  · Mình muốn: relevant context, not maximum context.

---

### STATEMENT - Chọn đúng format cho đúng loại thông tin
- Kicker: Text hay image?
- Title: Nội dung dùng text.\nLayout *dùng hình.*
- Markdown phù hợp với: PRD · User flow · Requirement · Structured content
- Hình ảnh phù hợp với: Wireframe · Layout · Visual hierarchy · Spatial relationship
- Một nguyên tắc đơn giản: đừng cố mô tả bằng chữ thứ mà hình ảnh có thể nói rõ hơn.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Ví dụ wireframe. Bạn có thể mất 10 dòng để mô tả vị trí của 5 block, hoặc đưa luôn hình wireframe.
  · Đôi khi hình ảnh chính là prompt tốt nhất.

---

## 8. Lesson 7: Xây Main Journey

---

### SECTION - Lesson 7
- Title: Lesson 7\nXây main journey
- Sub: Đây là lúc prototype bắt đầu thật sự chạy.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là lần đầu tiên mình build prototype thật.
  · Nếu bạn thấy hơi hồi hộp khi bấm build, bình thường.
  · Nhưng đừng đặt kỳ vọng rằng màn hình đầu tiên sẽ hoàn hảo.

---

### STATEMENT - Đặt kỳ vọng đúng
- Kicker: First build
- Title: Lần build đầu *không cần hoàn hảo.*
- Lead: Claude có thể dựng rất nhanh layout, component, content, interaction. Nhưng vẫn sẽ có những thứ cần chỉnh: spacing, hierarchy, grouping, visual details, interaction. Mục tiêu của lần build đầu là có một nền tảng đủ tốt để review, không phải có final UI.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Bạn có thể nhìn màn hình đầu tiên và nghĩ: "Wow, khá giống."
  · Sau đó zoom vào: "À... chưa giống lắm."
  · Đây là chuyện bình thường. Ổn từ xa chưa có nghĩa là đúng khi nhìn gần.

---

### PROCESS - Build từng màn hình
- Kicker: Build loop
- Title: Build. Review.\nRồi mới *tiếp tục.*
- Nội dung: Build màn hình 1 → Review → Fix → Build màn hình 2 → Review → Continue
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình:
  · Đây là workflow mình muốn bạn giữ từ giờ về sau.
  · Không phải: prompt → cả journey → xong.
  · Mà là: build → review → fix → continue.

---

### STATEMENT - Vì sao không build cả journey một lần?
- Kicker: Context overload
- Title: Càng nhét nhiều thứ vào một prompt,\ncàng dễ *bỏ sót.*
- Lead: Bạn có thể đã có Design System, Templates, CLAUDE.md, PRD, Wireframe, User flow. Nhưng vẫn không có nghĩa là nên đưa tất cả vào một prompt để build cả journey. Khi context quá dài, Claude dễ bỏ sót chi tiết ở giữa hoặc cuối. Build tuần tự giúp mỗi lần build tập trung hơn.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là một trong những lý do mình không khuyến khích: "Build all 10 screens for me."
  · Nghe thì rất nhanh.
  · Nhưng đến màn hình số 7, 8, 9, những chi tiết quan trọng ban đầu có thể bắt đầu lệch.

---

### PROMPT - Build một màn hình thật
- Kicker: Build main journey
- Title: Framework biến thành *build brief.*
- Journey: Onboarding → Explore Feed → Tip Detail
- Prompt card:
  "Build màn hình Explore Feed cho một user đang ở guest mode, chưa đăng ký nhưng đang khám phá những địa điểm được gợi ý. Người dùng có thể xem tips từ local và traveler thật.

  Màn hình cần có:
  · Header hiển thị 'Near Chiang Mai' và số lượng tips
  · Mode switcher gồm Near Me / Country / Map
  · Search bar và filter button có badge hiển thị số filter đang bật
  · Banner nhắc user đang ở guest mode
  · Feed gồm Tip Card với ảnh full-bleed, crowd level badge, quote, author và thời gian đăng
  · Guest paywall ở cuối feed
  · Bottom navigation cố định với 5 tabs

  Màn hình này đến từ Onboarding sau khi user chọn 'Explore without signing up'. Giữ guest mode trong journey. Khi user tap vào Tip Card, dẫn tới Tip Detail.

  Dùng đúng Template cho pattern feed đã có trong Design System. Không tạo cấu trúc mới nếu Template phù hợp đã tồn tại."
- Loại visual: AI chat bot (mockup giao diện chat AI hiển thị prompt) — không thuộc 3 loại chuẩn
- Ghi chú thuyết trình:
  · Đừng nhìn prompt này như một bài văn.
  · Hãy nhìn nó như một build brief ngắn cho một designer khác.
  · Mình đang nói: user là ai, màn hình cần làm gì, có gì trên màn hình, nó nằm ở đâu trong journey, và Claude nên dùng system nào.

---

### STATEMENT - Review vẫn là việc của Designer
- Kicker: AI builds. You decide.
- Title: Màn hình đẹp vẫn có thể là *màn hình sai.*
- Lead: Review bằng 6 câu hỏi:
  **01** Có đúng mục tiêu không?
  **02** User có biết mình đang ở đâu không?
  **03** Information hierarchy có đúng không?
  **04** Component và pattern có nhất quán không?
  **05** Hành động tiếp theo có rõ không?
  **06** Màn hình có nối đúng với journey không?
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là lúc vai trò của Designer không biến mất. Ngược lại.
  · AI làm phần build nhanh hơn, nên mình có nhiều thời gian hơn để làm phần quan trọng: nhìn, đánh giá và quyết định.

---

## 9. Lesson 8: Practice 2

---

### PRACTICE - Build Main Journey
- Kicker: Practice 2
- Title: Tự build main journey đầu tiên.
- Làm 2 đến 4 màn hình:
  **01** Viết build prompt theo 5 thành phần.
  **02** Build từng màn hình.
  **03** Review cạnh Figma gốc.
  **04** Check lại Template.
  **05** Nối các màn hình theo đúng flow context.
- Kết quả: một main journey có thể chạy được, dùng đúng component và token từ Design System.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đừng cố làm nhiều. 2 đến 4 màn hình là đủ.
  · Mục tiêu của Practice này không phải build thật nhiều.
  · Mục tiêu là bạn trải qua đúng loop: prompt → build → review → fix → continue.

---

## 10. Lesson 9: Review & Refine Prototype

---

### SECTION - Lesson 9
- Title: Lesson 9\nReview & Refine
- Sub: Biết mình muốn sửa gì chưa đủ. Bạn còn cần chọn đúng cách để sửa.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Ở Practice vừa rồi, mình đã có một prototype chạy được.
  · Bây giờ đừng vội sửa tất cả.
  · Trước tiên: review. Sau đó mới chọn cách refine phù hợp.

---

### TABLE - 4 cách refine
- Kicker: Pick the right tool
- Title: Chat. Comment. Edit.\n*Draw.*
- Bảng 4 dòng:

| Cách | Khi nào dùng? |
|---|---|
| **Chat** | Thay đổi lớn hoặc ảnh hưởng nhiều phần |
| **Inline comment** | Một component hoặc một vấn đề cụ thể |
| **Edit mode** | Màu, font, spacing và chỉnh trực tiếp |
| **Draw mode** | Vấn đề về vị trí hoặc layout khó mô tả bằng lời |

- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình:
  · Không phải lỗi nào cũng cần prompt lại.
  · "Đổi layout từ 1 cột thành 2 cột." → Chat.
  · "Button này contrast chưa đủ." → Comment.
  · "Spacing này đang là 24, mình muốn 16." → Edit.
  · "Block này phải dịch sang bên trái." → Có khi vẽ nhanh còn dễ hơn viết.

---

### STATEMENT - Chọn cách sửa nhanh
- Kicker: A simple rule
- Title: Nói được thì chat.\nChỉ đúng một chỗ thì *comment.*
- Lead: Ảnh hưởng nhiều phần? → Chat. Một component cụ thể? → Comment. Màu / font / spacing? → Edit. Khó mô tả bằng lời? → Draw.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đừng biến mọi lỗi thành một prompt dài.
  · Mình muốn bạn chọn cách ít tốn công nhất.

---

### STATEMENT - Muốn thử hướng khác?
- Kicker: Explore without losing
- Title: Đừng phá bản đang ổn.\nThử một *nhánh khác.*
- Lead: Nếu bạn đang có một version khá ổn nhưng muốn thử một hướng hoàn toàn khác: branch nó ra, giữ version hiện tại, thử hướng mới ở một nhánh riêng, sau đó so sánh. Vì sao? Bạn có thể experiment mà không phải đánh cược vào version đang có.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Không phải lúc nào cũng cần branch.
  · Nhưng khi bạn đang thử một hướng lớn, đây là cách an toàn hơn để experiment.

---

### STATEMENT - Refine không thay thế review
- Kicker: Review first
- Title: Đừng sửa vì thấy "chưa đẹp".\nBiết chính xác *vấn đề trước.*
- Lead: Trước khi refine:
  **01** Xác định vấn đề.
  **02** Đối chiếu 6 câu hỏi review.
  **03** Chọn cách sửa.
  **04** Kiểm tra lại sau khi sửa.

  Nếu không, bạn rất dễ rơi vào vòng: prompt → một version khác → lại prompt → lại một version khác. Có thay đổi, nhưng không chắc prototype tốt hơn.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là câu mình muốn học viên nhớ: don't prompt because you can, prompt because you know what needs to change.

---

## 11. Lesson 10: Chia Sẻ Prototype

---

### SECTION - Lesson 10
- Title: Lesson 10\nChia sẻ prototype
- Sub: Build xong chưa có nghĩa là người khác mở được.
- Loại visual: ☑ Illustration ☐ Diagram ☐ Real image
- Ghi chú thuyết trình:
  · Prototype chạy ngon trên máy mình là một chuyện. Người khác có mở được hay không là chuyện khác.
  · Ở Claude Design, cách share phụ thuộc khá nhiều vào việc người nhận có nằm trong cùng organization với bạn hay không.

---

### PROCESS - Trong tổ chức hay ngoài tổ chức?
- Kicker: 2 cách share
- Title: Người nhận ở đâu?\nCách share sẽ *khác.*
- Trong cùng organization: Project → Public / Private → Can use / Can edit → Share link
- Ngoài organization: Export → Standalone HTML → Hosting → Share link
- Export còn có: PDF · PPTX · Handoff to Claude Code
- Prototype tương tác: Standalone HTML phù hợp nhất.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là chỗ mình muốn bạn phân biệt rõ hai trường hợp.
  · Nếu stakeholder nằm trong cùng organization, share trực tiếp.
  · Nếu cần gửi prototype ra ngoài, không có public link, export standalone HTML rồi đưa lên một static hosting.

---

### PRACTICE - Trước khi gửi
- Kicker: Before you share
- Title: Đừng gửi link rồi mới phát hiện *nó không chạy.*
- Check 01: Link có mở được không? Test bằng incognito, thiết bị khác, account khác nếu cần.
- Check 02: Người nhận có biết họ đang xem gì không? Gửi kèm user goal + prototype gồm những màn hình nào.
- Ví dụ: "Prototype này mô phỏng flow refinance từ lúc user bắt đầu application đến lúc review loan offer."
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Đây là một bước nhỏ nhưng rất đáng làm.
  · Đừng gửi: "Hi, đây là prototype." Hãy cho người nhận biết họ đang nhìn cái gì.
  · Và quan trọng nhất: test link trước khi gửi.

---

### DIAGRAM - Nhìn lại cách mình làm việc với AI
- Kicker: Before we move on
- Title: Prototype đã xong.\nNhưng workflow của bạn *thì sao?*
- 3 câu hỏi:
  **01** Bạn build gì?
  **02** Claude làm điều gì khiến bạn bất ngờ?
  **03** Nếu không có Design System, bạn nghĩ mình sẽ mất thêm bao nhiêu thời gian?
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Ba câu hỏi này không chỉ để nói chuyện cuối lesson. Nó sẽ quay lại ở phần Practice chung.
  · Mục tiêu là bắt đầu nhận ra: AI giúp mình nhanh hơn ở đâu, và system giúp mình kiểm soát AI ở đâu.

---

## 12. Kết thúc

---

### END - Kết thúc Section 3
- Kicker: Takeaway
- Title: "Prototype đầu tiên không cần hoàn hảo. *Nhưng Design System phải có lý do để tồn tại."*
- Lead: Đến đây, bạn đã có: một Design System trong Claude Design, Templates để giữ pattern nhất quán, CLAUDE.md để giữ những rule quan trọng, một main journey có thể chạy, một workflow để review và refine, và một prototype có thể chia sẻ.

  Nhưng quan trọng hơn: bạn vừa đi qua một workflow có thể lặp lại. System → Build → Review → Refine → Continue.
- Sign: Winnie Nguyen
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình:
  · Nếu chỉ nhớ một điều sau section này, mình muốn bạn nhớ: đừng dùng AI như một cái máy tạo màn hình, hãy cho nó một system để làm việc cùng.
  · Từ đây, bạn có thể tiếp tục với track Figma Make, hoặc đi thẳng tới phần Practice chung.
  · Hai track khác tool. Nhưng cuối cùng vẫn quay về cùng một cách làm: build có hệ thống, review có chủ đích, rồi mới mở rộng.

---

## 13. Nguồn Tham Khảo

- Nielsen Norman Group — [Good from Afar, But Far from Good: AI Prototyping in Real Design Contexts](https://www.nngroup.com/articles/ai-prototyping/)
- Nielsen Norman Group — [AI Design Tools Are Marginally Better: Status Update](https://www.nngroup.com/articles/ai-design-tools-update-2/)
- Anthropic — [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs)
- Claude Help Center — [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)
- Claude Help Center — [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)
- Claude Help Center — [Claude Design admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans)
- Claude Help Center — [Set organization instructions](https://support.claude.com/en/articles/14546867-set-organization-instructions)
- Jeff Su — [Claude Design Tutorial: A Beginner's Guide](https://www.jeffsu.org/claude-design-tutorial/)
- Anthropic — [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic — [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Morph — [Context Rot: Why LLMs Degrade as Context Grows](https://www.morphllm.com/context-rot)
- LangChain — [Plan-and-Execute Agents](https://www.langchain.com/blog/planning-agents)
- GitHub Blog — [Spec-driven development with AI: Get started with a new open source toolkit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- arXiv — [Rethinking the UI of GenUI: A Tale of Two Designs](https://arxiv.org/html/2606.13843)
- Zoer — [Fix AI Memory Issues in Vibe-Coding Tools](https://zoer.ai/posts/zoer/fix-ai-memory-issues-vibe-coding-tools)
- HummingDeck — [How to Share Claude Design Outside Your Anthropic Organization](https://hummingdeck.com/blog/share-claude-design)

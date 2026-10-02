# Slide Outline: Section 1 - Giới Thiệu

> **Nguồn nội dung:** `section 1-lesson.md` (cùng thư mục). Bản outline chưa build thành deck HTML, chỉ là bản kế hoạch để duyệt trước khi build (theo Rule WF-5).
> **Lesson 1 không có slide.** Winnie tự quay video giới thiệu bản thân riêng (xem kịch bản ở `section 1-lesson.md`), không cần deck. Deck dưới đây chỉ phục vụ Lesson 2 và Lesson 3.
> **Ngôn ngữ:** Tiếng Việt, giữ nguyên tiếng Anh cho thuật ngữ chuyên môn (prototype pattern, component inventory, template, AI chat tool, AI coding tool, Figma...).
> **Không nêu tên AI tool cụ thể** (không "Claude", "Cursor", "Figma Make"...) trên slide hay trong ghi chú thuyết trình — luôn dùng nhãn chung "AI chat tool" / "AI coding tool", theo đúng quy ước chung của khóa học. **Ngoại lệ (2026-07-17):** slide "Tools you'll use" ở cuối Lesson 3 nêu tên tool cụ thể theo yêu cầu trực tiếp của Winnie — xem ghi chú "Sửa đồng bộ" tại slide đó bên dưới.
> **Loại visual:** Mỗi slide có dòng "Loại visual" riêng (Diagram / Illustration / Real image), phần lớn còn để trống chờ Winnie quyết định.
> **Ghi chú thuyết trình:** Rút gọn từ kịch bản đầy đủ ở `section 1-lesson.md` — chỉ là cue ngắn để Winnie đọc lướt, không phải nguyên văn lời thoại.
> **Cập nhật (đồng bộ với lesson.md mở rộng):** Đã tách persona và section thành các slide riêng theo đúng cấu trúc hiện tại (không dùng chung 1 slide NUMBERED nữa). Đã bỏ slide PROCESS roadmap đầu deck (không còn dùng). Đoạn minh họa "hộp Lego" (cách làm cũ vs cách làm mới) trong kịch bản mở rộng phát trong lúc slide STATEMENT vẫn đứng yên, không có slide riêng — nếu muốn tách riêng thành 1 slide COMPARE, báo Winnie quyết định trước khi build.

**SLIDE markers (từ kịch bản, theo đúng thứ tự xuất hiện):**
- [SLIDE: COVER, sau đó SECTION divider "Lesson 2"]
- [SLIDE: STATEMENT — Bạn có đang ở đây không? (lời thoại kéo dài qua cả phần minh họa "hộp Lego", vẫn 1 slide)]
- [SLIDE: Nhóm 1 — Career transitioner]
- [SLIDE: Nhóm 2 — Junior designer]
- [SLIDE: Nhóm 3 — Mid-level hướng senior]
- [SLIDE: QUOTE — Key message]
- [SLIDE: NUMBERED — Học xong, bạn sẽ làm được gì]
- [SLIDE: SECTION divider — Lesson 3]
- [SLIDE: Section 2 — Pattern-first thinking]
- [SLIDE: Section 3 — Build & refine]
- [SLIDE: Section 4 — Stitching prototype]
- [SLIDE: NUMBERED — Cần chuẩn bị gì trước khi bắt đầu]
- [SLIDE: Tools you'll use]
- [SLIDE: END — Kết thúc Section 1]

---

## Prompt để build (khi đã duyệt outline)

```
Dùng outline trong file này, build slide deck HTML cho Section 1 - Giới Thiệu
(khóa Systematic AI Prototyping for Product Designers, bản tiếng Việt).
Deck chỉ cần cho Lesson 2 và Lesson 3 (Lesson 1 là video riêng, không có slide).

Theo đúng rule trong _Config/rules/SLIDE_DECK_RULES.md.
Copy tokens.css và deck-stage.js vào thư mục "Section 1 - Giới Thiệu" để deck tự chứa (self-contained).

HƯỚNG DẪN THIẾT KẾ - áp dụng cho toàn bộ slide:
- Ưu tiên visual (diagram/illustration/real image) hơn bullet list thuần text.
- Mỗi slide có dòng "Loại visual" riêng - kiểm tra ô nào đã được chọn trước khi build. Nếu chưa
  chọn (còn để trống), dừng lại và hỏi Winnie trước khi build slide đó, đừng tự mặc định.
- Slide COVER dùng đúng layout `.cover` (ảnh nền + overlay), không dùng ảnh placeholder.
- Slide SECTION dùng layout `.section-divider` (nền `--paper-deeper`, không dùng nền tối).
- Slide QUOTE dùng layout `.quote` (nền `--ink`, chữ `--paper`).
- Slide END dùng layout `.end` (nền `--paper-deeper`, không dùng nền sienna).
- 3 slide persona (Nhóm 1/2/3) và 3 slide section (Section 2/3/4): dùng cùng 1 layout lặp lại
  (ví dụ `.statement` hoặc `.numbered` đơn giản hóa còn 1 item) để có cảm giác nhất quán khi
  chuyển từ slide này sang slide kia, không tự bịa layout mới cho mỗi slide.
- Giữ tiếng Anh cho thuật ngữ chuyên môn ngay trong câu tiếng Việt.
- Không nêu tên AI tool cụ thể trên bất kỳ slide nào — chỉ dùng "AI chat tool" / "AI coding tool".
- Dòng "Ghi chú thuyết trình" đưa vào phần speaker notes của HTML deck (không hiển thị trên
  slide chính), dùng đúng framework speaker-notes có sẵn trong SLIDE_DECK_RULES.md nếu có.
```

---

## Thống kê

**15 slide tổng cộng:** 1 cover + (Lesson 2: 1 divider + 6 nội dung = 7) + (Lesson 3: 1 divider + 5 nội dung + 1 end = 7).

| Phần | Số slide |
|---|---|
| Cover | 1 |
| Lesson 1: Chào mừng + giới thiệu bản thân | 0 (video riêng, không có slide) |
| Lesson 2: Khóa học dành cho ai | 1 divider + STATEMENT + Nhóm 1 + Nhóm 2 + Nhóm 3 + QUOTE + NUMBERED = 7 |
| Lesson 3: Cách khóa học được tổ chức | 1 divider + Section 2 + Section 3 + Section 4 + NUMBERED + Tools + END = 7 |
| **Tổng** | **15** |

> **Cập nhật:** Số liệu trước đây ghi 11 slide đã lỗi thời — thực tế đã tăng lên 15 sau khi tách persona (3 slide) và section (3 slide) thành slide riêng thay vì gộp chung 1 slide NUMBERED, đồng thời thêm slide "Tools you'll use" ở cuối Lesson 3. Tổng thời lượng lesson.md cũng tăng từ 8-10 phút lên 14-16 phút để khớp.

---

## 1. Cover

---

### COVER
- Kicker: Section 1 · Khóa Systematic AI Prototyping for Product Designers
- Title: Giới Thiệu
- Subtitle: Chào mừng vào khóa học Systematic AI Prototyping cho Product Designers
- 🎨 Visual: Ảnh chân dung hoặc không gian làm việc gần gũi (không cần phong cách "neon" của deck lớp live) — cover mang tinh thần chào đón, ấm áp hơn là kỹ thuật.
- Loại visual: Real image, lấy hình profile của Winnie
- Ghi chú thuyết trình: Slide mở đầu deck, xuất hiện ngay khi Lesson 2 bắt đầu (sau video giới thiệu bản thân của Lesson 1). Không cần đọc to tiêu đề, chỉ dùng làm điểm neo hình ảnh khi chuyển từ video sang phần có slide.

---

## 2. Lesson 2: Khóa Học Dành Cho Ai

---

### SECTION - Lesson 2
- Title: Lesson 2\nKhóa học\ndành cho ai
- Sub: Tự xác nhận khóa học có phù hợp với bạn không, và hình dung kết quả sau khi học xong
- 🎨 Visual: Nền `--paper-deeper`, số "02" mờ lớn góc trên trái, title căn giữa, giống section-divider của deck gốc.
- Loại visual: ☐ Diagram ☑ Illustration ☐ Real image
- Ghi chú thuyết trình: Chuyển vào Lesson 2. Đặt câu hỏi mở: "Khóa học này có thực sự dành cho mình không?" để học viên tự đối chiếu trong lúc xem.

---

### STATEMENT - Bạn có đang ở đây không?
- Kicker: Điều kiện đầu vào
- Title: Có Figma cơ bản. *Muốn AI hỗ trợ, không thay thế.*
- Lead: Dành cho product/UX designer đã biết tạo frame, dùng component, nối màn hình — muốn dùng AI để prototype nhanh hơn mà không đánh đổi sự nhất quán. Không cần biết code, không cần có sẵn design system hoàn chỉnh. Có dự án dang dở, dù mới sơ khai, đều dùng được.
- 🎨 Visual: Một khối UI đơn giản (vài frame + component) với icon Figma nhỏ góc, gợi "điểm xuất phát" tối thiểu cần có.
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Đọc chậm phần điều kiện đầu vào để học viên tự đối chiếu. Nhấn mạnh "không cần biết code" và "dự án dang dở cũng dùng được" để giảm rào cản tâm lý. **Lời thoại kéo dài qua cả phần minh họa "hộp Lego" (cách làm cũ vs cách làm mới) — slide này vẫn đứng yên trong lúc kể ẩn dụ, không chuyển slide giữa chừng.** Xem toàn văn ở `section 1-lesson.md`.

---

### SLIDE - Nhóm 1: Career transitioner
- Kicker: Ai đang chuyển ngành
- Title: Career transitioner
- Nội dung: Cần phương pháp rõ ràng, có hệ thống để tự tin bắt đầu, thay vì mò mẫm từng bước
- 🎨 Visual: Avatar / Illustration đơn giản
- Loại visual: Frame placeholder (illustration/image TBD)
- Ghi chú thuyết trình: Nhóm này thiếu quy trình, không thiếu gu thẩm mỹ — nhấn khóa học cho một quy trình rõ ràng từ định nghĩa hệ thống tới build sản phẩm thật.

---

### SLIDE - Nhóm 2: Junior designer
- Kicker: Đã quen Figma
- Title: Junior designer
- Nội dung: Muốn tăng tốc độ prototype bằng AI mà không làm sản phẩm rời rạc
- 🎨 Visual: Avatar / Illustration đơn giản
- Loại visual: Frame placeholder (illustration/image TBD)
- Ghi chú thuyết trình: Nhóm này thường đã thử AI rồi nhưng kết quả rời rạc, sửa còn tốn thời gian hơn tự làm — khóa học giữ tốc độ AI mà không mất chất lượng.

---

### SLIDE - Nhóm 3: Mid-level hướng senior
- Kicker: Hướng senior
- Title: Mid-level designer
- Nội dung: Cần chuẩn hóa quy trình, không chỉ cho mình mà cho cả team
- 🎨 Visual: Avatar / Illustration đơn giản
- Loại visual: Frame placeholder (illustration/image TBD)
- Ghi chú thuyết trình: Nhấn khóa học cho một ngôn ngữ và tài liệu cụ thể (prototype pattern) để dẫn dắt team, không chỉ dựa vào trực giác cá nhân.

---

### QUOTE - Key message
- Kicker: Khóa học này khác gì
- Quote: "Cách làm AI prototyping phổ biến nhất hiện nay là kiểu vibe coding: mô tả một màn hình, để AI generate ra, rồi lặp lại cho màn hình tiếp theo. Cách này bắt đầu rất nhanh, nhưng rạn nứt ngay khi số lượng màn hình tăng lên, vì không có gì được định nghĩa từ trước để AI dựa vào. Khóa học này đi theo hướng ngược lại: dạy các bạn định nghĩa hệ thống của mình một lần, rồi để AI build nhất quán ở bất kỳ quy mô nào. Không phải vibe-coded. Được thiết kế để mở rộng quy mô."
- Author: Winnie Nguyen · Systematic AI Prototyping for Product Designers
- 🎨 Visual: Không cần minh họa thêm, để quote đứng một mình trên nền `--ink`.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (không áp dụng — slide quote thuần chữ)
- Ghi chú thuyết trình: Đọc chậm, đặc biệt nhấn hai câu cuối "Không phải vibe-coded. Được thiết kế để mở rộng quy mô." — đây là câu định vị khóa học, nên để lại dư âm trước khi qua slide tiếp theo.
- **Sửa đồng bộ:** Quote đã được chỉnh lại đúng nguyên văn khớp với `section 1-lesson.md`. Đã bỏ cụm "trên thị trường" (so sánh với khóa học khác) theo yêu cầu của Winnie, đổi thành mô tả cách làm phổ biến thay vì nhắm vào khóa học đối thủ.

---

### NUMBERED - Học xong, bạn sẽ làm được gì
- Kicker: Kết quả sau khóa học
- Title: 3 điều bạn *làm được* sau khi học xong.
- Nội dung: 3 item đánh số:
  1. Định nghĩa hệ thống thiết kế của bạn thành một prototype pattern mà AI đọc được (token, component inventory, template)
  2. Dùng AI chat tool + AI coding tool build nhất quán, dù 3 hay 30 màn hình
  3. Nối nhiều màn hình thành 1 hành trình người dùng hoàn chỉnh, sẵn sàng demo cho stakeholder và test được với người dùng cuối
- 🎨 Visual: 3 icon tương ứng (tài liệu pattern / hai màn hình khớp nhau / chuỗi màn hình nối tiếp).
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Đây là slide "callback" — 3 outcome này map thẳng tới Section 2, 3, 4 sẽ giới thiệu ở Lesson 3. Có thể nói nhanh "và đây cũng chính là 3 section tiếp theo của khóa học" để bắc cầu.
- **Sửa đồng bộ:** Mục 1 đã đổi lại "prototype pattern" (bản trước ghi nhầm "design template", không khớp thuật ngữ chuẩn của khóa học).

---

## 3. Lesson 3: Cách Khóa Học Được Tổ Chức

---

### SECTION - Lesson 3
- Title: Lesson 3\nCách khóa học\nđược tổ chức
- Sub: Cấu trúc 4 section, và những gì cần chuẩn bị trước khi bắt đầu
- 🎨 Visual: Nền `--paper-deeper`, số "03" mờ lớn góc trên trái, cùng phong cách với divider Lesson 2.
- Loại visual: ☐ Diagram ☑ Illustration ☐ Real image
- Ghi chú thuyết trình: Chuyển vào Lesson 3, lesson cuối của Section 1. Nói ngắn gọn đây là "bản đồ" trước khi học viên chính thức bắt đầu. Câu mở đầu ("khóa học gồm 4 section...") đọc ngay trên slide này, trước khi chuyển sang slide Section 2.

---

### SLIDE - Section 2: Pattern-first thinking
- Kicker: Section 2
- Title: Section 2 — Pattern-first thinking
- Nội dung: Hiểu vì sao screen-by-screen rạn nứt; dùng AI chat tool tạo prototype pattern hoàn chỉnh. Gồm 2 phần nhỏ.
- 🎨 Visual: Frame placeholder (diagram/illustration TBD)
- Loại visual: Frame placeholder (illustration/image TBD)
- Ghi chú thuyết trình: Nhấn "2 phần nhỏ" — 1 phần tư duy, 1 phần thực hành tạo prototype pattern bằng chuỗi prompt.

### SLIDE - Section 3: Build & refine
- Kicker: Section 3
- Title: Section 3 — Build & refine
- Nội dung: Phần dày nhất, 3 phần nhỏ — dọn dẹp file, build bằng AI coding tool, tinh chỉnh, chia sẻ & phản tư
- 🎨 Visual: Frame placeholder (diagram/illustration TBD)
- Loại visual: Frame placeholder (illustration/image TBD)
- Ghi chú thuyết trình: Nói rõ đây là phần dày nhất khóa học (3 phần nhỏ), để học viên không bất ngờ khi thấy Section 3 dài hơn hẳn Section 2 và 4.

### SLIDE - Section 4: Stitching prototype
- Kicker: Section 4
- Title: Section 4 — Stitching prototype
- Nội dung: Nối màn hình thành hành trình người dùng liền mạch, đủ demo cho stakeholder trong 1 phút; có case study thực tế
- 🎨 Visual: Frame placeholder (diagram/illustration TBD)
- Loại visual: Frame placeholder (illustration/image TBD)
- Ghi chú thuyết trình: Nhắc sẽ có 1 case study thực tế (không nêu tên công ty) ở section này — tạo kỳ vọng nhẹ để học viên đi hết khóa học.

---

### NUMBERED - Cần chuẩn bị gì trước khi bắt đầu
- Kicker: Trước khi vào Section 2
- Title: 4 thứ *cần có sẵn.*
- Nội dung: 4 item đánh số:
  1. Kiến thức Figma cơ bản — tạo frame, dùng component, nối màn hình
  2. Một AI chat tool bất kỳ mà bạn quen dùng
  3. Một AI coding tool có thể đọc file Figma của bạn
  4. Một design project của chính bạn, dù mới sơ khai — mọi bài tập đều thực hành trên dữ liệu thật
- 🎨 Visual: 4 icon checklist đơn giản tương ứng 4 mục, layout dạng danh sách rõ ràng, không cần minh họa phức tạp.
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Nhấn mạnh mục 4 (design project thật) là quan trọng nhất — nếu chưa có, khuyến khích học viên chọn ngay một dự án dang dở, dù nhỏ, trước khi vào Section 2.

---

### SLIDE - Tools you'll use
- Kicker: Công cụ
- Title: Chọn AI tool theo nhu cầu
- Nội dung: Bảng 5 hàng, gộp tool cùng cơ chế hỗ trợ design system vào chung 1 hàng:

| Tool | Nhóm | Hỗ trợ Design System | Điểm mạnh | Dùng khi nào |
|---|---|---|---|---|
| Cursor / Claude Code / Windsurf | AI coding tool | Cao nhất. Qua Figma MCP, đọc trực tiếp variable, token, component, variant. | Chi tiết nhất về design system qua MCP. Cần tự setup kết nối. | Đã quen dùng code editor, cần build bám sát design system nhất. |
| Claude Design | AI design tool | Cao nhất. Tự dựng design system từ codebase và file thiết kế ngay lúc onboarding, rồi tự áp dụng cho mọi prototype sau. | Không cần setup MCP. Tạo prototype trực quan nhanh từ text hoặc ảnh, chỉnh sửa trực tiếp qua comment. | Muốn design system tự đồng bộ, không cần cấu hình. Cần prototype hay deck nhanh. |
| Bolt / Replit | AI coding tool | Cao. Đọc trực tiếp Figma metadata, gồm token và component thật. | Có sẵn frontend, backend, database. Fidelity cao. | App full-stack, vẫn giữ fidelity cao với thiết kế gốc. |
| Figma Make | AI design tool | Trung bình. Kết nối trực tiếp Figma nhưng chưa expose token rõ ràng. | Fidelity hình ảnh cao, dễ dùng nhất vì nằm ngay trong Figma. | Đã có design sẵn trong Figma, chỉ cần thêm tương tác. |
| Lovable | AI coding tool | Thấp. Dựa vào mô tả brand bằng lời, không extract token trực tiếp. | Generate cả app hoàn chỉnh từ mô tả bằng lời. | MVP hoặc small production app, không muốn đụng code. |

  + Bảng đã sắp xếp từ hỗ trợ design system mạnh nhất xuống thấp nhất (Cao nhất → Cao nhất → Cao → Trung bình → Thấp)
  + Lưu ý bắc cầu: cột "Hỗ trợ Design System" là lý do Section 3 Lesson 4 dạy setup MCP. Công cụ càng hỗ trợ tốt việc đọc token và component thật, càng ít phải đoán.
  + Caveat thời gian: đây là bức tranh tại thời điểm quay (07/2026). Thị trường đổi nhanh, nên nguyên tắc chọn theo nhóm và theo mức độ hỗ trợ design system bền hơn tên tool cụ thể.
- 🎨 Visual: Bảng so sánh đầy đủ 5 cột (Tool / Nhóm / Hỗ trợ Design System / Điểm mạnh / Dùng khi nào), dùng màu hoặc icon (Cao/Trung bình/Thấp) cho cột "Hỗ trợ Design System" để dễ quét mắt, nhóm theo 2 khối màu (design-first / code-first)
- Loại visual: ☑ Diagram (bảng so sánh) ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Đọc nhanh theo từng nhóm, không đọc hết bảng theo hàng. Nhấn cột "Hỗ trợ Design System" vì đây là cầu nối trực tiếp tới MCP Section 3 Lesson 4. Công cụ hỗ trợ tốt, như Cursor, Claude Code, Windsurf, Claude Design, hay Bolt và Replit, sẽ ít lệch với thiết kế gốc hơn công cụ chỉ dựa vào mô tả như Lovable. Nhắc học viên đây là bức tranh tại thời điểm quay, nguyên tắc chọn bền lâu hơn tên tool cụ thể.
- **Sửa đồng bộ (2026-07-18), ngoại lệ quy ước:** Theo yêu cầu trực tiếp của Winnie, slide này nêu tên tool cụ thể. Đây là ngoại lệ có chủ đích với quy ước "không nêu tên AI tool cụ thể" ở CLAUDE.md, chỉ áp dụng riêng cho slide này. Bảng đã qua nhiều vòng chỉnh: từ 8 hàng xuống 5 tool phổ biến nhất theo dữ liệu quy mô, thêm Claude Design thành tool thứ 6 vì minh họa rõ khái niệm tự dựng design system tự động, bỏ v0 để về lại 5 tool. Vòng gần nhất, Winnie yêu cầu gộp tool cùng cơ chế vào chung 1 hàng để nêu được nhiều tên hơn mà vẫn giữ 5 hàng: hàng Cursor gộp thêm Claude Code và Windsurf (cả 3 đều kết nối qua Figma MCP, cùng mức hỗ trợ Cao nhất), hàng Bolt gộp thêm Replit (cả 2 đều đọc trực tiếp Figma metadata, cùng mức Cao). Claude Design và Figma Make và Lovable vẫn đứng riêng vì không có tool nào khác cùng cơ chế để gộp. Bảng giờ có 5 hàng, 9 tên tool. Nhóm AI chat tool vẫn không có đại diện cụ thể, narration ở `section 1-lesson.md` giải thích đây là lựa chọn cá nhân, không cần xếp hạng. Khớp với thay đổi tương ứng trong `section 1-lesson.md` Lesson 3.

---

### END - Kết thúc Section 1
- Kicker: Xong phần giới thiệu
- Title: Hẹn gặp bạn *ở Section 2.*
- Sign: Winnie
- Contact: (để trống — Winnie điền kênh liên hệ nếu muốn hiển thị)
- 🎨 Visual: Không cần minh họa, giữ đúng phong cách tối giản của layout `.end`.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (không áp dụng — slide end thuần chữ)
- Ghi chú thuyết trình: Cảm ơn ngắn gọn, nhắc lại 4 thứ cần chuẩn bị một lần cuối, rồi chuyển sang Section 2.

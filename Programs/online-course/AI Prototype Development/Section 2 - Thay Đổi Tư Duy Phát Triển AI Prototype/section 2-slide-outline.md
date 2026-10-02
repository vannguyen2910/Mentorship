# Slide Outline: Section 2 Phần A - Tư Duy Pattern-First

> **Nguồn nội dung:** `module-01-pattern-first-thinking.md` (cùng thư mục). Đây là bản outline cho slide đi kèm 3 lesson của Module 01, chưa build thành deck HTML, chỉ là bản kế hoạch để duyệt trước khi build (theo Rule WF-5).
> **Cấu trúc:** 1 deck liền mạch cho cả module (không tách deck riêng theo từng lesson), có slide "divider" đánh dấu ranh giới mỗi lesson, cùng convention với deck lớp live (`ai-prototype-development-slide-outline.md`).
> **Ngôn ngữ:** Tiếng Việt, giữ nguyên tiếng Anh cho thuật ngữ chuyên môn (prototype pattern, component inventory, template, state, variant, AI chat tool, AI coding tool, Figma...).
> **Thuật ngữ:** Đã đổi "prototype framework" → "prototype pattern" để khớp với lesson file gốc và slide deck lớp live (cả hai đều dùng "pattern", có lý do giải thích rõ trong Overview: mượn từ Prototype Design Pattern trong lập trình).
> **Loại visual (mới):** Không mặc định mọi slide là illustration hay diagram. Mỗi slide giờ có dòng "Loại visual" riêng để chọn giữa Diagram / Illustration / Real image, hiện để trống (chưa quyết định), Winnie sẽ điền khi build. Mô tả 🎨 Visual hiện tại vẫn giữ nguyên làm gợi ý nội dung/bố cục, không phải chỉ định loại visual.
> **Ghi chú thuyết trình (mới):** Mỗi slide giờ có dòng "Ghi chú thuyết trình" riêng, viết theo văn nói (không phải văn viết trên slide), để Winnie đọc lướt qua khi trình bày trực tiếp. Đây là gợi ý cách nói, không phải nội dung bắt buộc phải đọc nguyên văn.

---

## Prompt để build (khi đã duyệt outline)

```
Dùng outline trong file này, build slide deck HTML cho Section 2 Phần A - Tư Duy Pattern-First
(khóa Systematic AI Prototyping for Product Designers, bản tiếng Việt).

Theo đúng rule trong _System/rules/SLIDE_DECK_RULES.md.
Copy tokens.css và deck-stage.js vào thư mục module này (`Phần A - Tư Duy Pattern-First`) để deck tự chứa (self-contained).

HƯỚNG DẪN THIẾT KẾ - áp dụng cho toàn bộ slide:
- Ưu tiên visual (diagram/illustration/real image) hơn bullet list thuần text.
- Mỗi slide có dòng "Loại visual" riêng (Diagram / Illustration / Real image) - kiểm tra ô nào
  đã được chọn trước khi build. Nếu chưa chọn (còn để trống), dừng lại và hỏi Winnie trước khi
  build slide đó, đừng tự mặc định là diagram.
- Với slide chọn Diagram: dùng inline SVG, chỉ dùng token colour (--sienna, --ochre, --sage,
  --ink, --paper) + accent tím của deck.
- Với slide chọn Illustration hoặc Real image: cần asset riêng (không phải SVG code), hỏi Winnie
  nguồn ảnh/minh hoạ trước khi build.
- Mỗi slide "divider" đánh dấu 1 lesson mới trong module: dùng layout .section-divider.
- Slide loại LAYER (giới thiệu 1 trong 3 layer của prototype pattern) dùng layout 3 phần rõ ràng:
  Là gì / Vì sao cần / Cách xác định, không gộp chung thành 1 đoạn văn dài.
- Slide PRACTICE (bài tập) và STATEMENT tổng kết cuối module dùng layout .practice / .end.
- Giữ tiếng Anh cho thuật ngữ chuyên môn ngay trong câu tiếng Việt.
- Dòng "Ghi chú thuyết trình" đưa vào phần speaker notes của HTML deck (không hiển thị trên
  slide chính), dùng đúng framework speaker-notes có sẵn trong SLIDE_DECK_RULES.md nếu có.
```

---

## Thống kê

**34 slide tổng cộng:** 1 cover + 1 roadmap + 4 lesson-divider + 23 slide nội dung (Lesson 1: 8, Lesson 2: 7, Lesson 3: 6, Lesson 4: 2) + 4 practice (bài tập) + 1 end.

| Phần | Số slide |
|---|---|
| Cover + Roadmap | 2 |
| Lesson 1: Cái Bẫy Screen-by-Screen | 1 divider + 8 nội dung = 9 |
| Lesson 2: Prototype Pattern Là Gì | 1 divider + 7 nội dung = 8 |
| Lesson 3: Chọn Câu Chuyện Của Prototype | 1 divider + 6 nội dung = 7 |
| Lesson 4: Dọn Dẹp Design File | 1 divider + 2 nội dung = 3 |
| Bài tập (1, 2, 3, 4) + Kết thúc | 5 |
| **Tổng** | **34** (không tính chia nhỏ khi build) |

> **Cập nhật (Lesson 4 mới, chuyển từ Section 3):** Đã thêm Lesson 4 "Dọn Dẹp Design File Trước Khi AI Đọc" (2 slide nội dung: TABLE 5 quy tắc + STATEMENT checklist) + Bài Tập 4 "Dọn Dẹp File Figma", chuyển nguyên vẹn từ Section 3 Lesson 1 + Lesson 2 (Practice 1), theo quyết định restructure khóa học tháng 8/2026: cleanup file Figma giờ thuộc bước chuẩn bị ở Section 2, không phải mở đầu Section 3. Tổng slide tăng từ 30 lên 34 (+1 divider, +2 nội dung, +1 practice). Slide "END" giữ nguyên không đổi.

> **Sửa số liệu:** Bảng thống kê trước đây ghi nhầm Lesson 1 là 7 slide nội dung, thực tế đã là 8 kể từ khi thêm slide COMPARE "Cách làm cũ vs Cách làm mới" ở lượt cập nhật trước. Số liệu ở đây đã khớp lại với số slide thực tế liệt kê bên dưới.

> **Cập nhật (thêm Bài tập 2 và 3):** Lesson file đã thêm 2 bài tập mới sau Bài tập 1 (Starter Sheet): Bài tập 2 - thiết kế 2–3 screens bằng tay trong Figma dựa trên core flow đã chọn, và Bài tập 3 - tự tay set up token, component inventory, và template từ chính các screen đó, trước khi Phần B dùng AI làm lại nhanh hơn. Cả 2 bài tập đều không có mốc thời lượng cụ thể (theo yêu cầu). Phần "Bài tập & Kết thúc" tăng từ 2 lên 4 slide (3 PRACTICE + 1 END).

> **Cập nhật (ghi chú thuyết trình):** Đã thêm dòng "Ghi chú thuyết trình" cho cả 28 slide, viết theo văn nói để Winnie đọc lướt khi trình bày trực tiếp, tách biệt với nội dung hiển thị trên slide (Kicker/Title/Lead). Bắt đầu từ yêu cầu viết ghi chú cho slide "DIAGRAM - Layer 3, phần A (danh mục template)", sau đó áp dụng cho toàn bộ outline.

> **Cập nhật (Layer 3 đổi tên thành Template):** "Interaction Pattern" đã đổi thành "Template" trên toàn bộ outline (Kicker/Title/Lead/Visual/Ghi chú thuyết trình), để khớp với thang Atomic Design Atom → Molecule → Organism → Template → Page dùng trong slide "3 layer, 1 document". Cả 2 phần của layer này đều đổi tên theo: phần A (danh mục 7 loại pattern tái sử dụng) và phần B (chuỗi màn hình gắn nhãn pattern) giờ dùng "template" thay cho "pattern". Không đổi "prototype pattern" (tên document tổng, giữ nguyên) hay "Pattern-First" (tên mindset của Module 01, giữ nguyên).

> **Cập nhật (bỏ slide state riêng của màn hình):** Đã bỏ slide DIAGRAM "Component inventory áp dụng cho cả màn hình" ở Lesson 2 (theo yêu cầu review). Lesson 2 giảm từ 8 xuống 7 slide nội dung. Nội dung ví dụ Home Dashboard/state màn hình vẫn còn trong `module-01-pattern-first-thinking.md` (Layer 2), chỉ không còn slide riêng minh hoạ nó, đã gộp ngầm vào phần nói của slide "LAYER - Layer 2: Component Inventory."

> **Cập nhật (3 layer, không phải 2):** Prototype pattern giờ gồm 3 layer, không phải 2: **Token** (tông màu/phong cách hệ thống, tách ra thành layer riêng), **Component Inventory** (đã bao gồm state, không đổi), và **Template** (tên gọi hiện tại, trước đây gọi là Interaction Pattern, xem cập nhật đổi tên bên trên). Mỗi layer có 1 slide loại "LAYER" riêng, trình bày theo cấu trúc cố định: Là gì / Vì sao cần / Cách xác định, để lesson dễ theo dõi hơn thay vì dồn cả 2 layer cũ vào chung 1 mạch. Lesson 2 tăng từ 6 lên 8 slide nội dung, giữ nguyên 14 phút.

> **Cập nhật (không còn Kiểm tra kiến thức):** Đã bỏ slide STATEMENT "Kiểm tra kiến thức" cuối module. Bài tập (PRACTICE) là hình thức thực hành duy nhất sau mỗi module, khớp với quyết định course-wide là mỗi module có 1 assignment thay vì thêm 1 bước quiz riêng.

> **Cập nhật (concept ban đầu trước khi dùng AI):** Đã thêm 1 slide STATEMENT "Phác thảo concept ban đầu của riêng bạn" ở Lesson 3, ngay trước slide Entry point, nhắc học viên phác thảo ít nhất 1-2 hướng concept riêng cho 2-3 màn hình đã chọn trước khi bước sang Phần B, để AI mở rộng ý tưởng chứ không thay thế tư duy sáng tạo của học viên. Bài tập cuối module cũng thêm câu hỏi số 5 tương ứng.

> **Cập nhật (Layer 3 đổi tên qua nhiều lượt):** "Interaction Map" đã đổi thành "Interaction Pattern", tách thành 2 slide: (A) danh mục 7 loại tái sử dụng (Read/Edit/Add/Confirm/Navigate/Search/Onboard, 1 màn hình có thể mang nhiều loại), và (B) chuỗi màn hình cụ thể gắn nhãn theo loại đã định nghĩa. Sau đó "Interaction Pattern" tiếp tục đổi thành "Template" (xem cập nhật ở trên) để khớp với thang Atomic Design.

> **Cập nhật:** Đã thêm 1 slide COMPARE "Cách làm cũ vs Cách làm mới" ở Lesson 1 (đồng bộ với phần Traditional prototype vs AI-assisted prototype vừa thêm vào lesson file), nên Lesson 1 tăng từ 6 lên 7 slide nội dung. Toàn bộ ví dụ/visual trong Lesson 1-2 giờ dùng chung ẩn dụ "hộp Lego" và "bản đồ board game" đơn giản, khớp với cách giải thích mới trong lesson file (dễ hiểu hơn, không giả định người xem đã biết Component Inventory hay Interaction Map là gì). Toàn bộ "prototype framework" đã đổi thành "prototype pattern" để khớp với lesson gốc.

> **Cập nhật (loại visual):** Đã thêm dòng "Loại visual" (Diagram / Illustration / Real image) cho từng slide bên dưới, hiện để trống chờ Winnie quyết định. Trước đây outline ngầm định mọi slide đều là diagram/illustration kiểu SVG - giờ đây là 3 lựa chọn tách biệt, có thể trộn lẫn giữa các slide.

---

## 1. Cover & Roadmap

---

### COVER
- Kicker: Section 2, Phần A · Khóa Systematic AI Prototyping for Product Designers
- Title: Tư Duy\nPattern-First
- Subtitle: Vì sao prototype bằng AI thất bại nếu không có kế hoạch, và cách khắc phục trước khi bắt đầu
- 🎨 Visual: Giữ tinh thần cover của deck lớp live (phone mockup neon) nhưng đơn giản hoá cho lesson online. Ví dụ: một khối UI đang "lệch" (drift) dần từ trái sang phải, gợi mở vấn đề mà module sẽ giải quyết.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Chào mừng học viên vào Section 2, Phần A. Nói rõ đây không phải bài học kỹ thuật Figma, mà là bài học tư duy: vì sao rất nhiều người dùng AI để prototype nhưng kết quả vẫn rời rạc, và cách khắc phục trước khi chạm vào bất kỳ màn hình nào.

---

### PROCESS - Lộ trình Section 2, Phần A
- Kicker: Trong module này
- Title: 4 lesson. *4 bài tập.*
- Nội dung: 4 ô ngang nối tiếp nhau: "Lesson 1: Cái bẫy screen-by-screen" → "Lesson 2: Prototype pattern là gì" → "Lesson 3: Chọn câu chuyện" → "Lesson 4: Dọn dẹp design file" → dẫn tới 4 ô cuối: "Bài tập 1: Starter sheet cho câu chuyện" → "Bài tập 2: Thiết kế screens trong Figma" → "Bài tập 3: Set up design system bằng tay" → "Bài tập 4: Dọn dẹp file Figma."
- 🎨 Visual: 8 node nối bằng đường kẻ ngang (giống layout .process), 4 node bài tập cuối tô đậm màu accent để nhấn đây là điểm đến của module.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Giới thiệu nhanh cấu trúc module, 4 lesson ngắn dẫn tới 4 bài tập nối tiếp nhau: viết starter sheet, thiết kế screen, tự tay set up design system, rồi dọn dẹp file Figma trước khi bước sang Section 3. Chưa cần đi sâu, chỉ cần học viên nắm bức tranh tổng thể trước khi vào từng phần.

---

## 2. Lesson 1: Cái Bẫy Screen-by-Screen

---

### SECTION - Lesson 1
- Title: Lesson 1\nCái bẫy\nscreen-by-screen
- Sub: Vì sao cách hầu hết designer đang prototype lại đang làm chậm chính họ
- 🎨 Visual: Nền tối (--ink), số "01" mờ lớn góc trên trái, title màu trắng căn giữa, giống section-divider của deck gốc.
- Loại visual: ☐ Diagram ☑ Illustration ☐ Real image
- Ghi chú thuyết trình: Chuyển vào Lesson 1. Có thể mở đầu bằng câu hỏi: "Có ai từng thấy quen cảnh này chưa?" để tạo tương tác trước khi qua slide tiếp theo.

---

### STATEMENT - Vòng lặp quen thuộc
- Kicker: Bạn có quen cảnh này không?
- Title: Mở Figma. Chọn 1 màn hình. *Lặp lại.*
- Lead: Tương tự việc tự tạo một viên gạch Lego mới ở mỗi phòng, thay vì lấy ra một hộp Lego có sẵn. "Mở Figma → chọn màn hình → thiết kế → chọn màn hình khác → thiết kế → thử nối chúng lại → nhận ra không khớp → quay lại sửa → lặp lại." Quy trình này có vẻ hiệu quả, nhưng trên thực tế không phải vậy.
- 🎨 Visual: Sơ đồ vòng lặp mũi tên khép kín (loop diagram) với 6-7 bước ngắn, bước cuối mũi tên quay lại bước đầu. Có thể lồng nhỏ icon viên gạch Lego ở góc để gợi ẩn dụ.
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Đọc chậm chuỗi hành động trong vòng lặp để học viên tự nhận ra chính họ trong đó. Nhấn giọng ở câu cuối, "có vẻ hiệu quả nhưng thực tế không phải vậy", vì đây là câu bản lề dẫn sang phần vấn đề.

---

### COMPARE - Cách làm cũ vs Cách làm mới
- Kicker: Sự khác biệt nằm ở đâu
- Title: Traditional prototype. *AI-assisted prototype.*
- Bảng 7 dòng, cột phải tô nhấn:

| | Traditional prototype | AI-assisted prototype |
|---|---|---|
| Cách thực hiện | Tự thiết kế từng màn hình | Định nghĩa hộp Lego 1 lần, AI ráp phần còn lại |
| Khi cần điều chỉnh | Sửa từng màn hình một | Sửa 1 chỗ, mọi màn hình tự update |
| Thời gian | Vài tuần đến vài tháng | Nhanh hơn nhiều |
| Yêu cầu kĩ thuật | Cần thành thạo design tool | Tùy tool: design tool dễ, coding tool cần setup |
| Độ chuyên nghiệp | Tùy kỹ năng cá nhân | Tùy chất lượng pattern |
| Khả năng mở rộng | Khó, càng nhiều càng nặng | Dễ, reuse cùng 1 system |
| Tính bền vững | Dễ bỏ cuộc | Ít burnout hơn |

- 🎨 Visual: Layout `.compare` 2 cột, giống slide "Traditional vs AI-assisted prototype" của deck lớp live, viền cột phải tô màu accent tím để nhấn đây là hướng module sẽ dạy.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: So sánh 2 cách làm ngay từ đầu để học viên hình dung đích đến trước khi đi sâu vào vấn đề. Nhấn mạnh dòng "reuse cùng 1 system" vì đây là insight quan trọng nhất trong bảng.

---

### DIAGRAM - Vòng lặp screen-by-screen
- Kicker: Đây là những gì thực sự xảy ra
- Title: Ba thứ *âm thầm rạn nứt.*
- Lead: Không phải bạn làm sai, chỉ là không có gì được định nghĩa trước khi bắt đầu.
- 🎨 Visual: 3 icon nhỏ tương ứng 3 vấn đề sắp trình bày (component/AI/state), làm cầu nối cho 3 slide tiếp theo.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Slide cầu nối, nói ngắn gọn rằng cả 3 vấn đề sắp trình bày đều xuất phát từ cùng 1 nguyên nhân, không có gì được định nghĩa trước khi bắt đầu, rồi chuyển sang slide tiếp theo.

---

### STATEMENT - Component bị lệch (drift)
- Kicker: Vấn đề 1
- Title: Component bị lệch. *Không ai để ý.*
- Lead: Nút bấm ở màn hình 1 có thể khác biệt nhẹ so với nút bấm ở màn hình 3. Sự khác biệt này thường không được chú ý, cho đến khi cần cập nhật style tại 12 vị trí khác nhau.
- 🎨 Visual: 3 khung phone-frame với button hơi lệch dần (bo góc, size khác nhau nhẹ), callout "Spacing đổi", "Bo góc khác", giống visual "drift" của deck gốc.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Vấn đề 1. Có thể hỏi học viên đã từng gặp trường hợp này chưa, để tăng tính tương tác trước khi qua vấn đề 2. Nhấn mạnh con số "12 vị trí khác nhau" để cho thấy chi phí sửa lại lớn thế nào.

---

### STATEMENT - Prompt AI bắt đầu lại từ 0
- Kicker: Vấn đề 2
- Title: Mỗi prompt, *một điểm xuất phát mới.*
- Lead: AI không lưu lại thông tin từ yêu cầu trước đó, nên nút bấm vừa được mô tả cần được tả lại từ đầu ở lần kế tiếp, và mỗi lần kết quả sẽ có sự khác biệt vì không có điểm tham chiếu.
- 🎨 Visual: 3 khối prompt rời rạc, không có đường nối giữa chúng (ngược lại hoàn toàn với slide "3 layer, 1 document" sẽ xuất hiện ở Lesson 2).
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Vấn đề 2. Có thể dùng ẩn dụ trong lesson file, nhờ một người vẽ lại cùng một con mèo nhiều lần nhưng mỗi lần phải mô tả lại từ đầu, để giải thích vì sao AI không có bộ nhớ giữa các lần yêu cầu.

---

### STATEMENT - State bị bỏ sót
- Kicker: Vấn đề 3
- Title: State bị bỏ sót. *Đến khi quá muộn.*
- Lead: State mặc định của màn hình login thường được thiết kế đầy đủ, trong khi các tình huống như sai mật khẩu, đang loading, hoặc mất mạng lại bị bỏ sót, và thường chỉ được phát hiện bởi developer hoặc user.
- 🎨 Visual: Khung phone hiện state "Default" rõ nét, 3 khung mờ dần bên cạnh ghi "Error?", "Loading?", "No internet?" như những khoảng trống chưa ai lấp.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Vấn đề 3. Hỏi trực tiếp học viên, màn hình login của bạn đã thiết kế trường hợp sai mật khẩu chưa, để họ tự đối chiếu với dự án của mình ngay tại chỗ.

---

### COMPARE - Pattern-first sửa cả ba
- Kicker: Giải pháp
- Title: Pattern-first. *Sửa cả ba cùng lúc.*
- Bảng 2 cột (Vấn đề / Giải pháp pattern-first):
  - Component bị lệch → Định nghĩa component tồn tại một lần, trước khi build bất kỳ màn hình nào
  - AI bắt đầu lại từ 0 → Đưa AI một prototype pattern document, nó build dựa trên đó mỗi lần
  - State bị bỏ sót → Map state trước khi build, không phải sau
- 🎨 Visual: Layout `.compare` 2 cột, cột phải (giải pháp) tô nhấn màu accent.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Slide bản lề quan trọng nhất của Lesson 1, chốt lại cả 3 vấn đề bằng đúng 1 giải pháp. Đi qua từng dòng bên trái trước, để học viên nhận ra cả 3 vấn đề đều quen thuộc, rồi mới lật sang cột phải: component bị lệch được giải quyết bằng cách định nghĩa component đúng một lần trước khi build, AI mất trí nhớ được giải quyết bằng việc luôn đưa AI đọc lại prototype pattern document thay vì mô tả lại từ đầu mỗi lần, và state bị bỏ sót được giải quyết bằng cách map state trước khi build chứ không phải vá sau. Đọc chậm cột phải, vì đây chính là lời hứa của cả module.

---

### STATEMENT - Chuyển tiếp sang Lesson 2
- Kicker: Một câu để nhớ
- Title: Prototype pattern không phải việc làm thêm. *Đó chính là việc.*
- Lead: Đây là công việc khiến mọi thứ sau đó nhanh hơn, không phải bước phụ trước khi "làm việc thật."
- 🎨 Visual: Slide trơn, chỉ chữ, giống các slide "STATEMENT" trầm lắng cuối phase trong deck gốc, không cần diagram.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Câu kết Lesson 1. Đọc chậm, để một khoảng lặng ngắn trước khi chuyển slide, vì đây là câu học viên nên nhớ nhất trong cả lesson.

---

## 3. Lesson 2: Prototype Pattern Là Gì

---

### SECTION - Lesson 2
- Title: Lesson 2\nPrototype\npattern là gì
- Sub: Ba thứ AI cần mà hầu hết designer chưa bao giờ viết ra
- 🎨 Visual: Nền tím/violet đậm, số "02" mờ lớn góc trên trái, title trắng căn giữa.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Chuyển vào Lesson 2, phần lõi và dài nhất của module. Có thể báo trước, đây là phần quan trọng nhất, nên sẽ đi chậm hơn các lesson khác.

---

### STATEMENT - Định nghĩa + tổng quan 3 layer
- Kicker: Bắt đầu từ đây
- Title: 1 document. *3 layer.*
- Lead: Prototype pattern là bản mô tả có cấu trúc về design system của bạn mà AI có thể build dựa vào: token, component inventory, và template.
- 🎨 Visual: Sơ đồ 3 khối xếp chồng (Token trên cùng, Component Inventory ở giữa, Template dưới cùng), mũi tên nối xuống 1 khung phone-frame ghi "AI build từ đây."
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Cho học viên xem bản đồ tổng thể 3 layer trước khi đi vào chi tiết từng layer. Nói rõ mỗi layer sắp tới sẽ được giải thích theo cùng 1 công thức, là gì, vì sao cần, cách làm, để học viên biết trước cách theo dõi.

---

### LAYER - Layer 1: Token
- Kicker: Layer thứ nhất, "tông màu và phong cách của cả hộp Lego"
- Title: Hệ thống này nên *cảm giác* ra sao?
- Là gì: Những quyết định nền tảng về cảm giác hệ thống, đặt ra trước khi bất kỳ component nào được định nghĩa: bảng màu, thang chữ, nhịp khoảng cách, độ bo góc.
- Vì sao cần: Bỏ qua bước này khiến mỗi component AI tạo ra có phong cách hơi khác nhau, vì không có quy tắc chung nào được thiết lập từ trước.
- Cách xác định: Mô tả cảm giác mong muốn bằng ngôn ngữ thường (êm dịu/năng động, tối giản/phong phú, nghiêm túc/vui tươi), từ đó suy ra bảng màu và thang chữ. Phần B sẽ hướng dẫn cách biến mô tả này thành token thật bằng AI.
- 🎨 Visual: Layout 3 cột hoặc 3 khối xếp dọc (Là gì / Vì sao / Cách làm), bên phải minh hoạ 1 dải màu (color swatch) + 1 thang chữ mẫu, không gắn với sản phẩm cụ thể nào.
- Loại visual: ☐ Diagram ☐ Illustration ☑ Real image
- Ghi chú thuyết trình: Nhấn mạnh token không phải là chọn màu cụ thể, mà là quyết định cảm giác trước. Ví dụ nhanh, êm dịu hay năng động, để học viên hình dung ngay chứ không nghĩ đây là bước kỹ thuật.

---

### LAYER - Layer 2: Component Inventory
- Kicker: Layer thứ hai, "danh sách những viên gạch bạn có"
- Title: Bạn có gì, và nó *trông ra sao?*
- Là gì: Danh sách mọi component tồn tại trong hệ thống, cùng toàn bộ variant và state của mỗi component, đã bao gồm state, không phải layer riêng.
- Vì sao cần: Nếu component không được liệt kê trước, mỗi màn hình sẽ được AI build với những biến thể hơi khác nhau của cùng một component, đúng vấn đề "component bị lệch" đã nêu ở Lesson 1.
- Cách xác định: Với mỗi component, ghi lại toàn bộ variant và state nó có thể mang, áp dụng cho cả màn hình lớn như Dashboard.
- 🎨 Visual: 2 card ví dụ (Button: Primary/Secondary/Ghost, Default/Hover/Loading/Disabled; Input Field: Text/Password/Search, Empty/Filled/Error/Focused), viền màu ochre giống deck gốc. Có thể vẽ nhỏ icon viên gạch Lego cạnh tiêu đề để nối lại ẩn dụ từ Lesson 1.
- Loại visual: ☐ Diagram ☐ Illustration ☑ Real image
- Ghi chú thuyết trình: Layer quen thuộc nhất với designer. Có thể hỏi nhanh, ai đã từng liệt kê component trước khi thiết kế màn hình chưa, rồi liên hệ ngược lại vấn đề "component bị lệch" đã nói ở Lesson 1. Nhắc thêm, ví dụ Home Dashboard cũng cần liệt kê state riêng của cả màn hình, không chỉ component nhỏ.

---

### LAYER - Layer 3: Template
- Kicker: Layer thứ ba, "loại nhiệm vụ + bản đồ chỉ đường"
- Title: Màn hình này đang làm *loại việc gì, và dẫn tới đâu?*
- Là gì: Giống một trò chơi board game, mỗi ô trên bàn cờ tương ứng với một loại nhiệm vụ quen thuộc. Template gồm 2 phần: danh mục loại tương tác, và chuỗi màn hình cụ thể.
- Vì sao cần: Không có bản đồ này, AI phải đoán màn hình này dẫn tới đâu, và mỗi lần đoán có thể ra kết quả khác nhau.
- Cách xác định: Gắn nhãn loại template cho từng màn hình (phần A), rồi vẽ transition và điều kiện giữa các màn hình (phần B).
- 🎨 Visual: Layout 3 cột (Là gì / Vì sao / Cách làm), bên phải minh hoạ nhỏ 1 phone-frame gắn chip "Confirm" nối mũi tên sang phone-frame khác, làm cầu nối cho 2 slide chi tiết tiếp theo.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Layer khó hình dung nhất trong 3 layer. Dùng ẩn dụ board game, mỗi ô trên bàn cờ ứng với 1 loại nhiệm vụ quen thuộc, để học viên nắm ý tưởng trước khi vào 2 slide chi tiết tiếp theo, danh mục template và chuỗi màn hình.

---

### DIAGRAM - Layer 3, phần A (danh mục template)
- Kicker: Danh mục 7 loại template
- Title: 7 loại. *Dùng lại nhiều nơi.*
- Lead: 7 loại template tái sử dụng được: Read, Edit, Add, Confirm, Navigate, Search/Filter, Onboard. Hầu hết prototype chỉ cần 3-4 loại, và 1 màn hình có thể mang nhiều template cùng lúc (vd. checkout vừa Edit vừa Confirm).
- 🎨 Visual: Bảng 7 dòng (giống bảng "Interaction pattern types" của deck lớp live) dạng 7 card nhỏ 4+3, mỗi card: tên loại + 1 dòng mô tả + ví dụ màn hình. Định nghĩa "Confirm" trong 1 card, rồi vẽ mũi tên nhỏ chỉ nó có thể "dán nhãn" lại cho nhiều phone-frame khác nhau, để nhấn ý "định nghĩa 1 lần, dùng nhiều nơi."
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: 7 loại template này là danh mục dùng để tra cứu, không phải danh sách phải học thuộc lòng, mục tiêu là mỗi khi nhìn một màn hình, học viên biết ngay nó thuộc loại nào. Đi theo đúng thứ tự card trên slide: Read là loại đơn giản nhất, user chỉ xem chứ không đổi gì, như dashboard hay trang hồ sơ. Edit là user sửa lại thứ đã có sẵn, ví dụ trang cài đặt hay sửa hồ sơ. Add là tạo ra thứ hoàn toàn mới, như đăng bài hay thêm sản phẩm vào giỏ. Confirm là bước xem lại và duyệt trước khi hành động chính thức xảy ra, kinh điển nhất là xác nhận thanh toán. Navigate không phải một hành động cụ thể mà là cách di chuyển giữa các phần, thanh tab hay menu. Search hoặc Filter là tìm hoặc lọc trong một danh sách, quen thuộc với bất kỳ trang kết quả tìm kiếm nào. Onboard là hướng dẫn user lần đầu, màn hình chào mừng hay các bước hướng dẫn. Chốt lại ở card cuối cùng: đừng cố dùng hết cả 7 loại, hầu hết prototype chỉ cần 3 đến 4 loại là đủ, và một màn hình hoàn toàn có thể mang nhiều template cùng lúc, ví dụ màn hình checkout vừa Edit vừa Confirm. Đây chính là lý do gọi là "template" chứ không phải "loại màn hình", nó là thứ được gắn nhãn, không cố định 1-1 với 1 màn hình, và cũng chính là lý do nó khớp với bậc Template trong thang Atomic Design.

---

### DIAGRAM - Layer 3, phần B (chuỗi màn hình)
- Kicker: Sau khi đã gắn nhãn template
- Title: Màn hình này *dẫn tới đâu?*
- Lead: Một sơ đồ các màn hình và đường nối giữa chúng: cái gì dẫn tới cái gì, trong điều kiện nào. Giống một trò chơi board game: bước vào ô này, bạn đi tới ô nào tiếp theo?
- 🎨 Visual: 3 khung phone-frame, mỗi khung có 1 chip nhỏ ghi tên template của nó (vd. "Confirm", "Read"), nối bằng mũi tên có nhãn: Login Screen → (Success) → Home Dashboard → (Tap product card) → Product Detail Screen; nhánh phụ Login Screen → (Error) → Login Screen (error state).
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Sau khi đã gắn nhãn template ở slide trước, bước tiếp theo là vẽ đường đi. Đọc ví dụ Login Screen theo đúng thứ tự trên sơ đồ, trường hợp thành công dẫn tới Home Dashboard trước, rồi mới tới nhánh lỗi quay lại chính màn hình đó, để học viên thấy rõ cả 2 nhánh đều cần được vẽ ra, không chỉ đường đi khi mọi thứ suôn sẻ.

---

### STATEMENT - 3 layer, 1 document
- Kicker: Ghép lại
- Title: Mọi thứ có thể set up theo truyền thống hoặc AI hỗ trợ.
- Lead: 3 layer này có thể được viết ra bằng AI, theo cách Phần B sẽ hướng dẫn, hoặc bạn tự thiết lập trực tiếp trong Figma, ví dụ đặt tên component rõ ràng và ghi chú loại template ngay trong file. Công cụ không quan trọng bằng việc cả 3 layer đều được viết ra ở một nơi rõ ràng, ai đọc cũng hiểu, kể cả AI lẫn đồng đội trong nhóm.
- 🎨 Visual: Sơ đồ dạng bậc thang theo đúng tinh thần Atomic Design (Brad Frost), để nối lại với chính thuật ngữ atom/molecule/organism đã dùng khi liệt kê component inventory: bậc 1 là Token (chấm màu + mẫu chữ, như nguyên liệu thô trước cả atom), bậc 2 là Component Inventory thể hiện qua chuỗi Atom → Molecule → Organism (1 nút đơn, ghép thành 1 form, rồi thành 1 khối nav bar), bậc 3 là Layer 3 của chúng ta, đặt tên là Template, đúng khớp với bậc Template → Page trong Atomic Design (khung phone-frame hoàn chỉnh, có đường nối giữa các màn hình). Ở góc trên cùng, tách 2 nhánh nhỏ dẫn tới icon AI chat tool (nhãn "Phần B: nhờ AI viết ra") và icon Figma (nhãn "Tự thiết lập trong Figma"), cho thấy cả bậc thang này có thể build bằng AI hoặc tự tay, không đổi thứ tự bậc.
- Loại visual: ☑ Diagram ☐ Illustration ☐ Real image
- Ghi chú thuyết trình: Slide tổng kết Lesson 2. Chỉ vào sơ đồ bậc thang và nhắc lại nhanh chuỗi atom, molecule, organism, template, page quen thuộc từ Atomic Design, để học viên thấy 3 layer vừa học không phải khái niệm mới hoàn toàn mà xếp gọn vào đúng thang bậc đó, và vì sao layer cuối được đặt tên là Template. Nhấn rõ đây là lựa chọn, không phải bắt buộc dùng AI: học viên có thể nhờ AI viết ra cả 3 layer như Phần B sắp hướng dẫn, hoặc tự gõ tay trong Figma bằng cách đặt tên component và ghi chú template rõ ràng. Điều thật sự quan trọng là cả 3 layer được viết ra ở đâu đó rõ ràng, không phải công cụ nào tạo ra nó, trước khi chuyển sang Lesson 3 nói về cách chọn scope.

---

## 4. Lesson 3: Chọn Câu Chuyện Của Prototype

---

### SECTION - Lesson 3
- Title: Lesson 3\nChọn một câu chuyện nhỏ
- Sub: Hộp Lego đã đầy đủ, nhưng chưa nói bạn sẽ lắp cái gì. Chọn đúng câu chuyện, không phải thêm hết mọi thứ
- 🎨 Visual: Nền sáng (--paper-deeper), số “03” mờ lớn góc trên trái, title đậm căn giữa.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Chuyển vào Lesson 3. Nhắc lại nhanh: 3 layer vừa xong chính là một hộp Lego hoàn chỉnh, nhưng hộp Lego không tự quyết định bạn xây gì. Nói rõ đây là lúc học viên bỏ việc “đưa hết mọi thứ vào prototype” và thay vào đó chọn đúng một câu chuyện nhỏ để kể.

---

### STATEMENT - Câu chuyện này cần gì?
- Title: Không phải "bao nhiêu thứ" mà là "cái gì là đúng".
- Lead: Nếu prototype là một trailer phim, bạn không cần kể toàn bộ cuộc đời nhân vật. Bạn chỉ cần chọn một khoảnh khắc quan trọng nhất, đủ để người xem hiểu ý tưởng và biết mình đang đi đâu.
- 🎨 Visual: Một khung poster trailer phim hoặc một khung cảnh cắt ngắn, không cần quá nhiều chi tiết, để gợi ý về việc chọn một khoảnh khắc thay vì toàn bộ câu chuyện.
- Loại visual: Real image (Place holder)
- Ghi chú thuyết trình: Dùng ẩn dụ trailer phim ngay từ đầu để cắt bỏ cảm giác scope là “giới hạn”. Nhấn rằng scope là cách chọn đúng thứ cần thấy.

---

### PROCESS - Quy tắc chọn câu chuyện
- Kicker: Quy tắc đơn giản
- Title: 1 goal. *2–3 màn hình. 1 câu chuyện rõ ràng.*
- Lead: Chọn đúng mục tiêu của người dùng. Chọn 2–3 màn hình đủ để thể hiện mục tiêu đó. Loại bỏ mọi thứ không giúp người dùng tiến gần hơn tới kết quả. Đây chính là nền tảng cho bước tiếp theo.
- 🎨 Visual: 1 chuỗi 3 bước ngắn, mỗi bước có icon nhỏ, layout `.process`.
- Loại visual: Illustration
- Ghi chú thuyết trình: Trình bày bằng 3 bước ngắn. Nói chậm và dùng câu “Nếu một màn hình không giúp người dùng tiến gần hơn, nó không thuộc câu chuyện này.”

---

### DIAGRAM - Các ví dụ
- Kicker: Cách làm tốt
- Title: 1 mục tiêu. *1 luồng đi.*
- Lead: Một prototype tốt không phải là một danh sách mọi thứ. Nó là một câu chuyện rõ ràng, với 1 mục tiêu và 1 đường đi hợp lý từ đầu tới cuối. Đây là thứ sẽ được dùng lại ở module tiếp theo.
- Ví dụ: "Tìm cửa hàng gần nhất" → Xem danh sách → Chọn trên bản đồ → Xem chi tiết và chỉ đường
- 🎨 Visual: 3 phone mockup thật trên nền vàng chanh, đặt cạnh nhau: màn 1 là danh sách cửa hàng dạng list, màn 2 là bản đồ với nhiều pin đánh dấu vị trí, màn 3 là chi tiết một cửa hàng kèm nút "Chỉ đường". Bên dưới có chuỗi 3 bước dạng pill nối bằng mũi tên: Danh sách cửa hàng → Xem bản đồ → Chi tiết & chỉ đường.
- Loại visual: Real image
- Ghi chú thuyết trình: Dùng ví dụ tìm cửa hàng gần nhất thay vì mô tả trừu tượng. Ba màn hình, ba bước rõ ràng: xem danh sách, chọn trên bản đồ, xem chi tiết và chỉ đường. Nhấn mạnh đây là một đường đi liền mạch phục vụ đúng một mục tiêu, không phải một nhóm màn hình rời rạc, rồi dừng lại hỏi học viên xem goal của dự án họ là gì.

---

### COMPARE/STATEMENT - Những điều cần tránh
- Kicker: Những điều cần tránh
- Title: 3 cái bẫy *khi chọn câu chuyện.*
- 3 card:
  1. Chọn nhiều user goal trong cùng một prototype: chúng sẽ không tự nhiên kết nối
  2. Chọn quá nhiều màn hình: scope creep giết chết prototype
  3. Chọn màn hình phức tạp nhất trước: hãy bắt đầu từ core flow
- 🎨 Visual: 3 card đánh số 01/02/03, tông màu trung tính/cảnh báo nhẹ.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đối lập trực tiếp với slide “Ví dụ tốt” vừa rồi. Nhấn mạnh lỗi phổ biến nhất là việc kéo câu chuyện quá rộng, vì đây là vấn đề dễ xảy ra nhất trong lớp.

---

### STATEMENT - Phác thảo concept trước khi dùng AI
- Kicker: Sẵn sàng trước khi dùng AI
- Title: Bạn cần một điểm neo *trước khi AI mở rộng.*
- Lead: Hãy dành thời gian thiết kế ít nhất 1–2 hướng concept riêng cho 2–3 màn hình đã chọn. Đây không phải để làm sản phẩm hoàn chỉnh, mà để xác định mình đang kể câu chuyện nào trước khi đưa nó vào AI.
- 🎨 Visual: 1 trang sổ tay phác thảo tay đơn giản (2–3 ô nhỏ, mỗi ô 1 hướng concept) đặt cạnh 1 khung AI chat tool mờ nhạt phía sau, gợi thứ tự “ý tưởng của bạn trước, AI hỗ trợ sau”.
- Loại visual: ☐ Diagram ☐ Illustration ☑ Real image (Winnie sẽ cung cấp ảnh sau)
- Ghi chú thuyết trình: Slide quan trọng để bảo vệ tư duy sáng tạo của học viên trước khi họ chạm vào AI ở Phần B. Nói rõ đây không phải bài tập bắt buộc nộp, mà là thói quen nên giữ suốt khóa học, ý tưởng của mình luôn đi trước, AI chỉ mở rộng chứ không quyết định thay.

---

### STATEMENT - Hướng đi của bài học
- Title: Bắt đầu từ một câu chuyện nhỏ, *rồi mới mở rộng.*
- Lead: Khi kết thúc module này, học viên cần có đủ 4 thứ để bước tiếp: hiểu rõ mục tiêu của người dùng, có sẵn 2–3 màn hình thiết kế chính, một AI tool như Cursor, Claude, hay khác, và một bộ design system có sẵn gồm token, component inventory, và template.
- 🎨 Visual: Layout 2x2 gồm 4 ô hình ảnh, mỗi ô đại diện cho một phần trong 4 điều cần có để bước tiếp: user goal, core flow, AI tool, và design system.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Xác nhận lại hướng đi mà cả khóa học sẽ theo. Đọc chậm câu cuối, bạn chỉ cần 1 user goal, 2–3 màn hình, và 1 AI tool, để trấn an học viên rằng họ đã có đủ điều kiện để bắt đầu ngay.

---

## 4b. Lesson 4: Dọn Dẹp Design File

> **Nguồn:** Chuyển từ Section 3 Lesson 1 + Lesson 2 (Practice 1), theo quyết định restructure khóa học tháng 8/2026 — dọn dẹp file Figma giờ thuộc về Section 2 (chuẩn bị trước khi chạm AI), không phải Section 3 (build bằng Claude Design).

---

### SECTION - Lesson 4
- Title: Lesson 4\nDọn dẹp design file\ntrước khi AI đọc
- Sub: AI không phân biệt được đâu là hệ thống thật, đâu là bản nháp bạn quên xoá
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn ngay từ đầu: bước này cảm giác giống dọn bàn hơn thiết kế, nhưng quyết định component inventory sau này (Section 3) sẽ chính xác hay lộn xộn.

---

### TABLE - 5 quy tắc dọn file
- Kicker: Theo tài liệu MCP chính thức của Figma
- Title: 5 quy tắc giúp AI đọc đúng file của bạn
- Bảng: Component hoá mọi thứ lặp lại · Đặt tên rõ ràng · Dùng Figma variables cho token · Dùng Auto Layout · Thêm annotation cho hành vi khó thấy.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đi qua từng dòng, nhấn "đặt tên rõ ràng" vì đây là lỗi phổ biến nhất (Frame1268 vs CTA_Button).

---

### STATEMENT - Checklist dọn dẹp
- Kicker: Trước khi bắt đầu Bài Tập 4
- Title: 4 bước. Làm một lần cho cả dự án.
- Lead: Xoá component không dùng, gộp biến thể trùng lặp, xoá layer ẩn/frame test, thống nhất tên gọi. Nếu file quá lớn, nhờ AI rà giúp bằng 1 prompt.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đưa luôn prompt mẫu nhờ AI rà soát cho học viên có file lớn, tránh cảm giác phải làm bằng tay hết.

---

## 5. Bài tập & Kết thúc

---

### PRACTICE - Bài tập 1/4: Tạo Starter Sheet cho câu chuyện
- Kicker: Trước khi qua Phần B
- Title: 4 bước. *1 trang starter sheet.*
- Nội dung (4 bước):
  1. Project bạn chọn là gì?
  2. Mục tiêu của người dùng là gì?
  3. 2–3 màn hình nào tạo nên core flow?
  4. Concept ban đầu của bạn cho những màn hình này là gì?
- 🎨 Visual: Layout `.practice` dạng 2x2 với 4 ô hình ảnh/khung nhập, mỗi ô phù hợp để chèn một ví dụ hoặc một phần nội dung từ học viên, giúp slide dễ dùng như một canvas để điền ví dụ thực tế.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Dành thời gian tại chỗ, hoặc giao về nhà, để học viên tạo một trang starter sheet nhỏ. Nhấn mạnh đây không phải bài tập dài, mà là một tài liệu dùng lại cho các module sau, và là bài tập đầu trong 3 bài tập của module này.

---

### PRACTICE - Bài tập 2/4: Thiết kế 2–3 screens trong Figma
- Kicker: Biến concept thành giao diện thật
- Title: Từ starter sheet, *tới screen thật.*
- Nội dung (bước làm):
  1. Mở lại Starter Sheet, xác nhận đúng user goal và thứ tự 2–3 screens trong core flow.
  2. Tạo file/frame Figma cho từng screen theo đúng thứ tự đó.
  3. Thiết kế đầy đủ mỗi screen ở trạng thái mặc định — chưa cần polish, chỉ cần rõ layout, nội dung, component đang dùng.
  4. Nối các screen theo đúng core flow.
- 🎨 Visual: Layout `.practice`, 1 khung Figma mockup nhỏ bên trái (frame rời rạc) nối mũi tên sang 1 khung starter-sheet thu nhỏ, gợi ý "concept → screen thật."
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn mạnh đây là bước thiết kế tay bình thường, không có gì mới về kỹ thuật Figma. Lưu ý học viên chưa cần đẹp, chỉ cần đủ rõ để dùng cho bài tập 3 ngay sau đó.

---

### PRACTICE - Bài tập 3/4: Set up design system bằng tay
- Kicker: Tự dựng hộp Lego, trước khi để AI làm
- Title: Token. Component inventory. *Template.*
- Nội dung (bước làm):
  1. Token: liệt kê lại bảng màu, thang chữ, spacing, radius đã dùng trong các screen thành 1 bộ thống nhất.
  2. Component Inventory: liệt kê mọi component xuất hiện, kèm variant và state của từng cái.
  3. Template: gắn nhãn loại tương tác cho từng screen, vẽ lại chuỗi màn hình.
  4. Đối chiếu: so với thiết kế thật ở bài tập 2, có component nào bị lệch không?
- 🎨 Visual: Layout `.practice` 3 cột (Token / Component Inventory / Template), mỗi cột 1 icon nhỏ khớp với slide LAYER tương ứng ở Lesson 2, gợi nhắc học viên quay lại đúng phần lý thuyết nào khi làm bài.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Đây là bài tập nặng nhất trong 4 bài, vì học viên tự tay làm lại đúng việc AI sẽ làm nhanh hơn ở Phần B. Mục tiêu không phải làm đẹp tài liệu, mà để học viên cảm nhận rõ giá trị của pattern-first trước khi thấy AI tăng tốc phần này.

---

### PRACTICE - Bài tập 4/4: Dọn dẹp file Figma
- Kicker: Trước khi bước sang Section 3
- Title: Áp dụng checklist dọn dẹp design file vào dự án của bạn
- Nội dung: Kiểm tra component → Gộp variations → Xoá layer ẩn → Chuẩn hoá tên gọi.
- 🎨 Visual: Layout `.practice`, checklist 4 dòng dạng checkbox, có thể lặp lại icon file Figma "trước/sau" từ slide TABLE ở Lesson 4 để nhấn hiệu quả trực quan.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Nhấn đây không phải bài nộp, chỉ là bước tự kiểm tra trước khi qua Section 3. Kết quả tối thiểu: 1 file Figma đã dọn dẹp, sẵn sàng để AI đọc.

---

### END - Kết thúc Phần A (chuyển sang Phần B)
- Kicker: Một điều mang theo
- Title: "Định nghĩa component. Map cách chúng nối nhau. *Rồi mới build.*"
- Lead: Đó là toàn bộ tư duy pattern-first. Phần B sẽ biến prototype pattern này thành một document thật, bằng AI.
- Sign: Winnie Nguyen
- 🎨 Visual: Nền sáng trơn, title xếp dòng lớn, dòng cuối tô màu accent tím, giống slide END của deck gốc.
- Loại visual: ☐ Diagram ☐ Illustration ☐ Real image (chưa quyết định)
- Ghi chú thuyết trình: Chốt phần bằng câu tổng kết 3 bước, định nghĩa, map, rồi mới build. Có thể preview nhanh Phần B sẽ biến toàn bộ lý thuyết vừa học thành thao tác thật với AI, để tạo động lực cho học viên tiếp tục.

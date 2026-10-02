# Slide Outline: Section 4 - Xây Dựng AI Prototype bằng Figma Make

> **Nguồn nội dung:** `section 4-lesson.md`  
> **Mục đích:** Outline cho slide đi kèm 4 lesson của Section 4. Đây là track tool thứ hai, song song với track Claude Design.
>
> Section này không dạy lại prototype pattern. Học viên đã có mindset và framework từ các phần trước. Ở đây, mình chỉ tập trung vào cách đưa workflow đó vào Figma Make và làm prototype thật.

---

## Prompt để build

```text
Dùng outline trong file này, build slide deck HTML cho Section 4 - Xây Dựng AI Prototype bằng Figma Make
(khóa Systematic AI Prototyping for Product Designers, bản tiếng Việt).

Theo đúng rule trong _System/rules/SLIDE_DECK_RULES.md.
Copy tokens.css và deck-stage.js vào thư mục Section 4 để deck tự chứa (self-contained).

Kiểm tra dòng "Loại visual" của từng slide trước khi build.
Nếu slide chưa có visual được chọn, dừng lại và hỏi Winnie trước khi build slide đó.

Với slide đã chọn Illustration hoặc Real image, dùng placeholder đơn giản
(khối màu hoặc icon đơn giản). Winnie sẽ update ảnh thật sau.
```

---

# Tổng quan

**15 slide tổng cộng:** 1 cover + 1 roadmap + 4 lesson divider + 8 slide nội dung + 1 end.

| Lesson | Số slide |
|---|---:|
| Cover + Roadmap | 2 |
| L1 Chuẩn bị Make kit & Guidelines.md | 3 |
| L2 Viết prompt build prototype | 3 |
| L3 Tinh chỉnh bằng prompt lặp lại | 3 |
| L4 Chia sẻ prototype từ Figma Make | 3 |
| End | 1 |
| **Tổng** | **15** |

---

# 1. Cover & Roadmap

## COVER

- **Kicker:** Section 4 · Systematic AI Prototyping for Product Designers
- **Title:** Xây Dựng AI Prototype  
  **bằng Figma Make**
- **Subtitle:** Cùng một mindset. Một tool khác. Từ Make kit đến prototype có thể chia sẻ.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Chào mừng đến với track Figma Make.

Nếu bạn vừa học track Claude Design thì phần này sẽ khá nhẹ. Mình không học lại cách nghĩ về prototype từ đầu. Mình chỉ lấy workflow đã có và xem nó chạy thế nào trong Figma Make.

Nói đơn giản:

**Pattern không đổi. Tool đổi.**

Nếu bạn đã quen với Claude Design và thấy workflow đó hợp với mình, bạn cũng không bắt buộc phải học track này. Hai track sẽ gặp nhau lại ở phần Practice.

---

## PROCESS - Lộ trình Section 4

- **Kicker:** Track 2 · Figma Make
- **Title:** Set up ít hơn.  
  **Nhưng mindset vẫn vậy.**
- **Nội dung:**

  **01 · Make kit**  
  Gom design system và guidelines để Make có context ngay từ đầu.

  **02 · Build**  
  Dùng cùng khung 5 thành phần để mô tả màn hình cần build.

  **03 · Refine**  
  Build xong chưa phải hết. Review rồi tiếp tục chỉnh bằng prompt.

  **04 · Share**  
  Publish prototype và gửi cho người khác test.

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Phần này đi nhanh hơn track Claude Design vì mình không cần dừng lại giải thích lại prototype pattern.

Bạn đã có framework rồi.

Bây giờ chỉ cần xem:

**Figma Make cần mình chuẩn bị gì, build thế nào và sửa ra sao.**

---

# 2. Lesson 1: Chuẩn Bị Make Kit & Guidelines.md

## SECTION - Lesson 1

- **Title:** Lesson 1  
  **Chuẩn bị Make kit**  
  **& Guidelines.md**
- **Sub:** Để Make biết bạn đang dùng design system nào và nên build theo cách nào.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Trước khi build, mình cần cho Make một chút context.

Không phải bằng một prompt dài kể lại cả design system.

Mình chuẩn bị một Make kit gồm:

**design system thật + guidelines cho AI.**

Làm một lần, sau đó có thể dùng lại cho những project khác.

---

## PROCESS - Tạo Make kit

- **Kicker:** Make kit
- **Title:** Set up một lần.  
  **Lần sau khỏi làm lại.**

- **Nội dung:**

  **01 · Publish library**  
  Publish design system library trước để Make có thể sử dụng các component và style.

  **02 · Create a kit**  
  Trong một file Make mới, vào Settings → Create a kit.

  **03 · Assemble**  
  Chọn library bạn muốn đưa vào kit.

  **04 · Add Guidelines.md**  
  Make tạo Guidelines.md để bạn thêm các rule riêng cho AI.

  **05 · Test rồi publish**  
  Build thử một màn hình nhỏ. Nếu Make đi lệch, chỉnh guidelines rồi publish kit.

  **06 · Reuse**  
  Ở project Make khác, chọn **Select a Make kit** trong prompt để dùng lại.

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Điểm mình muốn bạn nhớ ở đây là:

**Make kit chỉ biết những gì bạn đã publish.**

Nếu component vẫn nằm trong một file nháp và chưa được publish thành library thì Make không thể lấy nó từ đó.

Vì vậy đừng vội mở Make rồi prompt ngay.

Chuẩn bị nguồn trước.

Sau đó khi đã có kit, bạn không cần setup lại từ đầu cho mỗi project.

---

## TABLE - Guidelines.md

- **Kicker:** Một file, những rule quan trọng nhất
- **Title:** Guidelines.md  
  **Nơi Make biết “build theo cách của mình”.**

| Nhóm | Guidelines nên nói gì? |
|---|---|
| **Token** | Màu, typography, spacing, radius và các giá trị dùng chung |
| **Component** | Ưu tiên component có sẵn, tránh tạo component mới khi đã có cái tương tự |
| **Layout** | Responsive, cấu trúc layout rõ ràng, tránh positioning tuyệt đối khi không cần |
| **Interaction** | Những hành vi hoặc micro-interaction quan trọng cần giữ |
| **Code** | Code sạch, dễ đọc, refactor khi cần, tránh file quá lớn |

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Guidelines.md không phải nơi để kể lại toàn bộ product.

Mình không cần viết:

“Screen A đi tới Screen B, sau đó user làm C…”

Flow vẫn sẽ nằm trong prompt build của từng màn hình.

Guidelines chỉ cần trả lời một câu:

**“Nếu build sản phẩm này, có những rule nào AI phải luôn tuân theo?”**

Đó mới là thứ đáng để giữ lại và dùng cho nhiều project.

---

# 3. Lesson 2: Viết Prompt Build Prototype Trên Figma Make

## SECTION - Lesson 2

- **Title:** Lesson 2  
  **Viết prompt build**  
  **prototype**
- **Sub:** Không cần học cú pháp mới. Chỉ cần mô tả màn hình đủ rõ.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là chỗ khá dễ thở.

Khung 5 thành phần mình đã học trước đó vẫn giữ nguyên:

**Goal · Layout · Content · Audience · Flow context**

Không có “Figma Make prompt language” nào đặc biệt cần học.

Bạn chỉ cần nói cho Make biết mình muốn build cái gì, cho ai, nó trông như thế nào và nó nằm ở đâu trong flow.

---

## PROMPT - Ví dụ build một màn hình

- **Kicker:** 5 thành phần vẫn vậy
- **Title:** Đừng prompt dài hơn.  
  **Prompt rõ hơn.**

### Prompt

> Build màn hình **[tên màn hình]**.
>
> **Goal:** User đang cố làm gì?  
> **Layout:** Màn hình được chia thành những phần nào?  
> **Content:** Dùng dữ liệu mẫu thật, không dùng lorem ipsum.  
> **Audience:** Ai sẽ sử dụng màn hình này?  
> **Flow context:** User đến từ [màn hình trước] và sau đó sẽ đi tới [màn hình sau].
>
> Dùng đúng component và token từ Make kit, theo Guidelines.md.
>
> Không tạo component mới nếu đã có component hoặc variant tương tự.

- **Loại visual:** AI chat bot  
  *(Mockup giao diện chat AI đang gửi prompt)*

### Ghi chú thuyết trình

Hãy đọc prompt này như cách bạn đang brief cho một designer khác.

Không cần viết kiểu:

“Please carefully analyze…”

Không cần kể lại tất cả context mà Make kit đã biết.

**Những thứ đã có trong kit thì để kit lo.**

Prompt chỉ tập trung vào màn hình mình đang muốn build.

Một điểm khá tiện ở Figma Make là bạn nhìn thấy preview và code ngay trong cùng một nơi. Không cần mở thêm một file riêng chỉ để kiểm tra prototype đang tạo ra cái gì.

---

## STATEMENT - Kỳ vọng cho lần build đầu

- **Kicker:** First build
- **Title:** Lần build đầu không cần đẹp.  
  **Cần đúng hướng.**

- **Lead:**

  Đừng kỳ vọng prompt đầu tiên sẽ cho ra màn hình hoàn hảo.

  Có thể layout hơi lệch.  
  Có thể spacing chưa đều.  
  Có thể hierarchy chưa đúng ý.

  Chuyện đó bình thường.

  Workflow vẫn là:

  **Build → Review → Fix → Continue**

  Build một màn hình. Review kỹ. Sửa những gì chưa ổn. Rồi mới đi tiếp.

  **Đừng prompt cả main journey trong một lần.**

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Bạn có thể sẽ nhìn prototype ở xa và nghĩ:

“Ừ, cũng được mà.”

Nhưng khi zoom vào thì bắt đầu thấy đủ thứ.

Spacing sai một chút.  
Button hơi to.  
Group chưa hợp lý.  
Hierarchy chưa giống design gốc.

Đừng xem đó là thất bại của AI.

Đó chính là lý do mình không build cả journey trong một prompt.

**AI build nhanh. Designer vẫn phải review.**

---

# 4. Lesson 3: Tinh Chỉnh Bằng Prompt Lặp Lại

## SECTION - Lesson 3

- **Title:** Lesson 3  
  **Tinh chỉnh bằng**  
  **prompt lặp lại**
- **Sub:** Build xong chưa phải hết. Giờ mới là lúc bắt đầu chỉnh.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Figma Make khác với cách bạn làm UI truyền thống ở một điểm khá rõ.

Bạn không nhất thiết phải tự kéo từng pixel để sửa.

Bạn có thể nói cho Make biết:

**“Chỗ này chưa đúng. Sửa lại.”**

Và tiếp tục ngay trong conversation đang có.

---

## STATEMENT - Ví dụ follow-up prompt

- **Kicker:** Follow-up prompt
- **Title:** Đừng bắt đầu lại.  
  **Nói tiếp với Make.**

- **Lead:**

  Một vài ví dụ rất đời thường:

  > “Làm gọn phần hero section lại.”

  > “Thêm một testimonial card, dùng đúng Card component đang có.”

  > “Spacing giữa các item chưa đều. Chỉnh lại theo spacing token.”

  > “Button này đang quá nổi. Đưa hierarchy về giống design system.”

  Không cần viết lại toàn bộ prompt.

  **Review → nói điều cần sửa → xem lại → tiếp tục.**

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Prompt lúc này không cần dài.

Thậm chí càng cụ thể càng tốt.

Nếu mình thấy một vấn đề, nói đúng vấn đề đó.

Đừng bắt Make build lại cả màn hình chỉ vì một spacing đang sai.

Và quan trọng nhất, vẫn dùng 6 câu hỏi review đã học trước đó để biết mình đang sửa cái gì.

---

## STATEMENT - Lỗi lặp lại, sửa một chỗ

- **Kicker:** Pattern-first
- **Title:** Cùng một lỗi ở nhiều màn hình?  
  **Đừng sửa từng màn hình.**

- **Lead:**

  Nếu vấn đề nằm ở **token hoặc component dùng chung**, sửa ở nguồn.

  **Token sai → sửa token.**

  **Component sai → sửa component.**

  **Rule sai → cập nhật Guidelines.md.**

  Sau đó những màn hình dùng chung nguồn đó sẽ được hưởng lợi từ thay đổi.

  Đây là nguyên tắc:

  **Fix once. Benefit everywhere.**

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là lúc mindset pattern-first bắt đầu phát huy tác dụng.

Nếu mình thấy 5 màn hình đều có cùng một lỗi button, mình không muốn ngồi sửa 5 lần.

Mình muốn hỏi:

**“Tại sao nó sai ngay từ đầu?”**

Nếu lỗi nằm ở component hoặc rule, sửa ở đó.

Đó mới là cách để prototype lớn lên mà không biến thành một đống màn hình phải sửa tay.

---

# 5. Lesson 4: Chia Sẻ Prototype Từ Figma Make

## SECTION - Lesson 4

- **Title:** Lesson 4  
  **Chia sẻ prototype**  
  **từ Figma Make**
- **Sub:** Build xong thì gửi link. Không cần thêm một vòng hosting.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là một trong những phần khác biệt khá rõ so với track Claude Design.

Với Claude Design, bạn có thể cần đưa code sang GitHub rồi kết nối hosting.

Với Figma Make, phần publish đã nằm ngay trong tool.

Build xong, publish và lấy link.

---

## PROCESS - Cách publish

- **Kicker:** 3 bước
- **Title:** Publish.  
  **Có ngay một link để gửi.**

- **Nội dung:**

  **01 · Publish**  
  Chọn Publish trên project.

  **02 · Kiểm tra**  
  Xem lại nội dung và quyền truy cập trước khi chia sẻ.

  **03 · Share**  
  Publish để có URL riêng và gửi cho người khác.

  Nếu chỉ cần demo nhanh, có thể dùng **Present** để tạo link xem trước.

  Present phù hợp cho việc demo hoặc review nội bộ. Publish phù hợp hơn khi bạn cần một prototype có thể chia sẻ lâu dài.

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Điểm mình thích ở đây là workflow khá gọn.

Không cần nghĩ:

“Code này deploy ở đâu?”

“Hosting setup thế nào?”

Nếu mục tiêu chỉ là:

**“Mình muốn gửi prototype này cho stakeholder xem.”**

thì Figma Make đã có sẵn bước đó.

Nhưng trước khi gửi, nhớ kiểm tra quyền truy cập. Đừng build cả buổi rồi gửi cho stakeholder một link mà họ không mở được.

---

## PRACTICE - Trước khi gửi prototype

- **Kicker:** Before you share
- **Title:** Trước khi gửi, check 2 thứ.

- **Nội dung:**

  **01 · Link có mở được không?**  
  Thử bằng chế độ ẩn danh hoặc một thiết bị khác. Đừng chỉ test trên máy của mình.

  **02 · Người nhận có biết mình đang xem gì không?**  
  Gửi kèm một câu ngắn:

  **User goal + prototype có những màn hình nào.**

  Ví dụ:

  > “Prototype này mô phỏng flow refinance từ lúc user bắt đầu application đến lúc review loan offer.”

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là một bước nhỏ nhưng mình rất hay thấy bị bỏ qua.

Gửi một link trống không bao giờ tốt bằng việc cho người nhận biết:

**“Bạn đang xem cái gì và nên chú ý vào đâu?”**

Và trước khi gửi, luôn mở thử bằng một môi trường khác.

Prototype chạy tốt trên máy mình chưa có nghĩa là người khác mở cũng được.

---

# 6. Kết thúc

## END - Kết thúc Section 4

- **Kicker:** Takeaway
- **Title:** Tool đổi.  
  **Prototype pattern không đổi.**
- **Lead:**

  Dù bạn chọn **Claude Design** hay **Figma Make**, cách mình tiếp cận prototype vẫn giống nhau:

  **Có system trước.**  
  **Build theo pattern.**  
  **Review từng màn hình.**  
  **Sửa ở đúng chỗ.**  
  **Rồi mới mở rộng.**

  Tool chỉ thay đổi cách mình thực hiện workflow.

  Ở phần Practice tiếp theo, hai track sẽ gặp lại nhau.

  Mình sẽ tiếp tục build journey, mở rộng design system và nhìn lại cách mình làm việc với AI khi prototype bắt đầu lớn lên.

- **Sign:** Winnie Nguyen
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Nếu chỉ nhớ một câu sau section này, hãy nhớ câu này:

**Tool đổi. Prototype pattern không đổi.**

Mình không muốn bạn trở thành người chỉ biết dùng Figma Make hay Claude Design.

Mục tiêu là bạn hiểu workflow đủ rõ để có thể đổi tool mà vẫn build được.

Và từ đây, hai track sẽ quay lại cùng một Practice.

Lúc đó mình sẽ không còn nói nhiều về tool nữa.

Mình sẽ tập trung vào prototype.

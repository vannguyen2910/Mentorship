# Slide Outline: Section 5 - Xây Dựng AI Prototype bằng Claude Code

> **Nguồn nội dung:** `section 5-lesson.md`
> **Mục đích:** Outline cho slide đi kèm 4 lesson của Section 5. Section này đưa design system và prototype pattern đã có qua một AI coding tool thật, để có 1 link thật, tự cập nhật, độc lập với bất kỳ tool AI nào.
>
> Section này không dạy lại prototype pattern hay khung 5 thành phần. Học viên đã có mindset đó từ các phần trước. Ở đây, mình tập trung vào 3 việc mới: nối AI coding tool với Figma qua MCP, đưa design system vào code thật, và publish bằng GitHub.
>
> **Visual (2026-08-21):** 5 slide mô tả đúng 1 bước thao tác thật (MCP, setup MCP, rules file, prompt, GitHub) đã chọn sẵn Real image, Winnie tự chụp màn hình từ tài khoản của mình, chưa có ảnh thật thì dùng placeholder đơn giản khi build. Slide Publish dùng Diagram (Code → GitHub → Vercel/Netlify → URL), đã có nội dung cụ thể, không cần chọn thêm. Các slide còn lại là slide khái niệm (so sánh, mindset, roadmap, checklist), chưa chọn Loại visual, cần Winnie xác nhận Diagram hay Illustration trước khi build.

---

## Prompt để build

```text
Dùng outline trong file này, build slide deck HTML cho Section 5, Xây Dựng AI Prototype bằng Claude Code.
Đây là section trong khóa Systematic AI Prototyping for Product Designers.

Theo đúng rule trong _system/rules/SLIDE_DECK_RULES.md.
Dùng đúng design system và design template mình đã set up từ trước (tokens.css, các layout class trong rule file). Không tự tạo style, màu, hay layout mới.
Copy tokens.css và deck-stage.js vào thư mục Section 5 để deck tự chứa (self-contained).

Giữ nguyên thứ tự slide trong outline.

Kiểm tra dòng "Loại visual" của từng slide trước khi build.
Nếu slide chưa có visual được chọn, dừng lại và hỏi Winnie trước khi build slide đó.

Với slide đã chọn Illustration hoặc Real image, dùng placeholder đơn giản.
Winnie sẽ update ảnh thật sau.
```

---

# Tổng quan

**18 slide tổng cộng:** 1 cover + 1 roadmap + 4 lesson divider + 11 slide nội dung + 1 end.

| Lesson | Số slide |
|---|---:|
| Cover + Roadmap | 2 |
| L1 Vì Sao & Khi Nào Cần Bước Này | 3 |
| L2 Đưa Design System Vào | 4 |
| L3 Build & Refine Bằng Prompt | 4 |
| L4 GitHub & Publish | 4 |
| End | 1 |
| **Tổng** | **18** |

---

# 1. Cover & Roadmap

## COVER

- **Kicker:** Section 5 · Systematic AI Prototyping for Product Designers
- **Title:** Xây Dựng AI Prototype
  **bằng Claude Code**
- **Subtitle:** Từ Figma đến code thật, rồi đưa nó lên web.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Tới đây mình đã có prototype chạy được trong Claude Design hoặc Figma Make.

Nhưng có những lúc mình muốn đi thêm một bước. Ví dụ muốn gửi cho developer tiếp tục làm, muốn mở prototype trên điện thoại thật, hoặc đơn giản là muốn giữ nó thành một link riêng thay vì để nó nằm trong một tool.

**Lúc đó mình đưa nó sang Claude Code.**

Và đây là phần mình sẽ làm.

---

## PROCESS - Lộ trình Section 5

- **Kicker:** 4 bước
- **Title:** Từ prototype
  **đến một link có thể share**
- **Nội dung:**

  **01 · Khi nào cần code thật**
  Trước hết xem bước này có thật sự cần thiết không.

  **02 · Cho Claude đọc Design System**
  Kết nối Figma và setup những rule cần thiết.

  **03 · Build & chỉnh**
  Dùng lại framework 5 thành phần, nhưng lần này output là code.

  **04 · GitHub & Publish**
  Đưa code lên GitHub và có một link để share.

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Nếu bạn đã đi qua track Claude Design và Figma Make thì workflow này không có gì quá lạ.

Mình vẫn chuẩn bị system trước. Vẫn build từng màn hình. Vẫn review. Vẫn sửa.

**Chỉ có output khác đi thôi.** Lần này mình đang làm việc với code thật.

---

# 2. Lesson 1: Vì Sao & Khi Nào Cần Bước Này

## SECTION - Lesson 1

- **Title:** Lesson 1
  **Vì sao & khi nào**
  **cần bước này**
- **Sub:** Prototype chạy được và prototype có thể sống lâu hơn không phải lúc nào cũng là một.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Câu này đáng hỏi trước khi mình đụng vào MCP hay GitHub.

Nếu bạn chỉ cần demo một flow cho stakeholder ngày mai, thật ra không cần Claude Code. Figma Make hoặc Claude Design làm việc đó đủ tốt rồi.

Mình chỉ đi thêm bước này khi prototype cần sống lâu hơn một buổi review. Ví dụ developer cần lấy code tiếp tục, mình cần test trên thiết bị thật, hoặc mình muốn có một link riêng để gửi đi.

**Và đây cũng là lựa chọn khó hơn 2 track kia.** Đòi hỏi thêm kỹ năng, không chỉ thao tác trong 1 tool thiết kế.

---

## STATEMENT - Chạy được vs. chạy thật

- **Kicker:** Chạy được ≠ chạy thật
- **Title:** Chạy được chưa chắc cần code thật

- **Lead:**

  Prototype trong Claude Design hay Figma Make đã chạy được rồi. Vậy tại sao phải làm thêm?

  Vì đôi khi cái mình cần không còn là một prototype trong tool nữa. Mình cần code nằm trong repo, có thể mở ở nơi khác và tiếp tục sửa.

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây không phải câu chuyện "code thật tốt hơn prototype". Không phải.

Hai cái phục vụ hai nhu cầu khác nhau. Nếu prototype đã làm đúng việc của nó thì dừng ở đó. Đừng thêm technical work chỉ để thấy mình đang làm thứ gì đó "xịn" hơn.

**Đây cũng là bước khó hơn, đòi hỏi nhiều kỹ năng hơn 2 track trước.** Bạn cần thêm một số kỹ năng: đọc hiểu code ở mức cơ bản, làm quen với MCP, và biết cách publish qua GitHub. Không còn là chỉ thao tác trong 1 tool thiết kế nữa.

**Cân nhắc kỹ trước khi chọn đi tiếp.** Đây là lựa chọn đòi hỏi nhiều kỹ năng hơn, không phải bước "nâng cấp" mặc định ai cũng nên làm.

---

## STATEMENT - MCP, một khái niệm mới

- **Kicker:** Khái niệm mới
- **Title:** MCP nghe rất technical.
  **Thực ra bạn chỉ cần hiểu một việc.**

- **Lead:**

  Claude Code không tự đọc được file Figma của mình. MCP giúp nó đọc được. Vậy thôi.

  Sau khi setup, Claude Code có thể lấy thông tin từ Figma thay vì mình phải ngồi mô tả lại component, token hay layout bằng text.

- **Loại visual:** ☐ Diagram ☐ Illustration ☑ Real image
  *(Winnie tự chụp: màn hình xác nhận MCP đã kết nối, ví dụ trạng thái "connected" trong Claude Code hoặc Cursor. Placeholder khi build.)*

### Ghi chú thuyết trình

Đây là khái niệm mới nhất trong phần này. Nên nếu bạn thấy chữ MCP hơi đáng sợ thì cũng không sao.

Đừng cố học thuộc định nghĩa. Trong khóa này, bạn chỉ cần biết nó dùng để làm gì và setup nó thế nào.

---

# 3. Lesson 2: Đưa Design System Vào

## SECTION - Lesson 2

- **Title:** Lesson 2
  **Đưa design system**
  **vào code**
- **Sub:** Trước khi build, cho Claude biết mình đang dùng system nào.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Cái này mình đã làm quen rồi, ở track Claude Design. Khác ở chỗ Claude Design có cách riêng để đọc Design System.

Còn Claude Code thì mình phải nối nó với nguồn mình đang có. Nếu team đã có codebase rồi thì trỏ vào repo. Nếu mọi thứ vẫn nằm trong Figma thì dùng MCP.

---

## TABLE - 2 nhánh bắt đầu

- **Kicker:** Chọn đúng nhánh
- **Title:** Bạn đang có gì?

| Nếu team đã có code | Nếu mọi thứ vẫn ở Figma |
|---|---|
| Trỏ Claude vào repo | Kết nối Figma qua MCP |
| Đọc component / token có sẵn | Đọc component / token từ Figma |
| Không cần dựng lại | Không cần copy design system bằng tay |

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Mình tách hai trường hợp này ra vì rất dễ bị hiểu nhầm.

Nếu dev team đã có design system dưới dạng code thì đừng dựng lại nó chỉ vì đang học AI. Dùng cái đang có.

Còn nếu bạn là designer và design system vẫn nằm trong Figma thì MCP là thứ mình cần.

---

## PROCESS - Setup MCP (Nhánh B)

- **Kicker:** Setup một lần
- **Title:** Bắc cầu 1 lần.
  **Dùng lại cho mọi lần build sau.**

- **Nội dung:**

  **01 · Cài MCP**
  Cài MCP cho Claude Code hoặc bật Figma Dev Mode MCP Server nếu dùng Cursor.

  **02 · Cho phép truy cập**
  Xác nhận quyền để AI coding tool có thể đọc Figma.

  **03 · Kiểm tra connection**
  Đảm bảo trạng thái hiển thị là connected trước khi build.

  **04 · Chọn file Figma**
  Cho AI biết file Figma nào là nguồn chính.

  **05 · Test**
  Yêu cầu AI đọc thử một component hoặc token.

- **Loại visual:** ☐ Diagram ☐ Illustration ☑ Real image
  *(Winnie tự chụp: các bước cài MCP thật, cài plugin hoặc bật Dev Mode MCP Server, màn hình xác thực, trạng thái kết nối. Placeholder khi build.)*

### Ghi chú thuyết trình

Chỗ này mình sẽ demo trực tiếp nên slide không cần giải thích quá nhiều.

Mình chỉ muốn bạn nhớ một việc: **đừng setup xong rồi tin là nó đã chạy. Test nó.**

Bảo Claude đọc thử một component. Nếu nó đọc đúng thì mình mới đi tiếp.

---

## STATEMENT - Rules file, dù đi nhánh nào

- **Kicker:** Rules file
- **Title:** Figma có Design System rồi.
  **Nhưng Claude vẫn cần biết một vài rule.**

- **Lead:**

  Trước khi build, tạo một rules file cho project. File này có thể giữ:

  **Design System:** dùng system nào.
  **Component:** ưu tiên reuse component có sẵn.
  **Code:** cấu trúc code và cách đặt tên.
  **Pattern:** những pattern cần giữ nhất quán.
  **Rules:** những điều AI phải luôn tuân theo.

- **Loại visual:** ☐ Diagram ☐ Illustration ☑ Real image
  *(Winnie tự chụp: rules file mở trong editor, thấy rõ các category Design System/Component/Code/Pattern/Rules. Placeholder khi build.)*

### Ghi chú thuyết trình

Rules file là nơi mình giữ những thứ không muốn phải nhắc lại trong từng prompt.

Ví dụ: "Luôn dùng existing component trước." Nếu mình phải nhắc điều này lần thứ ba: đưa nó vào rules file.

**AI sẽ đọc nó mỗi lần làm việc với project.**

---

# 4. Lesson 3: Build & Refine Bằng Prompt

## SECTION - Lesson 3

- **Title:** Lesson 3
  **Build & refine**
  **bằng prompt**
- **Sub:** Code thật, nhưng cách mình làm vẫn quen thuộc.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là chỗ mình nghĩ bạn sẽ thấy workflow này quen nhất.

Mình không tạo thêm một framework prompt mới. Vẫn Goal. Layout. Content. Audience. Flow context.

Chỉ khác là thay vì bảo AI dựng một prototype trong tool, mình đang bảo nó viết code cho mình.

---

## PROMPT - Ví dụ build một màn hình

- **Kicker:** 5 thành phần vẫn vậy
- **Title:** Prompt vẫn vậy.
  **Chỉ đổi nơi nó chạy.**

### Prompt

> Build màn hình Explore Feed.
>
> **Goal:** User đang khám phá các địa điểm được gợi ý.
> **Layout:** Header, mode switcher, search, filter, feed và bottom navigation.
> **Content:** Dùng sample content thật, không dùng lorem ipsum.
> **Audience:** Guest user chưa đăng ký.
> **Flow context:** User đến từ Onboarding và có thể đi tới Tip Detail.
>
> Dùng component và token từ Figma.
> Reuse component có sẵn trước khi tạo mới.
> Tuân theo CLAUDE.md.

- **Loại visual:** ☐ Diagram ☐ Illustration ☑ Real image
  *(Winnie tự chụp: prompt thật đang gõ trong Claude Code hoặc Cursor, kèm kết quả build ngay bên cạnh. Placeholder khi build.)*

### Ghi chú thuyết trình

Đây là một prompt mình muốn bạn có thể nhìn vào và hiểu ngay. Không có magic ở đây.

Mình chỉ đang brief cho AI giống như brief cho một designer hoặc developer khác. User là ai. Màn hình cần làm gì. Có những gì. Nó nằm ở đâu trong flow. Và dùng system nào.

---

## STATEMENT - Đừng mong giống Figma 100% ngay lần đầu

- **Kicker:** First pass
- **Title:** Đừng mong lần đầu đã giống Figma 100%.

- **Lead:**

  Có thể spacing lệch. Có thể typography chưa đúng. Có thể một component bị tạo mới dù đã có component tương tự. Có thể interaction còn thiếu.

  Không sao. Việc đầu tiên mình cần biết là: **"Nó đang đi đúng hướng chưa?"**

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Nếu đúng hướng thì sửa tiếp. Nếu sai hướng thì quay lại prompt hoặc context.

Đừng ngồi soi từng pixel ngay từ giây đầu tiên. Nhưng cũng đừng thấy nó "trông khá ổn" rồi bấm build tiếp cả 10 màn hình.

---

## STATEMENT - Lỗi lặp lại? Đừng sửa từng màn hình

- **Kicker:** Fix once
- **Title:** Một lỗi lặp lại nhiều lần?
  **Đừng sửa từng màn hình.**

- **Lead:**

  Component sai? Sửa component. Token sai? Sửa token. Rule sai? Sửa CLAUDE.md. Một màn hình sai? Sửa màn hình đó.

  Trước khi sửa, hỏi một câu: **"Lỗi này bắt đầu từ đâu?"**

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là một trong những thói quen mình muốn bạn mang theo sau khóa học.

AI làm việc rất nhanh nên bạn sẽ gặp rất nhiều lỗi nhỏ. Nếu lỗi nào cũng giải quyết bằng cách prompt lại màn hình hiện tại thì prototype càng lớn càng khó kiểm soát.

**Tìm đúng nguồn sẽ nhẹ hơn rất nhiều.**

---

# 5. Lesson 4: GitHub & Publish

## SECTION - Lesson 4

- **Title:** Lesson 4
  **GitHub**
  **& publish**
- **Sub:** Code xong rồi. Giờ cho nó một chỗ để sống.
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là phần cuối. Và cũng là lúc mình biến cái prototype vừa build thành một thứ có thể gửi cho người khác.

Không cần biến mình thành developer. Mình chỉ cần hiểu workflow cơ bản:

**Code → GitHub → Hosting → Link**

---

## STATEMENT - GitHub là gì

- **Kicker:** GitHub 101
- **Title:** GitHub

- **Lead:**

  Code đang nằm trên máy bạn. GitHub giúp giữ nó ở một chỗ có thể tiếp tục làm việc.

  Claude Code có thể giúp mình: tạo Git repository, commit, tạo GitHub repository, push code.

  Sau đó hosting có thể lấy code từ GitHub để build website.

- **Loại visual:** ☐ Diagram ☐ Illustration ☑ Real image
  *(Winnie tự chụp: trang GitHub repo thật của prototype, hoặc màn hình tạo repo mới. Placeholder khi build.)*

### Ghi chú thuyết trình

Nếu bạn chưa dùng GitHub bao giờ thì đừng lo. Trong khóa này mình không học Git.

Mình chỉ cần hiểu nó nằm ở đâu trong workflow. **Claude Code có thể làm phần command cho mình.**

---

## PROCESS - Publish

- **Kicker:** Auto-deploy
- **Title:** Publish

- **Nội dung:**

  Code
  ↓
  GitHub
  ↓
  Vercel / Netlify
  ↓
  URL

- **Loại visual:** ☑ Diagram

### Ghi chú thuyết trình

Sau khi nối GitHub với hosting, phần còn lại khá đơn giản.

Mỗi lần code được push lên GitHub, hosting sẽ build lại. Bạn vẫn dùng một link đó.

**Code thay đổi thì website thay đổi theo.**

---

## PRACTICE - Trước khi gửi

- **Kicker:** Before you share
- **Title:** Có link không có nghĩa là gửi ngay.

- **Nội dung:**

  **01 · Check data**
  Không có: API key, password, secret, data thật, thông tin nhạy cảm.

  **02 · Check link**
  Mở thử bằng: incognito, thiết bị khác, account khác nếu cần.

  **03 · Check context**
  Cho người nhận biết prototype này dùng để làm gì.

  Và nhớ: **prototype chạy trên web vẫn là prototype.**

- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Chỗ này mình muốn bạn cẩn thận một chút. Có URL nhìn rất "real" nhưng không có nghĩa là production-ready.

Đừng đưa data thật vào. Đừng commit API key. Và đừng gửi link trước khi tự mở thử bằng incognito.

---

# 6. Kết thúc

## END - Kết thúc Section 5

- **Kicker:** Takeaway
- **Title:** Bạn không cần giỏi code để build prototype bằng code.

- **Lead:**

  Nhưng bạn cần biết mình đang yêu cầu AI làm gì.

  Design System vẫn phải rõ. Context vẫn phải đủ. Review vẫn là việc của bạn.

  Và khi prototype lớn lên, bạn vẫn phải biết sửa ở đâu thay vì cứ prompt lại cả màn hình.

- **Sign:** Winnie Nguyen
- **Loại visual:** ☐ Diagram ☐ Illustration ☐ Real image

### Ghi chú thuyết trình

Nếu nhìn lại từ track Claude Design đến đây, thật ra mình không thay đổi cách làm nhiều.

Mình vẫn bắt đầu từ system. Vẫn build từng bước. Vẫn review. Vẫn sửa.

Chỉ là bây giờ mình có thêm một lựa chọn: đưa prototype thành code thật khi mình thực sự cần nó.

**Và đó mới là điều mình muốn bạn mang theo sau khóa học.**

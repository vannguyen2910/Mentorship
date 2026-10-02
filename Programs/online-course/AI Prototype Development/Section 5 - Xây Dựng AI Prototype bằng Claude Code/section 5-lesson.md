---
title: "Section 5: Xây Dựng AI Prototype bằng Claude Code"
subtitle: "Từ prototype thị giác sang code thật, có link thật, tự cập nhật mỗi lần bạn sửa"
course: Systematic AI Prototyping for Product Designers
section: 5
source-lesson: Library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-08-21
language: vi
---

## Tổng Quan Section

> **Section mới (2026-08-19):** Section này dùng Claude Code làm ví dụ chính xuyên suốt, giống cách track Claude Design đã làm trước đó. Cursor hoạt động theo đúng logic tương tự (MCP, rules file, prompt để build và publish), chỉ khác tên gọi ở vài chỗ, sẽ được ghi chú riêng khi cần. Đây là ngoại lệ có chủ đích với quy tắc gọi tên tool chung chung của khoá học.

Tới đây, bạn đã có ít nhất 1 prototype chạy được, dựng bằng Claude Design hoặc Figma Make. Nó đủ tốt để demo, đủ tốt để test flow. Nhưng nó vẫn sống trong đúng 1 tool: đóng tài khoản, hết hạn dùng thử, hay tool ngừng hỗ trợ, prototype cũng biến mất theo.

Section này đưa design system và prototype pattern đã có qua một bước khác: build bằng 1 AI coding tool thật, ra code thật, rồi publish thành 1 link thật, độc lập với bất kỳ tool AI nào, ai cũng mở được, tự cập nhật mỗi lần bạn sửa.

Đây cũng là lựa chọn khó hơn, và đòi hỏi nhiều kỹ năng hơn, so với việc dừng lại ở Claude Design hay Figma Make. Bạn cần thêm một số kỹ năng: đọc hiểu code ở mức cơ bản, làm quen với MCP, và biết cách publish qua GitHub. Cân nhắc kỹ trước khi chọn đi tiếp.

**Kết thúc section này, bạn sẽ có thể:**
1. Nhận biết khi nào bước build bằng code thật đáng làm, và khi nào prototype trong Claude Design hay Figma Make đã đủ
2. Nối AI coding tool với Figma qua MCP, đọc đúng token và component đang có
3. Đưa design system vào codebase, dù bạn bắt đầu từ 1 repo có sẵn hay từ đúng file Figma
4. Build và refine main journey bằng prompt, ngay trong code thật
5. Publish prototype lên GitHub và có 1 link thật, tự cập nhật mỗi lần sửa code

**Nội dung section:**
- 4 lesson
- Cần có: design system đã chuẩn bị từ trước (token, component, template), 1 AI coding tool (Claude Code hoặc Cursor), 1 tài khoản GitHub

---

## Nội Dung Lesson

### Lesson 1: Vì Sao & Khi Nào Cần Bước Này
*Prototype chạy được và prototype có thể sống lâu hơn không phải lúc nào cũng là một.*

Claude Design và Figma Make tạo prototype chạy được ngay trong trình duyệt, đủ để demo, đủ để test flow. Nhưng cả 2 đều sống trong đúng 1 tool: prototype nằm trên server của tool đó, không phải 1 thứ bạn cầm trong tay và mang đi đâu cũng được.

Build bằng AI coding tool khác ở chỗ: kết quả là code thật, nằm trong 1 repo, chạy được ở bất kỳ đâu hỗ trợ web, không phụ thuộc 1 tài khoản hay 1 tool duy nhất còn sống hay không.

**Bước này đáng làm khi:**
- Bạn cần gửi prototype cho dev, để họ tiếp tục code thật từ đó, không phải build lại từ đầu
- Bạn cần test trên thiết bị thật, ngoài môi trường preview có sẵn trong tool
- Bạn muốn giữ 1 link portfolio sống lâu dài, không phụ thuộc tài khoản của tool AI đang dùng

**Không cần thiết khi:** bạn chỉ demo nội bộ nhanh, hoặc prototype đã hoàn thành đúng mục đích của nó rồi. Cách publish có sẵn trong tool bạn đang dùng vẫn đủ cho phần lớn trường hợp.

**Đây cũng là lựa chọn khó hơn, và đòi hỏi nhiều kỹ năng hơn 2 track trước.** Claude Design hay Figma Make vẫn là thao tác trong 1 tool thiết kế. Đi tiếp sang code thật, bạn cần thêm một số kỹ năng: đọc hiểu code ở mức cơ bản, làm quen với MCP, và biết cách publish qua GitHub. Cân nhắc kỹ trước khi chọn đi tiếp, đây không phải bước "nâng cấp" mặc định ai cũng nên làm.

**Một khái niệm mới ở đây: MCP.** Claude Design và Figma Make tự đọc được file Figma, vì cơ chế đó được xây sẵn bên trong tool. AI coding tool như Claude Code hay Cursor không có sẵn cơ chế đó, vì bản thân nó không phải tool thiết kế. MCP, viết tắt của Model Context Protocol, là cầu nối bạn tự bắc, để AI coding tool đọc được token, component, và layout từ đúng file Figma của bạn, thay vì bạn phải gõ lại toàn bộ design system thành lời mỗi lần.

**Một điều cần nói rõ trước khi bắt đầu:** kết quả ở section này vẫn là 1 prototype, không phải sản phẩm production. Có link chạy thật không có nghĩa là sẵn sàng cho user thật dùng. Bảo mật, xử lý lỗi, hay khả năng chịu tải chưa nằm trong phạm vi của bước này.

**Kết quả tối thiểu:** xác định được lý do bạn cần bước này, và AI coding tool bạn sẽ dùng, Claude Code hoặc Cursor.

---

### Lesson 2: Đưa Design System Vào: Chọn Đúng Nhánh
*Có sẵn code trên GitHub hay chỉ có Figma, quyết định bạn bắt đầu từ đâu.*

Trước khi build màn hình nào, AI coding tool cần biết token, component, và rule của bạn, giống cách track Claude Design cần 1 Design System file trước khi build. Cách đưa design system vào tuỳ thuộc bạn đang có gì sẵn.

**Nhánh A · Đã có design system dạng code trên GitHub**

Nếu team bạn đã có sẵn 1 component library hay token repo, do dev build từ trước, việc của bạn đơn giản hơn: trỏ AI coding tool vào đúng repo đó, để nó đọc convention đang có. Không cần dựng lại từ đầu, không cần MCP.

**Nhánh B · Chỉ có Figma, chưa có code**

Đây là trường hợp phổ biến hơn với Product Designer: design system chỉ tồn tại trong Figma, chưa từng thành code. Lúc này bạn cần MCP, làm 1 lần duy nhất:

1. Nối AI coding tool với Figma qua MCP. Với Claude Code, cài qua plugin có sẵn rồi xác thực quyền truy cập. Với Cursor, bật Dev Mode MCP Server ngay trong Figma desktop app, rồi thêm vào danh sách MCP tool của Cursor.
2. Xác nhận kết nối thành công, thường có dấu hiệu rõ như trạng thái "connected" hoặc số lượng tool hiển thị đúng.
3. Từ đây, AI coding tool đọc được component, variable (token), và layout trực tiếp từ file Figma bạn chỉ định, không cần bạn mô tả lại bằng lời.

**Dù đi nhánh nào, kết thúc bằng 1 rules file cho project.** File này có thể giữ: Design System (dùng system nào), Component (ưu tiên reuse component có sẵn), Code (cấu trúc code và cách đặt tên), Pattern (những pattern cần giữ nhất quán), và Rules (những điều AI phải luôn tuân theo). Nếu có một rule bạn phải nhắc lại nhiều lần khi prompt, đưa nó vào rules file, để AI đọc lại mỗi lần làm việc với project, không phải đoán lại từ đầu mỗi lần.

**Kết quả tối thiểu:** AI coding tool đã đọc được đúng design system của bạn, qua repo có sẵn hoặc qua MCP, và có 1 rules file phản ánh đúng token, component, và rule cần giữ.

---

### Lesson 3: Build & Refine Prototype Bằng Prompt
*Code thật, nhưng cách mình làm vẫn quen thuộc.*

Khung 5 thành phần đã học trước đó áp dụng y hệt ở đây: Goal, Layout, Content, Audience, Flow context. AI coding tool không cần 1 cú pháp prompt khác, nó cần cùng lượng thông tin cụ thể để không phải đoán.

**Prompt build 1 màn hình, ví dụ:**

> "Build màn hình Explore Feed. Goal: User đang khám phá các địa điểm được gợi ý. Layout: Header, mode switcher, search, filter, feed và bottom navigation. Content: Dùng sample content thật, không dùng lorem ipsum. Audience: Guest user chưa đăng ký. Flow context: User đến từ Onboarding và có thể đi tới Tip Detail. Dùng component và token từ Figma, reuse component có sẵn trước khi tạo mới. Tuân theo CLAUDE.md."

Không có gì magic ở đây. Đây là brief cho AI giống như brief cho một designer hoặc developer khác: user là ai, màn hình cần làm gì, có những gì, nằm ở đâu trong flow, và dùng system nào.

**Khác biệt khi build:** AI coding tool sửa trực tiếp trong file code, không có canvas riêng để xem trước như bạn đã quen. Cách review: chạy thử ngay trên máy, thường chỉ cần 1 lệnh khởi động mà AI coding tool có thể tự chạy giúp nếu bạn yêu cầu, mở trình duyệt, rồi so với file Figma gốc.

**Đừng mong lần đầu đã giống Figma 100%.** Có thể spacing lệch, typography chưa đúng, một component bị tạo mới dù đã có component tương tự, hoặc interaction còn thiếu. Không sao. Việc đầu tiên cần biết là nó đang đi đúng hướng chưa. Nếu đúng hướng thì sửa tiếp, nếu sai hướng thì quay lại prompt hoặc context. Đừng ngồi soi từng pixel ngay từ giây đầu, nhưng cũng đừng thấy nó "trông khá ổn" rồi bấm build tiếp cả 10 màn hình.

**Một lỗi lặp lại nhiều lần thì đừng sửa từng màn hình.** Component sai thì sửa component. Token sai thì sửa token. Rule sai thì sửa CLAUDE.md. Chỉ khi đúng 1 màn hình sai thì mới sửa riêng màn hình đó. Trước khi sửa, hỏi một câu: lỗi này bắt đầu từ đâu. Tìm đúng nguồn sẽ nhẹ hơn rất nhiều so với prompt lại từng màn hình mỗi lần gặp lỗi.

**Kết quả tối thiểu:** main journey 2-4 màn hình, chạy được trên máy bạn, dùng đúng component và token từ rules file.

---

### Lesson 4: GitHub Là Gì & Publish Bằng Prompt
*Code xong rồi. Giờ cho nó một chỗ để sống.*

Không cần biến mình thành developer. Workflow cơ bản chỉ có vậy: code, GitHub, hosting, link.

**GitHub là gì:** code đang nằm trên máy bạn. GitHub giúp giữ nó ở một chỗ có thể tiếp tục làm việc. Claude Code có thể giúp bạn làm hết phần command: tạo Git repository, commit, tạo GitHub repository, push code. Sau đó hosting lấy code từ GitHub để build website. Nếu bạn chưa dùng GitHub bao giờ thì đừng lo, khoá này không học Git, chỉ cần hiểu nó nằm ở đâu trong workflow.

**Publish:** sau khi nối GitHub với 1 dịch vụ hosting như Vercel hoặc Netlify, phần còn lại khá đơn giản. Mỗi lần code được push lên GitHub, hosting sẽ build lại, bạn vẫn dùng một link đó. Code thay đổi thì website thay đổi theo.

**Trước khi đẩy code lên GitHub, luôn kiểm tra 1 điều:** không có API key, password, secret, hay dữ liệu thật nào bị viết cứng trong code. GitHub repo mặc định có thể công khai, và đây vẫn là prototype để demo, không phải nơi lưu thông tin thật.

**Trước khi gửi link, check thêm 2 việc:**
- Mở thử bằng incognito, thiết bị khác, hoặc account khác nếu cần
- Cho người nhận biết prototype này dùng để làm gì

Có URL nhìn rất "real" không có nghĩa là production-ready. Prototype chạy trên web vẫn là prototype.

**Kết quả tối thiểu:** code đã đẩy lên GitHub, nối với 1 dịch vụ hosting, có 1 link thật đã xác nhận mở được, sẵn sàng gửi cho stakeholder hoặc dev.

---

## Nguồn Tham Khảo

- Figma Help Center — [Claude Code and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server)
- Figma Developers — [Set up the remote server (recommended)](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- Figma Developers — [Code Connect integration with the Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/code-connect-integration)
- Builder.io — [Cursor + Figma MCP Server](https://www.builder.io/blog/cursor-figma-mcp-server)
- Claude Code Docs — [How Claude remembers your project](https://code.claude.com/docs/en/memory)
- Design Systems Collective — [From Prompt to Production: A Designer's Step-by-Step Workflow](https://www.designsystemscollective.com/from-prompt-to-production-a-designers-step-by-step-workflow-with-claude-design-claude-code-a7705daad026)
- MindStudio — [How to Deploy a Claude Code Project to GitHub and Vercel](https://www.mindstudio.ai/blog/deploy-claude-code-project-github-vercel)
- Vercel — [4 ways to put a website on Vercel without Git or a CLI](https://vercel.com/i/deploy-to-vercel-without-git)

---

*Khóa học: Systematic AI Prototyping for Product Designers · Section 5 — Xây Dựng AI Prototype bằng Claude Code*
*Thực hiện bởi Winnie Nguyen · Cập nhật lần cuối tháng 8/2026*

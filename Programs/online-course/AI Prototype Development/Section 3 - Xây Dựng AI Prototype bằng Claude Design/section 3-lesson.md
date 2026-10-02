---
title: "Section 3: Xây Dựng AI Prototype bằng Claude Design"
subtitle: "Từ file Figma đến Design System sống trong Claude Design, main journey chạy được trong trình duyệt, và chia sẻ nó ra ngoài"
course: Systematic AI Prototyping for Product Designers
section: 3
source-lesson: Library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-08-18
language: vi
---

## Tổng Quan Section

> **Cập nhật cấu trúc (2026-08-18):** Viết lại toàn bộ section theo đúng cơ chế thật của Claude Design, thay cho khung generic "AI coding tool / AI design tool" trước đó. Bỏ lesson "Thiết lập Local Folder" và "Thiết lập MCP" (không áp dụng, vì Claude Design chạy trên trình duyệt và có cơ chế import riêng). Thay bằng 4 lesson mới bám sát đúng UI thật: Design System file, Pages, Templates folder, CLAUDE.md. Đây là ngoại lệ có chủ đích với quy tắc "generic tool" của khoá học — section này cam kết dùng đúng 1 tool (Claude Design), vì đây là 1 trong 2 track chính thức của khoá học, track còn lại là Figma Make ở phần tiếp theo.

Trước đó, bạn đã thiết kế 2-3 screen trong Figma, tự tay set up prototype pattern của mình (token, component inventory, template), và dọn dẹp file Figma sẵn sàng để AI đọc. Đó là bản kế hoạch. Đây là nơi bạn feed prototype pattern đó vào Claude Design, để nó trở thành một Design System sống, rồi từ đó build một prototype thật, chạy được trong trình duyệt, và chia sẻ nó ra ngoài.

Section này đi theo đúng thứ tự bạn sẽ làm trong Claude Design: import Figma vào một Design System file, hiểu cách file đó tổ chức theo Pages, xây phần Templates trong đó, viết CLAUDE.md để giữ mọi lần build nhất quán, rồi mới bắt đầu build main journey: 2 đến 4 màn hình liền mạch thể hiện đúng 1 user goal bạn đã chọn từ trước. Cuối cùng, refine bằng đúng công cụ Claude Design cho bạn, và chia sẻ prototype đó ra ngoài.

**Kết thúc section này, bạn sẽ có thể:**
1. Import file Figma vào Claude Design, tạo ra một Design System file với token và component được extract tự động
2. Đọc và tổ chức một Design System file theo Pages: Readme, các folder token, và folder Templates
3. Xây dựng Templates: mỗi loại màn hình có một page riêng, làm nguồn tham chiếu cho mọi lần build sau
4. Viết và duy trì CLAUDE.md làm rules sống cho project, được Claude đọc lại trước mỗi lần generate
5. Viết build prompt đầy đủ 5 thành phần, và build main journey 2-4 màn hình chạy được trong trình duyệt, dựa trên đúng Design System vừa set up
6. Refine prototype bằng đúng 4 cơ chế của Claude Design: chat, inline comment, edit mode, draw mode
7. Chia sẻ prototype theo cách người khác thực sự xem được, không chỉ bạn tự biết

**Nội dung section:**
- 10 lesson: 8 lesson nội dung và 2 practice
- 1 tài liệu tải về: Build & Journey Worksheet
- Cần có: file Figma đã thiết kế và dọn dẹp từ phần chuẩn bị trước đó (đã có component inventory và template dạng bản viết tay), tài khoản Claude Design

---

## Trước Khi Vào Bài Học

*Không phải một lesson riêng. Không đánh số. Hai slide ngắn trước khi bắt đầu Lesson 1.*

[SLIDE: STATEMENT]

**Cùng một công thức.**
**Lần này, đúng một cái bếp.**

Trước khi bắt đầu, có một điều cần nói rõ.

Từ đây, section này đi thẳng vào đúng giao diện và cơ chế thật của Claude Design: Design System file, Pages, Templates, CLAUDE.md. Không còn mô tả chung chung kiểu "AI coding tool" nữa.

Đây là một trong hai track công cụ chính thức của khoá học, track còn lại là Figma Make ở phần tiếp theo. Bạn không cần học cả hai, chỉ cần chọn đúng track khớp với công cụ bạn đang dùng.

Hãy nghĩ về prototype pattern như một công thức. Công thức đó không đổi. Nhưng lần này, mình sẽ nấu nó trong đúng một cái bếp cụ thể, từ đầu tới cuối, để bạn thấy chính xác từng nút bấm, không phải một bản mô tả chung chung rồi tự suy ra.

[SLIDE: COMPARE]

**Mindset không đổi.**
**Track thì có.**

Dù học track nào, Design System vẫn cần tồn tại trước khi build, và AI vẫn cần một nguồn tham chiếu để không tự đoán.

Điều khác nhau giữa hai track:
- Tên gọi cụ thể của từng lớp: Claude Design gọi là Design System file, Pages, Templates, CLAUDE.md; Figma Make có tên gọi và luồng thao tác riêng
- Nơi bạn tổ chức token, component, template
- Cơ chế refine và chia sẻ

Nếu bạn đang dùng Figma Make, phần tiếp theo sẽ đi qua đúng workflow đó với cùng logic. Nguyên tắc phía sau luôn giống nhau: prototype pattern là nền tảng, tool chỉ là cách bạn đưa nền tảng đó vào thực tế.

---

## Nội Dung Lesson

### Lesson 1: Đưa Design System Từ Figma Sang Claude Design
*Một lần import, để token và component của bạn trở thành một Design System file mà Claude đọc lại mỗi khi build.*

Claude Design tổ chức mọi thứ quanh một khái niệm gọi là Design System file: một file duy nhất chứa token, component, và (ở lesson sau) Templates của bạn, được Claude tự đọc lại trước mỗi lần build, thay vì bạn phải mô tả lại từ đầu mỗi lần.

**Cách import:**
1. Trong Claude Design, tạo một Design System file mới (hoặc mở file đã có)
2. Đưa file Figma của bạn vào: upload trực tiếp, kết nối qua Figma, hoặc dán link file, tuỳ phiên bản Claude Design bạn đang dùng. Claude Design cũng nhận GitHub repo, screenshot, hay style guide dạng PDF/slide nếu bạn không có file Figma sẵn
3. Claude tự động extract: bảng màu, typography, và các component pattern từ file bạn đưa vào

**Vì sao bước dọn dẹp file trước đó vẫn quan trọng ở đây:** Figma đề xuất dùng variable cho token thay vì giá trị gõ tay, để bất kỳ công cụ nào đọc file, kể cả Claude Design, cũng nhận đúng ý định thiết kế thay vì đoán. Nếu token trong file Figma của bạn chưa là variable, đây là lúc quay lại chuyển chúng thành variable trước khi import, chứ không phải sau.

**Đọc kỹ output.** Cũng như mọi bước "để AI đọc file thật" trong khoá học, đừng mặc định output đúng 100%. Mở Design System file Claude vừa tạo, đối chiếu với file Figma gốc, sửa lại tên hoặc giá trị nào bị sai trước khi đi tiếp.

**Dùng Design System này cho một project mới:** nếu bạn dùng gói cá nhân (Pro/Max), bấm "Use this system" để gắn Design System vào project bạn sắp build. Nếu tổ chức bạn dùng gói Team/Enterprise và bạn có quyền phù hợp, bạn có thể bấm "Published", rồi "Set as org default", để mọi project mới trong tổ chức tự động dùng đúng hệ thống này, không ai phải import lại từ đầu. Chọn cách nào tuỳ vào việc bạn build một mình hay Design System này sẽ được cả team dùng chung.

---

### Lesson 2: Pages — Tổ Chức Design System Của Bạn
*Một file, không phải một trang. Cách Claude Design chia nhỏ Design System để bạn không phải cuộn qua hàng trăm dòng để tìm một token.*

Design System file không phải một trang dài duy nhất. Nó được chia thành nhiều Pages, và Pages là cách Claude Design tổ chức toàn bộ hệ thống của bạn.

**Cấu trúc thường gặp trong một Design System file:**
- Một page Readme ở đầu, tóm tắt Design System này dùng cho sản phẩm gì
- Các page được nhóm theo folder, ví dụ folder Colors chứa từng page token màu riêng (Grey scale, Primary, các trạng thái semantic như Success/Warning), tách biệt rõ ràng thay vì gộp chung
- Một folder Templates, nơi mỗi loại màn hình có một page riêng (phần tiếp theo sẽ đi sâu vào đúng phần này)

Bạn không bắt buộc phải theo đúng cấu trúc này. Có thể thêm folder khác tuỳ nhu cầu, ví dụ Typography hay Components riêng. Điều quan trọng không phải đúng tên folder, mà là giữ nhất quán: mỗi loại thông tin có một chỗ cố định, để cả bạn và Claude đều tìm đúng chỗ mỗi lần cần.

**Vì sao chia Pages quan trọng hơn vẻ ngoài gọn gàng:** khi bạn yêu cầu Claude build hay sửa một màn hình, nó không đọc toàn bộ Design System file cùng lúc. Pages giúp Claude (và cả bạn) định vị đúng phần cần dùng: cần token màu, mở folder Colors; cần pattern cho một loại màn hình, mở folder Templates. Một Design System file tổ chức tốt giúp mọi lần build sau chính xác hơn, không phải vì Claude "thông minh hơn", mà vì bạn đã giảm khối lượng nó phải tự suy đoán.

---

### Lesson 3: Xây Templates Trong Design System
*Không phải bản build thật. Là bản mẫu Claude tham chiếu, mỗi khi bạn build một màn hình cùng loại.*

Trong folder Templates, mỗi loại màn hình có một page riêng, ví dụ một page cho pattern dạng list/feed, một page cho pattern dạng detail, một page cho pattern dạng form. Đây không phải màn hình thật trong prototype của bạn. Đây là bản mẫu: cấu trúc, component, và trạng thái mà bất kỳ màn hình nào thuộc loại đó nên có.

**Vì sao tách riêng, không gộp vào từng màn hình:** nếu main journey của bạn có 2 màn hình cùng dạng list (ví dụ Explore feed và một tab danh sách khác), và mỗi màn hình được build độc lập không tham chiếu cùng một pattern, khả năng cao chúng sẽ lệch nhau, khác spacing, khác cách hiển thị badge, khác vị trí nút hành động, dù cùng thuộc một loại. Một page Templates dùng chung loại bỏ khả năng lệch đó ngay từ đầu, không phải sửa lại sau khi đã build xong cả hai.

**Cách xây một page Templates:**

> "Dựa trên component đã có trong Design System này, tạo một page Templates cho pattern [loại màn hình, ví dụ 'list/feed']: layout tổng thể, component nào xuất hiện, thứ tự ưu tiên thông tin, và đủ state (loading, empty, có dữ liệu). Đây là bản mẫu tham chiếu, không phải màn hình thật."

Làm tương tự cho mỗi loại màn hình chính trong main journey của bạn. Không cần Templates cho mọi thứ, chỉ cần cho những loại màn hình sẽ lặp lại, hoặc đủ phức tạp để đáng có một chuẩn riêng.

**Từ giờ, mỗi khi build một màn hình thuộc loại đã có Templates:** nhắc Claude tham chiếu đúng page đó trong prompt, thay vì để nó tự suy ra cấu trúc từ đầu mỗi lần. Đây chính là điều khiến main journey của bạn ở phần sau nhất quán từ màn hình đầu tới màn hình cuối, thay vì mỗi màn hình một kiểu.

---

### Lesson 4: Đặt Rule Bằng CLAUDE.md
*File này không tĩnh. Sửa lúc nào cũng được, và Claude luôn đọc đúng bản mới nhất trước khi build.*

CLAUDE.md là file lưu rule cho project của bạn. Claude đọc file này trước mỗi lần generate, không cần bạn nhắc lại quy tắc ở từng prompt riêng lẻ.

**Điều quan trọng nhất về CLAUDE.md: nó sống, không phải viết một lần rồi để đó.** Bạn có thể mở và sửa file này bất cứ lúc nào, thêm rule mới, chỉnh lại rule cũ. Lần build tiếp theo sẽ tự động dùng đúng bản mới nhất, không cần bước "publish" hay "cập nhật" nào khác. Mỗi lần bạn sửa một lỗi lặp lại nhiều lần, đó chính là tín hiệu nên viết lỗi đó thành một rule trong CLAUDE.md, để nó không lặp lại nữa ở những lần build sau.

**CLAUDE.md nên có tối thiểu:**
- Trỏ tới Design System file và folder Templates, làm nguồn tham chiếu bắt buộc cho mọi màn hình
- Quy tắc đặt tên: component và page nên đặt tên theo đúng convention nào
- 1 quy tắc quan trọng nhất: *"Luôn kiểm tra Templates trước khi tạo ra một pattern mới. Nếu đã có page Templates cho loại màn hình này, dùng lại nó, đừng tự dựng cấu trúc mới."*
- Bất kỳ điều gì bạn nhận ra mình phải nhắc lại nhiều lần trong prompt, ví dụ giọng văn của content mẫu, hay cách đặt tên biến dữ liệu

**Ví dụ một CLAUDE.md ngắn:**

> "Dự án này dùng Design System 'Travel Buddy'. Luôn tham chiếu token và component trong Design System file này, không tự tạo màu hay spacing mới. Trước khi build một màn hình, kiểm tra folder Templates xem đã có pattern phù hợp chưa, nếu có thì dùng lại, chỉ tạo pattern mới khi thật sự chưa tồn tại. Đặt tên component theo dạng PascalCase, khớp đúng tên đã có trong Design System. Content mẫu dùng dữ liệu thật của sản phẩm, không dùng lorem ipsum."

CLAUDE.md không cần dài. Một file ngắn, rõ ràng, Claude đọc lại được mỗi lần, quan trọng hơn nhiều một file dài mà chẳng ai chắc Claude có đọc hết không.

---

### Lesson 5: Practice 1 — Set Up Design System Của Bạn
*Tự làm lại toàn bộ 4 bước trên, trên chính file của bạn, trước khi qua phần build.*

**Việc cần làm:**
1. Import file Figma của bạn vào một Design System file mới trong Claude Design
2. Kiểm tra Pages: có ít nhất 1 folder token (ví dụ Colors) và bắt đầu tổ chức cấu trúc bạn sẽ dùng
3. Xây ít nhất 1 page Templates, cho loại màn hình xuất hiện nhiều nhất trong main journey bạn đã chọn
4. Viết CLAUDE.md với tối thiểu 4 điều đã nêu ở lesson trước

**Kết quả tối thiểu:** một Design System file đã import từ Figma, có ít nhất 1 page Templates, và một CLAUDE.md đang hoạt động, sẵn sàng dùng để build main journey ở phần tiếp theo.

---

### Lesson 6: Những Lưu Ý Khi Viết Build Prompt
*Bạn không cần viết một prompt thật dài. Chỉ cần nói đủ những điều Claude cần biết để hiểu màn hình bạn muốn xây.*

Giờ bạn đã có Design System, Templates, và CLAUDE.md đáng tin cậy. Câu hỏi tiếp theo không phải "viết prompt sao cho dài và chi tiết", mà là làm sao truyền đạt đúng ý định thiết kế, để Claude không phải tự đoán bất kỳ điều gì.

Một nghiên cứu năm 2025 của NN/g (Nielsen Norman Group), thử nghiệm nhiều loại AI prototyping tool trên cùng một bài toán thiết kế thực tế, cho ra một kết luận khá rõ ràng: **prompt càng cụ thể, output càng gần với kết quả của một designer thật.** Khi prompt chỉ nêu mục tiêu chung chung, mỗi công cụ AI tự đoán theo một hướng khác nhau. Có công cụ hiểu "trang hồ sơ" là hồ sơ mạng xã hội, dù ngữ cảnh thực tế là trang hồ sơ học viên. Nhưng khi prompt nêu rõ layout, component, và trạng thái tương tác cần có, output từ nhiều công cụ khác nhau đều bám sát ý định ban đầu.

Tin tốt là bạn không cần học một kỹ năng hoàn toàn mới. 5 thành phần dưới đây chính là 5 câu hỏi một Product Designer thường đã tự hỏi khi thiết kế, chỉ khác là giờ bạn cần nói chúng ra thành lời, để Claude cũng "biết" những gì bạn đã biết:

| Thành phần | Câu hỏi cần trả lời | Ví dụ |
|---|---|---|
| **Goal** | Người dùng cần làm gì ở đây? | "User xem lại đơn hàng trước khi thanh toán" |
| **Layout** | Nội dung được sắp xếp và ưu tiên như thế nào? | "Danh sách sản phẩm ở trên, tổng tiền và nút thanh toán cố định ở dưới" |
| **Content** | Dữ liệu thật người dùng sẽ nhìn thấy là gì, không phải lorem ipsum | Tên sản phẩm, giá, số lượng thật từ dữ liệu mẫu |
| **Audience** | Ai đang sử dụng màn hình này? | "Người dùng đã đăng nhập, đang mua lần đầu" |
| **Flow context** | Họ đến từ đâu, đang ở đâu, và sẽ đi đâu tiếp theo? | "Đến từ màn hình giỏ hàng, dẫn tới màn hình xác nhận thanh toán, giữ lại số lượng sản phẩm đã chọn" |

**Vì sao "flow context" hay bị bỏ sót nhất:** một màn hình không tồn tại một mình. Đây là thành phần dễ quên nhất, vì nó không mô tả *màn hình này*, mà mô tả *quan hệ giữa các màn hình*. Khi thiếu flow context, Claude nhìn mỗi màn hình như một bài toán riêng: kết quả có thể đúng ở từng bước, nhưng khi nối lại, journey lại không còn liền mạch. Hãy luôn cho Claude biết 4 điều: người dùng đến từ đâu, họ đã làm gì trước đó, màn hình hiện tại cần giải quyết điều gì, và họ có thể đi đâu tiếp theo. Đây đúng là vấn đề "AI không lưu lại thông tin" giữa các lần yêu cầu, chỉ khác là lần này lỗi nằm ở người viết prompt quên nhắc, không phải AI quên nhớ, và CLAUDE.md chỉ giữ được rule chung, không giữ được flow context riêng của từng màn hình, bạn vẫn cần nêu nó trong từng prompt.

**Một khung prompt, dùng lại cho mọi màn hình:**

> "Build màn hình [tên màn hình]. Goal: [user đang cố làm gì ở đây]. Layout: [cách sắp xếp, ví dụ 'metrics ở hàng trên, chart chi tiết bên dưới']. Content: [tên field và dữ liệu mẫu thật, không phải lorem ipsum]. Audience: [ai đang dùng]. Flow context: màn hình này đến từ [màn hình trước] và dẫn tới [màn hình sau], giữ lại [dữ liệu/trạng thái cần mang theo]. Nếu đã có Templates phù hợp cho loại màn hình này, dùng lại đúng pattern đó. Khớp đúng tên component trong Design System. Output prototype tương tác."

Dùng cùng một khung này cho mọi màn hình trong journey, sang màn hình tiếp theo bạn chỉ cần thay nội dung phù hợp. Một khung nhất quán giúp bạn không bỏ sót thông tin quan trọng, so sánh các màn hình với nhau dễ hơn, giữ context xuyên suốt journey, và tái sử dụng được prompt khi build main journey và cả khi mở rộng sau này.

Nếu bạn có ảnh tham chiếu, chẳng hạn một màn hình tương tự, một layout đối thủ, hay cảm hứng thị giác, hãy đính kèm nó trước khi prompt. Cùng nghiên cứu của NN/g ghi nhận: khi prompt có kèm ảnh tham chiếu hoặc link Figma frame, output sát với thiết kế gốc hơn hẳn so với chỉ mô tả bằng lời. "Một tấm ảnh đáng giá ngàn từ" hoá ra đúng cả với AI.

**Đã có PRD, wireframe, hoặc user flow? Bạn không cần bắt đầu từ một trang giấy trắng.** PRD, wireframe, user flow, và solution list đều là nguồn context có giá trị, nhưng chúng không thay thế 5 thành phần trên, chúng giúp bạn điền framework nhanh hơn. Dùng tài liệu có sẵn để trả lời nhanh hơn, đặc biệt là Goal, Audience, và Flow context, sau đó chỉ lấy phần liên quan tới màn hình đang build. Đừng đưa toàn bộ tài liệu vào một prompt và yêu cầu Claude build cả journey cùng lúc: càng nhiều context không liên quan, Claude càng dễ bỏ sót chi tiết quan trọng. Lesson tiếp theo sẽ nói rõ hơn vì sao build tuần tự vẫn là lựa chọn đúng, ngay cả khi bạn đã chuẩn bị đầy đủ từ đầu.

**Không phải mọi thứ đều nên biến thành text.** Với PRD và user flow, markdown giúp Claude đọc trực tiếp nội dung và hiểu cấu trúc qua heading, hierarchy, đây là hướng đúng nếu bạn có thói quen convert tài liệu sang `.md`. Nhưng với wireframe, hãy giữ nguyên hình ảnh: vị trí, tỷ lệ, và mối quan hệ không gian thường khó truyền đạt đầy đủ bằng một đoạn mô tả chữ. Nếu cần ghi chú hành vi khó thấy bằng mắt, thêm caption ngắn cạnh ảnh, đúng nguyên tắc annotation đã học trước đó, không thay hẳn ảnh bằng text.

Lưu các tài liệu này làm context tham chiếu thường trực, tương tự cách CLAUDE.md trỏ tới Design System và Templates. Khi build một màn hình, chỉ đưa phần liên quan vào prompt, thay vì dán toàn bộ file mỗi lần.

---

### Lesson 7: Xây Dựng Main Journey (2-4 Màn Hình)
*Lần đầu tiên, ý tưởng của bạn bắt đầu trở thành một prototype có thể chạm vào.*

Dùng khung prompt 5 thành phần, build lần lượt từng màn hình trong main journey: 2 đến 4 màn hình bạn đã chọn từ trước, cùng thể hiện 1 user goal duy nhất.

**Đừng đánh giá cả quy trình qua lần build đầu tiên.** Claude có thể nhanh chóng dựng cấu trúc và giao diện ban đầu, nhưng spacing, hierarchy, grouping, và những chi tiết tạo nên chất lượng cuối cùng của UI vẫn cần bạn review và tinh chỉnh. Mục tiêu của lần build đầu tiên không phải là hoàn hảo, mà là có một nền tảng đủ tốt để bắt đầu làm việc. Một nghiên cứu NN/g năm 2025 đã trích ở phần trước gọi đúng cảm giác này: kết quả đầu tiên thường "ổn từ xa, chưa ổn khi nhìn gần". Đây không phải vì bạn prompt sai, mà là giới hạn hiện tại của công nghệ.

**Build. Review. Rồi mới tiếp tục.** Build màn hình đầu tiên, review kết quả, sửa những gì cần thiết, rồi mới chuyển sang màn hình tiếp theo. Giữ flow context trong mỗi prompt để Claude hiểu màn hình đang nằm ở đâu trong journey. Đúng công thức build → review → continue, không phải một prompt → cả journey.

**Vì sao không nên build cả journey trong một lần:** đến bước này, bạn đã có Design System, Templates, CLAUDE.md, thậm chí cả PRD và Wireframe. Nhưng có đủ tất cả không có nghĩa là nên đưa hết vào một prompt để build cả journey cùng lúc. Nghiên cứu về "context rot" cho thấy mọi model hàng đầu đều giảm chất lượng output khi input dài ra, kể cả khi thông tin cần thiết đã nằm sẵn trong đó, và thông tin ở giữa một prompt dài dễ bị bỏ sót hơn thông tin ở đầu hoặc cuối. Tài liệu kỹ thuật của Anthropic về context engineering cho agent, cũng như pattern "plan-and-execute" phổ biến trong thiết kế AI agent, đều đi đến cùng kết luận: có kế hoạch đầy đủ từ đầu không loại bỏ nhu cầu thực thi từng phần nhỏ, có ranh giới rõ ràng. Build tuần tự giúp từng prompt tập trung và chính xác hơn. Đây là giới hạn của công nghệ, không phải bạn làm sai.

**Ví dụ thực tế: main journey "Travel Buddy".** Main journey của Travel Buddy có 3 màn hình: Onboarding ("Explore without signing up") → Explore feed (chế độ guest) → Tip Detail (tap vào 1 Tip Card). Dưới đây là build prompt đầy đủ cho màn hình giữa, Explore feed, dùng đúng khung 5 thành phần với dữ liệu thật, không phải placeholder:

> "Build màn hình Explore feed. Goal: user đang ở chế độ guest (chưa đăng ký) khám phá địa điểm gợi ý gần Chiang Mai, xem tip từ local và traveler thật. Layout: header hiển thị vị trí 'Near Chiang Mai' kèm số lượng tip, mode switcher 3 tab (Near Me / Country / Map), thanh search kèm nút filter có badge số bộ lọc, banner nhắc đang ở guest mode, danh sách Tip Card dạng feed (ảnh full-bleed, badge mức độ đông đúc, quote, tác giả, thời gian đăng), chặn cuối feed bằng guest paywall, bottom nav 5 tab cố định. Content: 2 tip thật, 'Warorot Night Market' (Chiang Mai · Street food, quote 'Skip the tourist night bazaar, this is where I actually shop after work' của Niran K., Local resident, 2 ngày trước) và 'Doi Suthep Temple' (Chiang Mai · Culture, quote của Aisha M., Explorer, 5 ngày trước). Audience: user chưa đăng ký, đang browse ở chế độ guest, bị giới hạn xem trước khi chạm ngưỡng paywall. Flow context: màn hình này đến từ Onboarding sau khi user chọn 'Explore without signing up', giữ lại trạng thái guest mode; dẫn tới Tip Detail khi user tap vào 1 Tip Card. Dùng đúng Templates cho pattern dạng feed đã có trong Design System, không tự dựng cấu trúc mới. Khớp đúng tên component. Output prototype tương tác."

Để ý prompt này không có chỗ nào Claude phải tự đoán: layout cụ thể tới từng khối, content là dữ liệu thật lấy từ chính sản phẩm (không phải "tip card mẫu"), và flow context nêu rõ cả 2 chiều, đến từ đâu và dẫn đi đâu. Đây chính là mức độ chi tiết bạn nên nhắm tới cho mỗi màn hình trong main journey của mình.

**Review là công việc của Designer.** Claude tạo ra bản build đầu tiên, nhưng bạn mới là người quyết định nó có đúng hay không. Mở màn hình Claude vừa tạo cạnh file Figma gốc, rồi tự hỏi:
1. Màn hình có đúng mục tiêu không?
2. Người dùng có biết mình đang ở đâu không?
3. Thông tin có được ưu tiên đúng không?
4. Component và pattern có nhất quán với Templates không?
5. Hành động tiếp theo có rõ ràng không?
6. Màn hình có kết nối đúng với journey không?

Ghi lại những điểm cần chỉnh, chưa cần sửa ngay. Phần tiếp theo sẽ hướng dẫn cách chọn đúng cơ chế để sửa từng loại lỗi.

**Kết quả tối thiểu của lesson này:** main journey 2-4 màn hình, chạy được trong trình duyệt, có điều hướng nối giữa chúng.

**Nếu bạn thấy nản vì kết quả chưa đẹp:** đây là cảm giác bình thường, không phải dấu hiệu bạn đang làm sai. Con mắt của bạn là thứ biến một prototype "trông đúng" thành một prototype thực sự đúng. Đó không phải một khiếm khuyết của quy trình, đó chính là công việc của một designer trong quy trình này, và là điều lesson tiếp theo sẽ hướng dẫn cách thực hiện có hệ thống.

---

### Lesson 8: Practice 2 — Build Main Journey (2-4 Màn Hình)
*Áp dụng toàn bộ khung prompt 5 thành phần và quy trình build-review từng màn hình để có main journey chạy được, việc còn lại là làm thật.*

**Việc cần làm:**
1. Viết build prompt đầy đủ 5 thành phần cho từng màn hình trong main journey
2. Build và review từng màn hình cạnh file Figma gốc, đối chiếu với Templates đã có
3. Nối các màn hình theo đúng flow context đã nêu trong prompt

**Kết quả tối thiểu:** main journey 2-4 màn hình chạy được trong trình duyệt, dùng nhất quán component và token từ cùng một Design System. Đây là kết quả bạn sẽ mang sang phần tiếp theo để tinh chỉnh và mở rộng.

---

### Lesson 9: Review Và Refine Prototype
*Không phải mọi chỉnh sửa đều cần một prompt mới. Chọn đúng cơ chế, sửa nhanh hơn và ít rủi ro làm hỏng phần đang đúng.*

Claude Design cho bạn 4 cách khác nhau để refine, không chỉ có prompt lại từ đầu. Mỗi cách phù hợp với một loại chỉnh sửa khác nhau, và chọn sai cách thường khiến bạn mất công hơn cần thiết, hoặc vô tình làm hỏng phần đang đúng.

| Cơ chế | Phù hợp khi | Ví dụ |
|---|---|---|
| **Chat** | Thay đổi rộng, ảnh hưởng cấu trúc hoặc nhiều phần cùng lúc | "Đổi layout màn hình này sang dạng 2 cột, giữ nguyên nội dung" |
| **Inline comment** | Chỉnh sửa nhỏ, đúng vào một component cụ thể, có thể gộp nhiều comment rồi gửi cùng lúc | Click vào nút CTA, để lại comment "tăng contrast, hiện tại khó đọc trên nền sáng" |
| **Edit mode** | Chỉnh trực tiếp màu, font, spacing, không cần Claude generate lại | Kéo chỉnh khoảng cách giữa 2 block, đổi màu accent, tự làm không tốn thời gian chờ |
| **Draw mode** | Thay đổi khó diễn tả bằng lời, liên quan vị trí hay bố cục không gian | Vẽ mũi tên chỉ hướng muốn di chuyển 1 block, khoanh vùng cần gộp lại |

**Cách chọn nhanh:** nếu bạn có thể mô tả thay đổi bằng một câu ngắn và nó ảnh hưởng nhiều phần, dùng chat. Nếu chỉ một component cần sửa, dùng comment, và gom nhiều comment nhỏ lại gửi một lượt thay vì gửi từng cái một. Nếu là màu, font, spacing đơn thuần, tự sửa bằng edit mode, nhanh hơn chờ Claude generate lại. Nếu bạn thấy mình đang cố gõ thành lời một thứ chỉ cần vẽ 2 giây là rõ, chuyển sang draw mode.

**Muốn thử một hướng khác mà không mất bản đang có:** yêu cầu Claude giữ lại bản hiện tại và thử một hướng hoàn toàn khác, thay vì để nó ghi đè lên bản đang ổn. Đây là cách branch ra một phương án mới để so sánh, không phải đánh cược vào một lần sửa duy nhất.

**Refine không thay thế review.** Trước khi refine bất cứ điều gì, quay lại 6 câu hỏi review ở lesson trước, xác định rõ vấn đề là gì, rồi mới chọn cơ chế phù hợp để sửa đúng vấn đề đó. Refine ngẫu nhiên, không dựa trên review có mục đích, thường chỉ tạo ra một phiên bản khác, không chắc là phiên bản tốt hơn.

---

### Lesson 10: Chia Sẻ Prototype Của Bạn
*Prototype chạy trong Claude Design của bạn chưa chắc là một prototype người khác mở được.*

Prototype bạn vừa build và refine nằm trong Claude Design, không phải một file Figma hay code trên máy bạn. Cách chia sẻ nó phụ thuộc vào việc người xem có nằm trong cùng tổ chức Claude với bạn hay không. Design System đứng sau prototype này thì khác: nếu bạn đã publish nó ở bước đầu tiên, nó tự động sẵn sàng cho project tiếp theo trong tổ chức, không cần import lại. Nhưng bản thân prototype, phần bạn muốn người khác *xem*, vẫn cần một bước chia sẻ riêng.

**Nếu người xem nằm trong cùng tổ chức của bạn** (đồng nghiệp, người cùng công ty dùng chung gói Team/Enterprise), chia sẻ đơn giản:
1. Mở project, chọn quyền hiển thị: Public (mọi người trong tổ chức xem và dùng được) hoặc Private (chỉ người được mời)
2. Với từng người được mời, chọn quyền "Can use" (chỉ xem/dùng) hoặc "Can edit" (sửa được)
3. Gửi link nội bộ, người trong tổ chức mở được ngay, không cần thêm bước nào

**Nếu người xem không nằm trong tổ chức của bạn** (stakeholder ngoài công ty, hay bạn đang dùng gói Pro/Max cá nhân không có team) — đây là trường hợp phổ biến nhất khi demo cho người ngoài — Claude Design không có link công khai trực tiếp. Bạn cần export rồi host ở nơi khác:
1. Mở project, bấm Export ở góc trên bên phải
2. Chọn "Export as standalone HTML" — ra 1 file HTML duy nhất, gộp sẵn font, ảnh, mọi thứ cần thiết, chạy được ngay không cần server riêng
3. Kéo thả file này vào 1 dịch vụ hosting tĩnh miễn phí, ví dụ Netlify Drop hoặc tiiny.host — có link ngay trong vài giây, không cần biết deploy

Export cũng có 3 lựa chọn khác: PDF (giữ đúng hình thức nhưng mất tương tác), PPTX (tiện để đồng nghiệp sửa tiếp trong PowerPoint, nhưng convert từ HTML sang PPTX có thể lệch layout), và "Handoff to Claude Code" (nếu sau này muốn chuyển prototype này sang code thật, dùng AI coding tool để phát triển tiếp). Để chia sẻ prototype tương tác cho người xem, standalone HTML vẫn là lựa chọn đúng nhất.

**Ai đang xem quyết định bạn cần tinh chỉnh tới đâu.** Demo nhanh cho bạn học không cần hoàn hảo, nhưng gửi cho stakeholder cấp cao hay xin duyệt ngân sách thì đáng quay lại refine thêm trước khi export.

**Dù chia sẻ trong hay ngoài tổ chức, luôn xác nhận trước khi gửi:**
- Link mở được ở chế độ ẩn danh hoặc trên thiết bị khác, không riêng máy bạn
- 1 câu mô tả ngắn đi kèm link: prototype này thể hiện user goal gì, gồm những màn hình nào

**Khi chia sẻ, dẫn dắt bằng câu hỏi, không chỉ gửi link:**
- Bạn đã build gì? (user goal + các màn hình)
- Claude đã làm điều gì khiến bạn bất ngờ, tốt hoặc chưa tốt?
- Nếu không có Design System và Templates chuẩn bị từ đầu, việc này sẽ mất bao lâu hơn?

3 câu hỏi này không chỉ để nói chuyện xã giao. Chúng chính là khung cho phần "Nhìn Lại Quá Trình" ở practice tiếp theo, nơi bạn tự trả lời chúng một cách có cấu trúc.

---

## Worksheet: Build & Journey

Với main journey 2-4 màn hình đã chọn, điền:

1. **Design System setup:** link Design System file, danh sách page Templates đã có, và nội dung CLAUDE.md bạn đang dùng.

2. **Build prompt đầy đủ 5 thành phần** cho từng màn hình, dùng đúng khung đã học.

3. **Nhật ký review:** sau khi build mỗi màn hình, ghi lại tối thiểu 1 điểm cần chỉnh bạn phát hiện khi so với file Figma gốc, và cơ chế refine bạn dùng để sửa nó (chat, comment, edit mode, hay draw mode).

Giữ lại worksheet này. Phần tiếp theo sẽ dùng lại thông tin ở mục 3 khi bạn học cách chọn đúng chế độ tinh chỉnh ở quy mô lớn hơn.

---

## Nguồn Tham Khảo

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

---

*Khóa học: Systematic AI Prototyping for Product Designers · Section 3 — Xây Dựng AI Prototype bằng Claude Design*
*Thực hiện bởi Winnie Nguyen · Cập nhật lần cuối tháng 8/2026*

---
title: "Your Design Process, with AI"
subtitle: "Where design careers are heading, the four stages you already know, where AI helps in each, and the workspace every later lesson builds on"
type: lesson
program: ai-design-workflow
tags: [ai, design-process, double-diamond, terminology, context, folder, data-safety, hub, foundational]
level: foundational
duration: "2 x 90 min (buổi 1 dạy, buổi 2 thực hành)"
date: 2026-10-06
draft: true
slides: ""
previous-session: ""
next-session: "Discover the Problem"
---

## Abstract

Tài liệu này mô tả module đầu tiên của chương trình AI Design Workflow, dành cho Product Designer và UI/UX Designer ở cấp mid và senior. Module gồm hai buổi 90 phút: buổi 1 trình bày bối cảnh và khung kiến thức, buổi 2 là buổi thực hành trên case của chính người học.

Module giải quyết năm vấn đề, theo thứ tự trình bày:

1. **Định hướng nghề nghiệp.** AI đang thay đổi nghề UI/UX và product design như thế nào, dựa trên các nguồn có thể kiểm chứng, và ba hướng đi mà một designer có thể cân nhắc.
2. **Quy trình thiết kế khi có AI.** Bốn stage của Double Diamond (Discover, Define, Develop, Deliver), các method quen thuộc trong từng stage, và việc phân chia giữa phần AI hỗ trợ với phần designer vẫn phải tự thực hiện.
3. **Bộ khái niệm chung** để làm việc với AI tool, gồm mười thuật ngữ.
4. **Quy tắc về dữ liệu** an toàn để đưa cho AI tool.
5. **Một project folder** làm nền cho toàn bộ chương trình: mỗi module sau thêm một file hoặc một page vào cùng một case.

Điểm xuyên suốt ở mọi stage là **AI-assisted, không phải AI-generated**. AI-generated nghĩa là AI đưa ra quyết định. AI-assisted nghĩa là designer quyết định, AI hỗ trợ phần soạn nháp và lắp ráp. Nguyên tắc vận hành ở mọi stage là: **AI soạn nháp. Designer kiểm tra. Designer quyết định.**

Chương trình đặt ra một lập trường: **designer là partner cùng định nghĩa requirement với business và product.** Product, business và design cùng chọn vấn đề đáng giải trước khi build.

**Đối tượng.** Chương trình thiết kế cho Product Designer và UI/UX Designer. Product Owner, Product Manager và Business Analyst có thể học cùng trọn vẹn: cùng stage, cùng case folder, cùng hub. Họ không cần kỹ năng design và không phải build prototype từ đầu; ở phần prototype, họ dùng một design system có sẵn và để AI tạo template từ đó. Ở các module sau, những khác biệt theo vai trò được ghi trong mục "Nếu bạn là PO, PM hoặc BA".

**Nhịp học của cả chương trình.** Hai buổi online mỗi tuần, mỗi buổi 90 phút, 7 đến 8 học viên, hai buổi cách nhau khoảng ba ngày. Buổi đầu dạy một chủ đề và tương tác bằng câu hỏi; buổi thứ hai là thực hành trên case của học viên, có coaching, và là nơi tạo ra mọi output. Chuẩn bị tối đa 10 phút trước buổi dạy (khoảng 20 phút ở tuần đầu để kiểm tra tool); homework tối đa khoảng 45 phút và chỉ nối tiếp phần đã bắt đầu trên lớp. Buổi live không phụ thuộc vào việc homework đã hoàn thành hay chưa.

**Vị trí của module.** Module nằm trước bước đầu tiên của workflow. Module giả định người học đã có kinh nghiệm research, UX design và prototyping, và bổ sung lớp AI lên trên những kỹ năng đó.

---

## Learning Objectives

Sau hai buổi, học viên có thể:

1. **Mô tả** ba hướng đi nghề nghiệp (strategic designer, design builder, AI product designer), nêu bằng chứng hiện có và giới hạn của bằng chứng đó, và chọn hướng mình nghiêng về để định hướng cho cả chương trình
2. **Kể tên** các method chính trong từng stage của bốn stage, và nêu được AI hỗ trợ ở đâu, phần nào designer vẫn phải tự thực hiện
3. **Giải thích** mười thuật ngữ AI cốt lõi bằng lời của mình: AI chat tool, AI coding tool, context, context window, grounding, hallucination, agent, connector (MCP), reusable instructions (skills, rules file, project memory), và AI-assisted so với AI-generated
4. **Quyết định** dữ liệu nào an toàn để đưa cho AI tool: phân loại tài liệu thành ba nhóm (safe, ask first, never in a public tool), ẩn danh trước khi dán, và viết data rules của riêng mình
5. **Cài đặt** case folder của chương trình cho case của chính mình, gồm layout chuẩn, context pack đã bắt đầu và một hub trống
6. **Dùng lại** một file đã lưu làm context thay vì mô tả lại project, và yêu cầu AI chỉ rõ nguồn cho từng ý, kèm câu trả lời "unknown" khi không có thông tin
7. **Giải thích** cách chia sẻ hub với stakeholder: mặc định private (PDF hoặc folder nén), chỉ publish lên GitHub khi case được phép chia sẻ

---

## 1. Background: AI and the design profession

Nhiều designer đặt câu hỏi: khi AI phổ biến, UI/UX và product design sẽ ra sao? Mục này trình bày những gì các nguồn có thể kiểm chứng cho biết. Mỗi con số được ghi kèm nguồn, năm và cỡ mẫu. Các nguồn được liệt kê ở phần References.

### 1.1 Findings

| # | Phát hiện | Nguồn |
|---|---|---|
| 1 | **Mức dùng AI rất cao.** Trong khảo sát 906 designer tại hơn 60 quốc gia (2026), 91% dùng AI cho công việc design ít nhất mỗi tuần, tăng từ 54% một năm trước; 75% dùng mỗi ngày; trung bình mỗi người thường xuyên dùng 7 AI tool, tăng từ 3 | [1] |
| 2 | **Ranh giới giữa các vai trò mờ đi.** Một nửa số người trả lời đã đưa code do AI tạo ra lên production; 65% làm nhiều việc product hoặc engineering hơn; 40% cho biết PM và engineer làm nhiều việc design hơn | [1] |
| 3 | **Nghề chưa co lại trên số liệu dự báo.** Cục Thống kê Lao động Mỹ (BLS) dự báo số việc làm của web và digital interface designer tăng 7,0% trong giai đoạn 2024 đến 2034 (từ 128.900 lên 137.900), so với 3,1% của mọi ngành. Bảng mới hơn (2025 đến 2035) gộp web developer và digital designer, cho ra 5%, và ghi rằng việc dùng AI trong phát triển web "may soften" mức tăng. Hai con số dùng cách gộp nghề và năm gốc khác nhau, nên không so sánh trực tiếp | [4], [5] |
| 4 | **Áp lực lộ ra ở entry level.** Nielsen Norman Group (NN/g) nhận định thị trường UX đang ổn định sau giai đoạn 2023 đến 2024, nhưng vị trí entry-level vẫn "scarce and highly competitive" trong khi vị trí senior phục hồi nhanh hơn | [3] |
| 5 | **Cơ chế tác động.** Nghiên cứu của Stanford trên dữ liệu bảng lương ADP cho thấy người đi làm sớm (22 đến 25 tuổi) trong các nghề chịu tác động mạnh nhất của AI có việc làm giảm 16% tương đối, trong khi nhóm có kinh nghiệm ổn định; mức giảm tập trung ở nơi AI thay thế thay vì hỗ trợ công việc. Nghiên cứu xét mọi nghề, không tách riêng designer | [6] |
| 6 | **Cảm nhận phân hóa.** Theo một nguồn thứ cấp trích báo cáo State of the Designer 2026 của Figma, 36% designer cho rằng ngành đã tốt hơn, 35% cho rằng tệ hơn, 29% cho rằng không đổi | [2], qua nguồn thứ cấp; chưa đối chiếu với báo cáo gốc |

### 1.2 Interpretation

Từ các phát hiện trên, tài liệu rút ra hai nhận định. Cả hai là **suy luận**, không phải kết quả đo trực tiếp.

- **Phần việc bị nén nhanh nhất là từ brief sang screen.** Vị trí thiên về execution ở entry level (wireframe, sản xuất asset) là nơi áp lực rõ nhất [3], [6]. Không có nguồn nào đo trực tiếp nhóm "designer nhận brief rồi làm screen"; nhận định này suy ra từ cơ chế ở phát hiện 4 và 5.
- **Phần còn lại là phần AI chưa làm thay được:** chọn vấn đề đáng giải, thống nhất thế nào là thành công, và kiểm tra những gì AI soạn nháp. NN/g mô tả những practitioner thành công là "adaptable generalists", coi UX là việc giải quyết vấn đề mang tính chiến lược, không phải sản xuất deliverable [3].

Cùng một thời điểm và cùng những tool, cảm nhận của designer đi ngược chiều nhau (phát hiện 6). Tài liệu đọc điều này như một dấu hiệu rằng khác biệt nằm ở cách làm việc, không nằm ở tool. Đây là cách đọc của tác giả, không phải kết luận của báo cáo.

### 1.3 Limitations of the evidence

- Các khảo sát designer ([1], [2]) là tự khai báo và không dùng mẫu ngẫu nhiên; "91% designer" nên được hiểu là 91% những designer đã trả lời. Cả hai do bên có lợi ích trong lĩnh vực design và AI tooling thực hiện.
- Dự báo của BLS tính tác động của AI còn hạn chế và bản 2024 đến 2034 có trước phần lớn những thay đổi gần đây.
- Chưa có nguồn nào cho thị trường Việt Nam ở cấp độ designer. Số liệu ở trên chủ yếu về thị trường Mỹ và toàn cầu.
- Một số số liệu thường thấy trong các bài viết nghề nghiệp (ví dụ mức giảm tin tuyển junior theo phần trăm, hay mức tăng của từng chức danh) không truy ngược được nguồn và không được dùng ở đây.

---

## 2. Career directions

Ba hướng đi dưới đây không loại trừ nhau, và chúng mô tả xu hướng chứ không phải sự đảm bảo. Mức bằng chứng được ghi để người đọc cân nhắc.

| Hướng | Công việc chính | Kỹ năng trọng tâm | Bằng chứng và giới hạn | Chương trình này hỗ trợ |
|---|---|---|---|---|
| **Strategic designer** (senior generalist) | Cùng product và business chọn vấn đề đáng giải; research, framing, ra quyết định | Research, framing, stakeholder management, judgment | NN/g 2026: vị trí senior và generalist phục hồi nhanh hơn [3]; nghiên cứu Stanford cho thấy nhóm có kinh nghiệm ổn định [6]. **Mức vừa:** một bài phân tích có thẩm quyền cộng một nghiên cứu gián tiếp | Tuần 2 đến 4 (Discover, Frame); hub làm bằng chứng cho lập luận |
| **Design builder** (design engineer) | Dựng prototype chạy được và đưa lên production bằng AI coding tool | Design system, kiểm tra các file mà AI coding tool đã sửa, đọc output | Một nửa designer được khảo sát đã đưa code do AI tạo lên production [1]. **Mức vừa** về xu hướng; số liệu tuyển dụng thì yếu | Tuần 5 đến 6 (prototype, refine) |
| **AI product designer** | Thiết kế sản phẩm có AI bên trong: hành vi, ranh giới, lỗi và niềm tin của người dùng | Hiểu hallucination và grounding, đánh giá output, conversation design | NN/g và các nguồn nghề nghiệp nêu đây là chuyên môn đang lên [3]; số liệu tăng trưởng chưa đáng tin. **Mức yếu** | **Chỉ có nền tảng.** Chương trình dạy cách dùng AI để làm việc, không dạy thiết kế sản phẩm AI |

UX research là một hướng liên quan: NN/g nêu research và stakeholder management là những kỹ năng tạo khác biệt [3]. Hướng thiên về execution ở entry level (wireframe, sản xuất asset) là hướng chịu áp lực nhiều nhất theo các nguồn trên, và là lý do để chọn hướng sớm.

Ở buổi 1, học viên trao đổi theo cặp về hướng mình nghiêng về. Ở buổi 2, học viên ghi hai đến ba dòng vào `00-context/my-direction.md` (hướng nghiêng về, lý do, một kỹ năng muốn xây trong chương trình). File được xem lại ở tuần 7 và có thể thay đổi.

---

## 3. The design process with AI

### 3.1 The four stages

Double Diamond gồm bốn stage; output của stage này là input của stage kế tiếp. Với người đã học phiên bản Design Thinking năm stage, hai mô hình tương ứng như sau: Empathise là **Discover**, Define là **Define**, Ideate và Prototype là **Develop**, Test là **Deliver**.

| Stage | Hình dạng | Tạo ra |
|---|---|---|
| **Discover** | Mở rộng: hiểu người dùng và bối cảnh | Evidence, research thô |
| **Define** | Thu hẹp: diễn giải các phát hiện | Insight, opportunity, design challenge |
| **Develop** | Mở rộng rồi thu hẹp: brainstorm, select, prototype | Một hướng đã chọn và một prototype |
| **Deliver** | Thu hẹp: test và bàn giao | Findings, handoff pack, measurement plan |

Mỗi stage kết thúc bằng một checklist ngắn gọi là **gate** trước khi công việc đi tiếp. Chi tiết từng method và từng gate nằm ở module dành cho stage đó. Ở buổi 1, phần này chỉ trình bày mỗi stage gồm gì và AI hỗ trợ ở đâu; từng method được đọc trước trong pre-read brief và có method card riêng.

### 3.2 Methods and the division of work

Câu hỏi áp dụng cho mọi stage: **AI hỗ trợ được ở đâu, và phần nào designer vẫn phải tự thực hiện?**

| Stage | Method | AI hỗ trợ | Designer vẫn tự thực hiện |
|---|---|---|---|
| **Discover** | Research questions, desk research, competitor analysis, stakeholder meetings, questionnaire, user interviews, observation | Soạn nháp research questions, interview guide và questionnaire; đọc desk research và nguồn competitor đã thu thập rồi rút ra dữ kiện; phiên âm và tóm tắt các session | Chọn câu hỏi; nói chuyện và quan sát người thật; đối chiếu mọi bản tóm tắt với ghi chú gốc. **AI không phải là user và không thể thay thế user** |
| **Define** | Năm bước: identify themes, sort and cluster, define insights, frame opportunities, set design challenges. Công cụ thường dùng: empathy map, assumption map, jobs to be done, How Might We, current-state journey map, Lean UX canvas | Đề xuất theme và cluster từ ghi chú thô; soạn nháp insight statement và câu How Might We; chỉ ra chỗ evidence còn mỏng | Quyết định theme nào quan trọng; xếp hạng opportunity; thống nhất design challenge với product và business. **AI không đóng vai người phía product và business** |
| **Develop** | Brainstorm (Crazy 8s, How Might We ideation, brainwriting); select (impact vs effort, concept sketching, storyboarding); prototype (wireframes, interactive prototype, proof of concept) | Mở rộng tập ý tưởng và các biến thể; với AI coding tool, dựng prototype đầu tiên từ flow và design system | Chọn hướng đi và ghi lại lý do; kiểm tra từng quyết định với nhu cầu người dùng và các principle |
| **Deliver** | Internal feedback session, concept testing, usability testing (moderated hoặc unmoderated), A/B testing; handoff pack và kế hoạch đo lường thành công | Soạn nháp test plan và script; sắp xếp ghi chú; soạn nháp handoff | Chạy session với user thật; xếp findings theo mức độ quan trọng, không theo số lần được nhắc. **AI không thay thế user thật** |

Ở mọi stage, method thuộc về designer; AI giúp soạn nháp nhanh hơn, còn việc kiểm tra thuộc về designer. Mỗi method có một card tham khảo một trang (là gì, vì sao, khi nào, cách làm, AI hỗ trợ ở đâu, phần designer tự thực hiện): [mục lục method card](../../programs/ai-design-workflow/assets/method-cards/README.md).

### 3.3 The partner stance

Một brief tốt từ product là điểm xuất phát tốt. Phần AI làm nhanh nhất là biến brief thành screen. Phần AI không làm thay được là cùng product và business chọn vấn đề đáng giải và thống nhất thế nào là thành công. Việc này cần cả hai phía: design tham gia sớm với evidence; product và business chia sẻ những gì họ biết về vấn đề, outcome và ràng buộc. Mục tiêu là hai cách nhìn gặp nhau trước khi build, không phải sửa lại công việc của bất kỳ bên nào.

Mức độ làm việc chung với product khác nhau giữa các học viên: có người làm sát product mỗi ngày, có người chỉ liên lạc qua trung gian, có người chưa có cơ hội trao đổi. Chương trình vận hành được trong cả ba trường hợp; module Discover the Problem trình bày cách làm.

---

## 4. Working with AI: core concepts

### 4.1 Ten terms

| Nhóm | Thuật ngữ | Định nghĩa | Hệ quả thực hành |
|---|---|---|---|
| Các tool | **AI chat tool** | Người dùng viết, AI trả lời. Phù hợp cho tổng hợp, lên ý tưởng, viết | Dùng sâu một tool trước khi thử nhiều tool |
| Các tool | **AI coding tool** | Đọc và ghi file trong project folder; dựng prototype chạy được | Cung cấp flow và design system |
| Nói chuyện với AI | **Context** | Mọi thứ AI nhìn thấy tại thời điểm đó: instruction, text đã dán, file đính kèm, các tin nhắn trước | Đưa đúng tài liệu vào; AI không biết gì khác về project |
| Nói chuyện với AI | **Context window** | Giới hạn lượng thông tin AI giữ được cùng lúc; tài liệu dài và lộn xộn làm kết quả kém chính xác | Chỉ đưa những phần mà một bước cần |
| Nói chuyện với AI | **Grounding** | Gắn câu trả lời với tài liệu được cung cấp, không dựa vào kiến thức chung của AI | "Chỉ dùng tài liệu bên dưới. Mỗi ý lấy từ đâu?" |
| Khi nó làm sai | **Hallucination** | Câu trả lời tự tin nhưng bịa: một đối thủ không tồn tại, một câu quote chưa ai nói | Yêu cầu nguồn cho từng ý; cho phép AI trả lời "unknown" |
| Cách một số tool hành động | **Agent** | Tool tự thực hiện nhiều bước: đọc file, sửa, chạy lệnh, rồi báo lại | Kiểm tra các file đã bị sửa, không chỉ câu trả lời |
| Cách một số tool hành động | **Connector (MCP)** | Giống một cái USB: cắm giữa file design và AI tool để AI đọc được thứ đang làm [7] | Trước khi kết nối, xác định nó đọc và sửa được những gì |
| Mang theo chuẩn của mình | **Reusable instructions** (skills, rules file, project memory) | Instruction đã lưu, bộ quy tắc chung của project, hoặc context project đã lưu [7] | Viết một lần, dùng lại nhiều lần |
| Lập trường (thuật ngữ thứ mười) | **AI-assisted so với AI-generated** | AI-generated: AI quyết định. AI-assisted: designer quyết định, AI lắp ráp | AI soạn nháp. Designer kiểm tra. Designer quyết định |

Ba khái niệm phụ không đưa vào bảng: **model** là phần lõi phía sau một tool, **prompt** là thứ người dùng đưa cho AI, và **in-tool AI features** là các tính năng AI có sẵn trong design tool.

### 4.2 Worked example: one task, done twice

Ví dụ minh hoạ dùng một case hư cấu của chương trình.

*Case card (Kitchen Crate, hư cấu):* một app meal-kit theo gói đăng ký. Nhiều khách hàng mới tạm dừng sau hộp đầu tiên. Team muốn cải thiện onboarding. App có date picker chọn ngày giao, một màn hình menu và một bước thanh toán. Team nghi ngờ giá là lý do khách rời đi. Chưa có research nào được thực hiện.

- **Instruction 1 (mơ hồ):** "Làm sao để cải thiện onboarding cho app meal-kit của tôi?"
- **Instruction 2 (có cấu trúc, đính kèm case card):** "Chỉ dùng case card. Liệt kê năm điều quan trọng nhất bạn cần biết mà KHÔNG có trong đó, và nói vì sao mỗi điều quan trọng. Không đoán, không dùng kiến thức chung để lấp chỗ trống. Nếu chỗ nào chưa rõ, trả lời 'unknown'. Chỉ trả về danh sách."

**Quan sát điển hình.** Instruction 1 thường cho lời khuyên tự tin nhưng chung chung, và có thể nói về sản phẩm như thể đó là sự thật. Instruction 2 thường hỏi đúng những điều chỉ research hoặc business mới trả lời được.

**Diễn giải theo thuật ngữ.** Case card là **context**; "chỉ dùng case card" là **grounding**; lời khuyên tự tin của instruction 1 là rủi ro **hallucination**; câu trả lời "unknown" là lý do instruction 2 hữu ích. Cho phép AI trả lời "unknown" thường giúp giảm việc lấp chỗ trống bằng nội dung bịa; đây là giả định thực hành được kiểm nghiệm lại ở Activity 3 và 4, không phải kết quả đã được đo trong tài liệu này. Về **context window**: chỉ đưa những phần mà một bước cần. Về **agent**: AI coding tool tự thực hiện nhiều bước, nên cần kiểm tra các file đã bị sửa thay vì chỉ đọc câu trả lời.

### 4.3 Reuse rather than retype

Một cuộc hội thoại AI mới không biết gì về project. Trước khi mô tả project từ trí nhớ, cần đính kèm file đã lưu. Một instruction tốt gồm các thành phần: nêu rõ tài liệu cần dùng; yêu cầu một task duy nhất; quy định "chỉ dùng tài liệu này, nêu nguồn cho từng ý, trả lời 'unknown' nếu tài liệu không nói, chỉ trả về section của mình"; và nêu định dạng mong muốn. Cấu trúc này tương ứng với khung CARE của NN/g [8]; tổng quan rộng hơn về dùng AI trong UX có ở [9].

**Mẫu instruction:** "Tôi là UX designer đang làm [case trong một hoặc hai câu]. Đây là context file: [đính kèm product-and-users.md]. Chỉ dùng file này, hãy viết instruction nên dùng để nhờ bạn [task cụ thể]. Sau đó phản biện chính instruction đó: chỗ nào còn mơ hồ, chỗ nào có thể trả lời bằng cách đoán, và cần thêm gì để có thể nói 'unknown' thay vì đoán."

---

## 5. Data safety

Mục này là hướng dẫn thực tế, **không phải tư vấn pháp lý**; chính sách của công ty và luật địa phương là căn cứ quyết định.

### 5.1 Why it matters

PRD, design chưa phát hành, user research có tên người, file của client và số liệu tài chính thường là thông tin confidential hoặc nằm dưới NDA. Nhiều công ty giới hạn nhân viên được dùng AI tool nào. Ở Việt Nam, dữ liệu cá nhân được điều chỉnh bởi Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, do Quốc hội thông qua ngày 26 tháng 6 năm 2025 và có hiệu lực từ ngày 1 tháng 1 năm 2026 [10]. Nghị định 356/2025/NĐ-CP, ban hành ngày 31 tháng 12 năm 2025 và có hiệu lực cùng ngày với luật, quy định chi tiết việc thi hành luật và thay thế Nghị định 13/2023/NĐ-CP [11]. Tên, email, số điện thoại và bản ghi của người dùng đều là dữ liệu cá nhân. Văn bản hiện hành cần được kiểm tra trực tiếp hoặc hỏi công ty.

Dữ liệu đưa vào AI tool được xử lý thế nào còn tuỳ tool và gói sử dụng. Các nhà cung cấp AI tool lớn công bố cách tiếp cận hai lớp: ở gói consumer, người dùng có lựa chọn cho phép hay không cho phép dùng hội thoại để cải thiện model, và lựa chọn này có thể đi kèm thời hạn lưu trữ khác nhau; gói business, enterprise và API thường không dùng dữ liệu của khách hàng để train theo mặc định [12]. Cài đặt và điều khoản thay đổi thường xuyên, nên cần đọc trực tiếp trang data controls và điều khoản của tool đang dùng. Không nên mặc định rằng dữ liệu là private.

### 5.2 Three classes of material

| Nhóm | Ví dụ | Quy tắc |
|---|---|---|
| **Safe**: thông tin công khai, suy nghĩ của chính mình, case hư cấu | Trang giá công khai của một đối thủ; ghi chú về một app công khai; case card của chương trình | Dùng được với bất kỳ tool nào đã chấp nhận |
| **Ask first**: nội bộ nhưng không nhạy cảm | Ghi chú quy trình nội bộ; tóm tắt research chưa công bố và không có tên người | Chỉ dùng trong tool mà công ty đã duyệt |
| **Never in a public tool**: dữ liệu cá nhân, kế hoạch chưa phát hành, tài chính, tài liệu NDA | Transcript phỏng vấn có tên; danh sách khách hàng; spec chưa phát hành; ảnh chụp admin dashboard đang chạy thật | Không dán. Ẩn danh trước, dùng tool đã được duyệt, hoặc để ngoài |

### 5.3 Four habits before pasting

1. **Kiểm tra chính sách.** Nếu chưa có thì hỏi; còn phân vân thì không dán.
2. **Phân loại tài liệu** theo ba nhóm trên.
3. **Xoá thông tin định danh trước**, bằng find and replace trên máy của mình chứ không nhờ AI làm, vì khi đó dữ liệu đã được gửi đi. Ẩn danh không phải lúc nào cũng hoàn hảo.
4. **Giữ file confidential ngoài folder của tool**, vì AI coding tool hoặc agent đọc toàn bộ project folder.

Việc output của AI có được dùng cho công việc với client hay không, và quyền sở hữu thuộc về ai, tuỳ thuộc công ty và quốc gia. Nên ghi lại trong `case-log.md` những chỗ đã dùng AI.

Output của mục này là `00-context/data-rules.md`: ba dòng bằng lời của chính học viên (được dán gì, sẽ không dán gì, dùng tool nào cho việc gì), được viết trong Activity 2 ở buổi 2.

---

## 6. The workspace

### 6.1 File formats and location

- **Markdown (`.md`)** là tài liệu làm việc: plain text với vài ký hiệu đơn giản (`## Heading`, `**bold**`, danh sách `-`, bảng `|`), là định dạng phổ biến mà AI tool xử lý ổn định và dễ cung cấp có chọn lọc.
- **HTML** là phần trình bày, thứ browser hiển thị. Prototype do AI dựng và hub đều là file HTML. Designer giữ phần Markdown; khi stakeholder cần đọc, AI dựng page từ đó.
- **Local folder.** Case được giữ trong một folder local, không phải tài liệu trên cloud: AI coding tool mở cả folder làm project của nó và đọc mọi thứ bên trong, còn folder đồng bộ cloud có thể gặp lỗi khi đang ghi file. Folder lộn xộn cho output lộn xộn.

### 6.2 Case folder

```
[case-name]/
├── 00-context/          context pack: đưa vào các bước AI trước tiên
│   ├── product-and-users.md
│   ├── principle-checks.md          (viết ở module sau)
│   ├── design-system-notes.md       (thêm ở module sau)
│   ├── accessibility-rules.md
│   ├── data-rules.md
│   ├── my-direction.md              (viết ở buổi 2, xem lại ở tuần 7)
│   └── glossary.md                  (tuỳ chọn)
├── 01-discover/         một working file cho mỗi activity, cùng folder sources/
├── 02-define/           problem-brief.md
├── 03-develop/          options, alignment check, prototype/
├── 04-deliver/          test plan, findings, handoff
├── hub/                 Experience Hub: một trang HTML cho mỗi activity
└── case-log.md          mỗi quyết định một dòng, kèm lý do
```

Layout này phục vụ làm việc với AI vì: thư mục đánh số giữ thứ tự; mỗi activity một file cho mỗi bước AI một input có tên; `00-context` là thứ đưa vào đầu tiên ở mọi bước; file Markdown ngắn dễ cung cấp có chọn lọc.

### 6.3 Working-file rules

Mỗi activity điền vào một file Markdown, từng section một. Hai quy tắc giữ cho quy trình an toàn:

1. **AI chỉ trả về section của nó;** designer tự dán vào, để AI không âm thầm viết lại phần đã chốt.
2. **Bản nháp của AI và bản đã kiểm tra nằm ở hai section riêng.** Khoảng cách giữa hai bản chính là tỷ lệ lỗi của AI.

### 6.4 Experience Hub and sharing

Mọi output đi vào **Experience Hub**: một website nhỏ gồm các page liên kết, nằm trong case folder. Hub hoàn chỉnh là báo cáo cuối của chương trình; người đọc có thể bắt đầu từ bất kỳ quyết định thiết kế nào và lần ra nhu cầu, hypothesis, principle và test đứng sau nó. Mỗi module thêm một page.

**Hub mặc định là private.** Nó nằm trong case folder và không ai thấy được nếu người dùng không gửi. Để cho stakeholder xem, export trang Overview và các trang chính ra PDF, hoặc gửi folder hub dưới dạng file nén. Chỉ khi case được phép chia sẻ (case của chương trình, hoặc phiên bản đã làm sạch từ công việc thật) mới publish thành link trực tuyến trên GitHub. Người publish là người host và chịu trách nhiệm; GitHub Pages miễn phí cần repository public, đó là lý do công việc thật được giữ private. Hướng dẫn nằm trong `publish-guide.md`.

---

## 7. Session design

### 7.1 Structure

**Buổi 1 (teaching session, 90 phút).** Buổi dạy: trình bày ngắn, xen câu hỏi và trao đổi theo cặp. Không có file hay output mới; mọi output nằm ở buổi 2.

| Phase | Nội dung | Mục của tài liệu | Thời gian |
|---|---|---|---|
| 1 | Tương lai của nghề, ba hướng đi, trao đổi về hướng của mình, lập trường partner | 1, 2, 3.3 | 20 phút |
| 2 | Quy trình thiết kế cùng AI: mỗi stage gồm gì và AI hỗ trợ ở đâu (không đi vào từng method) | 3.1, 3.2 | 10 phút |
| 3 | Một task làm hai lần; thuật ngữ trong thực tế; Activity 1 | 4 | 19 phút |
| 4 | Data safety (trình bày và bài phân loại) | 5 | 12 phút |
| 5 | Tiếp theo là gì, hub, kết thúc phần trình bày (6 phút); hỏi đáp (15 phút) | 6.4, 10 | 21 phút |
| | **Tổng nội dung** | | **82 phút** |
| | Buffer, gồm phần nhắc chuẩn bị cho buổi 2 sau hỏi đáp | | 8 phút |

**Buổi 2 (practice session, 90 phút, khoảng ba ngày sau buổi 1).** Không có nội dung mới. Học viên làm việc trên case của chính mình trong breakout room 3 đến 4 người, có coaching.

| Phase | Nội dung | Mục của tài liệu | Thời gian |
|---|---|---|---|
| 6 | Check-in; viết hướng của mình; Activity 2 (data rules) | 2, 5 | 14 phút |
| 7 | File, folder và case folder | 6.1 đến 6.3 | 9 phút |
| 8 | Activity 3: dựng case folder | 6 | 40 phút |
| 9 | Activity 4: đọc chéo; xem một case folder trực tiếp | 4.3 | 16 phút |
| 10 | Kết thúc buổi và homework | 8 | 6 phút |
| | **Tổng nội dung** | | **85 phút** |
| | Buffer | | 5 phút |

Timing chưa được thử với một lớp thật.

### 7.2 Activities

**Warm-up: trao đổi về hướng của mình** (buổi 1, 3 phút, theo cặp, không có output). Mỗi người nói 30 giây: hướng đang nghiêng về và lý do. Không ai phải chọn dứt khoát.

**Activity 1: giải thích cho đồng nghiệp** (buổi 1, 4 phút, theo cặp, không có output). Mỗi người lấy hai thẻ thuật ngữ, giải thích từng thuật ngữ trong một câu kèm ví dụ từ case của mình; bạn cặp hỏi: "Từ điều đó, bạn sẽ làm khác đi điều gì?" `glossary.md` là tuỳ chọn, thực hiện ở homework.

**Bài phân loại dữ liệu** (buổi 1, 4 phút, theo cặp). Sáu thẻ: (1) trang giá công khai của một đối thủ, (2) transcript phỏng vấn có tên người tham gia, (3) ghi chú về một app công khai đang dùng, (4) một feature spec chưa phát hành, (5) danh sách email khách hàng, (6) ảnh chụp admin dashboard của công ty. Kết quả mong đợi: 1 và 3 là safe; 2, 4, 5 và 6 là never in a public tool (2 có thể thành safe sau khi ẩn danh; 6 tuỳ nội dung nhìn thấy được). Thảo luận khi có bất đồng.

**Activity 2: viết data rules** (buổi 2, 8 phút, cá nhân). *Mục đích:* áp dụng ba nhóm dữ liệu vào tài liệu thật của case. *Quy trình:* (1) 3 phút: liệt kê ba tài liệu thật của case (ví dụ một bản research, một feature spec, một transcript phỏng vấn) và xếp mỗi cái vào safe, ask first hoặc never in a public tool; (2) 5 phút: viết ba dòng vào `data-rules.md`; chỗ nào chưa biết chính sách của công ty thì ghi "cần hỏi". Học viên dùng case card của chương trình thì viết cho case card và viết lại cho case thật sau. *Output:* bản đầu của `data-rules.md`.

**Activity 3: dựng case folder** (buổi 2, 40 phút, cá nhân trong breakout room). *Mục đích:* dựng nền tảng mà cả chương trình chạy trên đó, và kiểm tra nó bằng một instruction giống instruction ở ví dụ 4.2. *Quy trình:*
1. (5 phút) Tạo case folder theo layout ở 6.2 và các subfolder; tên theo case, chữ thường, nối bằng dấu gạch ngang.
2. (10 phút) Bắt đầu context pack: viết phiên bản đầu của `product-and-users.md` (sản phẩm là gì, ai dùng, job chính của họ; nửa trang, đã ẩn danh); đưa `data-rules.md` từ Activity 2 vào. `accessibility-rules.md` được viết ở homework.
3. (5 phút) Copy folder template hub trống vào `hub/` và mở `index.html` trong browser; trang Overview hiển thị dữ liệu mẫu. Chưa chỉnh sửa gì.
4. (20 phút) Chạy một instruction với một file đã lưu. Đính kèm `product-and-users.md` vào AI chat tool và dùng: "Đây là context cho design case của tôi. Chỉ dùng file này. Liệt kê năm điều quan trọng nhất bạn cần biết về sản phẩm và người dùng mà KHÔNG có trong file, và nói vì sao mỗi điều quan trọng. Không đoán, không dùng kiến thức chung để lấp chỗ trống. Nếu chỗ nào chưa rõ, trả lời 'unknown'. Chỉ trả về danh sách." Đọc câu trả lời có phản biện: câu nào hữu ích, câu nào chung chung, câu nào tự tìm ra được; lưu những câu hữu ích vào `00-context/open-questions.md`.

*Output:* case folder, context pack đã bắt đầu, hub trống, `open-questions.md`. Học viên có công ty không cho phép AI tool, hoặc case quá nhạy cảm, dùng case card của chương trình cho bước 4.

**Activity 4: đọc chéo với bạn cặp** (buổi 2, 10 phút, theo cặp). *Mục đích:* nhìn file của mình qua mắt người không biết case, và dùng AI để chỉ ra chỗ còn thiếu. *Quy trình:* (1) 4 phút: đổi `product-and-users.md` đã ẩn danh; mỗi người đính kèm file của bạn cặp vào AI chat tool và chạy instruction ở bước 4 của Activity 3; (2) 4 phút: trao đổi với bạn cặp xem trong năm điều AI nói còn thiếu, điều nào thật sự thiếu và điều nào người viết trả lời được ngay trong một câu; (3) 2 phút: mỗi người ghi ba điều cần bổ sung. *Quy tắc dữ liệu:* chỉ đổi file đã ẩn danh và chỉ khi cả hai đồng ý; mỗi người dùng file của bạn cặp trong một cuộc hội thoại mới, không dán sang nơi khác, và đóng hoặc xoá cuộc hội thoại sau khi xong; học viên có case nhạy cảm dùng case card của chương trình cho activity này. *Ghi chú:* điều AI nói thiếu mà người viết trả lời được trong một câu cho thấy file còn chưa đủ chi tiết. *Output:* ba điều cần bổ sung vào `product-and-users.md`.

### 7.3 Participation

Học viên được khuyến khích ghi câu hỏi vào chat trong suốt buổi 1. Mười lăm phút cuối buổi 1 dành để trả lời các câu hỏi đó, ưu tiên những câu được nhiều người quan tâm; câu nào cần số liệu hoặc cần cân nhắc thêm được trả lời bằng văn bản sau buổi. Sau phần hỏi đáp là lời nhắc chuẩn bị cho buổi 2 (chọn và ẩn danh tài liệu của case, kiểm tra AI tool, giữa hai buổi chỉ dùng case card nếu muốn thử AI tool).

### 7.4 Preparation and materials

**Trước buổi 1** (khoảng 20 phút):
1. Mang một AI tool đã được công ty cho phép. Đọc handout về tool (`tools-to-bring.md`, khoảng 5 phút) và làm bài kiểm tra 5 phút trong đó. Cần một chat tool ngay, và một coding tool trước buổi 9 (tuần 5).
2. Đọc **pre-read brief** (khoảng 10 phút, xem Appendix A).
3. Chọn case: project, sản phẩm hoặc feature của chính mình, đã ẩn danh. Hub mặc định là private. Nếu công ty cấm AI tool hoặc case quá nhạy cảm để mang lên lớp, dùng case card của chương trình.
4. Nghĩ trước một câu hỏi: trong 12 tháng tới, mong muốn công việc khác đi ở điểm nào? Không cần có câu trả lời.
5. Tìm hiểu quy định của công ty về AI tool: có chính sách bằng văn bản không, tool nào được duyệt.

**Giữa hai buổi:** không có bài đọc mới. Chọn và ẩn danh tài liệu của case để dùng ở buổi 2, và kiểm tra lại AI tool. Nếu muốn thử AI tool, chỉ dùng case card của chương trình; chưa dán tài liệu thật của case vào AI tool trước khi viết data rules ở buổi 2.

**Tài liệu:** handout về tool (`tools-to-bring.md`), case card của chương trình (`course-case/case-card.md`), bộ thẻ thuật ngữ và sáu thẻ phân loại dữ liệu, template case folder và folder template hub trống, các method card, hướng dẫn publish (`publish-guide.md`).

---

## 8. Assessment and homework

### 8.1 Self-check questions

1. Chọn một stage: nêu một method, khi nào dùng, AI làm gì và designer vẫn làm gì.
2. AI-assisted khác AI-generated ở điểm nào?
3. Context window là gì, và khi tài liệu dài thì nên làm gì?
4. Vì sao nên cho phép AI trả lời "unknown"?
5. Agent làm được gì mà một câu trả lời chat không làm được, và sau đó cần kiểm tra gì?
6. Nêu hai thứ không nên dán vào một AI tool công khai, và việc cần làm trước khi dán một transcript phỏng vấn.
7. Vì sao hub mặc định là private, và khi nào có thể publish?
8. Nêu một con số về mức dùng AI của designer kèm nguồn, năm và cỡ mẫu, và nói con số đó không cho biết điều gì.
9. Nêu ba hướng đi nghề nghiệp, rồi với hướng mình nghiêng về, nêu một bằng chứng và một giới hạn của bằng chứng đó.
10. Trước khi mô tả project cho AI từ trí nhớ, cần làm gì? Một instruction tốt gồm những thành phần nào?

### 8.2 Homework (tối đa 45 phút, chỉ nối tiếp phần đã bắt đầu trên lớp)

**Assignment 1: case folder (bắt buộc, khoảng 25 phút).** Hạn: trước buổi đầu tiên của module tiếp theo. Phần lớn là bổ sung ba điều từ Activity 4 và dọn gọn. Sản phẩm gồm: case folder hoàn chỉnh theo layout chuẩn; `product-and-users.md` hoàn thiện (một trang: sản phẩm, người dùng, job chính, thành công có thể trông như thế nào, và những điều chưa biết); `accessibility-rules.md` (viết mới, các yêu cầu phải đáp ứng, vài dòng) và `data-rules.md` (ba dòng) hoàn thiện; hub trống đã copy vào `hub/`; `glossary.md` (tuỳ chọn). Nộp ảnh chụp cây folder và `product-and-users.md` để nhận feedback, sau khi ẩn danh mọi thông tin confidential. Tiêu chí: cấu trúc thật; `product-and-users.md` đủ cụ thể để người ngoài hình dung được người dùng; data rules bằng lời của chính học viên.

**Assignment 2: chia sẻ hub (tuỳ chọn, khoảng 20 phút).** Chọn một trong hai: (a) *Private:* export trang Overview của hub ra PDF và mở folder hub đã nén trên một thiết bị khác; (b) *Public, nếu case được phép chia sẻ:* làm theo `publish-guide.md` (tài khoản GitHub miễn phí, repository public, upload nội dung `hub/`, bật GitHub Pages, mở link trong cửa sổ ẩn danh). Người publish là người host và chịu trách nhiệm. Buổi live tiếp theo không phụ thuộc vào phần này.

---

## 9. Limitations and ethics

- **Thiên lệch của dữ liệu train.** AI tool phản ánh các pattern trong dữ liệu train, vốn nghiêng về phương Tây và tiếng Anh. Với người dùng Việt Nam hoặc Đông Nam Á, cần đối chiếu gợi ý với mental model của người dùng, không chỉ xem output có thuyết phục hay không.
- **Dữ liệu đưa vào có thể bị lưu lại.** Cần áp dụng data rules ở mỗi lần dùng.
- **Giới hạn của bằng chứng nghề nghiệp.** Xem mục 1.3. Các hướng đi ở mục 2 là xu hướng, không phải dự báo cá nhân.
- **Giới hạn của chương trình.** Chương trình không dạy thiết kế sản phẩm AI; chỉ cung cấp nền tảng cho hướng đó.
- **Thời gian trong thiết kế buổi học** chưa được kiểm chứng với lớp thật.

---

## 10. Connection to the series

| Module (tuần) | Vai trò |
|---|---|
| **Module này (tuần 1)** | Tương lai của nghề và ba hướng đi; bốn stage và các method; AI ở mức tổng quan; bộ từ vựng chung; data rules; case folder; hub trống; lập trường AI-assisted |
| Discover the Problem (tuần 2) | Lần đầu dùng case folder; bắt đầu từ câu hỏi của business; stakeholder check bằng văn bản; phỏng vấn user theo cặp; user-voice synthesis trên quote thật với quy tắc "unknown" |
| Frame the Problem Worth Solving (tuần 3) | Diễn giải findings và problem brief ở mức sâu; viết principle checks vào `00-context` và điền trang brief của hub |
| Explore Ideas (tuần 4) | Method brainstorm và select của Develop ở mức sâu; chọn một hướng; viết flows và content |
| Build Your First Prototype (tuần 5) | Thêm design system notes vào `00-context`; dựng prototype đầu tiên và điền hub |
| Refine and Test (tuần 6) | Refine, alignment check và usability test ở mức sâu; điền trang findings |
| Hand Off and Present (tuần 7) | Handoff pack, measurement plan và final project; hoàn thiện hub thành báo cáo cuối; xem lại `my-direction.md` đã viết ở tuần 1 |

---

## References

[1] Designer Fund và Foundation Capital. *AI in Design 2026* (khảo sát 906 designer, hơn 25 buổi phỏng vấn, 7 case study công ty, 2026). https://designerfund.com/blog/ai-in-design-2026

[2] Figma. *State of the Designer 2026* (906 digital designer, thực hiện cùng NewtonX, 2026). Báo cáo đầy đủ cần điền form miễn phí; tỷ lệ 36/35/29 được trích qua nguồn thứ cấp và cần xác nhận ở báo cáo gốc. https://www.figma.com/reports/state-of-the-designer-2026/

[3] Moran, K., Budiu, R., Gibbons, S. và các chuyên gia NN/g. *State of UX in 2026*. Nielsen Norman Group, 16/01/2026. https://www.nngroup.com/articles/state-of-ux-2026/

[4] U.S. Bureau of Labor Statistics. *Occupational Outlook Handbook: Web Developers and Digital Designers* (dự báo 2025 đến 2035; trang cập nhật 27/08/2026). https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm

[5] Adobe. *The Economic State of Creative Professions*, Edition 1, 06/2026 (bản tổng hợp số liệu BLS, gồm dự báo việc làm 2024 đến 2034; không bàn về tác động của công nghệ). https://www.adobe.com/cc-shared/assets/ai/research/adobe-ai-research-june-2026-economic-state-of-creative-professions.pdf

[6] Brynjolfsson, E., Chandar, B. và Chen, R. *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab, 13/11/2025 (dữ liệu bảng lương ADP). https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/

[7] Figma. *Design systems, AI and MCP* (blog). https://www.figma.com/blog/design-systems-ai-mcp/

[8] Nielsen Norman Group. *CARE: Structure for Crafting AI Prompts*. https://www.nngroup.com/articles/careful-prompts/

[9] Nielsen Norman Group. *Using AI for UX Work: Study Guide*. https://www.nngroup.com/articles/ai-work-study-guide/

[10] Quốc hội nước Cộng hòa xã hội chủ nghĩa Việt Nam. *Luật Bảo vệ dữ liệu cá nhân* số 91/2025/QH15, thông qua ngày 26/06/2025, có hiệu lực từ 01/01/2026 (toàn văn trên Thư viện Pháp luật). https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Bao-ve-du-lieu-ca-nhan-2025-so91-2025-QH15-625628.aspx

[11] Chính phủ. *Nghị định 356/2025/NĐ-CP* quy định chi tiết một số điều và biện pháp thi hành Luật Bảo vệ dữ liệu cá nhân, ban hành ngày 31/12/2025. https://english.luatvietnam.vn/decree-no-356-2025-nd-cp-dated-december-31-2025-of-the-government-detailing-a-number-of-articles-and-measures-for-the-implementation-of-the-law-on-p-422896-doc1.html

[12] Trang data controls và điều khoản dành cho người dùng của từng nhà cung cấp AI tool (nguồn gốc; cần đọc bản hiện hành của tool đang dùng). Danh sách các trang đã được đối chiếu và ngày kiểm tra nằm trong `programs/ai-design-workflow/04-future-of-design-careers.md`, mục 12.

Nhật ký bằng chứng đầy đủ, mức độ tin cậy từng con số và các nhận định chưa dùng nằm trong `programs/ai-design-workflow/04-future-of-design-careers.md`.

---

## Appendix A: Pre-read brief (khoảng 10 phút, đọc trước buổi 1)

Phần đọc tối thiểu trước buổi 1, theo thứ tự:

1. **Mục 3.1 và 3.2:** bảng bốn stage, method và phân chia giữa AI với designer (khoảng 4 phút).
2. **Mục 4.1:** mười thuật ngữ (khoảng 3 phút).
3. **Mục 6.2:** layout case folder (khoảng 1 phút).
4. **Mục 2:** ba hướng đi nghề nghiệp, để chuẩn bị cho phần trao đổi ở buổi 1 (khoảng 2 phút).

Không cần đọc hết các method card trước buổi học; có thể lướt những card của method ít dùng nhất.

---

*Created by Winnie Nguyen · AI Design Workflow · Last updated October 2026*

# VI_VOICE: Quy tắc viết tiếng Việt của Winnie

File chuẩn cho mọi nội dung tiếng Việt trong thư mục này: lesson, slide outline, teleprompter, method card, recap session, tài liệu gửi mentee và học viên. Quy tắc được rút ra từ transcript các buổi mentoring của Winnie và từ chính những chỗ Winnie sửa khi review (2026-10-06).

Ví dụ áp dụng thực tế: `programs/ai-design-workflow/voice-sample-vi.md` (bản thử, bảng trước và sau, một method card hoàn chỉnh).

## Thứ tự ưu tiên khi có mâu thuẫn

1. **File này thắng** về giọng văn, từ vựng, nhãn trên slide và quy ước ngôn ngữ.
2. `programs/online-course/AI Prototype Development/writing-style-guide.md` vẫn là nguồn cho cấu trúc riêng của khoá đó (format teleprompter, cấu trúc Practice/Bài Tập, format outline của khoá). Chỗ nào mâu thuẫn với file này thì theo file này.
3. Các quy tắc trong `CLAUDE.md` luôn còn hiệu lực: sync lesson và slide outline, không dùng tên tool AI cụ thể, không nhắc tên mentee trong lesson.

## Ngôn ngữ của file làm việc (quyết định 2026-10-11)

Winnie dạy bằng tiếng Việt và mentee là người Việt, nên tài liệu chuẩn bị viết bằng tiếng Việt.

| Loại file | Ngôn ngữ |
|---|---|
| Lesson và slide outline mới | Tiếng Việt: tiêu đề, Kicker, tên mục bằng tiếng Anh, nội dung bằng tiếng Việt. Dùng skill `vi-voice`, và `vietnamese-copy-polish` để kiểm tra lần cuối chữ trên slide |
| Lesson cũ đang viết bằng tiếng Anh | Giữ nguyên cho đến khi Winnie yêu cầu viết lại |
| Prep note, recap session, close-out recap (private) | Tiếng Việt, tiêu đề mục bằng tiếng Anh theo template |
| Playback, tin Zalo, homework gửi mentee | Tiếng Việt |
| Tin trả lời lead, tin nhắc việc | Theo ngôn ngữ người nhận |
| Tên file, folder, slug, khoá front matter, tag WF-4, lệnh | Luôn tiếng Anh (script đọc các phần này) |

## Giọng văn

Viết như một đồng nghiệp có kinh nghiệm chia sẻ cách làm với đồng nghiệp: gần gũi, rõ ràng, đi thẳng vào ý. Gần gũi nhưng vẫn chuyên nghiệp, đủ để đưa vào tài liệu chính thức hoặc slide deck.

- Ví dụ cụ thể trước, khái niệm sau.
- Câu ngắn, mỗi câu một ý. Hai câu đã tự nối ý thì không cần từ nối.
- Cần nối ý thì dùng "vì vậy", "do đó".
- Ví von đời thường khi giải thích khái niệm khó. Ví dụ đã dùng: MCP giống một cái USB, cắm giữa file design và AI tool.
- Ngôi xưng: "mình" cho cả nhóm và trong speaker notes; "bạn" khi nói trực tiếp với học viên. Không trộn hai ngôi trong cùng một câu.
- Em dash, nhịp staccato và các quy tắc dấu câu khác: theo `writing-style-guide.md`.

## Văn bản dạng paper (file lesson để chia sẻ với partner và học viên)

Từ 2026-10-07, file `*-lesson.md` được viết như một paper hoặc bản research, không phải kịch bản giảng. Quy ước:

- Giọng khách quan, không dùng "bạn", "mình", không có câu mệnh lệnh như "hãy", "đừng". Gọi người học là "học viên" hoặc "designer".
- Có Abstract, Background, Limitations, References. Mỗi số liệu ghi nguồn, năm, cỡ mẫu và đánh số trích dẫn [n].
- Tách rõ phát hiện (từ nguồn) và suy luận (của tác giả).
- Không có kịch bản từng phase, lời nhắc cho giảng viên, thứ tự cắt khi quá giờ. Phần giảng nằm trong speaker notes của slide outline. Bản cũ có kịch bản nằm ở `materials/_archive/`.
- Slide outline vẫn dùng giọng "mình" trong speaker notes như quy ước ở trên.

## Bỏ khỏi văn bản chính thức

Đây là cách nói khi giảng trực tiếp. Giữ chúng ở lời nói, không đưa vào tài liệu.

| Bỏ | Ví dụ |
|---|---|
| Chữ đệm khi nói | "thì á", "thì là", "cho nên là", "tại vì", "nói chung là", "ờ" |
| Từ cuối câu | "ha", "nha", "đúng không", "hả" |
| Câu nối rỗng | "có nghĩa là", "kiểu như" |
| Câu hỏi đuôi, câu cảm thán | "Nhớ nha!", "Đúng rồi!" |
| Lặp "cái" trước mỗi danh từ | "cái folder", "cái prototype" → "folder", "prototype" |

## Cụm dịch từ tiếng Anh cần tránh

| Tránh | Dùng |
|---|---|
| đánh trọng số | xếp theo mức độ quan trọng |
| chốt phase, chốt câu | kết lại, nhấn mạnh |
| phần của bạn | phần bạn vẫn tự làm |
| AI hỗ trợ ở đâu | AI giúp được ở đâu |
| draft (động từ) / (danh từ) | soạn nháp / bản nháp |
| verify | kiểm tra |
| con trỏ về | trích dẫn, dẫn chiếu |
| ứng viên (candidate) | tiềm năng; hoặc "để bạn kiểm tra lại" |
| làm mượt | làm mờ |
| đào sâu | hỏi sâu, đi sâu vào |
| kiểm tra chéo | đối chiếu |
| anonymise | ẩn danh |
| rút gọn mạnh nhất | thu hẹp nhanh nhất |
| tránh tốn | không uổng phí |
| show (chiếu) | chiếu, trình bày |

## Quy ước ngôn ngữ

| # | Quy tắc | Ví dụ |
|---|---|---|
| 1 | **Tiêu đề bằng tiếng Anh, nội dung bằng tiếng Việt.** Tên lesson, cover, header slide, Kicker, Title để tiếng Anh. On-slide và speaker notes bằng tiếng Việt | Title: "Your Design Process, with AI" |
| 2 | **Nhãn trên slide method bằng tiếng Anh:** What, Why, When, Where AI helps. Nội dung sau nhãn bằng tiếng Việt | "What: Đọc những gì product đã có…" |
| 3 | **Không ghi thời lượng trên slide.** Section divider không có dòng Sub chứa số phút. Thời gian chỉ nằm trong speaker notes và trên slide `MILESTONE` của activity | |
| 4 | **Giữ thuật ngữ nghề bằng tiếng Anh**, không dịch | business question, constraints, assumptions, support tickets, data analytics, existing research, user need, opportunity statement, live traffic, shortlist, sticky note, topic, item, group, cluster, interview guide, desk research, stakeholder interview, insight, deliver, context, folder, prototype, design system, handoff |
| 5 | **Dùng "group", "topic", "item", "sticky note"** thay vì dịch | "group các câu trả lời thành các topic" |
| 6 | **Mỗi dòng trên slide là một cụm ngắn,** đọc được trong một cái nhìn. Không câu nào quá khoảng 15 từ | "Không uổng phí buổi phỏng vấn cho những điều team đã biết" |
| 7 | **Why mở đầu bằng lợi ích cụ thể** (không uổng phí, thấy, biết, tránh) | Why: "Không uổng phí…" |
| 8 | **When ghi thời điểm hành động** | When: "Thực hiện sớm, trước primary research" |
| 9 | **Where AI helps nêu việc AI làm cụ thể**, không nêu chung chung | "Soạn nháp các item cần quan sát, và giúp sắp xếp lại sticky note" |
| 10 | **Slide và card tương ứng phải khớp nhau.** Sửa một bên thì sửa bên còn lại | |

## Trước và sau

**Lập trường của series**
- Trước: "Và một designer ngồi đợi PRD rồi biến nó thành screen là người dễ bị ảnh hưởng nhất, vì đó chính là bước AI rút gọn mạnh nhất."
- Sau: "Nếu chỉ đợi PRD rồi biến nó thành screen, bạn đang đứng đúng chỗ AI làm nhanh nhất. Nếu cùng business định nghĩa requirement ngay từ đầu, bạn làm phần AI không thay được: chọn vấn đề đáng giải và thống nhất thế nào là thành công."

**Câu hỏi lặp lại**
- Trước: "AI hỗ trợ ở đâu, và phần nào vẫn là của bạn?"
- Sau: "AI giúp được ở đâu, và đâu là phần bạn vẫn phải tự làm?"

**Dòng một câu**
- Trước: "AI draft. Bạn verify. Bạn quyết định."
- Sau: "AI soạn nháp. Bạn kiểm tra. Bạn quyết định."

**Giải thích khái niệm**
- Trước: "Một cách chuẩn để AI tool đọc một app khác, ví dụ file design của bạn."
- Sau: "Giống một cái USB: cắm giữa file design và AI tool để AI đọc được thứ bạn đang làm. Trước khi kết nối, hãy biết nó đọc và sửa được những gì."

**Xếp findings**
- Trước: "Đánh trọng số cho findings theo mức độ quan trọng, không theo tần suất."
- Sau: "Xếp findings theo mức độ quan trọng, không theo số lần được nhắc. Một vấn đề chỉ một người gặp nhưng khiến họ bỏ dở task vẫn quan trọng hơn một lỗi nhỏ có năm người cùng phàn nàn."

**Điểm chung của cả series**
- Trước: "Sợi chỉ đỏ ở mọi stage là AI-assisted, không phải AI-generated."
- Sau: "Điểm xuyên suốt ở mọi stage là AI-assisted, không phải AI-generated."

**Các dòng Winnie sửa trực tiếp trên slide**

| Trường | Trước | Sau |
|---|---|---|
| What (Desk research) | Đọc những gì đã có: analytics, ticket, nghiên cứu cũ, review | Đọc những gì product đã có: data analytics, support tickets, existing research, reviews |
| Why (Desk research) | Tránh tốn buổi phỏng vấn cho điều team đã biết | Không uổng phí buổi phỏng vấn cho những điều team đã biết |
| When (Desk research) | Sớm, trước primary research | Thực hiện sớm, trước primary research |
| What (Stakeholder meetings) | Các buổi trao đổi có cấu trúc với product, business, engineering | Structured discussions với product, business và engineering |
| Why (Stakeholder meetings) | Làm rõ câu hỏi của business, ràng buộc và giả định | Làm rõ business question, constraints và assumptions |
| What (Questionnaire) | Bộ câu hỏi cố định gửi cho nhiều người | Bộ câu hỏi gửi cho nhiều người để thu về các câu trả lời phù hợp |
| Where AI helps (Questionnaire) | Soạn nháp câu hỏi trung lập; nhóm câu trả lời mở thành theme | Soạn nháp câu hỏi và group các câu trả lời thành các topic |
| What (User interviews) | Trò chuyện một-một bằng câu hỏi mở | Trò chuyện một-một với các câu hỏi mở và đi sâu vào các vấn đề |
| Where AI helps (Observation) | Soạn nháp bảng quan sát; dọn field notes | Soạn nháp các item cần quan sát, và giúp sắp xếp lại sticky note từ những gì bạn ghi nhận |

## Kiểm tra trước khi giao

1. Tìm các chữ đệm trong bảng "Bỏ khỏi văn bản chính thức". Không còn chữ nào.
2. Tìm các cụm trong bảng "Cụm dịch từ tiếng Anh cần tránh". Không còn cụm nào.
3. Đọc to vài câu. Một designer Việt Nam có nói câu này khi làm việc không, hay nó chỉ đúng khi dịch ngược sang tiếng Anh? Nếu là vế sau, viết lại quanh ý chính.
4. Tiêu đề, Kicker và nhãn đúng quy ước ngôn ngữ ở trên; không còn số phút trên slide.
5. Slide và card (hoặc lesson và slide outline) đã khớp nhau.
6. Không có tên tool AI cụ thể, không có tên mentee (theo `CLAUDE.md`).
7. Winnie tự đọc lại. Câu nào Winnie sửa, thêm vào bảng "Các dòng Winnie sửa trực tiếp" để lần sau áp dụng đúng.

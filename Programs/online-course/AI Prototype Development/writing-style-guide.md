# Voice & Writing Style Guide — AI Prototype Development Course

Quy tắc viết Vietnamese lesson content, slide outline, và teleprompter script cho khoá học AI Prototype Development (và có thể áp dụng cho các nội dung mentoring khác của Winnie). File này là nguồn tham chiếu chính khi viết hoặc chỉnh sửa `*-lesson.md`, `*-slide-outline.md`, hay teleprompter script.

---

## Nguyên tắc chung

Viết như một Product Designer có kinh nghiệm đang nói chuyện với một Product Designer khác, một người đồng nghiệp chia sẻ cách làm tốt hơn, không phải AI giải thích công nghệ cho người mới. Trước khi chốt một câu, tự hỏi: "Product Designer thật sự cần hiểu gì ở đây? Điều gì giúp họ làm việc tốt hơn với AI? Có thể nói ngắn và tự nhiên hơn không?"

**Tone:** tự nhiên, human, rõ ràng. Có chuyên môn nhưng không corporate. Có chiều sâu nhưng không academic trừ khi chủ đề bắt buộc. Câu ngắn, có nhịp, dễ đọc khi lên slide. Dùng đúng từ vựng Product Designer thật sự dùng khi làm việc, không phải câu dịch từ tiếng Anh.

**Ngôi xưng (cập nhật 2026-08-18, pass 2):** "mình" là ngôi mặc định xuyên suốt Ghi chú thuyết trình, không chỉ ở những câu đang kể lại một bước cụ thể — gần như mọi câu trần thuật/giải thích trong Ghi chú thuyết trình nên dùng "mình" ("mình sẽ...", "mình muốn...", "mình rất thích cách nghĩ này"), trừ khi đang trích lời tưởng tượng của học viên hoặc hỏi ngược lại họ. Vẫn gọi học viên là "bạn" khi nói trực tiếp với họ trong Lead, Nội dung, hay prompt mẫu. Hai ngôi này song song theo field (Ghi chú thuyết trình = mình, Lead/Nội dung/prompt = bạn), không trộn trong cùng một câu.

Khi chỉnh sửa outline hay nội dung thô Winnie đưa:
1. Giữ nguyên ý cốt lõi và cấu trúc, không tự ý tái cấu trúc.
2. Không mở rộng thành giải thích dài. Đừng cố "thêm cho nhiều".
3. Làm câu chữ tự nhiên hơn, dễ đọc thành tiếng khi thuyết trình.
4. Ưu tiên rõ ràng hơn số lượng chữ.
5. Nếu có một insight chính, cô đọng nó thành một câu ngắn, dễ nhớ.
6. Nếu câu nào đọc lên nghe máy móc, viết lại theo cách một Product Designer thật sự sẽ nói với đồng nghiệp.

**Cụm từ chung chung/marketing bị cấm** (rewrite ngay khi thấy): "Trong thời đại AI...", "Điều này giúp tối ưu hóa quy trình...", "Mang lại trải nghiệm tốt hơn...", "Tận dụng sức mạnh của AI...". Đừng giải thích điều một Product Designer đã biết sẵn, đừng biến mọi thứ thành "framework", đừng làm nội dung nghe hay hơn bằng cách làm nó dài hơn.

**Không so sánh với "khoá học khác trên thị trường".** Khi cần đối lập cách tiếp cận (ví dụ vibe coding vs. pattern-first), so sánh với một *cách làm/phương pháp phổ biến* chung chung, không nhắm vào khoá học, sản phẩm, hay tên cụ thể nào khác.

---

## Không trích số Lesson/Section khác

Không bao giờ nhắc số thứ tự của một Lesson hay Section khác trong nội dung (Lead, Nội dung, Ghi chú thuyết trình, prose, worksheet) — kể cả khi có kèm giải thích ngay sau số đó. Học viên (và cả giáo viên khi đọc lại Ghi chú thuyết trình) không nhớ số, nên con số không mang nghĩa, chỉ tạo cảm giác phải "tra lại". Thay số bằng một trong hai cách:
- Tên nội dung cụ thể, nếu nội dung đó đã có tên riêng dùng xuyên khoá học (ví dụ "track Claude Design" thay vì "ở Section 3", "phần thực hành trước đó" thay vì "Practice 3, Section 2").
- Một cụm từ chung chung nếu không có tên riêng: "trước đó", "phần trước", "phần sau", "phần tiếp theo", "lesson này", "lesson sau".

**Ngoại lệ — giữ nguyên vì đây là nhãn "bạn đang ở đâu", không phải yêu cầu nhớ lại nội dung khác:** frontmatter/title tài liệu (`title: "Section 4: ..."`), header chia lesson (`### Lesson 1: ...`, `## 2. Lesson 1: ...`), footer (`· Section 4`), và Kicker tự giới thiệu section hiện tại (`Kicker: Section 4 · ...`).

Áp dụng như nhau cho cả `*-lesson.md` và `*-slide-outline.md`, không phân biệt file, không phân biệt backward hay forward reference.

---

## Từ vựng: tiếng Anh cho thuật ngữ kỹ thuật

Giữ tiếng Anh cho thuật ngữ kỹ thuật/domain (prototype pattern, component inventory, template, token, MCP, AI coding tool...), và mở rộng sang cả động từ/danh từ thông thường mà Product Designer hay nói tiếng Anh ngoài đời: "fix", "reuse", "variant", "workflow", "maintain", "outdated", "source (of truth)", "browser", "navigation", "system", "execution", "scale", "journey", "flow", "fidelity", "research", "states", "standards". Khi phân vân, để nguyên từ tiếng Anh nếu đó là từ một Product Designer Việt Nam thật sự nói ra miệng khi làm việc.

**Tên tool AI cụ thể:** mặc định toàn khoá học là generic ("AI chat tool", "AI coding tool", "your AI tool"), không nêu tên Claude/Cursor/ChatGPT/Copilot. Ngoại lệ: slide "Tools you'll use" (nêu tên thật để học viên chọn tool), Section 3 trọn vẹn (cập nhật 2026-08-18) — section này cam kết dùng đúng Claude Design làm ví dụ xuyên suốt (Design System file, Pages, Templates, CLAUDE.md, Claude Design nói thẳng tên), vì đây là 1 trong 2 track công cụ chính thức của khoá học — và Section 5 trọn vẹn (cập nhật 2026-08-19) — section này dùng Claude Code làm ví dụ chính xuyên suốt (MCP, CLAUDE.md, GitHub, Vercel), Cursor được ghi chú tương đương ở những chỗ tên gọi khác nhau (`.cursor/rules` thay CLAUDE.md, Dev Mode MCP Server thay plugin). Mỗi ngoại lệ phải ghi rõ phạm vi (1 slide, "toàn bộ Section 3", hoặc "toàn bộ Section 5"), không tự ý mở rộng ra chỗ khác hay đảo ngược lại thành generic nếu chưa được Winnie đồng ý.

**Punchline tiếng Anh trong Ghi chú thuyết trình (cập nhật 2026-08-18, pass 2):** ngoài thuật ngữ kỹ thuật, một câu chốt/aphorism tiếng Anh ngắn được phép xuất hiện nguyên văn trong Ghi chú thuyết trình khi đó là cách nói tự nhiên nhất và có nhịp landing rõ ("Garbage in, garbage out.", "Relevant context, not maximum context.", "Don't prompt because you can, prompt because you know what needs to change."). Không áp dụng cho Lead/Nội dung/Title — những field đó vẫn ưu tiên tiếng Việt, chỉ giữ tiếng Anh cho thuật ngữ.

---

## Dấu câu và cấu trúc câu

Em dash ("—") được dùng lại có chủ đích từ Section 4 trở đi, cho một aside ngắn hoặc câu chuyển ý/tương phản, dùng tiết chế, không dùng cho mọi cấu trúc appositive. (Quy tắc cũ "không bao giờ dùng em dash" đã bị thay thế, đừng quay lại áp dụng rule cũ.)

**Nhịp staccato:** một câu ngắn một đoạn, có chủ đích, đặc biệt ở những khoảnh khắc cần "landing" (payoff, cảnh báo, reveal). Không phải tối thiểu hoá số chữ trong một dòng, nếu một ý cần một câu đầy đủ, cứ viết đầy đủ, không cắt thành fragment cụt để cho ngắn.

**Danh sách ngắn song song** nên viết thành bullet list thật, kể cả trong lời thuyết trình, không lặp fragment giả-staccato kiểu "Là X.\nLà Y.\nLà Z."

**Ẩn dụ** dùng khung mời gọi, không phải phương trình cộc lốc: "Hãy nghĩ về X như một Y" thay vì "X là Y."

**Kết nối câu mềm hơn:** ưu tiên "có thể", "khá", "vì vậy" trước hệ quả, thay vì khẳng định cộc.

---

## Slide title / kicker / subtitle

1. Mỗi fragment phải mang nghĩa cụ thể, độc lập. Không viết fragment kiểu meta chung chung ("Trong section này", "Làm 1 lần.").
2. Kicker là nhãn ngắn, không phải câu mô tả: "Checkpoint 1", "Build Phase", không phải "Điểm dừng tự kiểm tra, không nộp bài".
3. Title/Subtitle mô tả kết quả/sự chuyển đổi cụ thể, không phải số liệu thô: "5 quy tắc giúp AI tạo prototype chính xác hơn", không phải "5 quy tắc. AI cần cả 5."
4. Dùng động từ tự nhiên, không viết tắt kiểu nói ("Rà" → "Kiểm tra", "Áp" → "Áp dụng").
5. Danh từ tool/kỹ thuật viết tiếng Anh, Title Case, như proper noun (MCP, Rules File, AI Coding Tool, Checkpoint N).
6. Slide so sánh nên viết dạng câu hỏi: "AI Coding Tool hay AI Design Tool?" Nội dung so sánh nên dùng dữ liệu thật song song cho từng cột khi có (ví dụ tên gọi thật của từng track: "Design System file / Pages / Templates / CLAUDE.md" cột Claude Design so với "Make kit / Guidelines.md / Prompt build" cột Figma Make), không dừng ở phạm trù trừu tượng ("không đổi" / "tuỳ tool") nếu có thể liệt kê cụ thể hơn (cập nhật 2026-08-18, pass 2).
7. Danh sách bước liên tiếp giữ cấu trúc Verb + Noun song song, có thể dùng danh từ tiếng Anh làm object.
8. Cắt bớt từ đệm không mang nghĩa thật ("file Figma thật" → "file Figma của bạn").
9. Title hai nhịp viết thành hai dòng bold riêng: "**Cùng một công thức.**\n**Khác nhau ở cái bếp.**", không gộp một dòng.

Test cuối cùng trước khi chốt bất kỳ field nào trên slide: một người làm khoá học Việt Nam có thật sự nói câu này không, hay nó chỉ có nghĩa vì đang "dịch từ cấu trúc tiếng Anh"? Nếu là vế sau, viết lại quanh ý nghĩa cốt lõi.

---

## Format cho slide outline

**Cập nhật (2026-08-18):** thay thế cách trình bày cũ (field gói trong 1 dòng bullet, Ghi chú thuyết trình chỉ 1 câu note). Convention H3-riêng-cho-Ghi-chú-thuyết-trình dưới đây áp dụng từ Section 4 trở đi — đừng quay lại format cũ cho những section đó.

**Ngoại lệ áp dụng sớm hơn (cập nhật 2026-08-18, pass 2):** dù Section 3 vẫn giữ format field-trong-1-bullet cũ (không chuyển sang H3 riêng), pattern số bước `**01 · Tên bước**` bên dưới áp dụng ngay cả trong format cũ, cho bất kỳ danh sách bước/checklist/process nào — không cần đợi tới Section 4. Ghi chú thuyết trình trong format cũ vẫn có thể viết nhiều dòng, nhịp staccato, ngôi "mình", miễn nằm gọn trong 1 bullet `- Ghi chú thuyết trình:` với các dòng con thụt lề, không cần tách H3.

- Giữ nguyên nhãn loại slide: SECTION, STATEMENT, PROCESS, TABLE, PROMPT, PRACTICE, END. Không tự chế nhãn mới (ví dụ đừng bịa ra "BRANCH").
- Giữ nguyên tên field: Kicker, Title, Sub/Lead, Loại visual.
- Cách dòng đôi giữa các nhóm ý, mỗi slide cách nhau bằng `---`.

**Cấu trúc heading:** H1 cho từng nhóm lesson/section trong outline (`# 1. Cover & Roadmap`), H2 cho tên từng slide (`## COVER`, `## PROCESS - Tên slide`), H3 riêng cho Ghi chú thuyết trình (`### Ghi chú thuyết trình`) đặt ngay dưới phần field của slide đó.

**Field của slide** viết dạng bullet đậm tên field: `- **Kicker:** ...`, `- **Title:** ...`.

**Bước/process liên tiếp** viết dạng số đậm + gạch giữa + nhãn ngắn, xuống dòng mô tả bên dưới: `**01 · Tên bước**` rồi 1 dòng giải thích. Không dùng lại lối cũ gộp "(1) X. (2) Y." trong 1 dòng.

**Ghi chú thuyết trình** là 1 subsection riêng (`### Ghi chú thuyết trình`), không còn gói trong 1 bullet. Viết như một đoạn thoại thật — nhiều câu ngắn, nhiều đoạn, có thể trích lời tưởng tượng của học viên hoặc stakeholder trong ngoặc kép ("Ừ, cũng được mà."), kết ở một câu chốt in đậm. Nguyên tắc nội dung không đổi: nói rõ cần nhấn gì, nối lại phần nào trước đó, minh hoạ bằng ví dụ gì, và insight chính học viên cần mang theo — chỉ khác là được viết dài hơn, gần với văn nói thật hơn là ghi chú tóm tắt.

**Lead** vẫn trả lời: điều gì đang xảy ra, vì sao Product Designer nên quan tâm, cần nhớ điều gì — nhưng giờ được phép viết bằng nhiều đoạn ngắn (1-3 câu/đoạn) thay vì chỉ gói trong 3-5 bullet.

**Bold** dùng rộng hơn trước: không chỉ ở title, mà đánh dấu câu chốt/payoff line ngay trong Lead và Ghi chú thuyết trình, để người đọc lướt vẫn bắt được ý chính.

**Blockquote (`>`)** dùng cho ví dụ prompt viết sẵn, và cho câu thoại trích dẫn (phản ứng tưởng tượng của học viên/stakeholder) khi cần minh hoạ giọng điệu thật.

---

## Format cho teleprompter script

Header chuẩn cho mọi teleprompter script:

> Đọc như đang nói chuyện trực tiếp với người học. Không cần đọc đều từng câu. Một số câu ngắn được tách riêng để tạo nhịp khi nói. Các dòng `[Slide X — ...]` chỉ là mốc để lật slide, không đọc thành tiếng.

- Slide marker không bold: `[Slide 1 — Cover]`, không phải `**[Slide 1 — Cover]**`.
- Stage direction/khoảng lặng dùng ngoặc vuông: `[Dừng một nhịp.]`, không dùng ngoặc đơn in nghiêng.
- Dấu "..." đánh dấu điểm dừng giữa ý, khi người nói tiếp tục cùng một mạch (khác với dấu chấm, là dừng hẳn, sang ý mới). Dùng khi liệt kê ví dụ/điều kiện từng cái một, hoặc khi build up tới một payoff line.
- Câu hỏi tu từ có thể lồng vào như suy nghĩ thầm của học viên ("mình nên bắt đầu từ đâu?"), dùng tiết chế.
- Liệt kê 3 phần trong lời thuyết trình dùng "Thứ nhất... / Thứ hai... / Và thứ ba...", không phải "Một / Hai / Ba" trần trụi (xem ngoại lệ bên dưới cho Practice script).
- Có thể thêm câu bridge/transition ngắn không có trong lesson.md gốc, để làm rõ chuyển ý khi nói thành tiếng.
- Một beat tóm tắt có thể tách thành hai dòng cực ngắn để tạo hiệu ứng landing ("Một lần.\nRồi sử dụng lại.").
- Sau một stage direction/khoảng lặng, nối lại bằng một cụm mềm ("Mà là...") trước khi vào payoff line, đừng nhảy thẳng vào câu chốt.
- Một beat xây dựng luận điểm thường cần một dòng closing, diễn lại insight chính bằng lời cụ thể hơn, không kết thúc ngay sau điểm hỗ trợ cuối.

---

## Riêng cho Practice / Bài Tập script (khác lesson content thường)

1. **Luôn mở đầu bằng một câu hook**, trước khi vào hướng dẫn. Hook có thể: (a) nói rõ bài tập này giúp ích gì cho phần sau ("Bài tập này sẽ có ích ngay cho phần tiếp theo, khi AI bắt đầu tham gia"), (b) hạ áp lực để học viên không ngại làm ("Đây là điểm dừng tự kiểm tra, không phải bài nộp, nên cứ thoải mái"), hoặc (c) cả hai, cộng thêm một lời mời hành động ("Khoan đã, đừng vội nhảy ngay vào setup kỹ thuật").
2. **Một câu punchline/khẩu ngữ có thể thay cho một dòng hướng dẫn khô khan**, đặt ngay trước bước dễ gây nản nhất. Ví dụ đã duyệt: "File quá lớn, rà bằng mắt muốn xỉu? Dùng đúng prompt gợi ý vừa rồi, để AI rà giúp." Dùng tiết chế, tối đa một lần mỗi script.
3. **Câu kết nói lại đúng MỘT kết quả tối thiểu cụ thể**, không phải tóm tắt lại toàn bộ bước. Ví dụ: "Kết quả tối thiểu, chỉ cần đúng một thứ: một file Figma đã dọn dẹp, sẵn sàng để AI đọc, không phải đoán."
4. **Bước đánh số nói "Một, [nhãn ngắn]. [hướng dẫn]."**, nhãn đóng vai trò như tiêu đề phụ nói ra miệng, không phải "Bước 1:" hay số trần trụi. Ví dụ: "Một, token. Xem lại hai tới ba screen, liệt kê bảng màu..."
5. **Số thứ tự bài tập có thể tính dồn qua nhiều section**, không phải reset theo từng section riêng. Nếu không chắc cách đánh số, hỏi lại thay vì tự đoán.

---

## Cách nhận feedback hiệu quả nhất

Ví dụ before/after cụ thể lấy trực tiếp từ văn bản luôn hữu ích hơn mô tả trừu tượng ("làm tự nhiên hơn"). Khi Winnie sửa một đoạn cụ thể, đó là tín hiệu tốt nhất để cập nhật quy tắc, vì cho thấy đúng pattern thật, thay vì phải đoán ý.

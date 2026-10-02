# Teleprompter — Lesson 3: Cách Khóa Học Được Tổ Chức

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 9 — Lesson 3 divider]**

Đây là lesson cuối cùng của phần giới thiệu.

Ở đây, mình muốn cho các bạn một overview về toàn bộ khóa học.

Để từ bây giờ, các bạn luôn biết mình đang ở đâu trong journey.

Và biết điều gì sẽ xảy ra tiếp theo.

Khóa học gồm bốn section.

Và chúng đi theo đúng cách một prototype thật sự được xây dựng.

Từ tư duy, đến system, đến build, rồi hoàn thiện thành một journey có thể demo.

**[Slide 10 — Section 2: Pattern-first thinking]**

Ở phần tiếp theo, các bạn sẽ hiểu vì sao cách làm screen-by-screen dễ bắt đầu bị rạn nứt khi project lớn dần.

Sau đó, các bạn sẽ sử dụng AI chat tool để tạo ra một prototype pattern cho chính project của mình.

Phần này có hai phần nhỏ.

Đầu tiên là hiểu cách tư duy pattern-first.

Sau đó là thực hành tạo prototype pattern bằng một chuỗi prompt cụ thể.

**[Slide 11 — Section 3: Build & refine]**

Đây là phần lớn nhất của khóa học.

Các bạn sẽ bắt đầu bằng việc chuẩn bị và dọn dẹp file Figma.

Sau đó kết nối AI coding tool với Figma.

Và bắt đầu build từng màn hình dựa trên prototype pattern vừa tạo.

Build.

Review.

Tinh chỉnh.

Và lặp lại.

Đây là nơi các bạn thật sự thấy system mình xây dựng hoạt động như thế nào khi đưa vào prototype thật.

**[Slide 12 — Section 4: Stitching prototype]**

Ở phần này, các bạn sẽ kết nối những màn hình đã build thành một user journey hoàn chỉnh.

Không còn là những màn hình riêng lẻ.

Mà là một flow có đầu, có cuối, và có thể demo như một câu chuyện hoàn chỉnh.

Đây cũng là nơi mình sẽ chia sẻ một case study thực tế từ chính công việc của mình.

**[Slide 13 — Cần chuẩn bị gì trước khi bắt đầu]**

Trước khi bước vào phần tiếp theo, có bốn thứ mình muốn các bạn chuẩn bị.

Một, Figma fundamentals.

Các bạn cần biết cách tạo frame, sử dụng component, và kết nối các màn hình.

Khóa học này không dạy lại Figma từ đầu.

Mình sẽ tập trung vào cách tổ chức những gì các bạn đã biết thành một system mà AI có thể đọc và sử dụng.

Hai, một AI chat tool.

Các bạn có thể sử dụng bất kỳ công cụ nào mà mình đã quen.

Công cụ này sẽ được dùng để research, phân tích, và xây dựng prototype pattern.

Ba, một AI coding tool.

Đây là công cụ sẽ thực sự build ra các màn hình.

Nó sẽ sử dụng prototype pattern mà các bạn đã định nghĩa trước đó.

Bốn, một design project thật của chính các bạn.

Đây là thứ mình khuyến khích các bạn chuẩn bị nhất.

Project không cần phải hoàn chỉnh.

Có thể chỉ là một vài màn hình.

Một file Figma chưa được clean up.

Hoặc một ý tưởng đang trong giai đoạn đầu.

Các bài tập trong khóa học được thiết kế để làm trên dữ liệu thật.

Vì vậy, học trên project của chính mình sẽ giúp các bạn thấy rõ hơn phương pháp này hoạt động như thế nào trong thực tế.

**[Slide 14 — Tools you'll use]**

Đến đây, mình muốn nói rõ tên.

Từ phần tiếp theo trở đi, các bạn sẽ cần chọn một công cụ thật để dùng, không chỉ nghe mô tả chung chung nữa.

Và có một nguyên tắc mình muốn các bạn nhớ trước khi nghe tên cụ thể.

Tool nào có thể đọc trực tiếp file Figma, hoặc tự dựng được design system của bạn, sẽ giữ được design fidelity tốt hơn tool chỉ dựa vào screenshot hay mô tả bằng lời.

Với AI chat tool, dùng để research và soạn prototype pattern, không cần chọn theo tên.

Công cụ chat nào bạn quen dùng cũng được, đây là lựa chọn cá nhân, không phải thứ cần xếp hạng.

Với AI design tool, tạo ra giao diện trực quan để bạn chỉnh tiếp, có hai hướng khác nhau.

Figma Make đọc thẳng file Figma của bạn nên fidelity hình ảnh cao nhất, hợp nếu bạn đã có design sẵn và chỉ cần thêm tương tác.

Claude Design đi theo hướng khác hẳn.

Ngay từ bước onboarding, nó tự đọc codebase và file thiết kế của bạn để dựng design system, rồi tự áp dụng đúng màu, typography, component cho mọi prototype sau đó.

Không cần bạn tự cấu hình gì thêm.

Với AI coding tool, build ra một app chạy thật, có logic và dữ liệu thật, chọn theo workflow của bạn.

Cần một MVP chạy được mà không muốn đụng code, Lovable phù hợp nhất.

Cần một app full-stack, có backend và database, Bolt hoặc Replit đọc thẳng metadata Figma nên vẫn giữ được fidelity cao.

Còn nếu bạn đã quen dùng code editor, Cursor, Claude Code, hay Windsurf kết nối trực tiếp qua Figma MCP, đọc được cả token, component, và variant, chi tiết nhất trong nhóm coding tool.

Đổi lại, bạn cần tự setup kết nối, bước này sẽ học kỹ hơn ở phần sau.

Bảng trên màn hình xếp cả năm nhóm theo đúng mức độ hỗ trợ design system, từ cao xuống thấp.

Chỉ cần nhớ một nguyên tắc thôi.

Công cụ nào đọc thẳng được file Figma, hoặc tự dựng design system như Claude Design, sẽ ít lệch với thiết kế gốc hơn công cụ chỉ đọc ảnh chụp hay dựa vào mô tả bằng lời.

Đó cũng chính là lý do phần build sẽ hướng dẫn thiết lập MCP.

Đây là bức tranh tại thời điểm mình quay khóa học này thôi.

Thị trường đổi rất nhanh, nên nếu sau này có công cụ mới hay một tool đổi tính năng, cứ áp nguyên tắc chọn này.

Xác định đúng nhóm mình cần, rồi ưu tiên công cụ đọc thẳng được file Figma hoặc tự dựng design system.

Chưa chắc công cụ mình đang dùng thuộc nhóm nào?

Cứ học tiếp, phần sau sẽ hướng dẫn cụ thể hơn cách kết nối công cụ với Figma trước khi bắt đầu build.

**[Slide 15 — Kết thúc phần giới thiệu]**

Vậy là chúng ta đã hoàn thành phần giới thiệu.

Các bạn đã biết một chút về mình, biết khóa học này dành cho ai, hiểu mình sẽ đi qua những gì, và biết cần chuẩn bị gì trước khi bắt đầu.

Trước khi sang phần tiếp theo, hãy chuẩn bị bốn thứ.

Figma fundamentals.

Một AI chat tool.

Một AI coding tool.

Và quan trọng nhất, một design project thật của chính các bạn.

*(để một khoảng lặng ngắn ở đây trước khi kết thúc)*

Hẹn gặp các bạn ở phần tiếp theo, nơi chúng ta sẽ bắt đầu xây dựng prototype pattern đầu tiên của riêng các bạn.

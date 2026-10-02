---
title: "Section 1 · Giới Thiệu"
subtitle: "Chào mừng bạn đến với khóa học — khóa học này dành cho ai, và chúng ta sẽ đi qua những gì"
course: Systematic AI Prototyping for Product Designers
section: 1
part: n/a
source-lesson: "Online Course/AI Prototype Development/course-02-outline-brief.md"
last-updated: 2026-07-17
language: vi
---

## Tổng Quan Phần

Đây là phần đầu tiên các bạn sẽ xem trước khi bắt đầu vào những nội dung kỹ thuật.

Mục tiêu của Section 1 khá đơn giản: để các bạn biết mình là ai, hiểu khóa học này có phù hợp với mình không, và biết trước chúng ta sẽ đi qua những gì. Mình không muốn các bạn học được nửa khóa rồi mới nhận ra đây không phải điều mình đang cần.

**Kết thúc phần này, các bạn sẽ:**
1. Biết mình là ai, mình đã đi qua hành trình nào, và vì sao mình xây dựng phương pháp systematic prototyping này
2. Biết khóa học có phù hợp với mình không, và hình dung rõ hơn mình sẽ làm được gì sau khi hoàn thành
3. Nắm được cấu trúc của cả 4 section và biết cần chuẩn bị gì trước khi bắt đầu Section 2

**Nội dung Section:**
- 3 lessons, tổng thời lượng khoảng 14-16 phút
- Lesson 1 là một video giới thiệu riêng, không có slide
- Lesson 2 và Lesson 3 có slide đi kèm
- Không có tài liệu download riêng cho Section này

## Quy Ước Kịch Bản

Các lesson trong Section này được viết theo cách nói chuyện trực tiếp. Mình sẽ xưng "mình", gọi các bạn là "các bạn" — giống như cách mình đang trò chuyện với các bạn, chứ không phải đọc một bài essay.

Các thuật ngữ chuyên môn như prototype pattern, component inventory, template, AI chat tool, AI coding tool và Figma sẽ được giữ nguyên bằng English khi nghe tự nhiên hơn trong câu.

Với Lesson 2 và Lesson 3, các dòng `[SLIDE: ...]` chỉ là marker để canh thời điểm chuyển slide khi quay video, khớp tên slide bên `section 1-slide-outline.md`. Đây không phải là phần cần đọc thành lời.

Trong toàn bộ Lesson 2 và 3, không nêu tên AI tool cụ thể — luôn dùng nhãn chung "AI chat tool" / "AI coding tool". **Ngoại lệ:** slide "Tools you'll use" ở cuối Lesson 3 nêu tên tool cụ thể theo yêu cầu trực tiếp của Winnie, vì học viên cần biết tên thật để chọn công cụ trước khi vào Section 2. Ngoại lệ này chỉ áp dụng cho slide đó.

---

## Nội Dung Lesson

### Lesson 1: Chào Mừng + Giới Thiệu Bản Thân

*Không có slide — đây là video giới thiệu riêng.*

Chào các bạn, mình là Winnie.
Rất vui vì các bạn đã có mặt ở đây.

Mình biết hiện tại có rất nhiều khóa học về AI prototyping ngoài kia. Vì vậy, trước khi bắt đầu, mình thật sự cảm ơn các bạn đã dành thời gian và chọn đồng hành cùng mình trong khóa học này.

Trước khi đi vào nội dung kỹ thuật, mình muốn dành một chút thời gian để giới thiệu bản thân.
Không phải để kể CV.
Mà để các bạn hiểu mình đến từ đâu, vì sao mình xây dựng khóa học này, và vì sao mình tin rằng cách tiếp cận này đáng để các bạn học.

**Một chút về hành trình nghề nghiệp của mình**

Mình là UX Product Designer và đã có hơn 11 năm làm việc trong ngành.

Hiện tại, mình đang thiết kế sản phẩm trong lĩnh vực tài chính - ngân hàng. Đây là một ngành mà mỗi quyết định thiết kế thường phải đi qua rất nhiều lớp kiểm duyệt. Sự nhất quán không chỉ là một điều "nên có". Nó gần như là một yêu cầu bắt buộc.

Nhưng trước khi làm trong banking, mình đã có cơ hội làm việc ở khá nhiều ngành khác nhau — từ edtech, e-commerce, social media, healthcare cho đến telecommunications. Mỗi ngành, mỗi sản phẩm, mỗi team đều cho mình một góc nhìn khác về việc làm sao để thiết kế nhanh hơn, đúng hơn, và vẫn giữ được sự nhất quán khi sản phẩm ngày càng lớn.

Nhìn lại hành trình đó, có một vấn đề mình thấy lặp đi lặp lại ở rất nhiều nơi.
Không phải designer thiếu kỹ năng.
Mà là khi mọi thứ bắt đầu scale, chúng ta thường thiếu một system để tổ chức những kỹ năng đó lại với nhau.

**Về việc giảng dạy**

Bên cạnh công việc full-time, mình cũng đã có hơn 6 năm giảng dạy — từ các trung tâm đào tạo, các chương trình trong công ty, cho đến mentoring 1:1.

Tính đến hiện tại, mình đã có cơ hội đồng hành cùng hơn 50 designer ở Việt Nam, Mỹ và Úc.

Các chủ đề mình thường giảng dạy bao gồm UX/UI Design, Design Thinking, Product Design, System Thinking, stakeholder management, và gần đây nhất là AI-assisted design workflow. Chính là chủ đề của khóa học này.

Nếu để ý kỹ, các chủ đề này có một điểm chung.
Chúng không chỉ nói về việc làm tốt từng task riêng lẻ.
Mà nói về cách xây dựng systems để mọi thứ có thể hoạt động tốt hơn khi quy mô tăng lên.

**Vì sao mình xây khóa học này**

Nếu nhìn lại hành trình của mình, mình từng bắt đầu như một designer thiên về execution.
Tức là nhận một task, làm tốt phần việc của mình, hoàn thành những màn hình được giao.

Sau đó, dần dần, mình chuyển sang một vai trò khác.
Một strategic partner trong tổ chức.
Người không chỉ tạo ra từng màn hình, mà còn tham gia xây dựng những standards và systems để cả team có thể làm việc nhất quán hơn.

Sự chuyển dịch đó không xảy ra trong một sớm một chiều.
Mình mất khá nhiều năm để hiểu sự khác biệt giữa hai vai trò này.
Một designer giỏi execution có thể tạo ra những màn hình rất tốt.
Nhưng một strategic partner còn cần nghĩ đến một câu hỏi lớn hơn: làm thế nào để cả team có thể tạo ra những màn hình tốt và nhất quán với nhau?

Đó cũng là nơi khóa học này bắt đầu.

Trong thời gian gần đây, khi AI tools bắt đầu phát triển rất nhanh, mình thấy rất nhiều designer bắt đầu dùng AI để prototype. Điều này hoàn toàn dễ hiểu. AI rất nhanh. Kết quả đầu tiên thường trông rất ấn tượng. Và cảm giác build được một màn hình chỉ sau vài phút thật sự rất hấp dẫn.

Nhưng sau vài màn hình, một số vấn đề bắt đầu xuất hiện.
Components không còn khớp nhau.
AI quên mất những quyết định đã đưa ra ở màn hình trước.
Spacing bắt đầu lệch.
Và cuối cùng, designer phải quay lại sửa thủ công rất nhiều thứ. Đôi khi còn mất nhiều thời gian hơn cả việc tự làm từ đầu.

Nhưng vấn đề không nằm ở AI.
Vấn đề là AI chưa có một system đủ rõ để dựa vào trước khi bắt đầu build.
Đó chính là khoảng trống mà khóa học này muốn giải quyết.

AI prototyping chỉ thực sự trở nên mạnh khi nó được xây dựng trên một system.
Không phải một chuỗi các prompt riêng lẻ.
Không phải mỗi màn hình là một lần bắt đầu lại từ đầu.
Mà là một cách làm có thể scale.

Và đó chính là điều mình sẽ hướng dẫn các bạn trong suốt khóa học này.

Ở lesson tiếp theo, mình sẽ nói rõ hơn khóa học này dành cho ai, các bạn sẽ làm được gì sau khi hoàn thành, và toàn bộ khóa học được tổ chức như thế nào.

Hẹn gặp các bạn ở lesson tiếp theo nhé.

---

### Lesson 2: Khóa Học Dành Cho Ai

*Giúp các bạn tự xác nhận khóa học có phù hợp với mình không, và hình dung rõ hơn kết quả sau khi hoàn thành.*

[SLIDE: COVER, sau đó SECTION divider "Lesson 2"]

Trước khi đi tiếp, mình muốn các bạn tự trả lời một câu hỏi khá đơn giản: khóa học này có thật sự dành cho mình không?

Mình muốn các bạn tự xác nhận điều đó ngay từ bây giờ. Không phải học đến giữa khóa rồi mới nhận ra nội dung này không phù hợp với nhu cầu của mình.

[SLIDE: STATEMENT — Bạn có đang ở đây không?]

**Bạn có đang ở đây không?**

Khóa học này dành cho product designers và UX designers đã có nền tảng Figma cơ bản. Các bạn biết cách tạo frame, sử dụng component và kết nối các màn hình lại với nhau. Các bạn muốn dùng AI để prototype nhanh hơn. Nhưng không muốn phải đánh đổi sự nhất quán để lấy tốc độ.

Và có một vài điều các bạn không cần phải có trước khi bắt đầu: không cần biết code, không cần có một design system hoàn chỉnh, và cũng không cần từng sử dụng AI coding tool trước đây.

Nếu các bạn đang có một project thật — dù mới chỉ có vài màn hình, một file Figma chưa được chuẩn hóa, hoặc thậm chí mới chỉ là một ý tưởng — các bạn hoàn toàn có thể mang project đó vào khóa học để thực hành. Thật ra, mình rất khuyến khích các bạn làm như vậy. Vì các bài tập trong khóa học này được thiết kế để làm trên dữ liệu thật của các bạn. Không phải một ví dụ giả định.

*(Vẫn slide STATEMENT, lời thoại tiếp tục.)*

**Một cách khác để hình dung vấn đề**

Để các bạn dễ hình dung hơn, hãy thử nghĩ đến việc xây một ngôi nhà bằng Lego.

Cách làm phổ biến hiện nay — mình gọi nó là kiểu vibe coding — giống như việc bạn tự tạo ra một viên Lego mới mỗi khi cần một thứ gì đó. Phòng khách có một viên gạch đỏ. Phòng ngủ có một viên gạch đỏ khác. Nhìn qua thì có vẻ giống nhau, nhưng kích thước lại hơi khác một chút.

Lúc đầu, có thể bạn không nhận ra. Nhưng càng xây nhiều phòng, ngôi nhà càng trở nên thiếu nhất quán. Và khi cần sửa một chi tiết nhỏ, bạn phải đi sửa từng phòng một.

Đó chính xác là điều có thể xảy ra khi bạn prototype bằng AI mà không có một system rõ ràng. Bạn mô tả một màn hình. AI generate ra. Bạn chuyển sang màn hình tiếp theo. Lại mô tả gần như từ đầu. Và rồi nhận ra hai màn hình không thực sự khớp nhau.

**Cách tiếp cận của khóa học này**

Cách làm mà khóa học này dạy đi theo hướng ngược lại.

Bạn định nghĩa bộ "Lego" của mình trước. Những components nào đang có? Chúng trông như thế nào? Có những states nào? Các màn hình kết nối với nhau ra sao?

Sau đó, AI sử dụng chính system đó để ráp các màn hình. Nếu cần thay đổi một chi tiết, bạn sửa ở đúng nơi cần sửa. Thay vì phải đi sửa từng màn hình một.

Và khi system đã được định nghĩa rõ, 30 màn hình không nhất thiết phải khó hơn 3 màn hình. Vì AI không phải đoán lại từ đầu mỗi lần. Nó đang build dựa trên cùng một source of truth.

[SLIDE: Nhóm 1 — Career transitioner]

**Nhóm 1 — Career transitioner**

Trong số các designer mình từng đồng hành, có ba nhóm thường xuất hiện nhiều nhất.

Nhóm đầu tiên là các bạn đang chuyển ngành sang UX hoặc Product Design. Các bạn thường không thiếu khả năng quan sát hay gu thẩm mỹ. Điều các bạn thiếu nhiều hơn là một quy trình rõ ràng để biết nên bắt đầu từ đâu và đi tiếp như thế nào.

Khóa học này giúp các bạn có một process cụ thể để follow. Từ việc định nghĩa system, đến việc build ra một prototype thật.

[SLIDE: Nhóm 2 — Junior designer]

**Nhóm 2 — Junior designer**

Nhóm thứ hai là junior designers. Các bạn đã quen với Figma, đã làm một vài project, và muốn dùng AI để tăng tốc độ prototype.

Rất nhiều bạn trong nhóm này gặp một vấn đề khá giống nhau. AI giúp build nhanh hơn. Nhưng kết quả lại bắt đầu trở nên rời rạc. Các màn hình không còn nhất quán. Và cuối cùng, các bạn mất rất nhiều thời gian để sửa lại.

Khóa học này giúp các bạn giữ được tốc độ của AI mà không phải đánh đổi chất lượng của design.

[SLIDE: Nhóm 3 — Mid-level hướng senior]

**Nhóm 3 — Mid-level designer đang hướng tới senior**

Nhóm thứ ba là mid-level designers đang hướng tới senior. Ở giai đoạn này, các bạn không chỉ cần làm tốt phần việc của riêng mình nữa. Các bạn bắt đầu cần nghĩ đến cách xây dựng những standards chung cho cả team.

Làm thế nào để một designer mới vào team cũng có thể prototype theo cùng một system? Làm thế nào để những quyết định design không chỉ nằm trong đầu của một người?

Khóa học này giúp các bạn biến những quyết định đó thành một ngôn ngữ và một source of truth mà cả team có thể sử dụng.

[SLIDE: QUOTE — Key message]

**Vậy khóa học này khác gì?**

Cách làm AI prototyping phổ biến nhất hiện nay là kiểu vibe coding: mô tả một màn hình, để AI generate ra, rồi lặp lại cho màn hình tiếp theo.

Cách này bắt đầu rất nhanh, nhưng rạn nứt ngay khi số lượng màn hình tăng lên, vì không có gì được định nghĩa từ trước để AI dựa vào.

Khóa học này đi theo hướng ngược lại: dạy các bạn định nghĩa hệ thống của mình một lần, rồi để AI build nhất quán ở bất kỳ quy mô nào.

Không phải vibe-coded. Được thiết kế để mở rộng quy mô.

[SLIDE: NUMBERED — Học xong, bạn sẽ làm được gì]

**Học xong, bạn sẽ làm được gì?**

Mình muốn nói rõ ba kết quả cụ thể.

Một. Các bạn có thể biến design system của mình thành một prototype pattern mà AI có thể đọc và sử dụng. Nó bao gồm ba lớp:
- Các token tạo nên visual language của system
- Các components hiện có và states của chúng
- Cách các màn hình được tổ chức và kết nối với nhau thông qua templates

Đây là một system các bạn có thể định nghĩa một lần và sử dụng xuyên suốt project.

Hai. Các bạn có thể sử dụng AI chat tool và AI coding tool để build những prototype nhất quán. Dù là 3 màn hình hay 30 màn hình. Màn hình sau không phải bắt đầu lại từ đầu. Nó được build dựa trên cùng một prototype pattern.

Ba. Các bạn có thể kết nối nhiều màn hình riêng lẻ thành một user journey hoàn chỉnh. Một journey đủ rõ để demo cho stakeholder. Và đủ thật để test với người dùng. Không còn là một collection của những màn hình rời rạc.

Nếu các bạn thấy mình trong những điều vừa rồi, thì có khả năng cao khóa học này phù hợp với các bạn.

Ở lesson tiếp theo, mình sẽ cho các bạn xem toàn bộ map của khóa học và những gì cần chuẩn bị trước khi bắt đầu.

---

### Lesson 3: Cách Khóa Học Được Tổ Chức

*Giúp các bạn hiểu toàn bộ structure của khóa học và biết cần chuẩn bị gì trước khi bắt đầu Section 2.*

[SLIDE: SECTION divider — Lesson 3]

Đây là lesson cuối cùng của Section 1. Ở đây, mình muốn cho các bạn một overview về toàn bộ khóa học. Để từ bây giờ, các bạn luôn biết mình đang ở đâu trong journey. Và biết điều gì sẽ xảy ra tiếp theo.

Khóa học gồm 4 sections. Và chúng đi theo đúng cách một prototype thật sự được xây dựng: từ tư duy → đến system → đến build → rồi hoàn thiện thành một journey có thể demo.

[SLIDE: Section 2 — Pattern-first thinking]

**Section 2 — Pattern-first thinking**

Ở Section 2, các bạn sẽ hiểu vì sao cách làm screen-by-screen dễ bắt đầu bị rạn nứt khi project lớn dần. Sau đó, các bạn sẽ sử dụng AI chat tool để tạo ra một prototype pattern cho chính project của mình.

Section này có hai phần. Đầu tiên là hiểu cách tư duy pattern-first. Sau đó là thực hành tạo prototype pattern bằng một chuỗi prompt cụ thể.

[SLIDE: Section 3 — Build & refine]

**Section 3 — Build & refine**

Section 3 là phần lớn nhất của khóa học. Các bạn sẽ bắt đầu bằng việc chuẩn bị và dọn dẹp file Figma. Sau đó kết nối AI coding tool với Figma. Và bắt đầu build từng màn hình dựa trên prototype pattern đã tạo ở Section 2.

Build. Review. Tinh chỉnh. Và lặp lại.

Đây là nơi các bạn thật sự thấy system mình xây dựng hoạt động như thế nào khi đưa vào prototype thật.

[SLIDE: Section 4 — Stitching prototype]

**Section 4 — Stitching prototype**

Ở Section 4, các bạn sẽ kết nối những màn hình đã build thành một user journey hoàn chỉnh. Không còn là những màn hình riêng lẻ. Mà là một flow có đầu, có cuối, và có thể demo như một câu chuyện hoàn chỉnh.

Đây cũng là nơi mình sẽ chia sẻ một case study thực tế từ chính công việc của mình.

[SLIDE: NUMBERED — Cần chuẩn bị gì trước khi bắt đầu]

**Cần chuẩn bị gì trước khi bắt đầu?**

Trước khi bước vào Section 2, có 4 thứ mình muốn các bạn chuẩn bị.

Một — Figma fundamentals. Các bạn cần biết cách tạo frame, sử dụng component và kết nối các màn hình. Khóa học này không dạy lại Figma từ đầu. Mình sẽ tập trung vào cách tổ chức những gì các bạn đã biết thành một system mà AI có thể đọc và sử dụng.

Hai — một AI chat tool. Các bạn có thể sử dụng bất kỳ công cụ nào mà mình đã quen. Ở Section 2, công cụ này sẽ được sử dụng để research, phân tích và xây dựng prototype pattern.

Ba — một AI coding tool. Đây là công cụ sẽ thực sự build ra các màn hình ở Section 3. Nó sẽ sử dụng prototype pattern mà các bạn đã định nghĩa trước đó.

Bốn — một design project thật của chính các bạn. Đây là thứ mình khuyến khích các bạn chuẩn bị nhất. Project không cần phải hoàn chỉnh. Có thể chỉ là một vài màn hình. Một file Figma chưa được clean up. Hoặc một ý tưởng đang trong giai đoạn đầu.

Các bài tập trong khóa học được thiết kế để làm trên dữ liệu thật. Vì vậy, học trên project của chính mình sẽ giúp các bạn thấy rõ hơn phương pháp này hoạt động như thế nào trong thực tế.

[SLIDE: Tools you'll use]

**Tools you'll use**

Đến đây, mình muốn nói rõ tên. Từ Section 2 trở đi, các bạn sẽ cần chọn một công cụ thật để dùng, không chỉ nghe mô tả chung chung nữa.

Và có một nguyên tắc mình muốn các bạn nhớ trước khi nghe tên cụ thể: tool nào có thể đọc trực tiếp file Figma, hoặc tự dựng được design system của bạn, sẽ giữ được design fidelity tốt hơn tool chỉ dựa vào screenshot hay mô tả bằng lời.

Với AI chat tool, dùng để research và soạn prototype pattern, không cần chọn theo tên. Công cụ chat nào bạn quen dùng cũng được — đây là lựa chọn cá nhân, không phải thứ cần xếp hạng.

Với AI design tool, tạo ra giao diện trực quan để bạn chỉnh tiếp, có hai hướng khác nhau. Figma Make đọc thẳng file Figma của bạn nên fidelity hình ảnh cao nhất, hợp nếu bạn đã có design sẵn và chỉ cần thêm tương tác. Claude Design đi theo hướng khác hẳn — ngay từ bước onboarding, nó tự đọc codebase và file thiết kế của bạn để dựng design system, rồi tự áp dụng đúng màu, typography, component cho mọi prototype sau đó, không cần bạn tự cấu hình gì thêm.

Với AI coding tool, build ra một app chạy thật, có logic và dữ liệu thật, chọn theo workflow của bạn. Cần một MVP chạy được mà không muốn đụng code, Lovable phù hợp nhất. Cần một app full-stack, có backend và database, Bolt hoặc Replit đọc thẳng metadata Figma nên vẫn giữ được fidelity cao. Còn nếu bạn đã quen dùng code editor, Cursor, Claude Code, hay Windsurf kết nối trực tiếp qua Figma MCP, đọc được cả token, component, và variant — chi tiết nhất trong nhóm coding tool. Đổi lại, bạn cần tự setup kết nối, đúng bước sẽ học ở Section 3.

Bảng trên màn hình xếp cả 5 nhóm theo đúng mức độ hỗ trợ design system, từ cao xuống thấp. Chỉ cần nhớ một nguyên tắc thôi: công cụ nào đọc thẳng được file Figma, hoặc tự dựng design system như Claude Design, sẽ ít lệch với thiết kế gốc hơn công cụ chỉ đọc ảnh chụp hay dựa vào mô tả bằng lời. Đó cũng chính là lý do Section 3 hướng dẫn thiết lập MCP.

Đây là bức tranh tại thời điểm mình quay khóa học này thôi. Thị trường đổi rất nhanh, nên nếu sau này có công cụ mới hay một tool đổi tính năng, cứ áp nguyên tắc chọn này: xác định đúng nhóm mình cần, rồi ưu tiên công cụ đọc thẳng được file Figma hoặc tự dựng design system.

Chưa chắc công cụ mình đang dùng thuộc nhóm nào? Cứ học tiếp. Section 3 sẽ hướng dẫn cụ thể hơn cách kết nối công cụ với Figma trước khi bắt đầu build.

[SLIDE: END — Kết thúc Section 1]

**Kết thúc Section 1**

Vậy là chúng ta đã hoàn thành phần giới thiệu. Các bạn đã biết một chút về mình, biết khóa học này dành cho ai, hiểu mình sẽ đi qua những gì, và biết cần chuẩn bị gì trước khi bắt đầu.

Trước khi sang Section 2, hãy chuẩn bị 4 thứ: Figma fundamentals. Một AI chat tool. Một AI coding tool. Và quan trọng nhất: một design project thật của chính các bạn.

Hẹn gặp các bạn ở phần tiếp theo. Ở đó, chúng ta sẽ bắt đầu xây dựng prototype pattern đầu tiên của riêng các bạn.

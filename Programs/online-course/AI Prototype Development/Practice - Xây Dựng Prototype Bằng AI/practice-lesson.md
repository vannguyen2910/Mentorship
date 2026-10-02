---
title: "Practice: Xây Dựng Prototype Bằng AI"
subtitle: "Build các journey còn lại, mở rộng design system đúng lúc, nhìn lại quá trình cộng tác với AI, và nộp bài"
course: Systematic AI Prototyping for Product Designers
section: practice
position: "Giữa Section 4 (Xây Dựng AI Prototype bằng Figma Make) và Section 5 (Stitching Prototype) — không đánh số Section riêng, theo quyết định restructure khóa học tháng 8/2026"
source-lesson: Library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-08-17
language: vi
---

## Tổng Quan

> **Nguồn:** Gộp từ Section 4 cũ ("Mở Rộng Quy Mô Prototype") + Section 5 cũ Lesson 2-3 ("Đóng Gói & Chia Sẻ Prototype"), theo quyết định restructure khóa học tháng 8/2026. Lesson chia sẻ prototype (Section 5 cũ, Lesson 1) đã chuyển sang cuối Section 3. Phần này áp dụng được cho prototype build từ Section 3 (Claude Design) hoặc Section 4 (Figma Make), tuỳ bạn chọn tool nào.

Phần trước để lại cho bạn một main journey đã chạy được — chưa hoàn hảo, nhưng đã có nền tảng: một component inventory và một bộ token dùng chung, và bạn đã biết cách chia sẻ nó ra ngoài.

Đây là lúc mở rộng từ đó, rồi dừng lại nhìn lại toàn bộ quá trình trước khi bước sang phần Stitching.

Bạn sẽ build các journey còn lại, học cách nhận ra khi nào system thật sự cần được mở rộng, rồi nhìn lại quá trình cộng tác với AI bằng câu hỏi cụ thể, không chỉ "thấy hay".

**Kết thúc phần này, bạn sẽ có thể:**
1. Build các journey còn lại mà vẫn giữ được sự nhất quán với main journey
2. Nhận biết khi nào nên reuse, khi nào nên tạo variant, và khi nào thật sự cần thêm component hoặc template mới
3. Nhìn lại quá trình cộng tác với AI bằng 3 câu hỏi cụ thể, không chỉ nhận xét chung chung
4. Mở rộng prototype qua bài tập, nộp bài, và biết nơi tra cứu lại toàn bộ prompt đã học

**Nội dung phần:**
- 4 lesson ngắn: 3 lesson nội dung và 1 bài tập tổng
- Cần có: prototype đã build và tinh chỉnh xong ở Section 3 hoặc Section 4, Build & Journey Worksheet

---

## Nội Dung Lesson

### Lesson 1: Build Các Journey Còn Lại
*Lặp lại quy trình. Nhưng lần này, bạn đã biết mình đang làm gì.*

Không có kỹ thuật mới nào ở đây.

Bạn chỉ cần lặp lại quy trình build và review đã học trước đó cho các user goal còn lại.

Điểm khác biệt là: lần này bạn đã có kinh nghiệm từ main journey đầu tiên.

Bạn đã biết AI thường build sai ở đâu. Bạn đã biết cách review. Và bạn cũng đã biết những vấn đề nào cần sửa ở source thay vì sửa từng màn hình một.

**Lỗi lặp lại? Fix một lần ở source.**

Ví dụ, nếu bạn phát hiện spacing hoặc màu sắc đang sai trong main journey, hãy kiểm tra xem lỗi đó có xuất hiện ở những journey tiếp theo không.

Vì tất cả đều đang build từ cùng một component inventory và token system, một lỗi có thể xuất hiện ở nhiều nơi.

Nếu đúng là lỗi của component hoặc token, hãy sửa ở đó.

**Fix một chỗ. Mọi nơi dùng nó sẽ được hưởng lợi.**

Đó chính là lợi ích thực tế của pattern-first approach mà bạn đã xây dựng từ trước.

**Với mỗi journey, hãy đi theo đúng quy trình:**
1. Viết một build prompt đầy đủ 5 thành phần, bao gồm cả flow context nối với journey trước
2. Build từng màn hình và review cạnh file Figma gốc
3. Fix những gì cần fix trước khi chuyển sang màn hình tiếp theo

**Build. Review. Rồi mới tiếp tục.**

Đừng build tất cả các journey cùng một lúc.

Hoàn thành một journey trước. Review nó. Fix những gì cần fix. Sau đó mới chuyển sang journey tiếp theo.

Đây vẫn là nguyên tắc bạn đã áp dụng khi build main journey đầu tiên — chỉ là bây giờ áp dụng nó ở quy mô lớn hơn.

**Đừng dồn tất cả vào một prompt.**

Đến thời điểm này, bạn đã có khá nhiều thứ để đưa cho AI:
- Design Tokens
- Components
- Templates
- PRD
- Wireframes
- Main journey đã build làm reference

Và chính vì có quá nhiều thứ sẵn có, bạn rất dễ nghĩ: "Hay là đưa hết vào một prompt và build luôn tất cả các journey?"

Nghe có vẻ nhanh hơn.

Nhưng input càng lớn, AI càng dễ bỏ sót những chi tiết quan trọng. Đó chính là vấn đề về context rot.

Vì vậy, vẫn cứ đi từng bước.

**Một journey. Một màn hình. Một lần review.**

Đó thường là cách nhanh hơn để đi đến một kết quả đúng.

**Review lại bằng 6 câu hỏi**

Sau mỗi lần build, hãy quay lại đúng 6 câu hỏi đã dùng ở main journey đầu tiên:
- Màn hình này có đúng mục tiêu không?
- Người dùng có biết mình đang ở đâu không?
- Thông tin đã được ưu tiên đúng chưa?
- Components và patterns có nhất quán không?
- Next action có rõ ràng không?
- Màn hình này có kết nối đúng với journey không?

**Đẹp không có nghĩa là đúng.**

Ngay cả khi bạn đã build đến journey thứ 2 hoặc thứ 3.

Đừng để việc một màn hình trông đẹp khiến bạn bỏ qua việc kiểm tra xem nó có thật sự phục vụ đúng user goal hay không.

**Trước khi kết thúc, kiểm tra consistency**

Mở các journey cạnh nhau.

Nhìn vào những thứ dễ bị lệch:
- Buttons
- Colors
- Spacing
- Typography
- Components
- Interaction patterns

Chúng có còn nhất quán không?

Nếu có, đó là bằng chứng cho thấy pattern-first approach đang thực sự hoạt động.

Không phải vì bạn tình cờ làm mọi thứ giống nhau.

Mà vì tất cả các journey đều được build dựa trên cùng một source of truth.

Bạn cũng có thể mở `design_system.html` cạnh các journey để đối chiếu trực tiếp.

**Đừng cố nhớ design system. Mở nó lên và kiểm tra.**

**Kết quả tối thiểu:**

Toàn bộ journey đã chọn:
- Chạy được trong browser
- Có navigation kết nối giữa các journey
- Dùng nhất quán components và tokens từ cùng một system

---

### Lesson 2: Mở Rộng Design System Đúng Cách
*Không phải màn hình mới nào cũng cần một component mới.*

Càng build nhiều màn hình, bạn càng dễ rơi vào một trong hai tình huống.

Một là ép mọi màn hình dùng lại component cũ — ngay cả khi nó không còn phù hợp.

Hai là tạo một component mới cho mỗi biến thể nhỏ.

Cả hai đều có vấn đề.

Một bên làm UI trở nên gượng ép.

Một bên khiến component inventory nhanh chóng phình to và khó maintain.

Lesson này giúp bạn biết khi nào nên reuse, khi nào nên tạo variant, và khi nào thật sự cần mở rộng system.

**Trước khi tạo bất cứ thứ gì mới, hãy hỏi:**
1. Component tương tự đã có trong inventory chưa?
2. Sự khác biệt chỉ nằm ở state, size, content hoặc một vài properties khác?
3. Nếu có sự khác biệt, đây nên là một variant của component cũ hay thật sự là một component riêng?
4. Nếu cần một template mới, template đó có thể reuse các components hiện có không?
5. Hay nó thật sự cần một layout và structure hoàn toàn khác?

**Đừng tạo mới chỉ vì nó nhanh hơn**

Default choice nên là reuse.

Chỉ tạo mới khi bạn đã kiểm tra và xác nhận rằng những gì đang có thật sự không đáp ứng được nhu cầu mới.

Đừng tạo một component mới chỉ vì việc tìm lại component cũ mất thêm vài phút.

Vài phút đó có thể giúp bạn tránh một component mới mà sau này phải maintain mãi mãi.

**Đừng dùng trí nhớ. Mở `design_system.html` lên.**

Bạn đã có `design_system.html` từ trước.

Đây là nơi visualise các tokens, components và templates hiện có.

Khi gặp một màn hình mới, hãy mở file lên và đối chiếu trực tiếp.

Sau đó mới quyết định: Reuse → Create a variant → Create something completely new.

Nếu không chắc, bạn cũng có thể prompt AI để kiểm tra.

**Prompt kiểm tra trước khi mở rộng:**

> "Đây là `design_system.html` hiện tại của tôi: [đính kèm file hoặc cung cấp link]. Tôi cần build màn hình [mô tả màn hình]. Hãy kiểm tra design system hiện tại và cho tôi biết:
>
> - Component nào có thể reuse?
> - Có component nào cần thêm variant không?
> - Hay tôi thật sự cần tạo một component mới?
>
> Hãy giải thích lý do cho từng recommendation."

Điểm quan trọng là AI cần được đối chiếu với source thật.

Không phải đoán dựa trên những gì bạn mô tả trong chat.

**Mở rộng system xong → cập nhật lại ngay**

Thêm component hoặc template mới? Cập nhật lại `design_system.html`.

Mỗi lần system được mở rộng, hãy generate lại file để nó phản ánh đúng system hiện tại.

Nếu không, file sẽ nhanh chóng trở nên outdated.

Và một file outdated thì không còn đáng tin để làm reference cho lần build tiếp theo.

**Kết quả tối thiểu:**
- Mọi màn hình mới đều được đối chiếu với `design_system.html` trước khi build
- Inventory chỉ tăng khi thật sự cần
- Mỗi lần mở rộng system đều được cập nhật lại vào `design_system.html`

---

### Lesson 3: Nhìn Lại Quá Trình Cộng Tác Với AI
*"Tôi thấy nó hay" không phải một lần nhìn lại quá trình. Đây là câu hỏi cụ thể hơn thế.*

Nhìn lại quá trình không phải bước làm cho có. Đây là bước biến kinh nghiệm build vừa xong thành hiểu biết bạn mang theo sang những prototype tiếp theo, kể cả những prototype không nằm trong khoá học này.

**Dùng lại nhật ký review trong Build & Journey Worksheet của bạn** (đã ghi lại trong lúc build) để trả lời 3 câu hỏi sau bằng ví dụ cụ thể, không phải cảm nhận chung chung:

1. **AI đã làm đúng điều gì nhanh hơn nếu bạn tự làm bằng tay?** Ví dụ: lắp ráp đúng component theo inventory, tạo nhiều biến thể bố cục để so sánh.

2. **AI đã bỏ sót điều gì mà bạn phải tự sửa?** Đây chính là dữ liệu trong nhật ký review. Mở lại worksheet, chọn ra 1 ví dụ điển hình nhất về lỗi bạn phát hiện và cách bạn sửa nó.

3. **Nếu không có prototype pattern, tức component inventory và template bạn đã chuẩn bị từ đầu, việc build hôm nay sẽ khác thế nào?** Câu hỏi này không có câu trả lời "đúng" cố định. Mục đích là buộc bạn tự nhận ra giá trị cụ thể mà việc chuẩn bị prototype pattern từ đầu mang lại cho cả quá trình build, thay vì chỉ nghe giảng viên nói điều đó.

**Một nghịch lý đáng nhớ:** nghiên cứu năm 2025 của NN/g chỉ ra một điều nghe có vẻ ngược đời. AI hứa hẹn thu hẹp khoảng cách kỹ năng, nhưng lại hoạt động tốt nhất trong tay người *đã* hiểu rõ nghề. Để ra lệnh chính xác cho AI, bạn cần hiểu bố cục, kiểu chữ, cách đặt tên component, và luồng người dùng, đúng những kiến thức bạn đã học trước khi tới khoá học này. AI không thay thế kiến thức thiết kế. Nó khuếch đại khoảng cách giữa một kết quả tạm ổn và một kết quả thực sự tốt, và con mắt tinh tế, gu thẩm mỹ, khả năng tinh chỉnh có chủ đích chính là thứ tạo ra khoảng cách đó.

---

### Lesson 4: Bài Tập & Prompt Library
*Mở rộng prototype của bạn, và biết nơi tra cứu lại mọi prompt đã học khi build.*

**Bài tập: Mở rộng prototype pattern-first**

Mở rộng prototype bạn đã build:
- Thêm ít nhất 2 màn hình nữa vào template của bạn
- Đảm bảo mọi component ở 2 màn hình mới đều lấy từ component inventory đã có, không thêm component mới mà không cập nhật lại inventory trước
- Ghi lại 1 điều AI đã làm sai, và cách bạn đã sửa nó

**Nộp bài:** 1 đường link (live link hoặc repo code, đã học cách tạo ở cuối Section 3) + 1 đoạn nhìn lại quá trình 3 câu về trải nghiệm cộng tác với AI, dựa trên khung 3 câu hỏi ở Lesson 3.

**Prompt Library: tra cứu lại khi cần**

Toàn bộ prompt đã dùng xuyên suốt phần build, từ dọn dẹp, setup MCP hoặc Make kit, generate token/inventory/template, build màn hình, review, đến sửa lỗi, đều nằm trong 1 tài liệu tham chiếu duy nhất mà bạn có thể quay lại bất cứ lúc nào, không cần nhớ thuộc lòng:

| Mục đích | Khi nào dùng |
|---|---|
| Generate token, component inventory + template từ file thật | Ngay khi bắt đầu build, hoặc bất cứ khi nào file Figma của bạn thay đổi |
| Build 1 màn hình (khung 5 thành phần) | Mỗi lần build màn hình mới |
| Review output | Ngay sau khi build, trước khi tinh chỉnh |
| Chọn chế độ tinh chỉnh (chat / targeted feedback / direct adjustment) | Khi đã có danh sách điểm cần sửa |
| Sửa lỗi có cấu trúc | Khi đã biết rõ điều gì cần khác đi |

Prompt Library không phải nội dung học mới, nó là công cụ tra cứu. Giữ nó lại, vì bạn sẽ dùng lại chính những prompt này ở phần tiếp theo, khi nối nhiều prototype thành một hành trình hoàn chỉnh.

---

## Bài Tập: Build Journey Còn Lại, Nhìn Lại Quá Trình & Nộp Bài

*Lần này, không có ai build mẫu cho bạn. Không phải bài nộp giữa chừng — đây là bài tập khép lại phần này.*

Bạn tự chọn một user goal khác. Tự viết prompt. Tự build. Rồi tự review. Đây là lúc kiểm tra xem quy trình đã thực sự trở thành một workflow của bạn chưa — từ việc viết prompt, build màn hình, review kết quả, đến việc biết mình cần fix gì.

**Việc cần làm:**
1. Chọn một user goal khác với main journey
2. Tự viết build prompt, đính kèm design files bạn có hoặc mô tả những gì AI cần biết
3. Build journey, đối chiếu với main journey
4. Review bằng 6 câu hỏi (Lesson 1), fix những gì cần thiết
5. Mở rộng: thêm ít nhất 2 màn hình vào template, dùng đúng component inventory đã có — nếu cần component/template mới, áp dụng quy trình ở Lesson 2 trước khi tạo
6. Ghi lại 1 điều AI làm sai ở các màn hình mới, và cách bạn đã sửa
7. Nhìn lại quá trình: trả lời 3 câu hỏi ở Lesson 3 bằng ví dụ cụ thể
8. Nộp bài: 1 link (live link hoặc repo) + đoạn nhìn lại quá trình

**Kết quả tối thiểu:**
- Một journey mới chạy được, đã đi qua đủ 6 câu hỏi review
- Components và tokens nhất quán với main journey
- 1 link + 1 đoạn nhìn lại quá trình 3 câu, dựa trên khung ở Lesson 3

Phần tiếp theo (Section 5 — Stitching Prototype) sẽ dùng chính prototype này, cùng với prototype của những người khác nếu học trong nhóm, để học cách nối nhiều mảnh rời rạc thành một hành trình người dùng hoàn chỉnh.

---

*Khóa học: Systematic AI Prototyping for Product Designers · Practice (giữa Section 4 và Section 5)*
*Thực hiện bởi Winnie Nguyen · Cập nhật lần cuối tháng 8/2026*

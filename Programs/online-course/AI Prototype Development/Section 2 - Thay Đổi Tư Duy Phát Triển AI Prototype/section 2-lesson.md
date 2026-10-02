---
title: "Section 2 · Phần A: Tư Duy Pattern-First"
subtitle: "Vì sao prototype bằng AI thất bại nếu không có kế hoạch, và cách khắc phục trước khi bắt đầu"
course: Systematic AI Prototyping for Product Designers
section: 2
part: A
source-lesson: Library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-08-17
language: vi
---

## Tổng Quan Phần

Phần lớn designer đang prototype sai cách, mà thường chẳng nhận ra cho tới khi đã quá muộn. Quy trình quen thuộc là mở Figma (hoặc một AI tool), chọn một màn hình, thiết kế nó, rồi qua màn hình tiếp theo, cứ thế lặp lại. Kết quả là màn hình này không khớp màn hình kia, component cứ lệch dần (drift), và mỗi lần prompt AI lại phải kể lại từ đầu, vì chưa có gì được viết ra rõ ràng trước đó.

Phần này mình sẽ làm ngược lại. Trước khi chạm vào bất kỳ màn hình nào, chúng ta sẽ tìm hiểu prototype pattern là gì, qua những ví dụ cụ thể, dễ hình dung, không cần biết trước thuật ngữ nào cả, vì sao đây chính là thứ AI thật sự cần để build, và vì sao tư duy pattern-first lại giúp cả quy trình phía sau nhanh hơn, nhất quán hơn, và đỡ rối hơn hẳn.

**Xong phần này, bạn sẽ:**
1. Giải thích được vì sao prototype theo kiểu screen-by-screen (từng màn hình một) sẽ rạn nứt, và rạn nứt từ lúc nào
2. Mô tả được ba layer của một prototype pattern: token, component inventory (đã gồm cả state), và template
3. Biết AI tool đang cần gì ở bạn, trước khi nó build ra được thứ gì đó tử tế
4. Chốt được 2–3 màn hình bạn sẽ prototype xuyên suốt khóa học này
5. Dọn dẹp design file Figma đúng cách, sẵn sàng để AI đọc và build từ đó

**Nội dung phần:**
- 4 lesson ngắn (~10-12 phút mỗi lesson)
- 4 bài tập: (1) Xác định phạm vi (scope) prototype của bạn, (2) Thiết kế 2–3 screens trong Figma, (3) Set up basic design system bằng tay (token, component inventory, template), (4) Dọn dẹp file Figma theo checklist
- Không cần tải tài liệu nào cho phần này, có một cuốn sổ ghi chú và Figma là đủ

---

## Trước Khi Bắt Đầu

Khóa học này giả định bạn đã biết Figma cơ bản: tạo frame, dùng component, nối màn hình lại với nhau được là đủ. Bạn không cần có sẵn một design system hoàn chỉnh, cũng không cần biết code. Nếu đang có một dự án dang dở, dù mới chỉ ở giai đoạn phác thảo, cứ dùng luôn dự án đó, đừng bịa ra một dự án giả để học cho "an toàn". Mọi bài tập trong khóa học này đều làm trên chính dự án thật của bạn.

---

## Nội Dung Lesson

### Lesson 1: Cái Bẫy Screen-by-Screen (10 phút)
*Vì sao cách hầu hết designer đang prototype lại đang làm chậm chính họ.*

Bạn hãy hình dung chúng ta đang xây một ngôi nhà bằng Lego. Thay vì lấy ra một hộp Lego có sẵn, với các viên gạch đã được phân loại rõ ràng, chúng ta tự nặn ra một viên gạch mới mỗi khi cần, ở từng phòng riêng biệt. Phòng khách dùng một màu đỏ. Phòng ngủ dùng một màu đỏ khác, nhỉnh hơn một chút. Cứ lặp đi lặp lại như vậy, đến cuối cùng chúng ta có một ngôi nhà đầy đủ, nhưng dùng cả chục màu gạch khác nhau, chẳng thứ nào khớp thứ nào.

Đó chính xác là những gì xảy ra khi chúng ta prototype theo kiểu screen-by-screen, tức từng màn hình một:

> Mở Figma → chọn một màn hình → thiết kế nó → chọn màn hình khác → thiết kế nó → thử nối chúng lại → nhận ra chúng không khớp → quay lại sửa → lặp lại.

Nhìn qua thì có vẻ ổn, nhưng thực ra không phải vậy.

**Cách làm cũ và cách làm mới**

| | Cách làm truyền thống (Traditional prototype) | Cách làm mới, có AI hỗ trợ (AI-assisted prototype) |
|---|---|---|
| Cách thực hiện | Tự thiết kế từng màn hình, từng chi tiết một | Định nghĩa hộp Lego 1 lần, AI ráp phần còn lại |
| Khi cần điều chỉnh 1 thứ | Sửa từng màn hình một | Sửa 1 chỗ, mọi màn hình tự update |
| Thời gian | Vài tuần đến vài tháng | Nhanh hơn nhiều |
| Yêu cầu kĩ thuật | Cần thành thạo design tool | Tùy tool: design tool dễ, coding tool cần setup |
| Độ chuyên nghiệp | Tùy kỹ năng cá nhân | Tùy chất lượng pattern |
| Khả năng mở rộng | Khó, càng nhiều màn hình càng nặng, 3 màn hình đã đủ mệt | Dễ, reuse cùng 1 system, 30 màn hình không khác gì 3 |
| Tính bền vững | Dễ bỏ cuộc | Ít burnout hơn |

Đó là lý do vì sao phần này tồn tại: giúp bạn định nghĩa "hộp Lego" đó trước, để AI build đúng ngay từ lần đầu, không phải đoán mò.

**Ba vấn đề âm thầm xảy ra khi làm theo cách cũ:**

**1. Component bị lệch, y hệt viên gạch Lego tự nặn mỗi lần.** Nút bấm (button) ở màn hình 1 có thể khác một chút so với nút bấm ở màn hình 3, chỉ vì mỗi lần đều tạo mới thay vì lấy từ cùng một hệ thống. Tới lúc cần đổi màu nút bấm, bạn phải sửa ở 12 chỗ khác nhau.

**2. AI chẳng nhớ gì giữa các lần yêu cầu.** Mỗi lần bạn nhờ một AI tool hỗ trợ, nó không giữ lại điều gì từ lần trước cả. Giống như nhờ ai đó vẽ lại cùng một con mèo nhiều lần, nhưng lần nào cũng phải mô tả lại từ đầu, vì người đó không nhớ mô tả cũ. Không có tài liệu để AI đọc lại, mỗi prompt là một điểm xuất phát mới, và mỗi lần kết quả sẽ hơi khác nhau một chút.

**3. Vài trạng thái quan trọng bị bỏ quên.** Màn hình đăng nhập thường chỉ được thiết kế cho trường hợp thành công, còn những tình huống như nhập sai mật khẩu, đang tải trang, hay mất kết nối mạng thì chẳng ai để ý tới. Mỗi tình huống như vậy gọi là một "state" (trạng thái), và thường chỉ được phát hiện bởi developer, hoặc chính user, sau khi sản phẩm đã ra đời rồi.

**Pattern-first giải quyết cả ba vấn đề này cùng một lúc:**

| Vấn đề | Cách pattern-first giải quyết |
|---|---|
| Component bị lệch (tạo mới mỗi lần) | Liệt kê "hộp Lego" một lần duy nhất, sử dụng cho mọi màn hình |
| AI không lưu lại thông tin | Cung cấp cho AI một tài liệu ghi rõ mọi thứ, để AI đọc theo tài liệu đó mỗi lần |
| Bỏ sót các trạng thái | Liệt kê toàn bộ state trước khi bắt đầu thiết kế, không phải sau khi thiết kế xong mới bổ sung |

Prototype pattern không phải một bước làm thêm cho có. Nó chính là thứ khiến cả quy trình phía sau chạy nhanh hơn hẳn.

---

### Lesson 2: Prototype Pattern Là Gì (14 phút)
*Ba lớp thông tin AI cần mà hầu hết designer chưa bao giờ viết ra.*

Ở Lesson 1, chúng ta đã nói tới khái niệm "hộp Lego". Một prototype pattern chính là tài liệu mô tả hộp Lego đó, viết ra để AI đọc và build theo. Tài liệu này có ba phần, gọi là ba layer: **token**, **component inventory**, và **template**. Mỗi layer dưới đây mình sẽ trình bày theo cùng một cách: layer đó là gì, vì sao cần, và làm sao xác định nó.

**Layer 1: Token — "tông màu và phong cách của cả hộp Lego"**

*Là gì:* Token là những quyết định gốc rễ về cảm giác của hệ thống, chốt trước khi bất kỳ component nào được định nghĩa: bảng màu (color palette), thang chữ (type scale), nhịp khoảng cách (spacing), độ bo góc (radius). Đây là quyết định áp dụng cho toàn bộ hệ thống, không riêng cho một component hay màn hình nào cả.

*Vì sao cần:* Bỏ qua layer này mà nhảy thẳng vào liệt kê component, mỗi component AI tạo ra sẽ có phong cách hơi khác nhau, đơn giản vì chưa có quy tắc chung nào được đặt ra từ trước. Token chính là quy tắc chung đó, giống như chọn tông màu và chất liệu cho cả bộ Lego, trước khi lắp bất kỳ viên gạch cụ thể nào.

*Cách xác định:* Ở bước này bạn chưa cần gì phức tạp, chỉ cần mô tả cảm giác mong muốn bằng ngôn ngữ đời thường: hệ thống nên "êm dịu hay năng động", "tối giản hay phong phú", "nghiêm túc hay vui tươi", tương tác "nhanh hay chậm rãi". Từ những mô tả này, bảng màu và thang chữ cụ thể sẽ dần hiện ra. Phần B sẽ chỉ bạn cách biến những mô tả này thành token thật, bằng AI.

**Layer 2: Component Inventory — "danh sách những viên gạch đang có"**

*Là gì:* Một bản liệt kê đầy đủ những mảnh ghép UI (component) nào đang tồn tại trong hệ thống, và mỗi mảnh có thể biến đổi ra sao. Cái quan trọng ở đây không phải hình thức của component, mà là bản chất và chức năng của nó.

*Vì sao cần:* Component không được liệt kê trước thì mỗi màn hình sẽ được AI build ra một biến thể hơi khác của cùng một component, chính là vấn đề "component bị lệch" mình vừa nói ở Lesson 1.

*Cách xác định:* Với mỗi component, ghi lại toàn bộ variant (kiểu dáng) và state (trạng thái) nó có thể mang. Ví dụ, một nút bấm (Button) có thể có:
- 3 kiểu dáng khác nhau (variants): Primary (nút chính), Secondary (nút phụ), Ghost (nút viền mờ)
- 4 trạng thái nó có thể mang (states): Default (bình thường), Hover (khi rê chuột vào), Loading (đang xử lý), Disabled (bị khoá, không bấm được)

```
Button
  - Variants: Primary, Secondary, Ghost
  - States: Default, Hover, Loading, Disabled

Input Field
  - Variants: Text, Password, Search
  - States: Empty, Filled, Error, Focused
```

Nguyên tắc này không chỉ áp dụng cho mảnh ghép nhỏ như button, mà cả một màn hình lớn như Dashboard cũng vậy. Trạng thái của cả màn hình cũng nên được liệt kê ở đây luôn:
```
Home Dashboard
  - Loading (đang tải, thể hiện bằng màn hình xám chờ)
  - Loaded (đã có nội dung hiện ra)
  - Empty (user mới, chưa có dữ liệu)
  - Error (tải bị lỗi)
```

**Layer 3: Template — "loại tương tác và bản đồ chỉ đường"**

*Là gì:* Bạn nghĩ tới một trò chơi board game xem, mỗi ô trên bàn cờ thường ứng với một loại nhiệm vụ quen thuộc: xem thông tin, chỉnh sửa, hay thực hiện một giao dịch. Template cũng vậy, áp dụng cho prototype qua hai phần: danh mục loại tương tác, và chuỗi màn hình cụ thể.

*Vì sao cần:* Không có bản đồ này, AI buộc phải đoán màn hình này dẫn tới đâu, thay vì được nói rõ, và mỗi lần đoán có thể ra một kết quả khác.

*Cách xác định, phần A — danh mục các loại tương tác (dùng lại được nhiều lần):*

Mỗi màn hình sẽ rơi vào một hoặc nhiều loại tương tác quen thuộc dưới đây. Mỗi loại chỉ cần định nghĩa đúng một lần, sau đó cứ áp dụng cho bất kỳ màn hình nào cần đến, không phải mô tả lại từ đầu:

| Loại template | User đang làm gì | Ví dụ màn hình |
|---|---|---|
| Read | Xem nội dung, không thay đổi gì | Dashboard, trang chi tiết, hồ sơ |
| Edit | Chỉnh sửa nội dung đã có sẵn | Cài đặt, sửa hồ sơ |
| Add | Tạo ra thứ gì đó mới | Đăng bài mới, thêm vào giỏ hàng |
| Confirm | Xem lại và duyệt một hành động | Tóm tắt đơn hàng, xác nhận thanh toán, xác nhận xoá |
| Navigate | Di chuyển giữa các phần | Thanh tab, menu |
| Search / Filter | Tìm kiếm hoặc lọc một danh sách | Kết quả tìm kiếm, bộ lọc |
| Onboard | Hướng dẫn user lần đầu sử dụng | Màn hình chào mừng, các bước hướng dẫn |

Thường thì một prototype chỉ cần dùng tới 3-4 loại trong bảng này thôi. Một màn hình cũng có thể mang nhiều template cùng lúc, ví dụ màn hình checkout vừa là Edit (chỉnh số lượng), vừa là Confirm (xác nhận thanh toán). Một khi template "Confirm" đã được định nghĩa rõ, bạn dùng lại nó cho màn hình xác nhận xoá, xác nhận đặt hàng, hay bất kỳ chỗ nào cần người dùng xem lại trước khi phê duyệt, khỏi phải định nghĩa lại từ đầu.

*Cách xác định, phần B — chuỗi màn hình cụ thể:*

Gắn nhãn template xong rồi, bước tiếp theo là vẽ ra: màn hình này dẫn tới màn hình nào, trong điều kiện gì.

```
Login Screen (template: Confirm)
  - Success → Home Dashboard
  - Error → Login Screen (error state)
  - Forgot Password → Password Reset Screen

Home Dashboard (template: Read)
  - Tap product card → Product Detail Screen
  - Tap nav: Profile → Profile Screen
```

Ba layer này bạn có thể nhờ AI viết ra, theo cách Phần B sắp hướng dẫn, hoặc tự tay thiết lập trong Figma, ví dụ đặt tên component rõ ràng, ghi chú loại template ngay trong file. Dùng công cụ gì không quan trọng bằng việc cả ba layer đều được viết ra ở một chỗ rõ ràng, ai đọc vào cũng hiểu.

Khi cả ba layer, token, component inventory, và template, được đưa đủ cho một AI tool, nó không còn phải đoán mò nữa. AI biết hệ thống nên mang cảm giác gì, biết những gì đang tồn tại kể cả mọi trạng thái có thể xảy ra, biết từng màn hình đang làm loại việc gì, và biết các màn hình nối với nhau ra sao. Nhờ vậy, prompt cụ thể hơn, output nhất quán hơn, và prototype trở thành thứ bạn có thể mang đi trình bày cho stakeholder, hoặc dùng để test với user thật.

Ba layer này chính là một hộp Lego hoàn chỉnh, đầy đủ, dùng lại được cho bất kỳ sản phẩm nào. Nhưng một hộp Lego, dù đầy đủ tới đâu, cũng không tự quyết định bạn sẽ lắp ra cái gì. Câu hỏi tiếp theo không còn là "hệ thống này có gì", mà là "lần này, bạn muốn dùng nó để kể câu chuyện nào". Đó chính là chuyện của Lesson 3.

---

### Lesson 3: Chọn Câu Chuyện Của Prototype (10 phút)
*Chọn đúng câu chuyện mà bạn muốn kể trong prototype.*

Cái khó nhất ở lesson này không phải hiểu khái niệm "scope", mà là hiểu vì sao nó quan trọng. Scope không phải là liệt kê hết mọi thứ bạn muốn làm. Đây là chọn đúng một câu chuyện nhỏ, đủ rõ để người xem hiểu ngay sản phẩm đang phục vụ điều gì.

Nghĩ tới một trailer phim đi. Bạn đâu có đủ thời gian kể hết cuộc đời một nhân vật. Bạn chỉ chọn đúng một khoảnh khắc quan trọng nhất, đủ để người xem thấy nhân vật đó muốn gì, đang đi đâu. Prototype cũng vậy thôi. Cố kể quá nhiều chuyện, người xem chỉ thấy một đống màn hình, chẳng biết đâu là điểm chính.

**Quy tắc đơn giản để chọn câu chuyện:**
1. Chọn 1 user goal duy nhất.
2. Chọn 2–3 màn hình đủ để kể câu chuyện đó.
3. Loại bỏ mọi thứ không giúp người dùng tiến gần hơn tới goal đó.

Nếu một màn hình không giúp người dùng tiến gần hơn tới mục tiêu, nó không thuộc câu chuyện này.

**Cách chọn màn hình:**

Bắt đầu từ câu hỏi: *"User đang cố làm gì?"* Đừng bắt đầu từ danh sách feature. User goal là điều duy nhất người dùng đang cố làm, kiểu "đặt được một chuyến bay" hay "hoàn tất đăng ký tài khoản". Goal này trở thành xương sống (spine) của prototype, giống cốt truyện chính của một câu chuyện. Mỗi màn hình bạn đưa vào phải giúp user tiến gần hơn tới goal đó, không có ngoại lệ.

Ví dụ tốt:
- User goal: "Tìm cửa hàng gần nhất" → Màn hình: Xem danh sách → Chọn trên bản đồ → Xem chi tiết và chỉ đường

Câu chuyện tốt ở đây không nằm ở "có bao nhiêu màn hình", mà ở "một đường đi rõ ràng, đưa người dùng tới gần hơn một mục tiêu duy nhất".

**Những điều cần tránh:**
- Chọn nhiều user goal trong cùng một prototype, vì chúng sẽ không tự nhiên kết nối với nhau.
- Chọn quá nhiều màn hình chỉ vì bạn muốn cover mọi thứ.
- Chọn màn hình phức tạp nhất đầu tiên. Hãy bắt đầu từ core flow, tức phần đơn giản nhưng quan trọng nhất.

**Phác thảo concept ban đầu của riêng bạn**

Trước khi qua Phần B, chỗ AI bắt đầu tham gia, dành vài phút phác thảo ít nhất một, hai hướng concept của riêng bạn cho 2–3 màn hình đã chọn. Đây chưa phải lúc làm sản phẩm hoàn chỉnh. Đây là lúc xác nhận mình đang kể câu chuyện nào.

Bước này giữ cho tư duy sáng tạo của bạn dẫn dắt cả quá trình, thay vì để AI quyết định hết hướng đi ngay từ prompt đầu tiên. Khi bắt đầu dùng AI ở Phần B, hãy dùng nó để mở rộng hoặc thử thách concept ban đầu, đừng để nó thay thế hoàn toàn. Output của AI là một điểm khởi đầu tốt để lấy thêm ý tưởng, nhưng đừng vội xem nó là concept cuối cùng khi chưa tự mình đánh giá kỹ.

**Entry point của bạn cho khóa học này:**

Khóa học này đi theo Entry Point A: prototype pattern được build từ đầu bằng AI, bắt đầu từ việc xác định hệ thống nên mang *cảm giác* gì, trước khi tính tới diện mạo cụ thể. Bạn không cần có sẵn một design system hoàn chỉnh mới được bắt đầu. Chỉ cần 1 user goal, 2–3 màn hình, và 1 AI tool là đủ.

---

### Lesson 4: Dọn Dẹp Design File Trước Khi AI Đọc (8 phút)
*AI không phân biệt được đâu là hệ thống thật, đâu là bản nháp bạn quên xoá.*

Trước khi AI đọc bất kỳ điều gì trong file Figma của bạn, hãy dọn dẹp nó trước. Đây là bước dễ bị bỏ qua nhất, vì nó không giống "công việc thật", cảm giác giống dọn bàn hơn là thiết kế. Nhưng đây chính là bước quyết định component inventory sau này sẽ chính xác hay lộn xộn.

**Vì sao bước này quan trọng:** AI không có khả năng tự suy luận đâu là component chính thức của hệ thống, đâu là bản thử bạn quên xoá 2 tuần trước. Nếu file có component không dùng, biến thể trùng lặp, hay layer ẩn từ những lần thử nghiệm cũ, AI sẽ đưa hết vào component inventory. Kết quả là prototype ở các lesson sau sẽ phình to với những thứ không ai định dùng.

Tài liệu hướng dẫn chính thức của Figma về MCP cũng xác nhận điều này: chất lượng code AI tạo ra phụ thuộc trực tiếp vào cách file được cấu trúc, không chỉ vào prompt. Vài quy tắc quan trọng nhất, bạn đã quen thuộc từ session Atomic Design rồi:

| Quy tắc | Vì sao AI cần nó |
|---|---|
| Mọi thứ lặp lại phải là component | Nếu button chỉ là một nhóm shape rời rạc, AI không biết đó là 1 thành phần tái sử dụng |
| Đặt tên layer/component rõ ràng, có ý nghĩa | Tên như "Frame1268", "Group5" không nói gì về chức năng; tên như "CardContainer", "CTA_Button" giúp AI hiểu ngay nó dùng để làm gì |
| Dùng Figma variables cho token | Màu, chữ, spacing, radius nên là variable, không phải giá trị gõ tay lặp lại ở từng layer |
| Dùng Auto Layout | Giúp AI hiểu đúng ý định bố cục, tránh việc positioning tuyệt đối gây ra code cứng nhắc |
| Thêm annotation cho hành vi khó thấy bằng mắt | Ví dụ "card này auto-scroll ngang" hay "nút này disable khi form trống", những điều AI không đoán được chỉ từ hình |

**Checklist dọn dẹp trước khi build:**
- Xoá hoặc archive những component không dùng trong prototype này
- Gộp các biến thể trùng lặp của cùng 1 component (ví dụ 2 button hơi khác nhau nhưng đặt tên khác nhau)
- Xoá layer ẩn, layer test và những frame thử nghiệm cũ không còn dùng
- Kiểm tra tên gọi nhất quán, cùng 1 component không nên có 2 tên khác nhau ở 2 nơi

Nếu file của bạn đủ lớn để không thể rà bằng mắt, dùng prompt sau với AI chat tool: *"Đây là danh sách component trong file Figma của tôi: [dán danh sách]. Cái nào trông giống bản trùng lặp, biến thể không dùng, hoặc thử nghiệm một lần rồi bỏ, thay vì component thật của hệ thống?"*

Bước này dễ bị coi là việc phụ, không phải việc thật. Nhưng không phải vậy. Đây chính là khác biệt giữa một component inventory chính xác, và một component inventory lộn xộn được build trên một file chưa dọn.

---

## Bài Tập 1: Tạo Starter Sheet Cho Câu Chuyện

Bài tập này cứ giữ nhẹ nhàng, cụ thể, và có ích ngay cho Phần B. Thay vì trả lời một loạt câu hỏi dài dòng, tạo một tài liệu nhỏ mà bạn sẽ dùng lại sau này: một trang ghi chú, một frame Figma, hay một bản Notion, gì cũng được.

Hãy điền 4 phần sau:

1. **Dự án của bạn là gì?** Viết 1–2 câu về user và vấn đề mà sản phẩm đang giải quyết.

2. **User goal duy nhất là gì?** Viết theo dạng: *"User muốn [goal]."*

3. **Core flow của bạn là gì?** Chọn 2–3 màn hình và ghi lại chúng theo đúng thứ tự tiến triển.

4. **Concept ban đầu của bạn là gì?** Ghi lại 1–2 dòng về cảm giác, phong cách, hoặc hướng đi bạn muốn cho prototype này.

Bạn có thể thêm một dòng cuối: **"Mình chưa chắc về..."** để ghi lại điều bạn còn phân vân, để giải quyết ở các module sau.

Giữ tài liệu này ở chỗ dễ tìm lại, vì nó sẽ là điểm khởi đầu cho toàn bộ quá trình ở các module tiếp theo.

---

## Bài Tập 2: Thiết Kế 2–3 Screens Trong Figma

Từ user goal và core flow đã chọn ở Bài Tập 1 (Starter Sheet), giờ thiết kế trực quan 2–3 screens đó trong Figma. Đây là bước biến concept bằng lời thành giao diện thật, làm nguyên liệu cho Bài Tập 3.

**Hướng dẫn:**
1. Mở lại Starter Sheet — xác nhận đúng user goal và thứ tự 2–3 screens trong core flow.
2. Tạo file/frame Figma mới cho từng screen theo đúng thứ tự đó.
3. Thiết kế đầy đủ mỗi screen ở trạng thái mặc định (default state), chưa cần polish đẹp, chỉ cần rõ layout, nội dung, và component đang dùng.
4. Nối các screen theo đúng core flow (dùng Figma prototype link nếu muốn xem luồng chạy thử).
5. Lưu file — bạn sẽ dùng chính các screen này ở Bài Tập 3, không thiết kế thêm screen mới.

---

## Bài Tập 3: Set Up Basic Design System (Token, Component Inventory, Design Template)

Nhìn lại các screen vừa thiết kế ở Bài Tập 2, giờ tự tay hệ thống hóa 3 layer pattern đã học ở Lesson 2. Đây là lúc "dựng hộp Lego" bằng tay, để cảm được giá trị của pattern trước khi thấy AI làm việc này nhanh hơn nhiều ở Phần B.

**Hướng dẫn:**
1. **Token:** xem lại 2–3 screen, liệt kê bảng màu, thang chữ, spacing, độ bo góc bạn đã dùng (kể cả chỗ không nhất quán) — viết lại thành 1 bộ token thống nhất duy nhất.
2. **Component Inventory:** liệt kê toàn bộ component xuất hiện trong các screen (button, input, card...), ghi rõ variant và state của từng cái, theo đúng format Lesson 2 (ví dụ: Button — variants Primary/Secondary/Ghost, states Default/Hover/Loading/Disabled).
3. **Template:** gắn nhãn loại tương tác cho từng screen (Read/Edit/Add/Confirm/Navigate/Search-Filter/Onboard), rồi vẽ lại chuỗi màn hình — screen nào dẫn tới screen nào, trong điều kiện gì.
4. **Đối chiếu:** so sánh bảng vừa liệt kê với thiết kế thật ở Bài Tập 2 — có component nào bị lệch (không nhất quán giữa các screen) không? Ghi lại 1–2 ví dụ cụ thể.
5. Lưu tài liệu 3 layer này cùng chỗ với Starter Sheet — đây là bản "làm tay" để đối chiếu khi Phần B dùng AI tự động build lại.

---

## Bài Tập 4: Dọn Dẹp File Figma

*Điểm dừng tự kiểm tra, không nộp bài, trước khi bước sang Section 3.*

Áp dụng checklist dọn dẹp design file (Lesson 4) vào chính file Figma bạn sẽ dùng cho prototype này.

**Việc cần làm:**
1. Rà lại toàn bộ component sẽ dùng trong main journey, xoá component không dùng và gộp biến thể trùng
2. Xoá layer ẩn, frame test cũ
3. Xác nhận tên gọi nhất quán giữa các component
4. Nếu file quá lớn để rà bằng mắt, dùng prompt gợi ý ở Lesson 4 để nhờ AI rà giúp

**Kết quả tối thiểu:** 1 file Figma đã dọn dẹp, sẵn sàng để AI đọc ở Section 3.

---

*Khóa học: Systematic AI Prototyping for Product Designers · Section 2 — Phần A/2*
*Thực hiện bởi Winnie Nguyen · Cập nhật lần cuối tháng 8/2026*

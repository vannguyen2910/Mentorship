# Teleprompter — Lesson 2: Prototype Pattern Là Gì

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 12 — Lesson 2 divider]**

Sang Lesson 2.

Đây là phần lõi, và dài nhất của cả phần này.

Nói về prototype pattern, cụ thể là những thứ AI cần mà hầu hết designer chưa bao giờ viết ra.

**[Slide 13 — 1 document. 3 layer.]**

Ở phần trước, chúng ta đã nói tới khái niệm hộp Lego.

Một prototype pattern chính là tài liệu mô tả hộp Lego đó, viết ra để AI đọc và build theo.

Tài liệu này gồm ba layer: token, component inventory, và template.

Mỗi layer mình sẽ trình bày theo cùng một cách.

Layer đó là gì.

Vì sao cần.

Và làm sao xác định nó.

**[Slide 14 — Layer 1: Token]**

Layer thứ nhất, token.

Câu hỏi ở đây: hệ thống này nên mang cảm giác gì?

Token là những quyết định gốc rễ về cảm giác của hệ thống, chốt trước khi bất kỳ component nào được định nghĩa.

Bảng màu, thang chữ, nhịp khoảng cách, độ bo góc.

Vì sao cần?

Bỏ qua layer này mà nhảy thẳng vào liệt kê component, mỗi component AI tạo ra sẽ có phong cách hơi khác nhau.

Đơn giản vì chưa có quy tắc chung nào được đặt ra từ trước.

Cách xác định?

Bạn chưa cần gì phức tạp.

Chỉ cần mô tả cảm giác mong muốn bằng ngôn ngữ đời thường.

Hệ thống nên êm dịu hay năng động.

Tối giản hay phong phú.

Nghiêm túc hay vui tươi.

Từ đó, bảng màu và thang chữ cụ thể sẽ dần hiện ra.

**[Slide 15 — Layer 2: Component Inventory]**

Rồi tới layer thứ hai, component inventory.

Câu hỏi lúc này: bạn có gì, và nó trông ra sao?

Đây là bản liệt kê đầy đủ những component nào đang tồn tại trong hệ thống, và mỗi cái có thể biến đổi ra sao.

Cái quan trọng không phải hình thức của component, mà là bản chất và chức năng của nó.

Vì sao cần?

Component không được liệt kê trước, mỗi màn hình sẽ được AI build ra một biến thể hơi khác của cùng một component.

Đúng vấn đề component bị lệch mà chúng ta vừa nói ở phần trước.

Cách xác định?

Với mỗi component, ghi lại toàn bộ variant và state nó có thể mang.

Ví dụ, một Button có thể có ba variant: Primary, Secondary, Ghost.

Và bốn state: Default, Hover, Loading, Disabled.

Nguyên tắc này không chỉ áp dụng cho component nhỏ như button.

Một màn hình lớn như Dashboard cũng vậy, state của cả màn hình cũng nên được liệt kê ở đây luôn.

**[Slide 16 — Layer 3: Template]**

Và layer cuối cùng, template.

Câu hỏi ở đây: màn hình này đang làm loại việc gì, và dẫn tới đâu?

Nghĩ tới một trò chơi board game xem.

Mỗi ô trên bàn cờ thường ứng với một loại nhiệm vụ quen thuộc.

Xem thông tin, chỉnh sửa, hay thực hiện một giao dịch.

Template cũng vậy, gồm hai phần: danh mục loại tương tác, và chuỗi màn hình cụ thể.

Vì sao cần?

Không có bản đồ này, AI buộc phải đoán màn hình này dẫn tới đâu, thay vì được nói rõ.

Và mỗi lần đoán có thể ra một kết quả khác.

Cách xác định?

Gắn nhãn template cho từng màn hình trước.

Rồi vẽ ra: màn hình này dẫn tới màn hình nào, trong điều kiện gì.

**[Slide 17 — Danh mục 7 loại template]**

Danh mục đó gồm bảy loại template hay lặp lại nhất.

Read, là xem nội dung, không thay đổi gì, như dashboard hay trang hồ sơ.

Edit, là chỉnh sửa nội dung đã có sẵn, như cài đặt hay sửa hồ sơ.

Add, là tạo ra thứ gì đó mới, như đăng bài mới hay thêm vào giỏ hàng.

Confirm, là xem lại và duyệt một hành động, như xác nhận thanh toán.

Navigate, là di chuyển giữa các phần, như thanh tab hay menu.

Search hoặc Filter, là tìm kiếm hoặc lọc một danh sách.

Và Onboard, là hướng dẫn user lần đầu sử dụng.

Nhưng đừng cố dùng hết cả bảy loại.

Hầu hết prototype chỉ cần ba đến bốn loại thôi.

Và một màn hình có thể mang nhiều template cùng lúc.

Ví dụ, màn hình checkout vừa là Edit, chỉnh số lượng, vừa là Confirm, xác nhận thanh toán.

Một khi template Confirm đã được định nghĩa rõ, bạn dùng lại nó cho bất kỳ chỗ nào cần người dùng xem lại trước khi phê duyệt.

Khỏi phải định nghĩa lại từ đầu.

**[Slide 18 — Màn hình này dẫn tới đâu?]**

Gắn nhãn template xong rồi, bước tiếp theo là vẽ ra.

Màn hình này dẫn tới màn hình nào, trong điều kiện gì.

Ví dụ, Login Screen, template Confirm.

Thành công, dẫn tới Home Dashboard.

Lỗi, quay lại chính Login Screen, ở error state.

Quên mật khẩu, dẫn tới Password Reset Screen.

Cả hai nhánh đều cần được vẽ ra.

Không chỉ đường đi khi mọi thứ suôn sẻ.

**[Slide 19 — 3 layer, 1 document]**

Ba layer này bạn có thể nhờ AI viết ra.

Hoặc tự tay thiết lập trong Figma, đặt tên component rõ ràng, ghi chú loại template ngay trong file.

Dùng công cụ gì không quan trọng bằng việc cả ba layer đều được viết ra ở một chỗ rõ ràng.

Ai đọc vào cũng hiểu, kể cả AI lẫn đồng đội trong nhóm.

Khi cả ba layer, token, component inventory, và template, được đưa đủ cho một AI tool, nó không còn phải đoán mò nữa.

AI biết hệ thống nên mang cảm giác gì.

Biết những gì đang tồn tại, kể cả mọi trạng thái có thể xảy ra.

Biết từng màn hình đang làm loại việc gì.

Và biết các màn hình nối với nhau ra sao.

Nhờ vậy, prompt cụ thể hơn, output nhất quán hơn.

Và prototype trở thành thứ bạn có thể mang đi trình bày cho stakeholder, hoặc dùng để test với user thật.

Ba layer này chính là một hộp Lego hoàn chỉnh, đầy đủ, dùng lại được cho bất kỳ sản phẩm nào.

Nhưng một hộp Lego, dù đầy đủ tới đâu, cũng không tự quyết định bạn sẽ lắp ra cái gì.

Câu hỏi tiếp theo không còn là hệ thống này có gì.

Mà là lần này, bạn muốn dùng nó để kể câu chuyện nào.

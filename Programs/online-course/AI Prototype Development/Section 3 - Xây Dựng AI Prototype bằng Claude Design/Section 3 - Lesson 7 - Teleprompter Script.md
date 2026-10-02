# Teleprompter — Lesson 7: Xây Dựng Main Journey (kèm Practice 1, 3 và kết thúc phần này)

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 32 — Lesson 7 divider]**

Sang Lesson 7: xây dựng main journey.

Lần đầu tiên, ý tưởng của bạn bắt đầu trở thành một prototype có thể chạm vào.

Đây là lần build thật đầu tiên.

Nếu bản build đầu tiên chưa đẹp, bạn không làm sai.

**[Slide 33 — Đừng đánh giá cả quy trình qua lần build đầu tiên]**

AI có thể nhanh chóng dựng cấu trúc và giao diện ban đầu.

Nhưng spacing, hierarchy, grouping, và những chi tiết tạo nên chất lượng cuối cùng của UI vẫn cần bạn review và tinh chỉnh.

Mục tiêu của lần build đầu tiên không phải là hoàn hảo.

Mà là có một nền tảng đủ tốt để bắt đầu làm việc.

Kết quả đầu tiên thường "ổn từ xa, chưa ổn khi nhìn gần".

Đây không phải vì bạn prompt sai, mà là giới hạn hiện tại của công nghệ.

**[Slide 34 — Build. Review. Rồi mới tiếp tục.]**

Dùng khung prompt năm thành phần, build lần lượt từng màn hình trong main journey.

Hai đến bốn màn hình bạn đã chọn từ trước, cùng thể hiện một user goal duy nhất.

Build màn hình đầu tiên.

Review kết quả.

Sửa những gì cần thiết.

Rồi mới chuyển sang màn hình tiếp theo.

Giữ flow context trong mỗi prompt để AI hiểu màn hình đang nằm ở đâu trong journey.

Đúng công thức: build, review, continue.

Không phải một prompt cho cả journey.

**[Slide 35 — AI càng phải xử lý nhiều thứ cùng lúc, càng dễ bỏ sót điều quan trọng]**

Đến bước này, bạn đã có Design Tokens, đã có Components, đã có Template, thậm chí cả PRD và Wireframe.

Nhưng có đủ tất cả không có nghĩa là nên đưa hết vào một prompt để build cả journey cùng lúc.

Nghiên cứu về "context rot" cho thấy mọi model hàng đầu đều giảm chất lượng output khi input dài ra, kể cả khi thông tin cần thiết đã nằm sẵn trong đó.

Thông tin ở giữa một prompt dài dễ bị bỏ sót hơn thông tin ở đầu hoặc cuối.

Có kế hoạch đầy đủ từ đầu không loại bỏ nhu cầu thực thi từng phần nhỏ, có ranh giới rõ ràng.

Build tuần tự giúp từng prompt tập trung và chính xác hơn.

Đây là giới hạn của công nghệ, không phải bạn làm sai.

**[Slide 36 — Ví dụ: build main journey]**

Ví dụ thực tế, main journey "Travel Buddy".

Ba màn hình: Onboarding, "Explore without signing up", rồi tới Explore feed ở chế độ guest, rồi tới Tip Detail khi tap vào một Tip Card.

Đây là build prompt đầy đủ cho màn hình giữa, Explore feed, dùng đúng khung năm thành phần với dữ liệu thật.

Build màn hình Explore feed cho một user đang ở guest mode, chưa đăng ký nhưng đang khám phá những địa điểm được gợi ý.

Người dùng có thể xem tip từ local và traveler thật.

Màn hình cần có header hiển thị "Near Chiang Mai" và số lượng tip, mode switcher gồm Near Me, Country, Map, search bar và filter button có badge hiển thị số lượng filter đang bật, banner nhắc người dùng rằng họ đang ở guest mode, feed các Tip Card với ảnh full-bleed, crowd level badge, quote, author và thời gian đăng, guest paywall ở cuối feed, và bottom navigation cố định với năm tab.

Màn hình này đến từ Onboarding sau khi user chọn "Explore without signing up".

Giữ lại guest mode trong journey.

Khi user tap vào một Tip Card, dẫn tới Tip Detail.

Sử dụng component inventory và design template đã tạo trước đó.

Để ý prompt này không có chỗ nào AI phải tự đoán.

Layout cụ thể tới từng khối, content là dữ liệu thật lấy từ chính sản phẩm, và flow context nêu rõ cả hai chiều, đến từ đâu và dẫn đi đâu.

Đây chính là mức độ chi tiết bạn nên nhắm tới cho mỗi màn hình trong main journey của mình.

**[Slide 37 — Một màn hình đẹp vẫn có thể là một màn hình sai]**

AI tạo ra bản build đầu tiên, nhưng bạn mới là người quyết định nó có đúng hay không.

Mở màn hình AI vừa tạo cạnh file Figma gốc, rồi tự hỏi sáu câu.

Màn hình có đúng mục tiêu không?

Người dùng có biết mình đang ở đâu không?

Thông tin có được ưu tiên đúng không?

Component và pattern có nhất quán không?

Hành động tiếp theo có rõ ràng không?

Màn hình có kết nối đúng với journey không?

Ghi lại những điểm cần chỉnh, chưa cần sửa ngay.

Con mắt của bạn là thứ biến một prototype "trông đúng" thành một prototype thực sự đúng.

Nếu bạn thấy nản vì kết quả chưa đẹp, đây là cảm giác bình thường, không phải dấu hiệu bạn đang làm sai.

Đó không phải một khiếm khuyết của quy trình.

Đó chính là công việc của một designer trong quy trình này.

**[Slide 38 — Practice 1: Generate component inventory và template]**

Trước khi qua bước build đầy đủ, một điểm dừng tự kiểm tra.

Chạy lại prompt tạo component inventory trên file Figma đã dọn dẹp của bạn.

Chạy lại prompt tạo template dựa trên inventory vừa có.

Đối chiếu hai kết quả này với bản viết tay từ trước, ghi lại ít nhất một điểm khác biệt, nếu có, và lý do.

Mục tiêu không phải đúng một trăm phần trăm.

Mục tiêu là học cách AI "đọc" design system.

Kết quả tối thiểu: một component inventory và một template đã xác nhận, sẵn sàng dùng để build main journey.

**[Slide 39 — Practice 2: Build main journey (2-4 màn hình)]**

Áp dụng toàn bộ khung prompt năm thành phần và quy trình build-review từng màn hình để có main journey chạy được.

Việc còn lại là làm thật.

Viết build prompt đầy đủ năm thành phần cho từng màn hình trong main journey.

Build và review từng màn hình cạnh file Figma gốc.

Nối các màn hình theo đúng flow context đã nêu trong prompt.

Kết quả tối thiểu: main journey hai đến bốn màn hình, chạy được trong trình duyệt, dùng nhất quán component và token từ cùng một hệ thống.

Đây là kết quả bạn sẽ mang sang phần tiếp theo để tinh chỉnh và mở rộng.

**[Slide 40 — Kết thúc phần này]**

Prototype đầu tiên không cần hoàn hảo.

*(để một khoảng lặng ngắn ở đây)*

Cần đúng hệ thống.

Đến đây, bạn đã có một main journey hoạt động với component và design token nhất quán.

Nhưng đây mới chỉ là bước đầu.

Phần tiếp theo sẽ tập trung vào việc tinh chỉnh chất lượng, mở rộng thêm các journey còn lại, và scale prototype thành một hệ thống có thể sử dụng trong thực tế.

# Teleprompter — Lesson 1: Xây Dựng Các Journey Còn Lại (kèm Practice 1)

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 1 — Cover]**

Chào mừng bạn tới phần Practice: Xây Dựng Prototype Bằng AI.

Phần trước để lại cho bạn một main journey gồm hai tới bốn màn hình đã chạy được.

Chưa hoàn hảo, nhưng đã có nền tảng.

Một component inventory và một bộ token dùng chung.

Đây là lúc mở rộng từ đó.

Phần này không phải "sửa cho đẹp".

Đây là build các journey còn lại, và học cách mở rộng hệ thống đúng lúc.

**[Slide 2 — Lộ trình phần này]**

Từ một journey, mở rộng thành cả hệ thống.

Bắt đầu với journey tiếp theo.

Lặp lại quy trình đã biết: build, review, tiếp tục.

Khi một pattern lặp lại đủ nhiều, quyết định có nên đưa nó thành component hoặc template dùng chung.

Mở rộng hệ thống từng bước, chỉ khi prototype thực sự cần.

Lesson đầu tiên không có kỹ thuật mới, chỉ lặp lại quy trình build và review bạn đã học.

Phần mở rộng hệ thống thật sự nằm ở lesson sau.

Ghi nhớ insight này: build trước, thấy pattern lặp lại, rồi mới quyết định mở rộng.

**[Slide 3 — Lesson 1 divider]**

Bắt đầu với Lesson 1: xây dựng các journey còn lại.

Không có kỹ thuật mới nào ở đây.

Bạn chỉ cần lặp lại quy trình build và review đã học, cho các user goal còn lại.

Khác biệt duy nhất, lần này bạn mang theo bài học.

Lỗi đã gặp.

Cách sửa.

Từ main journey đầu tiên.

**[Slide 4 — Hoàn thành một journey. Rồi mới chuyển sang journey tiếp theo.]**

Với mỗi journey, đi theo đúng quy trình.

Viết một build prompt đầy đủ năm thành phần, bao gồm cả flow context nối với journey trước.

Build từng màn hình và review cạnh file Figma gốc.

Fix những gì cần fix trước khi chuyển sang màn hình tiếp theo.

Build.

Review.

Rồi mới tiếp tục.

Đừng build tất cả các journey cùng một lúc.

Hoàn thành một journey trước.

Review nó.

Fix những gì cần fix.

Sau đó mới chuyển sang journey tiếp theo.

Đây vẫn là nguyên tắc bạn đã áp dụng khi build main journey đầu tiên, chỉ là bây giờ áp dụng nó ở quy mô lớn hơn.

**[Slide 5 — Đừng dồn hết vào 1 prompt]**

Đến thời điểm này, bạn đã có khá nhiều thứ để đưa cho AI.

Design Tokens.

Components.

Templates.

PRD.

Wireframes.

Main journey đã build làm reference.

Và chính vì có quá nhiều thứ sẵn có, bạn rất dễ nghĩ: hay là đưa hết vào một prompt và build luôn tất cả các journey?

Nghe có vẻ nhanh hơn.

Nhưng input càng lớn, AI càng dễ bỏ sót những chi tiết quan trọng.

Đó chính là vấn đề về context rot.

Vì vậy, vẫn cứ đi từng bước.

Một journey.

Một màn hình.

Một lần review.

Đó thường là cách nhanh hơn để đi đến một kết quả đúng.

**[Slide 6 — Lỗi lặp lại? Sửa 1 chỗ, không sửa từng màn hình.]**

Ví dụ, nếu bạn phát hiện spacing hoặc màu sắc đang sai trong main journey.

Kiểm tra xem lỗi đó có xuất hiện ở những journey tiếp theo không.

Vì tất cả đều đang build từ cùng một component inventory và token system.

Một lỗi có thể xuất hiện ở nhiều nơi.

Nếu đúng là lỗi của component hoặc token, hãy sửa ở đó.

Fix một chỗ.

Mọi nơi dùng nó sẽ được hưởng lợi.

Đó chính là lợi ích thực tế của pattern-first approach mà bạn đã xây dựng từ trước.

**[Slide 7 — Đẹp không có nghĩa là đúng]**

Sau mỗi lần build, quay lại đúng sáu câu hỏi đã dùng ở main journey đầu tiên.

Màn hình này có đúng mục tiêu không?

Người dùng có biết mình đang ở đâu không?

Thông tin đã được ưu tiên đúng chưa?

Components và patterns có nhất quán không?

Next action có rõ ràng không?

Màn hình này có kết nối đúng với journey không?

Ngay cả khi bạn đã build đến journey thứ hai hoặc thứ ba.

Đừng để việc một màn hình trông đẹp khiến bạn bỏ qua việc kiểm tra xem nó có thật sự phục vụ đúng user goal hay không.

**[Slide 8 — Mở tất cả journey cạnh nhau]**

Trước khi kết thúc, kiểm tra consistency.

Mở các journey cạnh nhau.

Nhìn vào những thứ dễ bị lệch: buttons, colors, spacing, typography, components, interaction patterns.

Chúng có còn nhất quán không?

Nếu có, đó là bằng chứng cho thấy pattern-first approach đang thực sự hoạt động.

Không phải vì bạn tình cờ làm mọi thứ giống nhau.

Mà vì tất cả các journey đều được build dựa trên cùng một source of truth.

Bạn cũng có thể mở design_system.html cạnh các journey để đối chiếu trực tiếp.

Đừng cố nhớ design system.

Mở nó lên và kiểm tra.

Kết quả tối thiểu: toàn bộ journey đã chọn chạy được trong browser, có navigation kết nối giữa các journey, dùng nhất quán components và tokens từ cùng một system.

**[Slide 9 — Practice 1: Build & Review một journey khác]**

Lần này, không có ai build mẫu cho bạn.

Bạn tự chọn một user goal khác.

Tự viết prompt.

Tự build.

Rồi tự review.

Đây không phải là một bài nộp.

Đây là lúc kiểm tra xem quy trình đã thực sự trở thành một workflow của bạn chưa, từ việc viết prompt, build màn hình, review kết quả, đến việc biết mình cần fix gì.

Chọn một user goal khác với main journey.

Tự viết build prompt.

Đính kèm các design file bạn có, hoặc mô tả những gì AI cần biết trong prompt.

Build journey.

Đối chiếu với main journey.

Review bằng sáu câu hỏi.

Fix những gì cần thiết.

Kết quả tối thiểu: một journey mới chạy được, đã đi qua đủ sáu câu hỏi review, components và tokens nhất quán với main journey, và biết rõ mình cần fix gì trước khi tiếp tục.

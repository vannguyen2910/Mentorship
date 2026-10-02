# Demo Script — Lesson 4: 5 Quy Tắc Dọn File Trước Khi AI Đọc

> **Nguồn:** Chuyển từ Section 3 Lesson 1, theo quyết định restructure khóa học tháng 8/2026 — dọn dẹp file Figma giờ thuộc về Section 2 (chuẩn bị trước khi chạm AI), không phải mở đầu Section 3 (build bằng Claude Design). Nội dung demo giữ nguyên không đổi.

Đọc như đang nói chuyện trực tiếp với người học. Không cần đọc đều từng câu. Một số câu ngắn được tách riêng để tạo nhịp khi nói. Các dòng `[Demo X — ...]` là mốc để chuyển sang thao tác trong Figma, không đọc thành tiếng. Thời lượng ước tính: khoảng 4 phút, mở file Figma ví dụ để demo song song lúc nói.

---

[Demo 1 — Mở đầu]

AI không có khả năng tự suy luận đâu là component chính thức của hệ thống.

Đâu là bản thử bạn quên xoá hai tuần trước.

Tài liệu chính thức của Figma về MCP xác nhận đúng điều này.

Chất lượng code AI tạo ra phụ thuộc trực tiếp vào cách file được cấu trúc.

Không chỉ vào prompt bạn viết.

Để thấy rõ điều đó, mình sẽ mở một file Figma ví dụ.

Đi qua từng quy tắc một, cho bạn thấy sự khác biệt bằng mắt.

[Mở file Figma ví dụ.]

[Demo 2 — Trước và sau khi dọn dẹp]

Trước khi vào từng quy tắc cụ thể, nhìn qua ví dụ này.

[Demo: mở file 1, một design system tải về từ nguồn có sẵn trên mạng.]

Đây là một design system bạn có thể tải về ở bất kỳ đâu.

Nhìn vào, có rất nhiều variant.

Nhiều cái trong số này, dự án của bạn sẽ không bao giờ dùng tới.

Nếu bạn feed thẳng file này cho AI.

Nó không biết variant nào bạn thật sự cần.

AI sẽ đưa hết vào component inventory, kể cả phần bạn không dùng.

[Demo: chuyển sang file 2, cùng design system nhưng đã được tối ưu hoá.]

Còn đây là cùng một design system.

Nhưng đã được tối ưu hoá.

Chỉ giữ lại đúng những gì dự án này cần.

Không hơn.

File càng gọn, AI càng đọc đúng.

Component inventory sinh ra càng sát với thứ bạn thật sự sẽ dùng.

Đây chính là lý do bước dọn dẹp luôn đứng đầu tiên, trước khi đi vào từng quy tắc cụ thể.

Giờ mình cùng xem 5 quy tắc đó là gì.

[Demo 3 — Quy tắc 1: Component hoá mọi thứ lặp lại]

Quy tắc đầu tiên: mọi thứ lặp lại phải là component.

[Demo: trỏ vào một button chỉ là nhóm shape rời rạc, chưa được component hoá.]

Nhìn cái button này.

Nó chỉ là một nhóm shape, rectangle với text nằm rời rạc bên trong.

Với mắt người, bạn biết ngay đây là một button.

Nhưng AI thì không.

Nó không biết đây là một thành phần tái sử dụng, hay chỉ là một nhóm shape ngẫu nhiên.

[Demo: chuyển sang phiên bản đã component hoá, chỉ vào icon component ở panel layer.]

Còn cái này đã được tạo thành component thật.

AI đọc ngay được: đây là một thành phần, có thể tái sử dụng ở nhiều nơi.

[Demo 4 — Quy tắc 2: Đặt tên rõ ràng]

Quy tắc thứ hai: đặt tên layer và component rõ ràng, có ý nghĩa.

[Demo: trỏ vào một layer tên "Frame 1268" hoặc "Group 5".]

Tên như "Frame 1268" không nói cho AI biết gì cả.

Nó chỉ là một con số Figma tự đặt.

[Demo: chỉ sang một component đã đặt tên rõ, ví dụ "CardContainer" hay "CTA_Button".]

Còn tên như "CardContainer", "CTA_Button", AI hiểu ngay chức năng chỉ từ cái tên.

Đây là bước nhỏ, tốn vài giây mỗi lần đặt tên.

Nhưng nhân lên cả trăm layer trong một file, sự khác biệt rất lớn.

[Demo 5 — Quy tắc 3: Dùng Figma variables cho token]

Quy tắc thứ ba: dùng Figma variables cho token.

[Demo: mở panel fill của một shape, chỉ vào giá trị hex code gõ tay.]

Nếu màu này chỉ là một giá trị hex gõ tay.

AI không biết đây là token màu chính của hệ thống, hay chỉ là một màu bạn chọn ngẫu nhiên lúc thử nghiệm.

[Demo: chuyển sang một shape dùng variable, chỉ vào tên variable, ví dụ "color/primary".]

Còn khi giá trị này được gán vào một variable, có tên rõ ràng.

AI đọc thẳng ra: đây là token, dùng lại ở mọi nơi cần màu chính.

Áp dụng y hệt cho typography và spacing.

[Demo 6 — Quy tắc 4: Dùng Auto Layout]

Quy tắc thứ tư: dùng Auto Layout.

[Demo: chỉ vào một frame dùng positioning tuyệt đối, các phần tử đặt tự do.]

Frame này, các phần tử được đặt tự do bằng toạ độ x, y.

AI không biết ý định bố cục của bạn là gì.

Phần tử nào nên nằm cạnh nhau, phần tử nào nên co giãn theo nội dung.

[Demo: chuyển sang một frame dùng Auto Layout, chỉ vào icon Auto Layout ở panel bên phải.]

Còn frame này dùng Auto Layout.

AI đọc được đúng ý định: đây là một hàng, đây là một cột, khoảng cách giữa các phần tử là bao nhiêu.

Kết quả là code sinh ra dùng flexbox hoặc grid thật, không phải positioning cứng nhắc.

[Demo 7 — Quy tắc 5: Thêm annotation cho hành vi khó thấy]

Quy tắc cuối cùng: thêm annotation cho hành vi khó thấy bằng mắt.

[Demo: chỉ vào một card hoặc component có hành vi đặc biệt, ví dụ auto-scroll ngang hoặc nút disable theo điều kiện.]

Nhìn card này, bạn biết nó auto-scroll ngang khi có nhiều item.

Nhưng đó là điều bạn biết vì bạn thiết kế nó.

AI chỉ nhìn thấy một hình ảnh tĩnh.

Nó không đoán được hành vi này chỉ từ mỗi cái nhìn.

[Demo: thêm một comment hoặc annotation ngắn ngay cạnh component, ví dụ "auto-scroll ngang khi > 4 item".]

Một dòng annotation ngắn ngay tại đây, là đủ để AI biết điều nó không thể tự suy luận.

[Demo 8 — Kết]

Năm quy tắc này không phải kiến thức mới.

Bạn đã quen thuộc từ trước.

Điều khác biệt là giờ bạn áp dụng nó với một mục tiêu rõ ràng: để AI đọc đúng file của bạn.

Trước khi build bất kỳ điều gì, hãy dành thời gian rà lại file theo đúng năm quy tắc này.

Đây chính là khác biệt giữa một component inventory chính xác.

Và một component inventory lộn xộn, build trên một file chưa dọn.

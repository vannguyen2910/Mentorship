# Teleprompter — Lesson 6: Những Lưu Ý Khi Thiết Lập Foundation

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 26 — Lesson 6 divider]**

Sang Lesson 6: những lưu ý khi thiết lập foundation.

Bạn không cần viết một prompt thật dài.

Chỉ cần nói đủ những điều AI cần biết để hiểu màn hình bạn muốn xây.

Giờ bạn đã có component inventory và template đáng tin cậy.

Câu hỏi tiếp theo không phải "viết prompt sao cho dài và chi tiết".

Mà là làm sao truyền đạt đúng ý định thiết kế, để AI không phải tự đoán bất kỳ điều gì.

**[Slide 27 — Goal. Layout. Content. Audience. Flow context.]**

Một nghiên cứu năm 2025 của NN/g, thử nghiệm nhiều loại AI prototyping tool trên cùng một bài toán thiết kế thực tế, cho ra một kết luận khá rõ ràng.

Prompt càng cụ thể, output càng gần với kết quả của một designer thật.

Khi prompt chỉ nêu mục tiêu chung chung, mỗi công cụ AI tự đoán theo một hướng khác nhau.

Nhưng khi prompt nêu rõ layout, component, và trạng thái tương tác cần có, output từ nhiều công cụ khác nhau đều bám sát ý định ban đầu.

Tin tốt là bạn không cần học một kỹ năng hoàn toàn mới.

Năm thành phần dưới đây chính là năm câu hỏi một Product Designer thường đã tự hỏi khi thiết kế.

Chỉ khác là giờ bạn cần nói chúng ra thành lời, để AI cũng "biết" những gì bạn đã biết.

Goal, người dùng cần làm gì ở đây.

Layout, nội dung được sắp xếp và ưu tiên như thế nào.

Content, dữ liệu thật người dùng sẽ nhìn thấy là gì, không phải lorem ipsum.

Audience, ai đang sử dụng màn hình này.

Và Flow context, họ đến từ đâu, đang ở đâu, và sẽ đi đâu tiếp theo.

**[Slide 28 — Đừng chỉ mô tả màn hình. Hãy cho AI biết nó nằm ở đâu trong journey.]**

Một màn hình không tồn tại một mình.

Flow context là thành phần dễ quên nhất, vì nó không mô tả màn hình này, mà mô tả quan hệ giữa các màn hình.

Khi thiếu flow context, AI nhìn mỗi màn hình như một bài toán riêng.

Kết quả có thể đúng ở từng bước, nhưng khi nối lại, journey lại không còn liền mạch.

Hãy luôn cho AI biết bốn điều: người dùng đến từ đâu, họ đã làm gì trước đó, màn hình hiện tại cần giải quyết điều gì, và họ có thể đi đâu tiếp theo.

Đây đúng là vấn đề AI không lưu lại thông tin mà chúng ta đã nói trước đó.

Mỗi lần nhờ AI, nó không giữ lại gì từ lần trước, mỗi prompt là một điểm xuất phát mới nếu không có tài liệu để đọc lại.

Chỉ khác là lần này lỗi nằm ở người viết prompt quên nhắc, không phải AI quên nhớ.

**[Slide 29 — Đừng viết lại từ đầu. Dùng cùng một khung.]**

Build màn hình, nêu Goal, người dùng đang cố làm gì ở đây.

Layout, cách sắp xếp.

Content, tên field và dữ liệu mẫu thật, không phải lorem ipsum.

Audience, ai đang dùng.

Flow context, màn hình này đến từ đâu và dẫn tới đâu, giữ lại dữ liệu hay trạng thái cần mang theo.

Dùng toàn bộ component inventory và template ở trên, không chỉ phần liên quan tới màn hình này.

Khớp đúng tên component.

Dùng cùng một khung này cho mọi màn hình trong journey, sang màn hình tiếp theo bạn chỉ cần thay nội dung phù hợp.

Một khung nhất quán giúp bạn không bỏ sót thông tin quan trọng, so sánh các màn hình với nhau dễ hơn, giữ context xuyên suốt journey, và tái sử dụng được prompt khi build main journey và cả khi mở rộng sau này.

Nếu bạn có ảnh tham chiếu, chẳng hạn một màn hình tương tự, một layout đối thủ, hay cảm hứng thị giác, hãy đính kèm nó trước khi prompt.

Nghiên cứu của NN/g ghi nhận: khi prompt có kèm ảnh tham chiếu hoặc link Figma frame, output sát với thiết kế gốc hơn hẳn so với chỉ mô tả bằng lời.

"Một tấm ảnh đáng giá ngàn từ" hoá ra đúng cả với AI.

**[Slide 30 — Tài liệu có sẵn không thay thế framework]**

Đã có PRD, wireframe, hoặc user flow?

Bạn không cần bắt đầu từ một trang giấy trắng.

PRD, wireframe, user flow, và solution list đều là nguồn context có giá trị.

Nhưng chúng không thay thế năm thành phần trên, chúng giúp bạn điền framework nhanh hơn.

Dùng tài liệu có sẵn để trả lời nhanh hơn, đặc biệt là Goal, Audience, và Flow context.

Sau đó chỉ lấy phần liên quan tới màn hình đang build.

Đừng đưa toàn bộ tài liệu vào một prompt và yêu cầu AI build cả journey cùng lúc.

Càng nhiều context không liên quan, AI càng dễ bỏ sót chi tiết quan trọng.

**[Slide 31 — Markdown cho nội dung. Hình ảnh cho layout.]**

Không phải mọi thứ đều nên biến thành text.

Với PRD và user flow, markdown giúp AI đọc trực tiếp nội dung và hiểu cấu trúc qua heading, hierarchy.

Đây là hướng đúng nếu bạn có thói quen convert tài liệu sang định dạng markdown.

Nhưng với wireframe, hãy giữ nguyên hình ảnh.

Vị trí, tỷ lệ, và mối quan hệ không gian thường khó truyền đạt đầy đủ bằng một đoạn mô tả chữ.

Nếu cần ghi chú hành vi khó thấy bằng mắt, thêm caption ngắn cạnh ảnh, đúng nguyên tắc annotation đã học trước đó, không thay hẳn ảnh bằng text.

Lưu các tài liệu này làm context tham chiếu thường trực trong local folder, tương tự cách rules file trỏ tới design_system.html.

Khi build một màn hình, chỉ đưa phần liên quan vào prompt, thay vì dán toàn bộ file mỗi lần.

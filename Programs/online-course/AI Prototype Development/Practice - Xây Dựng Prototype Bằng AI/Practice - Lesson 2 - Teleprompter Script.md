# Teleprompter — Lesson 2: Mở Rộng Design System Đúng Cách (kèm kết thúc phần này)

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 10 — Lesson 2 divider]**

Sang Lesson 2: mở rộng design system đúng cách.

Không phải màn hình mới nào cũng cần một component mới.

Càng build nhiều màn hình, bạn càng dễ rơi vào một trong hai tình huống.

Một là ép mọi màn hình dùng lại component cũ, ngay cả khi nó không còn phù hợp.

Hai là tạo một component mới cho mỗi biến thể nhỏ.

Cả hai đều có vấn đề.

Một bên làm UI trở nên gượng ép.

Một bên khiến component inventory nhanh chóng phình to và khó maintain.

Lesson này giúp bạn biết khi nào nên reuse, khi nào nên tạo variant, và khi nào thật sự cần mở rộng system.

**[Slide 11 — Cái này thật sự mới, hay chỉ là 1 biến thể?]**

Trước khi tạo bất cứ thứ gì mới, hãy hỏi ba câu.

Component tương tự đã có trong inventory chưa, chỉ khác state, size, hay content?

Nếu có sự khác biệt, đây nên là một variant của component cũ, hay thật sự là một component riêng?

Nếu cần một template mới, template đó có thể reuse các component hiện có, hay thật sự cần một layout và structure hoàn toàn khác?

Đừng tạo mới chỉ vì nó nhanh hơn.

Default choice nên là reuse.

Chỉ tạo mới khi bạn đã kiểm tra và xác nhận rằng những gì đang có thật sự không đáp ứng được nhu cầu mới.

Đừng tạo một component mới chỉ vì việc tìm lại component cũ mất thêm vài phút.

Vài phút đó có thể giúp bạn tránh một component mới mà sau này phải maintain mãi mãi.

**[Slide 12 — Tra cứu design_system.html, đừng dùng trí nhớ]**

Bạn đã có design_system.html từ trước.

Đây là nơi visualise các token, component, và template hiện có.

Khi gặp một màn hình mới, mở file lên và đối chiếu trực tiếp.

Rồi mới quyết định: reuse, tạo một variant, hay tạo một thứ hoàn toàn mới.

Nếu không chắc, bạn cũng có thể nhờ AI kiểm tra.

Đính kèm design_system.html hiện tại.

Mô tả màn hình cần build.

Hỏi AI: component nào có thể reuse, có component nào cần thêm variant, hay bạn thật sự cần tạo một component mới.

Yêu cầu AI giải thích lý do cho từng recommendation.

Điểm quan trọng là AI cần được đối chiếu với source thật.

Không phải đoán dựa trên những gì bạn mô tả trong chat.

**[Slide 13 — Mở rộng xong. Cập nhật lại ngay.]**

Thêm component hoặc template mới?

Cập nhật lại design_system.html.

Mỗi lần system được mở rộng, generate lại file để nó phản ánh đúng system hiện tại.

Nếu không, file sẽ nhanh chóng trở nên outdated.

Và một file outdated thì không còn đáng tin để làm reference cho lần build tiếp theo.

Kết quả tối thiểu: mọi màn hình mới đều được đối chiếu với design_system.html trước khi build, inventory chỉ tăng khi thật sự cần, và mỗi lần mở rộng system đều được cập nhật lại vào design_system.html.

**[Slide 14 — Kết thúc phần này]**

Hệ thống đúng.

*(để một khoảng lặng ngắn ở đây)*

Mở rộng bao nhiêu cũng vững.

Đó là toàn bộ tinh thần pattern-first, xuyên suốt cả hành trình vừa qua.

Định nghĩa một lần.

Build nhất quán ở bất kỳ quy mô nào.

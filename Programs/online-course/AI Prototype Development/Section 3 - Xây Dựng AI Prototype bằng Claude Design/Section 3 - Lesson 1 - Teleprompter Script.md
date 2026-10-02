# Teleprompter — Lesson 1: Thiết Lập Local Folder & Rules File Cho Project

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 9 — Lesson 1 divider]**

Sang Lesson 1: thiết lập local folder và rules file cho project.

Cách chuẩn bị khác nhau tùy loại AI tool bạn dùng.

Nhưng chỉ cần một file duy nhất để giữ cho mọi thứ nhất quán từ đầu tới cuối.

**[Slide 10 — AI Coding Tool hay AI Design Tool?]**

Có hai nhánh, tùy AI tool bạn sử dụng, chỉ cần theo đúng nhánh của mình.

Nếu bạn dùng AI coding tool, một công cụ đọc và ghi code trực tiếp trên máy bạn, bạn cần một folder thật trên máy tính, làm nơi chứa toàn bộ code AI tạo ra.

Tạo một folder mới, đặt tên theo project của bạn.

Mở folder đó trong AI coding tool bạn đang dùng.

Đây sẽ là "nhà" của prototype trong suốt phần còn lại.

Mọi màn hình bạn build đều nằm trong cùng một folder này, không rải rác nhiều nơi.

Nếu bạn dùng AI design tool chạy trên trình duyệt, một công cụ quản lý project của bạn trên cloud, không cần cài gì trên máy, bỏ qua bước tạo folder.

Công cụ dạng này tự quản lý project cho bạn, không có khái niệm folder local.

Đi thẳng sang phần thiết lập MCP.

**[Slide 11 — Rules file]**

Dù bạn dùng loại tool nào, nếu công cụ hỗ trợ một file cấu hình hay instructions ở cấp project, đọc trước mọi prompt, không cần bạn nhắc lại, hãy tạo nó ngay ở bước này.

Đây chính là cơ chế giữ cho việc build về sau nhất quán và mở rộng được, thay vì phải nhắc lại quy tắc ở từng prompt riêng lẻ.

Rules file nên có tối thiểu bốn điều.

Trỏ tới prototype pattern của bạn, làm nguồn tham chiếu bắt buộc cho mọi màn hình.

Quy tắc đặt tên, component và file nên đặt tên theo đúng convention nào.

Một quy tắc quan trọng nhất: luôn kiểm tra component inventory trước khi tạo ra một component mới.

Nếu component tương tự đã tồn tại, dùng lại nó, đừng tạo bản mới.

Và một đường dẫn tới file design_system.html, sẽ thêm sau khi có đủ token, component và template.

Rules file không cần dài.

Một file ngắn, rõ ràng, AI đọc lại được mỗi lần, quan trọng hơn nhiều một file dài mà chẳng ai chắc AI có đọc hết không.

Nếu công cụ của bạn không hỗ trợ rules file cấp project, dán lại ba điều trên vào đầu mỗi prompt build màn hình ở các bước sau.

Chậm hơn một chút, nhưng không phải bước bắt buộc phải bỏ qua.

**[Slide 12 — design_system.html là gì?]**

Vì sao có dòng design_system.html ở rules file, dù chưa tạo được ngay?

Token và component inventory của bạn chưa tồn tại ở bước này, nên chưa thể generate file đó.

Cách tạo nó sẽ được hướng dẫn ngay sau khi cả ba layer đã sẵn sàng.

Ghi chỗ trống này vào rules file ngay từ bây giờ, để bạn không quên cập nhật lại sau.

Design_system.html là một trang HTML duy nhất, hiển thị trực quan mọi token, màu sắc, typography, và component của bạn, kèm đủ variant và state.

Ngành UX gọi kỹ thuật này là "living style guide".

Vì file luôn được AI generate lại từ token và component thật mỗi khi có thay đổi, chứ không viết tay, nên không bao giờ lệch với sản phẩm thực tế.

Từ khi có file này trở đi, đây là nguồn tham chiếu hình ảnh chính, bạn và AI cùng dùng để so sánh mọi màn hình build sau này.

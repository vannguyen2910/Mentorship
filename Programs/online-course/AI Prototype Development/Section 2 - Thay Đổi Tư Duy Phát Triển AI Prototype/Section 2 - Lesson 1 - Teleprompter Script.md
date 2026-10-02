# Teleprompter — Lesson 1: Cái Bẫy Screen-by-Screen

Đọc liền mạch, có câu nối giữa các ý để không bị vấp. Mỗi câu một hàng. Dòng in đậm dạng `[Slide X — ...]` là mốc để biết lúc nào lật slide — không đọc, chỉ liếc qua.

---

**[Slide 1 — Cover]**

Chào mừng bạn đến với Tư Duy Pattern-First.

Phần này không phải một bài học kỹ thuật Figma.

Đây là bài học tư duy.

Vì sao rất nhiều người dùng AI để prototype, mà kết quả vẫn rời rạc?

Và làm sao khắc phục điều đó, trước khi chạm vào bất kỳ màn hình nào?

**[Slide 2 — Lộ trình phần này]**

Phần này gồm ba lesson ngắn.

Cái bẫy screen-by-screen.

Prototype pattern là gì.

Rồi chọn câu chuyện của prototype.

Ba lesson đó dẫn tới ba bài tập nối tiếp nhau.

Viết starter sheet cho câu chuyện của bạn.

Thiết kế hai tới ba screen trong Figma.

Rồi tự tay set up design system từ chính những screen đó.

Chưa cần nhớ hết ngay bây giờ, cứ đi từng lesson một.

**[Slide 3 — Lesson 1 divider]**

Bắt đầu với Lesson 1.

Có ai từng thấy quen cảnh này chưa?

**[Slide 4 — Vòng lặp quen thuộc]**

Hãy tưởng tượng việc xây prototype cũng giống như xây một ngôi nhà bằng Lego.

Thay vì lấy ra một hộp Lego có sẵn, bạn tự nặn một viên gạch mới mỗi khi cần, ở từng phòng riêng biệt.

Và đây là vòng lặp quen thuộc khi prototype theo kiểu đó.

Mở Figma.

Chọn một màn hình, thiết kế nó.

Chọn màn hình khác, thiết kế tiếp.

Thử nối chúng lại.

Nhận ra không khớp.

Quay lại sửa.

Rồi lặp lại từ đầu.

Nhìn qua thì có vẻ ổn.

Nhưng thực ra không phải vậy.

**[Slide 5 — Traditional prototype vs AI-assisted prototype]**

Có hai hướng để nhìn vào chuyện này.

Cách làm truyền thống, gọi là traditional prototype.

Và cách làm có AI hỗ trợ.

Traditional prototype là tự thiết kế từng màn hình một, không có tài liệu nào để tham chiếu.

Cần đổi một thứ, bạn sửa lại từng màn hình.

Càng nhiều màn hình, càng nặng, ba màn hình đã đủ mệt.

Còn cách làm có AI hỗ trợ thì ngược lại.

Định nghĩa hộp Lego một lần, để AI ráp phần còn lại.

Cần đổi một thứ, sửa đúng một chỗ, mọi màn hình tự động đúng theo.

Và điểm quan trọng nhất, reuse cùng một system.

Ba mươi màn hình cũng không khác gì ba màn hình.

**[Slide 6 — Ba thứ âm thầm rạn nứt]**

Vậy vì sao cách làm cũ lại rạn nứt?

Không phải vì bạn làm sai.

Chỉ là chưa có gì được định nghĩa trước khi bắt đầu.

Có ba thứ âm thầm xảy ra vì điều đó.

**[Slide 7 — Vấn đề 1: Component bị lệch]**

Vấn đề đầu tiên, component bị lệch.

Nút bấm ở màn hình 1 có thể khác một chút so với nút bấm ở màn hình 3.

Sự khác biệt này thường không ai để ý.

Cho tới khi cần cập nhật style ở mười hai vị trí khác nhau.

**[Slide 8 — Vấn đề 2: Mỗi prompt một điểm xuất phát mới]**

Vấn đề thứ hai, AI không lưu lại thông tin giữa các lần yêu cầu.

Giống như nhờ ai đó vẽ lại cùng một con mèo nhiều lần.

Nhưng lần nào cũng phải mô tả lại từ đầu, vì người đó chẳng nhớ mô tả cũ.

Nút bấm vừa mô tả xong, lần sau lại phải tả lại, mỗi lần một chút khác nhau.

Vì AI chẳng có điểm nào để tham chiếu cả.

**[Slide 9 — Vấn đề 3: State bị bỏ sót]**

Vấn đề thứ ba, vài trạng thái quan trọng bị bỏ sót.

Màn hình login thường được thiết kế đầy đủ cho trường hợp thành công.

Nhập sai mật khẩu thì sao?

Đang tải thì sao?

Mất mạng thì sao?

Màn hình login của bạn đã có state cho sai mật khẩu chưa?

Những state đó thường chẳng ai nghĩ tới, cho tới khi sản phẩm đã ra đời rồi.

**[Slide 10 — Pattern-first, sửa cả ba cùng lúc]**

Giải pháp cho cả ba vấn đề này, gói gọn trong một cụm từ: pattern-first.

Component bị lệch?

Định nghĩa component tồn tại đúng một lần, trước khi build bất kỳ màn hình nào.

AI bắt đầu lại từ đầu mỗi lần?

Đưa AI một prototype pattern document, để nó build dựa trên đó mỗi lần, không phải đoán mò.

State bị bỏ sót?

Map state trước khi build, không phải vá lại sau.

**[Slide 11 — Chuyển tiếp sang Lesson 2]**

Xây dựng pattern cho prototype không phải một việc làm thêm.

Đây chính là công việc khiến toàn bộ quy trình còn lại diễn ra nhanh hơn.

*(để một khoảng lặng ngắn ở đây trước khi qua slide tiếp theo)*

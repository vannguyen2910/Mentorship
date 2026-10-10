---
title: "Section 6: Stitching Prototype"
subtitle: "Nhiều đoạn rời rạc, một hành trình kể được trọn vẹn: từ bản đồ tới demo 1 phút"
course: Systematic AI Prototyping for Product Designers
section: 6
source-lesson: library/lessons/ai-prototype-development/materials/ai-prototype-development-lesson.md
last-updated: 2026-08-19
language: vi
---

## Tổng Quan Section

Tới lúc này, bạn đã có ít nhất 1 đoạn prototype, có thể build bằng track Claude Design, track Figma Make, hoặc cả 2. Section này không dạy build thêm màn hình nào. Nó dạy cách nối những gì đang có lại thành một hành trình xem được trọn vẹn, sẵn sàng demo cho stakeholder.

Prototype của bạn có thể nằm ở nhiều nguồn khác nhau: nhiều file Figma riêng biệt, một link publish từ Claude Design, một link khác từ Figma Make. Section này áp dụng chung cho cả 2 track, không phân biệt bạn đã chọn tool nào ở phần trước.

**Kết thúc section này, bạn sẽ có thể:**
1. Giải thích thế nào là một stitched prototype, và khi nào cần dùng.
2. Áp dụng quy trình 5 bước để nối nhiều prototype rời rạc, kể cả khi chúng nằm ở nguồn khác nhau, thành một hành trình liền mạch.
3. Nhận biết ranh giới giữa việc AI làm tốt ở từng màn hình và việc chỉ người mới giữ được ở cấp độ cả hành trình.
4. Demo một stitched prototype trong 1 phút, sẵn sàng cho buổi review với stakeholder.

**Nội dung section:**
- 5 lesson nội dung, kết ở 1 Bài Tập riêng
- Cần có: ít nhất 1 đoạn prototype đã build từ trước, không phân biệt track nào

---

## Nội Dung Lesson

### Lesson 1: Stitched Prototype Là Gì
*Nối nhiều đoạn hành trình thành một câu chuyện xem được. Dù chúng chưa từng ở chung một file.*

**Stitched prototype là gì:** một hành trình demo được, ghép lại từ nhiều prototype vốn tách rời, có thể là nhiều đoạn bạn đã build trước đó, nhiều phần do nhiều người làm song song, hoặc nhiều lần generate AI khác nhau. Khác với một prototype liền mạch xây từ đầu trong 1 file, stitch không giả định mọi thứ nằm chung một chỗ.

**Nguồn có thể khác nhau hoàn toàn:** nhiều file Figma riêng biệt, mỗi file 1 journey. Một link publish từ track Claude Design. Một link publish khác từ track Figma Make. Thậm chí một prototype cũ dựng bằng tool khác, còn dùng được. Stitch không cố gộp tất cả vào 1 file. Việc đó thường không khả thi, và cũng không phải mục đích.

**Prototype không chỉ có một vai trò.** Có prototype để test độ chi tiết của 1 màn hình: look and feel. Có prototype để test tính khả thi kỹ thuật: implementation. Và có prototype để test một điều khác hẳn: cả hành trình có kể được đúng câu chuyện không, từ bước đầu tới bước cuối. Stitch nằm ở nhóm cuối. Nó không cần từng đoạn hoàn thiện như nhau. Nó cần cả chuỗi mạch lạc.

**Vì vậy 1 đoạn thô hơn không phải lỗi.** Nếu đoạn giữa hành trình chưa polish bằng đoạn đầu, đó không phải điều cần giấu trước khi demo. Vấn đề chỉ thật sự xảy ra khi người xem không hiểu được cả câu chuyện, không phải khi 1 màn hình chưa đẹp bằng màn hình khác.

**Kết quả tối thiểu:** xác định được stitched prototype của bạn gồm bao nhiêu đoạn, nằm ở nguồn nào. Chưa cần nối, chỉ cần biết rõ phạm vi trước khi bước sang phần sau.

---

### Lesson 2: Quy Trình 5 Bước
*Không nối màn hình với màn hình. Nối bản đồ với bản đồ.*

**Bước 1 · Kiểm kê**
Liệt kê từng đoạn hành trình đang có: nằm ở đâu (file Figma nào, link nào), ai làm, tới đâu rồi. Đừng bỏ qua đoạn còn dở. Kiểm kê để biết rõ mình có gì, không phải để lọc ra đoạn đẹp nhất.

**Bước 2 · Vẽ bản đồ hành trình**
Xếp các đoạn theo đúng thứ tự người dùng sẽ đi qua. Với mỗi đoạn, ghi rõ điểm vào và điểm ra. Đánh dấu đoạn nào cùng nguồn (nối trực tiếp được) và đoạn nào khác nguồn (sẽ phải nhảy ra ngoài).

**Bước 3 · Gọi tên đường nối**
Có 2 loại. Cùng file: token hay component lệch nhau vì AI generate riêng từng lần. Khác nguồn: cả context đổi hẳn, có khi cả nền tảng hiển thị cũng khác. Gọi tên rõ loại nào đang gặp, trước khi quyết định sửa hay để nguyên.

**Bước 4 · Nối kỹ thuật**
Cùng file, dùng connection bình thường: chọn hotspot, kéo tới màn hình đích. Khác nguồn, không có cách nối liền mạch thật sự: bạn cần một trang mở đầu, liệt kê rõ từng đoạn dẫn ra link nào, và chuẩn bị sẵn 1 câu chuyển tiếp bằng lời cho lúc demo.

**Bước 5 · Diễn tập demo 1 phút**
Chọn đúng 1 happy path xuyên suốt, kể cả khi phải nhảy nguồn giữa chừng. Tập câu chuyển tiếp cho từng điểm nhảy, để người xem không cảm thấy đang chuyển sang một sản phẩm khác.

**Kết quả tối thiểu:** 1 bản đồ hành trình, xác định rõ điểm nối cùng nguồn và khác nguồn cho toàn bộ stitched prototype.

---

### Lesson 3: AI Ở Cấp Độ Journey
*AI giỏi 1 màn hình. Giữ nhất quán cả hành trình vẫn là việc của bạn.*

AI build từng màn hình dựa trên prompt bạn đưa cho lần đó. Nó không nhớ toàn bộ hành trình trừ khi bạn nhắc lại mỗi lần. Vì vậy 2 màn hình build cách nhau vài ngày có thể lệch nhau, dù cùng 1 design system, dù cùng 1 người prompt.

Đây không phải AI làm sai. AI đang làm đúng việc nó được giao: build tốt trong phạm vi 1 lần prompt. Việc giữ toàn bộ hành trình nhất quán, từ đầu tới cuối, chưa bao giờ là việc AI tự làm được. Đó là lý do stitch cần một bước riêng, không tự động xảy ra chỉ vì đã dùng đúng component.

**Vì vậy trước khi nối:** đối chiếu nhanh các đoạn sắp stitch với nhau, không chỉ với design system gốc. Lệch giữa 2 đoạn AI-generated dễ xảy ra hơn lệch trong 1 đoạn bạn tự làm liền mạch.

**Kết quả tối thiểu:** danh sách ngắn các điểm lệch giữa các đoạn, tìm được trước khi bắt đầu nối, không phải phát hiện giữa lúc demo.

---

### Lesson 4: Case Study Thực Tế
*Một hành trình, nhiều squad, không ai chờ ai xong mới bắt đầu phần mình.*

> **Case minh hoạ (2026-08-18):** dựng từ các yếu tố đã biết về dự án thật (mortgage platform, 3 giai đoạn, nhiều squad song song). Số liệu, đường nối cụ thể, và cách xử lý thực tế cần Winnie xác nhận lại trước khi dùng công khai.

Case này đến từ một nền tảng vay mua nhà doanh nghiệp, chia hành trình người dùng qua 3 giai đoạn: nộp hồ sơ, xác minh, giải ngân. Mỗi giai đoạn do một squad khác nhau phụ trách, build song song, không tuần tự.

**Kiểm kê ban đầu:** hơn một nửa số đoạn hành trình nằm ở các file Figma khác nhau, một số đoạn đã có prototype AI-generated riêng, độ hoàn thiện không đều: có đoạn gần production-ready, có đoạn mới dừng ở wireframe.

**Đường nối gặp phải:** token màu cảnh báo không khớp giữa đoạn xác minh và đoạn giải ngân, vì 2 squad build cách nhau vài tuần, mỗi bên tự diễn giải design system theo cách riêng. Điểm chuyển từ đoạn nộp hồ sơ sang đoạn xác minh cũng không có handoff rõ ràng. Người xem demo không biết mình đang rời khỏi 1 flow để bước sang flow khác.

**Cách xử lý:** phân loại đúng như bước gọi tên đường nối ở phần trước: đường nối lệch token thì sửa ở component gốc, áp dụng lại cho cả 2 đoạn. Đường nối lệch flow thì không cố nối liền mạch bằng thiết kế, thêm 1 slide chuyển tiếp ngắn, giải thích bằng lời khi demo. Ưu tiên sửa trước: đường nối nào khiến stakeholder hiểu sai mục tiêu hành trình. Đường nối chỉ ảnh hưởng thẩm mỹ, để lại sau.

Buổi review dùng đúng định dạng cross-squad: nhiều squad ngồi lại xem chung 1 hành trình, không phải nghe từng squad báo cáo riêng phần mình.

**Kết quả tối thiểu:** thấy quy trình 5 bước áp dụng vào 1 case nhiều squad trông ra sao, và cách chọn đường nối nào ưu tiên sửa trước demo.

---

### Lesson 5: Tư Duy Stitch
*Đường nối lộ ra không phải lỗi của bạn. Nó là một phần của việc demo.*

Khi 2 đoạn không khớp hoàn toàn, phản xạ thường là cố giấu: polish thêm, che bớt, hy vọng không ai để ý. Cách nhìn khác: đường nối là điểm tự nhiên xuất hiện khi nhiều phần được build riêng, không phải bằng chứng bạn làm ẩu. Nói thẳng với stakeholder về nó thường hiệu quả hơn cố giấu: "đoạn này còn ở early stage, đoạn kia đã build kỹ hơn" là câu hoàn toàn nói được trong demo.

**Stitched prototype không sống lâu.** Nó tồn tại để phục vụ 1 buổi demo hoặc 1 quyết định cụ thể. Sau đó, phiên bản thật sẽ thay thế nó. Đừng đầu tư đánh bóng một thứ vốn dĩ chỉ cần sống tới hết buổi review.

---

### Lesson 6: Bài Tập · Stitch Prototype Của Bạn
*Ghép các đoạn đang có thành 1 hành trình, rồi tập demo trong đúng 1 phút.*

**Kết quả tối thiểu:** 1 Stitch Index Template điền đầy đủ (đoạn hành trình, nguồn, link, trạng thái, điểm vào/ra), và 1 lần diễn tập demo 1 phút, ghi âm hoặc tự đọc lại trước khi nộp.

---

*Khóa học: Systematic AI Prototyping for Product Designers · Section 6 — Stitching Prototype*
*Thực hiện bởi Winnie Nguyen · Cập nhật lần cuối tháng 8/2026*

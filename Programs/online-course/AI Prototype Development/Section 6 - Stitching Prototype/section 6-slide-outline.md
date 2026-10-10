# Slide Outline: Section 6 - Stitching Prototype

> **Nguồn nội dung:** `section 6-lesson.md`
> **Mục đích:** Outline cho slide đi kèm 6 lesson của Section 6. Section này áp dụng chung cho cả 2 track tool, không phân biệt Claude Design hay Figma Make.
>
> Section không dạy build mới. Học viên đã có prototype từ trước, ở đây học cách nối chúng lại thành một hành trình demo được.
>
> **Lesson 4 (Case Study) đang dùng nội dung minh hoạ.** Cần Winnie xác nhận lại số liệu/đường nối/cách xử lý thật trước khi build slide chính thức cho lesson này.
>
> **Visual (2026-08-19):** Section này không có real image sẵn có, nên toàn bộ slide ưu tiên Diagram hoặc Illustration, không dùng Real image, chọn sẵn theo loại nội dung của từng slide (Diagram cho process/comparison, Illustration cho concept/mindset), để tăng engagement khi build.

---

## Prompt để build

```text
Dùng outline trong file này, build slide deck HTML cho Section 6 - Stitching Prototype
(khóa Systematic AI Prototyping for Product Designers, bản tiếng Việt).

Theo đúng rule trong _system/rules/SLIDE_DECK_RULES.md.
Copy tokens.css và deck-stage.js vào thư mục Section 6 để deck tự chứa (self-contained).

Section này không có real image, toàn bộ slide dùng Diagram hoặc Illustration
(xem dòng "Loại visual" của từng slide, đã chọn sẵn theo loại nội dung).
Với slide Illustration, dùng minh hoạ concept/mindset (không phải chụp màn hình thật).
Với slide Diagram, dùng sơ đồ/process visual thể hiện đúng cấu trúc đã mô tả trong "Nội dung"/"Lead".

Với mọi slide Illustration hoặc Diagram, dùng placeholder đơn giản
(khối màu hoặc icon đơn giản). Winnie sẽ tinh chỉnh phong cách minh hoạ sau.
```

---

# Tổng quan

**19 slide tổng cộng:** 1 cover + 1 roadmap + 6 lesson divider + 10 slide nội dung + 1 end.

**Visual mix:** 11 Illustration (cover, 6 divider Lesson, statement mindset), 8 Diagram (process, table, statement cấu trúc/so sánh), 0 Real image.

| Lesson | Số slide |
|---|---:|
| Cover + Roadmap | 2 |
| L1 Stitched Prototype Là Gì | 3 |
| L2 Quy Trình 5 Bước | 3 |
| L3 AI Ở Cấp Độ Journey | 2 |
| L4 Case Study Thực Tế | 3 |
| L5 Tư Duy Stitch | 3 |
| L6 Bài Tập | 2 |
| End | 1 |
| **Tổng** | **19** |

---

# 1. Cover & Roadmap

## COVER

- **Kicker:** Section 6 · Systematic AI Prototyping for Product Designers
- **Title:** Stitching
  **Prototype**
- **Subtitle:** Nhiều đoạn rời rạc, một hành trình kể được trọn vẹn.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image
  *(Concept: nhiều mảnh/thread rời rạc đang được nối lại thành một đường liền. Ẩn dụ "stitch" theo nghĩa đen, không dùng screenshot sản phẩm.)*

### Ghi chú thuyết trình

Tới đây, bạn đã có một hoặc nhiều đoạn prototype rồi.

Có thể build bằng Claude Design, có thể bằng Figma Make. Có thể nằm rải rác ở vài file Figma khác nhau.

Phần này không dạy bạn build thêm màn hình nào cả.

Nó dạy một việc khác:

**Nối những gì đang có thành một hành trình xem được trọn vẹn.**

---

## PROCESS - Lộ trình Section 6

- **Kicker:** Từ nhiều đoạn đến một hành trình
- **Title:** Không nối màn hình.
  **Nối bản đồ.**
- **Nội dung:**

  **01 · Định nghĩa**
  Hiểu đúng stitched prototype là gì, và khi nào cần nó.

  **02 · Quy trình**
  5 bước để nối nhiều đoạn, kể cả khi chúng ở nguồn khác nhau.

  **03 · Vai trò của AI**
  Biết rõ AI giữ được gì và không giữ được gì ở cấp độ cả hành trình.

  **04 · Case thật**
  Xem quy trình áp dụng vào một case nhiều squad, nhiều đường nối.

  **05 · Tư duy**
  Đường nối không phải lỗi cần giấu. Đó là một phần của việc demo.

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(5 node theo chiều ngang hoặc dọc, đánh số 01-05, giống timeline/roadmap. Không cần icon riêng cho từng bước, ưu tiên rõ thứ tự.)*

### Ghi chú thuyết trình

Section này ngắn nhưng không nhẹ.

Cái khó không nằm ở kỹ thuật nối. Cái khó nằm ở việc nhìn ra đường nối trước khi ai đó khác nhìn ra giúp bạn, giữa buổi demo.

---

# 2. Lesson 1: Stitched Prototype Là Gì

## SECTION - Lesson 1

- **Title:** Lesson 1
  **Stitched Prototype**
  **Là Gì**
- **Sub:** Một hành trình demo được, ghép từ nhiều prototype vốn tách rời.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image
  *(Concept: các mảnh rời rạc, hình chữ nhật/khung màn hình nhỏ, nằm tản mác, gợi ý sắp được gom lại.)*

### Ghi chú thuyết trình

Trước khi nối gì cả, mình cần thống nhất một khái niệm.

Stitched prototype không phải một prototype đẹp hơn, đầy đủ hơn.

Nó là một prototype **được ghép**, từ nhiều đoạn có thể build ở thời điểm khác nhau, người khác nhau, thậm chí tool khác nhau.

---

## STATEMENT - Định nghĩa & nguồn

- **Kicker:** Định nghĩa
- **Title:** Stitch không giả định
  **mọi thứ nằm chung 1 file.**
- **Lead:**

  Nguồn có thể khác nhau hoàn toàn.

  Nhiều file Figma riêng biệt, mỗi file một journey.

  Một link publish từ track Claude Design. Một link khác từ track Figma Make.

  Thậm chí một prototype cũ, dựng bằng tool khác, vẫn còn dùng được.

  **Gộp tất cả vào 1 file thường không khả thi. Và cũng không phải mục đích.**

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(3-4 nguồn khác nhau: file Figma, link Claude Design, link Figma Make, hội tụ về 1 điểm trung tâm/index, thể hiện đúng ý "nhiều nguồn, 1 hành trình".)*

### Ghi chú thuyết trình

Đây là điểm nhiều người bị vướng ngay từ đầu.

Họ nghĩ stitch nghĩa là phải dồn hết vào 1 file, 1 prototype liền mạch.

Không phải vậy.

Nếu 3 squad build 3 đoạn ở 3 file khác nhau, bạn không cần gộp file. Bạn cần một cách để đi từ đoạn này sang đoạn kia mà người xem vẫn hiểu đang ở đâu trong câu chuyện.

**Đó là việc stitch thật sự làm.**

---

## STATEMENT - Vai trò & đường nối

- **Kicker:** Vai trò của prototype
- **Title:** Không phải mọi prototype
  **đang chứng minh cùng một thứ.**
- **Lead:**

  Có prototype để test độ chi tiết: look and feel.

  Có prototype để test tính khả thi: implementation.

  Và có prototype để test một điều khác hẳn: **cả hành trình có kể đúng câu chuyện không.**

  Stitch nằm ở nhóm cuối. Nó không cần từng đoạn hoàn thiện như nhau.

  **Nó cần cả chuỗi mạch lạc.**

  Vì vậy một đoạn thô hơn không phải lỗi, trừ khi nó khiến người xem không hiểu được câu chuyện.

- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image
  *(Concept nhẹ: một sợi chỉ/đường liền chạy xuyên qua các mảnh độ hoàn thiện khác nhau, nhấn mạnh mạch chuyện quan trọng hơn độ đồng đều.)*

### Ghi chú thuyết trình

Mình thấy nhiều designer cố polish đều tất cả các đoạn trước khi dám demo.

Không cần thiết.

Nếu đoạn giữa chưa đẹp bằng đoạn đầu, nhưng người xem vẫn hiểu được mạch chuyện, vậy là đủ cho một buổi demo.

**Vấn đề chỉ thật sự xảy ra khi người xem lạc mất câu chuyện, không phải khi 1 màn hình chưa đẹp bằng màn hình khác.**

---

# 3. Lesson 2: Quy Trình 5 Bước

## SECTION - Lesson 2

- **Title:** Lesson 2
  **Quy Trình**
  **5 Bước**
- **Sub:** Không nối màn hình với màn hình. Nối bản đồ với bản đồ.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image

### Ghi chú thuyết trình

5 bước này không phức tạp.

Nhưng bỏ qua bước nào cũng dễ khiến buổi demo đi lệch hướng.

---

## PROCESS - 5 bước stitch

- **Kicker:** Quy trình
- **Title:** Từ kiểm kê
  **đến diễn tập.**

- **Nội dung:**

  **01 · Kiểm kê**
  Liệt kê từng đoạn hành trình đang có: nằm ở đâu, ai làm, tới đâu rồi.

  **02 · Vẽ bản đồ hành trình**
  Xếp các đoạn theo đúng thứ tự người dùng đi qua, ghi rõ điểm vào/ra.

  **03 · Gọi tên đường nối**
  Phân loại: lệch trong cùng file, hay lệch vì khác hẳn nguồn.

  **04 · Nối kỹ thuật**
  Cùng file thì nối trực tiếp. Khác nguồn thì cần một trang mở đầu dẫn ra link.

  **05 · Diễn tập demo 1 phút**
  Chọn đúng 1 happy path, tập câu chuyển tiếp cho từng điểm nhảy nguồn.

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(5 bước dạng flow ngang có mũi tên, đúng thứ tự. Đây là slide quan trọng nhất để làm diagram rõ, học viên sẽ quay lại nhìn slide này nhiều nhất.)*

### Ghi chú thuyết trình

Bước dễ bị bỏ qua nhất là bước một, kiểm kê.

Đừng bỏ qua đoạn còn dở. Kiểm kê để biết mình có gì thật, không phải để lọc ra đoạn đẹp nhất đem khoe.

Và bước cuối, diễn tập, nhiều người coi là thừa.

**Không thừa. Đó là lúc bạn phát hiện chỗ nối nào còn ngượng, trước khi stakeholder phát hiện giúp bạn.**

---

## TABLE - Nối kỹ thuật: cùng nguồn vs khác nguồn

- **Kicker:** Bước 4, chia 2 nhánh
- **Title:** Cùng file, nối được.
  **Khác nguồn, phải dẫn ra.**

| | Cùng nguồn (1 file) | Khác nguồn |
|---|---|---|
| **Cách nối** | Hotspot → connection → destination | Trang mở đầu, dẫn link ra ngoài |
| **Trải nghiệm** | Liền mạch, không cảm giác chuyển | Có điểm nhảy, cần chuẩn bị trước |
| **Cần chuẩn bị** | Không nhiều, connection có sẵn trong tool | 1 câu chuyển tiếp bằng lời cho lúc demo |

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(2 nhánh song song minh hoạ ngay cạnh bảng: 1 đường liền (cùng nguồn) vs 1 đường đứt có điểm nhảy (khác nguồn), củng cố trực quan cho nội dung bảng.)*

### Ghi chú thuyết trình

Đừng cố biến điểm nhảy nguồn thành liền mạch bằng thiết kế, thường không đáng công.

Cách hiệu quả hơn nhiều: chuẩn bị sẵn một câu chuyển tiếp, nói ra miệng lúc demo.

**"Giờ mình bước sang phần xác minh, được build ở một file khác."**

Một câu vậy là đủ để người xem không cảm thấy lạc.

---

# 4. Lesson 3: AI Ở Cấp Độ Journey

## SECTION - Lesson 3

- **Title:** Lesson 3
  **AI Ở Cấp Độ**
  **Journey**
- **Sub:** AI giỏi 1 màn hình. Giữ nhất quán cả hành trình vẫn là việc của bạn.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image

### Ghi chú thuyết trình

Một câu hỏi hay gặp: sao AI không tự giữ nhất quán được, nếu đã dùng đúng design system?

Câu trả lời nằm ở chính cách AI hoạt động.

---

## STATEMENT - Ranh giới của AI

- **Kicker:** Ranh giới
- **Title:** AI không nhớ
  **cả hành trình.**
- **Lead:**

  AI build từng màn hình dựa trên prompt của lần đó, không nhớ toàn bộ hành trình trừ khi bạn nhắc lại mỗi lần.

  2 màn hình build cách nhau vài ngày có thể lệch nhau, dù cùng 1 design system, dù cùng 1 người prompt.

  Đây không phải AI làm sai. AI đang làm đúng việc nó được giao.

  **Giữ toàn bộ hành trình nhất quán chưa bao giờ là việc AI tự làm được.**

  Vì vậy trước khi nối, đối chiếu nhanh các đoạn sắp stitch với nhau, không chỉ với design system gốc.

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(2 màn hình build cách nhau trên 1 trục thời gian, mỗi màn hình có "bong bóng context" riêng không kết nối nhau, thể hiện AI không giữ trí nhớ giữa các lần build.)*

### Ghi chú thuyết trình

Đừng xem đường nối như bằng chứng AI chưa đủ tốt.

**AI build nhanh, đúng phạm vi được giao. Giữ mạch cả câu chuyện vẫn luôn là việc của designer.**

Lệch giữa 2 đoạn AI-generated dễ xảy ra hơn lệch trong 1 đoạn bạn tự làm liền mạch từ đầu. Biết trước điều này để không bất ngờ khi kiểm kê.

---

# 5. Lesson 4: Case Study Thực Tế

## SECTION - Lesson 4

- **Title:** Lesson 4
  **Case Study**
  **Thực Tế**
- **Sub:** Một hành trình, nhiều squad, không ai chờ ai xong mới bắt đầu phần mình.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image

### Ghi chú thuyết trình

Case này đến từ một nền tảng vay mua nhà doanh nghiệp.

Hành trình chia qua 3 giai đoạn: nộp hồ sơ, xác minh, giải ngân, mỗi giai đoạn một squad khác nhau phụ trách, build song song.

---

## STATEMENT - Kiểm kê & đường nối thực tế

- **Kicker:** Kiểm kê
- **Title:** Hơn nửa số đoạn
  **nằm ở file khác nhau.**
- **Lead:**

  Một số đoạn đã có prototype AI-generated riêng. Độ hoàn thiện không đều: có đoạn gần production-ready, có đoạn mới dừng ở wireframe.

  Đường nối gặp phải: token màu cảnh báo không khớp giữa đoạn xác minh và đoạn giải ngân, vì 2 squad build cách nhau vài tuần.

  Điểm chuyển từ đoạn nộp hồ sơ sang đoạn xác minh cũng không có handoff rõ ràng.

  **Người xem demo không biết mình đang rời khỏi 1 flow để bước sang flow khác.**

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(3 giai đoạn theo hàng ngang: nộp hồ sơ, xác minh, giải ngân, mỗi giai đoạn gắn nhãn squad phụ trách và mức độ hoàn thiện khác màu, điểm nối giữa 2 giai đoạn có đánh dấu đường nối rõ.)*

### Ghi chú thuyết trình

Đây là đường nối khá điển hình khi nhiều squad build song song.

Không ai sai. Mỗi squad tự diễn giải design system theo cách riêng, ở thời điểm riêng.

**Vấn đề không phải ai làm ẩu. Vấn đề là chưa ai đứng ở góc nhìn toàn hành trình để thấy chỗ lệch.**

---

## STATEMENT - Cách xử lý

- **Kicker:** Xử lý
- **Title:** Ưu tiên sửa đường nối
  **làm lệch mục tiêu, không phải đường nối lệch thẩm mỹ.**
- **Lead:**

  Phân loại đúng như bước gọi tên đường nối: đường nối lệch token, sửa ở component gốc, áp dụng lại cho cả 2 đoạn. Đường nối lệch flow, thêm 1 slide chuyển tiếp ngắn, giải thích bằng lời khi demo.

  Buổi review dùng định dạng cross-squad: nhiều squad ngồi lại xem chung 1 hành trình, không phải nghe từng squad báo cáo riêng phần mình.

  **Kết quả: buổi demo tập trung đúng câu hỏi stakeholder cần trả lời, không bị lệch hướng bởi khác biệt nhỏ giữa các đoạn.**

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(2 nhánh quyết định, "lệch mục tiêu → sửa trước" vs "lệch thẩm mỹ → để sau", dạng sơ đồ rẽ nhánh đơn giản.)*

### Ghi chú thuyết trình

Không phải mọi đường nối đáng để dừng lại sửa trước demo.

Hỏi đúng một câu: đường nối này có khiến stakeholder hiểu sai mục tiêu của hành trình không?

Nếu có, sửa trước. Nếu chỉ là thẩm mỹ, để lại sau, vẫn còn thời gian sau buổi demo.

---

# 6. Lesson 5: Tư Duy Stitch

## SECTION - Lesson 5

- **Title:** Lesson 5
  **Tư Duy**
  **Stitch**
- **Sub:** Đường nối lộ ra không phải lỗi của bạn. Nó là một phần của việc demo.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image

### Ghi chú thuyết trình

Phần cuối này không phải kỹ thuật.

Nó là cách bạn đứng trước stakeholder khi hành trình chưa hoàn hảo.

---

## STATEMENT - Đường nối không phải lỗi

- **Kicker:** Reframe
- **Title:** Đừng giấu đường nối.
  **Gọi tên nó.**
- **Lead:**

  Khi 2 đoạn không khớp hoàn toàn, phản xạ thường là cố giấu: polish thêm, che bớt, hy vọng không ai để ý.

  Cách nhìn khác: đường nối là điểm tự nhiên xuất hiện khi nhiều phần được build riêng, không phải bằng chứng bạn làm ẩu.

  > "Đoạn này còn ở early stage, đoạn kia đã build kỹ hơn."

  **Một câu vậy, nói thẳng, thường hiệu quả hơn cố giấu.**

- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image
  *(Concept: 2 mảnh vải/2 khối khác màu được khâu lại, đường chỉ khâu hiện rõ và được tôn lên thay vì giấu đi. Ẩn dụ trực tiếp cho "gọi tên, không giấu".)*

### Ghi chú thuyết trình

Mình từng nghĩ im lặng về đường nối sẽ an toàn hơn.

Ngược lại.

Stakeholder phát hiện ra đường nối mà không được báo trước, họ nghi ngờ cả phần còn lại. Stakeholder được báo trước, họ tập trung đúng vào câu hỏi bạn cần họ trả lời.

**Chủ động gọi tên, chủ động dẫn dắt.**

---

## STATEMENT - Tuổi thọ ngắn có chủ đích

- **Kicker:** Transient
- **Title:** Stitch không sống lâu.
  **Và không cần sống lâu.**
- **Lead:**

  Stitched prototype tồn tại để phục vụ 1 buổi demo hoặc 1 quyết định cụ thể.

  Sau đó, phiên bản thật sẽ thay thế nó.

  **Đừng đầu tư đánh bóng một thứ vốn dĩ chỉ cần sống tới hết buổi review.**

- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image
  *(Concept: prototype như một cấu trúc tạm, giàn giáo, lều dựng nhanh, gợi ý "đủ dùng cho 1 buổi", không phải công trình vĩnh viễn.)*

### Ghi chú thuyết trình

Đây là điểm khác biệt lớn nhất so với việc build 1 prototype để dùng lâu dài.

Biết trước stitch sẽ hết vòng đời sau buổi demo giúp bạn quyết định nhanh hơn: chỗ nào đáng sửa, chỗ nào không cần.

**Không phải mọi thứ đáng để hoàn hảo. Chỉ những thứ giúp buổi demo đạt mục tiêu mới đáng.**

---

# 7. Lesson 6: Bài Tập

## SECTION - Lesson 6

- **Title:** Lesson 6
  **Bài Tập ·**
  **Stitch Prototype Của Bạn**
- **Sub:** Ghép các đoạn đang có thành 1 hành trình, rồi tập demo trong đúng 1 phút.
- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image

### Ghi chú thuyết trình

Đây là điểm dừng để áp dụng cả 5 bước vào chính prototype bạn đang có.

Không cần hoàn hảo, cần đúng quy trình.

---

## PRACTICE - Nội dung bài tập

- **Kicker:** Bài tập
- **Title:** Điền index.
  **Diễn tập demo.**

- **Nội dung:**

  **01 · Stitch Index Template**
  Điền đầy đủ: đoạn hành trình, nguồn, link, trạng thái, điểm vào/ra.

  **02 · Diễn tập demo 1 phút**
  Ghi âm hoặc tự đọc lại trước khi nộp.

- **Loại visual:** ☑ Diagram ☐ Illustration ☐ Real image
  *(Checklist 2 mục dạng diagram đơn giản, ô vuông/tick, không cần minh hoạ phức tạp.)*

### Ghi chú thuyết trình

Kết quả tối thiểu chỉ cần đúng 2 thứ:

**Một Stitch Index Template điền đầy đủ, và một lần diễn tập demo 1 phút.**

Không cần mượt ngay lần đầu. Diễn tập chính là để tìm ra chỗ còn ngượng, trước khi đứng trước stakeholder thật.

---

# 8. Kết thúc

## END - Kết thúc Section 6

- **Kicker:** Takeaway
- **Title:** Không phải giấu đường nối.
  **Là dẫn dắt qua nó.**
- **Lead:**

  Stitched prototype không cần hoàn hảo ở từng đoạn.

  Nó cần:

  **Kiểm kê rõ.**
  **Bản đồ rõ.**
  **Đường nối được gọi tên.**
  **Demo được diễn tập.**

  Đó là toàn bộ hành trình khoá học này, từ tư duy pattern-first, qua build bằng AI, đến giờ là kể lại thành một câu chuyện hoàn chỉnh.

- **Loại visual:** ☐ Diagram ☑ Illustration ☐ Real image
  *(Quay lại đúng concept ở COVER, các mảnh rời rạc giờ đã nối thành 1 đường liền, tạo cảm giác khép vòng cho cả section.)*

### Ghi chú thuyết trình

Đây là điểm kết của cả khoá học.

Bạn đã đi từ một mindset, pattern-first thay vì vibe-coding, qua build thật bằng AI, và giờ là biết cách trình bày nó như một hành trình hoàn chỉnh, không phải một mớ màn hình rời rạc.

**Prototype tốt không phải prototype không có đường nối. Là prototype biết đường nối của mình nằm ở đâu.**

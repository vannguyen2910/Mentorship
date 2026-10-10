# Section 1.3 - Chọn Công cụ AI cho Prototype (Raw Transcript)

Chuyển từ file .srt gốc, đã gộp các dòng bị wrap thành câu hoàn chỉnh và bỏ số thứ tự/timestamp. Nội dung giữ nguyên như bản gốc (auto-caption). Một vài từ có vẻ bị nghe sai (ChatsTVT, Vidma/Vidma Mac, MCB, Cloud Code, DesignPaste/Codepase, ProtoTyrant) — có thể lần lượt là ChatGPT, Figma/Figma Make, MCP, Claude Code, codebase, prototype — giữ nguyên để không làm sai lệch bản ghi gốc, cần đối chiếu lại với video khi dùng.

---

## Nguyên tắc chọn công cụ

Việc đầu tiên của chúng ta trong khóa học này là chúng ta muốn chọn những công cụ AI mà phù hợp với chúng ta, phải không nè. Ở ngoài Marketplace hiện tại có rất là nhiều công cụ AI mà các bạn sẽ không biết được là chúng ta nên chọn như thế nào. Có một vài nguyên tắc mà mình muốn các bạn nhớ tới trước khi mà các bạn quyết định là mình sẽ sử dụng công cụ AI nào và xuống tiền cho nó.

Chúng ta nên chọn những công cụ nào mà AI có thể đọc trực tiếp từ những file Figma bằng cách connection hoặc là qua MCB hoặc là có thể tự dẫn được những cái design system của mình một cách tốt nhất vì nó sẽ giữ được cái tính design fidelity tốt nhất cho chúng ta. Chắc chắn rằng nó sẽ tốt hơn những cái công cụ mà chỉ có dựa vào những cái screenshot hoặc là mô tả bằng lời.

## AI Chat Tool

Có bốn nhóm AI quen thuộc như là AI Chat Tool như ChatsTVT, Gemini thì những công cụ này dùng để research hoặc là cho chúng ta brainstorm về cách mà chúng ta tổ chức cái prototype hoặc là cái journey như thế nào cho cái prototype của chúng ta thì đối với mình cái công cụ chat nào cũng được hết, chỉ cần các bạn có thể đã quen thuộc.

## AI Design Tool

Và nhóm thứ 2 là AI Design Tool. Nó có thể tạo ra những giao diện trực quan bởi design page. Các bạn có thể chỉnh sửa trực tiếp trên đó. Hiện tại có 2 design tool trên thị trường.

Thứ nhất là Vidma Mac sẽ phù hợp nếu các bạn đã có design sẵn, chúng ta chỉ cần interact, chúng ta muốn tương tác trực tiếp giữa design và prototype thông qua ecosystem của Vidma.

Và cái thứ hai là Claude Design. Đây là một cái cơ bản, công cụ AI khá là phổ biến ở thị trường AI hiện nay. Nó sẽ đi theo một hướng hoàn toàn khác hẳn. Ngay mình có thể sử dụng nó khi mà on board, khi mình chưa có bất cứ một cái gì. Nó có thể tự đọc code base, hoặc là có thể đọc những cái file thiết kế của bạn, để nó có thể tự dẫn ra những cái design system áp dụng đúng với những cái colors, Typography, Component cho những cái Prototype, những cái Screens về sau mà chúng ta không cần phải setup thêm nữa.

## AI Coding Tool

Và cái nhóm thứ 3 là AI Coding Tool. Nó sẽ build ra nhật cho bạn những cái app có thể chạy bằng Codepase. Nó có những cái Conditional Logic và những cái Data thật, nó sẽ làm tốt hơn những cái công cụ về DesignPaste.

Nó cũng sẽ rất là mạnh, nếu như bạn có thể quen được và sử dụng những dạng như là Code Editor, như là Cursor nè, hoặc là Cloud Code. Nó có thể để kết nối trực tiếp qua Figma qua MCB thì nó có thể đọc được cho bạn những cái Token, Component và Variant. Nhưng mà đổi lại bạn cần phải có một cái knowledge về technical cố định vì nó sẽ có đòi hỏi bạn phải setup kết nối cũng như là có một cái môi trường để host cho mình một cái ProtoTyrant để có thể đem test với user.

## Công cụ không khuyến khích

Nhóm cuối cùng cũng là cái nhóm mà mình sẽ không có khuyến khích sử dụng trong cái khóa học này, thì những loại công cụ như là Lovable thì nó sẽ rất là tốt nếu như mà chúng ta cần một cái thử nghiệm về MVP version của cái prototype và muốn nhanh để testing idea thì nó là rất là tốt.

Nhưng ở cái khóa học này mình muốn nói thiên về systematic prototype với những cái cách setup mà nói thiên về systematic, scaleable và consistent, cho nên là chúng ta sẽ bỏ qua cái công cụ này ở khóa học này nha.

## Bảng xếp hạng & lưu ý

Đây là các công cụ AI xây dựng prototype phổ biến nhất trên cái thị trường AI hiện nay. Thì cái table ở trên sẽ xếp hạng nằm nhóm theo mức độ hỗ trợ Design System từ trên cao xuống thấp.

Và lưu ý là đây chỉ là bức tranh tại thời điểm mà mình quay khóa học này thôi nha. Thị trường thay đổi rất nhiều, nhất là AI. Nên nếu sau này các công cụ mới hoặc là một tool đổi tính năng thì các bạn chỉ cần nhớ là áp dụng nguyên tắc chọn lựa này.

Thứ nhất là chọn đúng nguyên tắc. Thứ 2 là chọn ưu tiên các công cụ mà đọc thẳng từ cái file Figma hoặc là có thể support chúng ta xây dựng design system.

## Tổng kết

Nếu như mà bạn chưa có một cái công cụ nào để quyết định để sử dụng cho mình, thì cũng không sao hết. Các bạn cứ học tiếp nha, vì những cái bài học phía sau, mình sẽ hướng dẫn cụ thể hơn cái cách mà kết nối với cái công cụ này, và các bạn có thể chọn lựa được những công cụ mà cảm thấy phù hợp nhất cho mình.

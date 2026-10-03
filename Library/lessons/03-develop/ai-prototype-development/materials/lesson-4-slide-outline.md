---
title: "Lesson 4: Publish It"
lesson_file: "lesson-3-4-stub.md"
level: "intermediate"
slide_count: 23
duration: "100 min"
status: deck-built
built_deck: "../slides/Lesson 4 - Publish It.dc.html"
last_synced: 2026-10-03
---

> **Reverse-synced from the built deck on 2026-10-03 (second pass).** The deck was restructured in the design tool after the first sync: Collaboration moved up to Section 5, the AI-tool material was pulled into one closing Section 6, the "Simulate One Oops" section was removed, and speaker notes were rewritten in Vietnamese with Figma analogies. This outline mirrors that deck. The lesson file (`lesson-3-4-stub.md`) was fully re-synced to this deck the same day; unresolved gaps are listed under "Drift to resolve" here and "Open decisions" there.
> **Speaker notes are Vietnamese bullets, copied from the deck.** Each carries a Figma-based analogy ("Ví dụ"). English slide copy stays English. Checkpoints ("Kiểm tra") live in the notes, not on a slide.
> **The ten-word glossary (slide 4) is the reference for the whole lesson** — notes tell the facilitator to come back to it for Branch, Main and Pull request in Section 5.
> **Previous local version archived** at `slides/_archive/Lesson 4 - Publish It (2026-10-03 local, pre-reimport).dc.html` — it had a standalone "ask your AI tool to run the loop" slide that the new deck replaces with the six-prompt reference card (slide 21).

---

## Session metadata

| Field | Value |
|---|---|
| Program | SYSTEMATIC AI PROTOTYPING |
| Track / session | Lesson 4 |
| Stage | Develop |
| Prior session | Lesson 3: Scaling the Prototype |
| Next session | Lesson 5: Beyond the Pattern (optional bonus) |
| Running example | The mentee's own anchor project, then a public sandbox team repo |
| Deck file | `slides/Lesson 4 - Publish It.dc.html` |

## Slide structure — 23 slides

| # | Section | Slides | Minutes |
|---|---|---|---|
| 0 | Opening | 2 | — |
| 1 | The Local-vs-Published Mental Model | 4 | 10 |
| 2 | Setup & Connect | 2 | 10 |
| 3 | First Publish | 3 | 20 |
| 4 | Make It Live | 3 | 15 |
| 5 | The Collaboration | 5 | 25 |
| 6 | The AI-Tool Shortcut | 4 | 10 |
| 7 | Closing | 1 | — |

> **Agenda adds up to 90 minutes** (10 + 10 + 20 + 15 + 25 + 10) under a "One hundred minutes" title; the Agenda notes say "about 90 minutes of content, the rest for transitions and Q&A".
> **Section 5 is hands-on against a public sandbox repo** the facilitator owns. The mentee is invited as a collaborator beforehand (public repos can be forked by anyone, but only collaborators push branches). A one-page `CONTRIBUTING.md` is the team SOP — template at `materials/contributing-template.md`.

---

## 0. Opening

### COVER · Cover
- Category line: SYSTEMATIC AI PROTOTYPING
- Kicker: LESSON 4
- Title: Publish\nIt (second line accented)
- Subtitle: Git and GitHub Desktop for non-technical designers.
- Author: Winnie Nguyen — UX Product Design Instructor
- Speaker notes:
  - Mở đầu bằng một dự án thật: cho xem trước (chỉ là thư mục) và sau (có lịch sử và link chạy được), không đọc chữ trên slide
  - Nói một câu trước khi nhắc tên công cụ: máy tính của mình là bản nháp, GitHub là bản đã đăng, Push là nút đăng
  - Ví dụ: màn hình app trong Figma chỉ mình thấy là bản nháp. Gửi link prototype cho khách bấm thử là bản đã đăng. Push giống bấm Publish
- 🎨 Visual: Two-column cover on white — text panel left, image slot right.

### AGENDA · One Hundred Minutes
- Title: One hundred minutes\nLocal becomes\nlive.
- On-slide, numbered with minutes: 01 Local vs. Published (10) · 02 Setup & Connect (10) · 03 First Publish (20) · 04 Make It Live (15) · 05 The Collaboration (25) · 06 The AI-Tool Shortcut (10)
- Speaker notes:
  - Tổng cộng khoảng 90 phút nội dung, phần còn lại dành cho chuyển tiếp và hỏi đáp
  - Nói rõ lộ trình: từ prototype trên máy đến một link ai cũng bấm thử được, rồi tập làm việc nhóm
  - Ví dụ: đi từ thiết kế một mình đến cả nhóm cùng thiết kế một app trong một file chung
- 🎨 Visual: Six numbered cards in a 3×2 grid with a mono minutes label each.

---

## 1. The Local-vs-Published Mental Model

### SECTION DIVIDER · Section 1: The Local-vs-Published Mental Model
- Kicker: Section 1
- Title: The Local-vs-Published\nMental Model
- On-slide: Everything built so far lives on one machine. That changes now.
- Speaker notes:
  - Mọi thứ làm ở Bài 1 đến 3 chỉ nằm trên một máy tính, hôm nay điều đó thay đổi
  - Ví dụ: prototype làm xong nhưng chỉ mở được trên máy mình thì khách chưa thể bấm thử. Hôm nay mình đưa nó lên mạng

### STATEMENT · Local Is the Draft, GitHub Is Published
- Kicker: The mental model
- Title: Local folder = draft.\nGitHub = published.
- On-slide diagram: Local folder — "A draft only you can see" → GitHub — "Commit history + a live URL"
- Speaker notes:
  - Cho xem một dự án thật trước khi giải thích: thư mục thường và trang GitHub có lịch sử
  - Thư mục trên máy = bản nháp. GitHub = bản đã đăng
  - Ví dụ 1: file Figma đang làm dở (nháp) và link prototype gửi cho khách bấm thử (đã đăng)
  - Ví dụ 2: file là nơi làm việc, còn thư viện component đã publish là thứ cả team dùng thật sự
  - Link prototype của một công cụ phụ thuộc vào tài khoản còn hoạt động. Link GitHub Pages thì vẫn mở được khi hết hạn dùng thử
  - Kiểm tra: mời các bạn tự nói lại ý 'nháp và đã đăng' bằng lời của mình trước khi đi tiếp
- 🎨 Visual: Folder icon → arrow → globe with commit history; two labelled cards.

### GLOSSARY · The Words You'll Hear Today
- Kicker: Ten words, defined our way
- Title: The words you'll\nhear today.
- On-slide, ten terms: Repo — the project's home on GitHub, with all its files and history · Clone — download a copy of a project from GitHub to your laptop · Commit — a saved snapshot, with a short note describing what changed · Push — sending your commits up to GitHub · Pull — bringing the team's latest changes down to your laptop · Branch — your own copy of the project to try changes in, without touching the original · Main — the team's official version; everyone relies on it, so never edit it directly · Pull request — asking a teammate to review your branch before it joins main (GitLab calls it a Merge Request) · Merge — adding your approved changes into main · Clash — two people changed the same thing, so you choose which version to keep
- Speaker notes:
  - Mười từ này được định nghĩa theo cách của lớp mình, không phải từ điển. Quay lại slide này mỗi khi có từ mới, nhất là Branch, Main và Pull request ở Phần 5
  - Repo: như một file Figma của dự án, chứa mọi màn hình và lịch sử các lần sửa
  - Commit: như bấm Save to version history trong Figma và đặt tên 'Thêm nút Đăng nhập'. Cần quay lại bản đó lúc nào cũng được
  - Push: gửi bản đã lưu lên mạng cho cả team thấy. Pull: tải về những gì bạn khác vừa cập nhật, như nhận bản mới của thư viện component
  - Branch: như duplicate một màn hình để thử ý tưởng mới, thử hỏng cũng không ảnh hưởng bản gốc. Main: file chính của team, ai cũng dựa vào đó nên không sửa thẳng lên
  - Pull request: gửi màn hình bản thử cho đồng nghiệp comment trước khi đưa vào file chính. Merge: đưa bản đã được duyệt vào file chính
  - Clash: hai người cùng đổi màu của cùng một nút nhưng chọn màu khác nhau, phải bàn xem giữ màu nào
  - Ghi chú commit rõ ràng giống đặt tên layer rõ ràng. Mơ hồ thì sau này tốn công hơn
- 🎨 Visual: Ten term cards, two columns of five.

---

## 2. Setup & Connect

### SECTION DIVIDER · Section 2: Setup & Connect
- Kicker: Section 2
- Title: Setup & Connect
- On-slide: Confirm the prework, then connect the tool to the real project.
- Speaker notes:
  - Xác nhận phần chuẩn bị trong 30 giây, không mất giờ học: tài khoản và việc cài Desktop là bài tập về nhà ở Bài 3
  - Ví dụ: như kiểm tra đã đăng nhập Figma và có sẵn file trước khi bắt đầu thiết kế

### STEPS · Connect GitHub Desktop to Your Project
- Kicker: Step 1
- Title: Connect GitHub Desktop\nto your project.
- On-slide, numbered: 1. Open GitHub Desktop, confirm signed in · 2. Create a new Repo · 3. Point it at the existing project folder
- Screenshots: `gh-desktop-diff-warning.png`, `gh-desktop-create-new-repo.png`, `gh-desktop-repo-connected.png`
- Speaker notes:
  - Nói to sự khác nhau giữa Add và Create: thói quen hay bấm 'Create New', nhưng nó tạo ra một repo trống thứ hai bên cạnh repo thật
  - Ví dụ: đã có file Figma của dự án rồi mà lại tạo thêm một file trống mới, thay vì mở file đang có
  - Tab Changes sẽ liệt kê mọi file là 'mới' vì chưa có lịch sử. Điều này bình thường
  - Kiểm tra: GitHub Desktop đã mở, đã đăng nhập và đang hiện đúng thư mục dự án của mình
- 🎨 Visual: Three numbered steps with a screenshot each.

---

## 3. First Publish

### SECTION DIVIDER · Section 3: First Publish
- Kicker: Section 3
- Title: First Publish
- On-slide: One commit, one push — the repo goes live for the first time.
- Speaker notes:
  - Luôn xem thử trên máy trước khi đăng: chắc chắn prototype vẫn chạy rồi mới bấm Commit hay Push
  - Ví dụ: bấm thử prototype một lượt để chắc nút nào cũng chuyển đúng màn hình trước khi gửi cho khách

### STEPS · Open GitHub Desktop, Then Commit
- Kicker: Step 2
- Title: Open it,\nthen commit.
- On-slide, numbered with "use this" lines: 1. Open GitHub Desktop — use this to check the right repo is selected before touching anything · 2. Write a message, commit — use this every time you save a change, before it can be pushed anywhere
- Screenshots: `gh-desktop-open-app.png`, `gh-desktop-commit-message.png`
- Speaker notes:
  - Xác nhận GitHub Desktop đang mở và đã chọn đúng dự án trước khi làm gì khác
  - Nói trước điều các bạn sắp hỏi: file làm từ nhiều tuần trước vẫn hiện là 'mới' ở lần commit đầu tiên
  - Ví dụ ghi chú tốt: 'Đổi nút Đăng nhập sang màu cam', giống tên phiên bản trong Figma. Càng cụ thể càng dễ tìm lại
  - Ví dụ ghi chú tệ: 'sửa lung tung', giống file tên 'final_v3_FINAL_thật'

### STEPS · Publish, Then Push
- Kicker: Step 2, continued
- Title: Publish,\nthen push.
- On-slide, numbered with "use this" lines: 3. Click Publish repository — use this the first time, the repo doesn't exist on GitHub yet · 4. Push origin sends it up — use this every time after, the repo already exists
- On-slide flag: Everything shows as new or added — there's no prior commit to compare against yet.
- Screenshots: `gh-desktop-publish-repository.png`, `gh-desktop-push-origin.png`
- Speaker notes:
  - Publish repository làm hai việc cùng lúc: tạo repo mới trên GitHub và gửi lần đầu
  - Ví dụ: Publish giống lần đầu bấm Share cho một file Figma. Push là những lần sau chỉ cập nhật phần vừa sửa
  - Kiểm tra: dự án đã có trên GitHub và tab Changes trong Desktop đã trống

---

## 4. Make It Live

### SECTION DIVIDER · Section 4: Make It Live
- Kicker: Section 4
- Title: Make It Live
- On-slide: Turn the repo into a URL that updates itself.
- Speaker notes:
  - Đây là khoảnh khắc quan trọng nhất của cả bài, không lướt qua
  - Ví dụ: biến prototype trên máy thành một link ai cũng bấm thử được, như gửi link prototype cho khách

### STEPS · Find Pages, Then Pick a Branch
- Kicker: Step 3 — the payoff
- Title: Find Pages,\nthen pick a branch.
- On-slide, numbered with "use this" lines: 1. Repo Settings → Pages — use this to open the repo's settings, where the Pages config lives · 2. Open the branch dropdown — use this the first time, it defaults to None until a branch is chosen
- Screenshots: `gh-pages-settings-tab.png`, `gh-pages-branch-none.png`
- Speaker notes:
  - Xác nhận đang ở đúng phần Settings của đúng dự án trước khi cuộn tìm Pages
  - Ô Branch ban đầu là None cho đến khi chọn. Đó là bình thường, không phải lỗi
  - Ví dụ: như chọn 'trang nào là trang chủ của prototype'. Chưa chọn thì chưa có gì để hiện

### STEPS · Pick a Folder, Then Visit the Site
- Kicker: Step 3, continued — the payoff
- Title: Pick a folder,\nthen visit the site.
- On-slide, numbered with "use this" lines: 3. Select branch, folder, Save — use this to tell Pages which branch and folder hold the stitched `index.html` · 4. Wait for the build, visit the URL — use this once it says "Your site is live"
- Screenshots: `gh-pages-branch-selected.png`, `gh-pages-live-url.png`
- Speaker notes:
  - Lần đầu chạy mất một hai phút. Dùng thời gian chờ để xem trước phần sau, không ngồi im
  - Nói rõ chữ 'tự cập nhật': đây là mục tiêu thật của bài, rất dễ bị bỏ qua như một chú thích nhỏ
  - Ví dụ: như link prototype Figma tự hiện thiết kế mới khi file được sửa, không cần gửi link khác
  - Kiểm tra: link đang mở trên trình duyệt và hiện đúng sản phẩm thật, không phải danh sách file

---

## 5. The Collaboration

### SECTION DIVIDER · Section 5: The Collaboration
- Kicker: Section 5
- Title: The\nCollaboration
- On-slide: Join a teammate's project, work on your own copy, then ask for a review.
- Speaker notes:
  - Từ đầu đến giờ là dự án của chính mình, giờ chúng ta tham gia một dự án do người khác tạo
  - Ví dụ: trước đây thiết kế app một mình, giờ vào file chung của team để cùng làm các màn hình

### DIAGRAM · Not Alone in This Repo for Long
- Kicker: What changes with a team
- Title: Right now you're the only one in this repo.\nThat won't last.
- On-slide diagram: You, local branch (`feature/rules-v2`) → push / pull → GitHub shared team repo (`rules.md · v2 merged`) → pull / push → teammate's laptop
- On-slide captions: You push your branch to the shared repo — that's the workspace everyone can see · Your teammate pulls it down; nothing syncs by itself · Pull when you sit down, push when you stand up, and clashes stay small
- Speaker notes:
  - Mở đầu 25 phút tiếp theo: trước giờ là dự án của mình, giờ mình vào dự án của người khác
  - Ví dụ: như file thiết kế chung của team nhưng không tự đồng bộ. Mình phải tự đẩy phần mình lên và tự tải phần của bạn về
  - Push là 'đứng dậy thì gửi phần mình lên', Pull là 'ngồi xuống thì xem bạn có cập nhật gì không'
  - Khi hai người sửa cùng một chỗ, công cụ sẽ hỏi giữ bản nào. Ví dụ: hai người cùng đổi màu một nút. Chọn bản nào là quyết định thiết kế, không phải lỗi
  - Nói to: dự án mẫu là công khai, ai cũng nhìn thấy mọi thứ đã đẩy lên. Không bao giờ để mật khẩu hay key
- 🎨 Visual: Three-node sync diagram (laptop → GitHub → teammate's laptop) with push/pull arrows.

### STEPS · Clone the Team's Repo
- Kicker: Step 1: joining
- Title: Clone the team's project,\nthen read it first.
- On-slide, three columns: 1. Accept the invite — open the invite email or GitHub notification, click Accept, do this once; it lets your account add your work to the team's project · 2. Clone — in GitHub Desktop: File → Clone Repository, paste the project link, pick a fresh folder · 3. Read first — README: how the project works; rules file and CONTRIBUTING.md: how the team works; do this before you change anything
- Screenshot: `clone-repo.png`
- Speaker notes:
  - Dự án mẫu công khai nhưng muốn đẩy bài lên phải được mời. Gửi lời mời trước buổi học và xác nhận mọi người đã nhận
  - Clone là tải về một dự án đã có trên GitHub. Add Local Repository là chỉ vào thư mục đã có sẵn trên máy
  - Ví dụ: Clone giống Duplicate file của team về mục Drafts để làm việc. Add là mở lại file đã có sẵn trên máy
  - Chọn một thư mục mới cho bản clone, không dùng thư mục dự án của chính mình
  - Luôn đọc README, rules file và CONTRIBUTING.md trước khi sửa. Ví dụ: đọc design guideline của team trước khi thiết kế màn hình mới
  - Kiểm tra: dự án mẫu đã mở trong GitHub Desktop và ba file trên đã được đọc
- 🎨 Visual: Three numbered columns with the Clone Repository dialog screenshot.

### NUMBERED · The Team Loop
- Kicker: The loop you'll repeat
- Title: Pull. Branch. Commit.\nPush. Pull request. Pull.
- On-slide, six cells: 1 Pull — check for new work from the team every time you sit down · 2 Branch — a new branch for each change, like `tokens/update-spacing`; your own copy to try things in; never work directly on main · 3 Commit — save it with one clear note on what changed and why · 4 Push the branch — Publish branch sends your copy to GitHub and leaves the team's main version alone · 5 Pull request — describe your change; a teammate looks it over and approves it, then it is merged into main · 6 Pull again — bring in the approved result, then start your next branch
- Speaker notes:
  - Đi qua sáu bước theo thứ tự một lần, rồi chạy thật trên dự án mẫu với một thay đổi rất nhỏ (đổi một token hoặc một dòng trong rules file)
  - Vì sao cần Branch: Main là file chính của cả nhóm, đẩy sai lên đó thì ai cũng bị hỏng. Ví dụ: không ai sửa thẳng design system đang dùng, mọi người thử ý tưởng trong một branch riêng
  - Vì sao cần Pull request: đây là chỗ duy nhất để bạn khác nói 'tên token này bị trùng rồi' trước khi thay đổi vào file chính. Ví dụ: nhờ đồng nghiệp comment vào màn hình trước khi bàn giao
  - Khi hai người sửa cùng một dòng, GitHub Desktop sẽ hỏi giữ bản nào. Ví dụ: hai người cùng đổi spacing của một nút, phải bàn xem chọn số nào
  - Kiểm tra: pull request đã mở trên GitHub và đã được merge
- 🎨 Visual: Two-row grid of six cards.

### TWO-CARD · The Working Agreement Ships With the Repo
- Kicker: The team's one-page SOP
- Title: The working agreement\nships with the repo.
- Left card — CONTRIBUTING.md: never work directly on main, one branch per change · check for new work before you start each session · branch names `area/short-description` · commit notes say what changed and why
- Right card — Pull requests & staying safe: every pull request has a short summary, a screenshot if the UI changed, and which tokens or components you touched · one teammate reviews, the owner merges · two people changed the same file? stop and ask who owns it · this project is public, so never add passwords, keys or `.env` files
- Speaker notes:
  - Bản thỏa thuận làm việc chỉ dài một trang, nằm ngay trong dự án với tên CONTRIBUTING.md, cả người và công cụ AI đều đọc được
  - Nói to: đây lại là ý tưởng rules file, một tài liệu viết ra chứ không phải lời dặn miệng. Ví dụ: design guideline của team được ghi lại để ai vào cũng làm theo
  - Mở file CONTRIBUTING.md thật của dự án mẫu trên màn hình, không đọc lại slide
  - Câu hỏi cuối phần: ai là người duyệt và ai là người merge trong team của mình?
- 🎨 Visual: Lavender background; two white cards with mono labels.

---

## 6. The AI-Tool Shortcut

### SECTION DIVIDER · Section 6: The AI-Tool Shortcut
- Kicker: Section 6
- Title: The AI-Tool\nShortcut
- On-slide: Every Git habit, asked for in plain language.
- Speaker notes:
  - Mười phút, không dạy lại từ đầu. Mình đã làm việc với công cụ AI từ Bài 1, đây là cùng thói quen cho một mục tiêu mới
  - Ví dụ: như nhờ công cụ AI dựng prototype bằng cách mô tả màn hình cần làm, giờ nhờ nó làm việc Git bằng cách mô tả điều mình cần

### PROMPT · First Push Through Your AI Tool
- Kicker: Once per project
- Title: Set up the first push\nthrough your AI tool.
- On-slide prompt: "Push the [Project Name] folder to my new GitHub repo: https://github.com/<username>/<repo>.git — Init git if needed, commit everything as "Initial commit", and push to main."
- On-slide caption: Swap in your own folder name and repo URL, and create the empty repo first.
- Speaker notes:
  - Dùng một lần cho mỗi dự án, ngay sau khi tạo repo trống trên GitHub
  - Dán link repo, nói tên thư mục, ghi rõ lời nhắn commit và nhánh để công cụ không phải đoán
  - Ví dụ: như viết prompt dựng màn hình cho đủ: màn hình nào, bố cục ra sao, màu gì. Càng rõ thì kết quả càng đúng
  - Sau đó, câu lệnh hằng ngày ở slide tiếp theo sẽ thay thế
- 🎨 Visual: Dark chat-bubble prompt card.

### PROMPT · Publish Through Your AI Tool
- Kicker: The same habit, pointed at GitHub
- Title: Publish through\nyour AI tool.
- On-slide prompt: "Commit these changes with a short message describing what changed, and push them to GitHub."
- Speaker notes:
  - Làm thử cửa sổ xin quyền đăng nhập trên máy mình trước để không bị bất ngờ khi tự làm
  - Giữ cách gọi chung là 'công cụ AI viết code', vì bài này áp dụng cho mọi công cụ
  - GitHub Desktop vẫn là nền tảng bên dưới cho cả hai cách
  - Ví dụ: như bảo công cụ AI 'đổi màu nút này' thay vì tự mở code. Ở đây là 'lưu và gửi lên giúp mình'
- 🎨 Visual: Dark chat-bubble prompt card.

### CARD GRID · More Things to Ask Your AI Tool
- Kicker: Beyond commit and push
- Title: Six more things\nto ask for.
- On-slide, six prompt cards: Get the team's latest — "Check if my teammates added anything new, and bring it into my project." · Start a new branch — "Create a new branch called tokens/update-spacing and switch to it. Don't touch main." · See what changed — "Show me what I've changed since my last commit, in plain language." · Ask for a review — "Open a pull request for this branch. Write a short summary of what changed and why." · Join a team project — "Clone https://github.com/<username>/<repo>.git into a new folder and tell me what's in it." · Go back one step — "Undo my last commit but keep my changes, so I can edit them again."
- Speaker notes:
  - Cùng một thói quen: mô tả điều muốn làm, không cần nhớ tên nút
  - Chọn hai thẻ để làm thử trực tiếp, bốn thẻ còn lại để tra cứu
  - Ví dụ 1: 'Lấy bản mới của team về' giống cập nhật thư viện component khi team có bản mới
  - Ví dụ 2: 'Tạo branch mới' giống duplicate màn hình để thử một ý tưởng mà không làm hỏng bản đang dùng
  - Ví dụ 3: 'Quay lại một bước' giống Undo hoặc mở lại một version cũ trong history
  - Luôn đọc câu trả lời của công cụ AI trước khi đồng ý, nhất là những việc sửa hoặc xóa commit
- 🎨 Visual: Six prompt cards in a 3×2 grid; two to try live, four for reference.

---

## 7. Closing

### CLOSING · What You've Got
- Kicker: Lesson 4: arc complete
- Title: What You've\nGot.
- On-slide checklist: ✓ Project connected to a real GitHub repo · ✓ At least two commits pushed, one of them unaided · ✓ A live, self-updating URL · ✓ A pull request merged into a team repo
- On-slide line: Exit ticket — publish one more thing on your own this week.
- Author: Winnie Nguyen
- Speaker notes:
  - Tóm tắt lại bằng lời của chính mình nếu còn thời gian, giống cách kết thúc ở Bài 1 đến 3
  - Đây là buổi cuối của cả hành trình, nói rõ điều đó rồi giới thiệu Bài 5 là phần thưởng tùy chọn
  - Ví dụ để kết: từ prototype chỉ có trên máy mình thành một sản phẩm thật của cả team, có link, có lịch sử, có review
- 🎨 Visual: Lavender background; four-item checklist, exit ticket line beneath.

---

## Drift to resolve

Where the deck and the lesson stub (`lesson-3-4-stub.md`) disagree. The lesson file wins per the sync rule, but it is still an objectives-only stub, so this needs a decision rather than a silent overwrite.

- **No "Simulate One Oops" section.** The stub plans "simulate one mistake and recover from it" — "the part students actually need". The deck now has only the "Go back one step" prompt card (slide 21). The Discard Changes and Amend Commit screenshots were never recoverable.
- **No solo practice rep, no SHOW teach-back, no presentation coaching.** The closing checklist still promises "at least two commits pushed, one of them unaided", but no slide makes that second commit happen.
- **Agenda is 90 minutes against a 100-minute title.** The notes say the rest is transitions and Q&A. Confirm that is intended.
- **"You published the method too" line is gone.** The stub's instructor notes ask the close to say the rules file ships with the repo. The CONTRIBUTING.md slide (17) says it for the SOP, but not for the Lesson 1/3 rules file.
- **Setup slide wording.** Slide 6 step 2 says "Create a new Repo" while its notes warn against the "Create New" habit and say to use Add. One of them is stale.
- **Closing notes call Lesson 5 an optional bonus**, as the previous deck did — confirm against the Lesson 5 outline.

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026*

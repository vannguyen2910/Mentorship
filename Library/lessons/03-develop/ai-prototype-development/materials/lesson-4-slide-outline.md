---
title: "Lesson 4: Publish It"
lesson_file: "lesson-3-4-stub.md"
level: "intermediate"
slide_count: 25
duration: "100 min"
status: deck-built
built_deck: "../slides/AI Prototyping - Lesson 4.html"
last_synced: 2026-10-03
---

> **Reverse-synced from the built deck on 2026-10-03 (third pass).** The deck was reworked again in the design tool: the team-collaboration section became a **solo "Try Ideas Safely" section on the mentee's own repo** (branch, self-reviewed pull request, merge), a localhost-preview slide was added before the first commit, and a **Homework** slide was added before the close. The sandbox repo and Clone slide are gone from the deck. The lesson file (`lesson-3-4-stub.md`) was re-synced the same day.
> **Speaker notes are Vietnamese bullets, copied from the deck.** Each carries a Figma-based analogy ("Ví dụ"). English slide copy stays English. Checkpoints ("Kiểm tra") live in the notes, not on a slide.
> **The ten-word glossary (slide 4) is the reference for the whole lesson** — notes tell the facilitator to come back to it for Branch, Main and Pull request in Section 5. In this version Main is "your live site", and a pull request on your own repo is a self-review.
> **Previous versions archived** in `slides/_archive/` — including the collaboration-based deck with the Clone slide and the sandbox-repo walkthrough.

---

## Session metadata

| Field | Value |
|---|---|
| Program | SYSTEMATIC AI PROTOTYPING |
| Track / session | Lesson 4 |
| Stage | Develop |
| Prior session | Lesson 3: Scaling the Prototype |
| Next session | Lesson 5: Beyond the Pattern (optional bonus) |
| Running example | The mentee's own anchor project and its live site |
| Deck file | `slides/AI Prototyping - Lesson 4.html` |

## Slide structure — 25 slides

| # | Section | Slides | Minutes |
|---|---|---|---|
| 0 | Opening | 2 | — |
| 1 | The Local-vs-Published Mental Model | 3 | 10 |
| 2 | Setup & Connect | 2 | 10 |
| 3 | First Publish | 4 | 20 |
| 4 | Make It Live | 3 | 15 |
| 5 | Try Ideas Safely | 5 | 25 |
| 6 | The AI-Tool Shortcut | 4 | 10 |
| 7 | Homework | 1 | — |
| 8 | Closing | 1 | — |

> **Agenda adds up to 90 minutes** (10 + 10 + 20 + 15 + 25 + 10) under a "One hundred minutes" title; the Agenda notes say "about 90 minutes of content, the rest for transitions and Q&A".
> **Section 5 runs on the mentee's own repo, not a sandbox.** Main is the live site, so every push is public; branches are how a solo designer tests an idea safely. A one-page `CONTRIBUTING.md` is the mentee's own rulebook — template at `materials/contributing-template.md`, and Homework 2 has them copy it.

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
- On-slide, numbered with minutes: 01 Local vs. Published (10) · 02 Setup & Connect (10) · 03 First Publish (20) · 04 Make It Live (15) · 05 Try Ideas Safely (25) · 06 The AI-Tool Shortcut (10)
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
- On-slide, ten terms: Repo — the project's home on GitHub, with all its files and history · Clone — download a copy of a project from GitHub to your laptop · Commit — a saved snapshot, with a short note describing what changed · Push — sending your commits up to GitHub · Pull — bringing the latest changes from GitHub down to your laptop · Branch — your own copy of the project to try changes in, without touching the original · Main — the official version, and your live site; never edit it directly · Pull request — asking for a review of your branch before it joins main; alone, you review it yourself (GitLab: Merge Request) · Merge — adding your approved changes into main · Clash — two copies changed the same thing, so you choose which version to keep
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

### PROMPT · Preview It Through Your AI Tool
- Kicker: Before every commit
- Title: Preview it first,\nthen publish.
- On-slide prompt: "Run localhost so I can preview my work."
- On-slide cards: What is localhost? — a private preview that only opens on your own computer; nobody else can see it yet · Use this every time — before you commit, so you only publish work you have clicked through
- Speaker notes:
  - Đây là câu lệnh dùng trước mỗi lần commit, nên nói rõ 'mỗi lần'
  - localhost là bản xem thử riêng chỉ mở được trên máy mình, giống mở prototype ở chế độ Preview trước khi bấm Share
  - Cho xem cách làm: gõ câu lệnh, công cụ AI mở một địa chỉ như http://localhost:3000, bấm thử vài nút
  - Nếu bản xem thử sai thì sửa ngay, vì những gì được commit và push sẽ lên mạng thật
  - Kiểm tra: bản xem thử đã mở trên trình duyệt và chạy đúng
- 🎨 Visual: Dark chat-bubble prompt card, two light explainer cards beneath.

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

## 5. Try Ideas Safely

### SECTION DIVIDER · Section 5: Try Ideas Safely
- Kicker: Section 5
- Title: Try Ideas\nSafely
- On-slide: Work on a branch, review it yourself, then merge it into main.
- Speaker notes:
  - Từ đầu đến giờ mọi thay đổi đi thẳng vào bản chính. Giờ mình học cách thử ý tưởng mà không làm hỏng bản đang chạy
  - Ví dụ: không sửa thẳng lên file Figma đang bàn giao cho khách, mà duplicate ra một trang nháp để thử rồi mới đưa vào

### DIAGRAM · Every Push Goes Live
- Kicker: Why branches matter, even alone
- Title: Right now every push\ngoes straight to your live site.
- On-slide diagram: You, local branch (`try/new-nav`) → push / pull → GitHub: your repo + live site (`main · live site`) → pull / push → your other laptop
- On-slide captions: You push your branch to GitHub; your live site, main, stays untouched · On another laptop, pull to bring it down; nothing syncs by itself · Try the idea on a branch. Only what you merge reaches main.
- Speaker notes:
  - Mở đầu phần này: làm một mình nhưng vẫn cần an toàn, vì mỗi lần push vào main là live site đổi ngay
  - Ví dụ: sửa thẳng trên bản đang chạy giống như chỉnh prototype khi khách đang xem. Branch giống duplicate ra một trang nháp để thử
  - Push là 'đứng dậy thì gửi lên', Pull là 'ngồi xuống ở máy khác thì tải về'. Dùng hai laptop hoặc để công cụ AI push thay thì Pull càng quan trọng
  - Nếu thử hỏng thì bỏ branch đi, main không bị ảnh hưởng
  - Nói to: repo công khai thì ai cũng thấy mọi thứ đã đẩy lên. Không bao giờ để mật khẩu hay key
- 🎨 Visual: Three-node sync diagram with push/pull arrows.

### STEPS · Branch Before You Change Anything
- Kicker: Step 1: branch
- Title: Make a branch,\nthen work on it.
- On-slide, three columns: 1. New branch — in GitHub Desktop: Current Branch → New Branch; name it for the idea, like `try/new-nav` · 2. Change and commit — make the change, preview it with localhost; commit with a note on what changed and why · 3. Publish branch — click Publish branch; your live site, main, stays untouched
- On-slide flag: Never work directly on main. It is your live site.
- Speaker notes:
  - Làm thật trên dự án của mình, không cần dự án mẫu
  - Ví dụ: Branch giống duplicate trang Figma để thử bố cục mới. Không ai bàn giao từ trang nháp
  - Luôn xem thử bằng localhost trước khi commit
  - Nói to: không bao giờ làm trực tiếp trên main vì main là live site
  - Kiểm tra: branch mới đã được publish và hiện trong GitHub Desktop
- 🎨 Visual: Three numbered columns.

### NUMBERED · The Safe Loop
- Kicker: The loop you'll repeat
- Title: Pull. Branch. Commit.\nPush. Pull request. Merge.
- On-slide, six cells: 1 Pull — check GitHub for new changes before you start, especially with two laptops or when your AI tool pushes for you · 2 Branch — a new branch for each idea, like `tokens/update-spacing`; your own copy to try things in · 3 Commit — one clear note on what changed and why · 4 Push the branch — Publish branch sends your copy to GitHub and leaves main alone · 5 Pull request — open it on your own repo and read the changes as if someone else wrote them · 6 Merge, then pull — merge into main and your live site updates; pull, then start your next branch
- Speaker notes:
  - Đi qua sáu bước theo thứ tự một lần, rồi chạy thật trên dự án của mình với một thay đổi rất nhỏ (đổi một token hoặc một dòng trong rules file)
  - Vì sao cần Branch: main là live site, đẩy sai lên đó thì ai mở link cũng thấy lỗi. Thử ý tưởng trong branch riêng thì hỏng cũng không sao
  - Vì sao cần Pull request khi làm một mình: đây là lúc đọc lại thay đổi như người khác viết, giống xem lại màn hình trước khi bàn giao. Công cụ AI có thể sửa nhiều file cùng lúc nên bước này bắt lỗi rất tốt
  - Merge xong thì live site tự cập nhật, đó là phần thưởng của vòng lặp
  - Kiểm tra: pull request đã mở trên GitHub, được đọc lại và merge
- 🎨 Visual: Two-row grid of six cards.

### TWO-CARD · Your Rules Ship With the Repo
- Kicker: Your one-page rulebook
- Title: Your rules\nship with the repo.
- Left card — CONTRIBUTING.md: never work directly on main, one branch per idea · pull before you start each session · branch names `area/short-description` · commit notes say what changed and why
- Right card — Pull requests & staying safe: every pull request has a short summary, a screenshot if the UI changed, and which tokens or components you touched · read your own changes before you merge · something broke? delete the branch, main is untouched · public repo: never add passwords, keys or `.env` files
- Speaker notes:
  - Bản rulebook chỉ dài một trang, nằm ngay trong dự án với tên CONTRIBUTING.md, cả mình và công cụ AI đều đọc được
  - Nói to: đây lại là ý tưởng rules file, một tài liệu viết ra chứ không phải nhớ trong đầu. Ví dụ: design guideline được ghi lại để lần sau làm theo mà không phải nghĩ lại
  - Mở file CONTRIBUTING.md mẫu trên màn hình, không đọc lại slide
  - Câu hỏi cuối phần: nếu hỏng thì làm gì? Trả lời: xóa branch, main vẫn nguyên
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
- On-slide, six prompt cards: Get the latest — "Check if GitHub has anything new for this project, and bring it into my folder." · Start a new branch — "Create a new branch called tokens/update-spacing and switch to it. Don't touch main." · See what changed — "Show me what I've changed since my last commit, in plain language." · Open a pull request — "Open a pull request for this branch. Write a short summary of what changed and why." · Set up on another laptop — "Clone https://github.com/<username>/<repo>.git into a new folder and tell me what's in it." · Go back one step — "Undo my last commit but keep my changes, so I can edit them again."
- Speaker notes:
  - Cùng một thói quen: mô tả điều muốn làm, không cần nhớ tên nút
  - Chọn hai thẻ để làm thử trực tiếp, bốn thẻ còn lại để tra cứu
  - Ví dụ 1: 'Lấy bản mới của team về' giống cập nhật thư viện component khi team có bản mới
  - Ví dụ 2: 'Tạo branch mới' giống duplicate màn hình để thử một ý tưởng mà không làm hỏng bản đang dùng
  - Ví dụ 3: 'Quay lại một bước' giống Undo hoặc mở lại một version cũ trong history
  - Luôn đọc câu trả lời của công cụ AI trước khi đồng ý, nhất là những việc sửa hoặc xóa commit
- 🎨 Visual: Six prompt cards in a 3×2 grid; two to try live, four for reference.

---

## 7. Homework

### HOMEWORK · Three Things Before Next Time
- Kicker: Homework
- Title: Three things\nbefore next time.
- On-slide, three tasks, each with a "Done when": 1. Start a new repo — pick a project not on GitHub yet; preview it with localhost, create the repo and commit; publish it for the first time on your own, then turn on Pages. Done when: the project has its own live URL · 2. Write your project's rules — copy the CONTRIBUTING.md template; fill in branch names and how you write commit notes; save it in your project and push it. Done when: the file is on GitHub · 3. Practice the loop solo — make a new branch; commit one tiny change and publish the branch; open a pull request on your own repo, review it yourself, then merge it. Done when: your pull request is merged
- Speaker notes:
  - Giao bài tập về nhà ngay trước phần kết, để mình ra về với việc cụ thể
  - Việc 1 là tự tạo repo mới và push lần đầu cho một dự án khác, đúng như checklist ở slide cuối đã hứa về commit tự làm. Có thể dùng GitHub Desktop hoặc câu lệnh nhờ công cụ AI
  - Việc 2 dùng lại ý tưởng rules file: viết luật ra giấy để chính mình và công cụ AI cùng làm theo, không phải nhớ trong đầu
  - Việc 3: dù làm một mình, vẫn tạo branch và pull request cho dự án của mình. Tự xem lại thay đổi trước khi merge giống như xem lại màn hình trước khi bàn giao. Main luôn sạch, và thử hỏng thì bỏ branch đi
  - Việc 1 và 3 đều nên xem thử bằng localhost trước khi commit
  - Gửi link kết quả hoặc ảnh chụp trước buổi sau để được góp ý
- 🎨 Visual: Three numbered task cards, each ending in a Done-when line.

---

## 8. Closing

### CLOSING · What You've Got
- Kicker: Lesson 4: arc complete
- Title: What You've\nGot.
- On-slide checklist: ✓ Project connected to a real GitHub repo · ✓ At least two commits pushed, one of them unaided · ✓ A live, self-updating URL · ✓ A pull request merged into your own repo
- On-slide line: Exit ticket — publish one more thing on your own this week.
- Author: Winnie Nguyen
- Speaker notes:
  - Tóm tắt lại bằng lời của chính mình nếu còn thời gian, giống cách kết thúc ở Bài 1 đến 3
  - Đây là buổi cuối của cả hành trình, nói rõ điều đó rồi giới thiệu Bài 5 là phần thưởng tùy chọn
  - Ví dụ để kết: từ prototype chỉ có trên máy mình thành một sản phẩm thật của cả team, có link, có lịch sử, có review
- 🎨 Visual: Lavender background; four-item checklist, exit ticket line beneath.

---

## Drift to resolve

Where the deck and the lesson file (`lesson-3-4-stub.md`) may still disagree after this pass; the lesson file's "Open decisions" list is the working copy.

- **Agenda is 90 minutes against a "One hundred minutes" title.** The Agenda notes say the remainder is transitions and Q&A. Homework adds no in-session time.
- **No "simulate a mistake and recover" beat, no teach-back, no presentation coaching.** Recovery survives only as the "Go back one step" prompt card and the "delete the branch, main is untouched" line.
- **The "unaided second commit" promised on the closing checklist is now Homework task 1**, so the checklist is satisfied after the session, not during it.
- **Setup slide wording.** Slide 6 step 2 says "Create a new Repo" while its notes warn against the "Create New" habit and say to use Add.
- **Closing notes call Lesson 5 an optional bonus** — confirm against the Lesson 5 outline.
- **Team collaboration is no longer taught here.** Clone, a shared repo and teammates' review appear only in the glossary and the "Set up on another laptop" prompt. If Lesson 5 is meant to pick that up, check its outline expects it.

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026*

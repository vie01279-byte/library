from pathlib import Path
import json, re

BOOK = Path('books/la-connect.html')
CATALOG = Path('data/library.json')

vi = r'''Ngày 5 tháng 8 năm 2026, khi viết phần phụ lục về LA-P để khép lại bản LA-CONNECT lúc ấy, tôi đã cố ghi lại hệ thống ở trạng thái mà mình có thể nhìn thấy rõ nhất. LA-P đã có những gói kỹ năng, các quy trình làm việc, những lớp hướng dẫn, các công cụ xử lý dữ liệu và một cơ chế để những bài học sau mỗi lần sửa không biến mất cùng phiên trò chuyện. Tôi đã đi một quãng đủ dài để tin rằng thứ mình làm ra không còn chỉ là vài câu lệnh hay vài đoạn hướng dẫn rời rạc.

Một hệ thống có thể rất hữu ích với người tạo ra nó mà vẫn chưa phải một sản phẩm thật sự dành cho người khác. Tôi biết dữ liệu nằm ở đâu, phần hướng dẫn nào nên được gọi ra, quy trình nào đang có giới hạn, khi nào cần nhìn vào dòng lệnh, khi nào phải quay lại lịch sử thay đổi, và nếu Agent cư xử lạ thì nên nghi ngờ phần nào trước. Những hiểu biết ấy vẫn nằm trong đầu tôi nhiều hơn tôi muốn thừa nhận. Nếu người dùng mới vẫn cần tôi ngồi cạnh để chỉ cách cài đặt, kết nối môi trường, tìm đúng chức năng hay xử lý một trục trặc kỹ thuật, thì tôi mới chỉ chuyển công việc của mình vào một hệ thống phức tạp hơn; tôi chưa thật sự chuyển giao được nó.

Từ sự trăn trở đó, tôi bắt đầu LA-Page.

## Khi LA-P trở thành LA-PAGE

Ngay từ ngày 22 tháng 8, LA-Page đã được xác định không phải là một lớp giao diện đẹp hơn đặt lên trước LA-P, càng không phải một bản sao mới của AppSheet. Mục tiêu là tạo ra một ứng dụng web độc lập cho công việc giám định tổn thất, nơi người dùng chỉ cần mở trình duyệt và đi qua một hành trình làm việc liền mạch: đăng nhập, tạo và quản lý hồ sơ vụ việc, phân công, khảo sát hiện trường, yêu cầu chứng từ, đọc và tổ chức tài liệu, chuẩn bị báo cáo, dùng AI khi phù hợp, chuyển hồ sơ để kiểm tra và phê duyệt, lưu lại dấu vết thay đổi và tiếp tục công việc trên máy tính, máy tính bảng hoặc điện thoại.

Bên dưới vẫn có thể là cơ sở dữ liệu, Google Drive, các chương trình xử lý riêng và những năng lực được chọn từ LA-P. Nhưng tất cả những thứ đó phải dần trở nên vô hình đối với người làm nghề.

Tôi không còn muốn người dùng phải biết Git là gì, dòng lệnh nằm ở đâu, tên một gói kỹ năng là gì hay dữ liệu trước đây đến từ AppSheet theo cách nào. Người dùng chỉ cần biết mình đang xử lý hồ sơ tổn thất nào, hồ sơ đang ở giai đoạn nào, việc gì cần làm tiếp theo, tài liệu nào còn thiếu, bằng chứng nào liên quan và quyết định nào vẫn phải do con người chịu trách nhiệm.

Ngay từ cổng quyết định đầu tiên, 3 nhóm người dùng chính được xác định là Giám định viên (LA), NV hỗ trợ ở văn phòng (Admin) và Cấp Quản lý (Senior/Manager). Phiên bản khả dụng tối thiểu cũng không được hiểu là một bản trình diễn có thật nhiều màn hình. Nó phải hỗ trợ được một hành trình công việc có thật: đăng nhập, hồ sơ vụ việc, phân công, tài liệu, hỗ trợ của AI, kiểm tra và phê duyệt, lưu vết và khả năng sử dụng thực tế trên nhiều thiết bị. Những bước xác lập tiếp theo lần lượt khóa phạm vi nghiệp vụ, vòng đời hồ sơ, quyền hạn theo vai trò, kiến trúc dữ liệu và lưu trữ.

## Từ một KHUNG được duyệt đến một chuỗi công việc có thật

Bản thiết kế sản phẩm dần hình thành với những khu vực chính như tổng quan công việc, quản lý hồ sơ, khảo sát hiện trường, yêu cầu tài liệu, kho hồ sơ, báo cáo giám định, tổng hợp bồi thường, bảng chấm công, không gian làm việc với AI, quản lý đội ngũ và quản trị hệ thống. Một quyết định giao diện mà đến nay tôi vẫn thấy đúng là điện thoại không nên bị biến thành phiên bản thu nhỏ của màn hình máy tính. Điện thoại phù hợp hơn với việc chụp, ghi nhận, xem nhanh và trao đổi; còn những bảng dữ liệu lớn và thao tác nặng nên dành cho không gian làm việc rộng hơn.

Hôm nay là ngày CN cuối tuần (06/09), tôi đã sai em AI làm cho tôi cái báo cáo tóm tắt để tạm lưu lại tiến trình còn dở dang, và cũng là để tôi sẽ còn đọc lại rất nhiều lần để "ngấm" dần thành bài học cho hành trình Developer sắp tới. Phần sau đây hầu hết là do AI viết, tôi không chỉnh sửa gì mà để nguyên như vậy cho nó mộc mạc (hihihi).

### 1. Những lần builder bị lạc lối

Tôi thấy có **4 bài học lớn**.

#### a. AppSheet từ migration source dần biến thành “legacy authority”

Ban đầu mục tiêu đúng là:

> migrate data → LA-Page thay AppSheet.

Nhưng trong quá trình MIG-R1, historical incompleteness, legacy mappings, original refs, reconciliation state bắt đầu ảnh hưởng quá mạnh tới thiết kế operational mới.

Có lúc logic trở thành:

> dữ liệu historical null → không cho update Case.

Điều này đảo ngược mục tiêu sản phẩm.

PO sau đó sửa lại thành:

> historical blank business field là hợp lệ và phải được bổ sung.

Và hôm nay PO đi thêm một bước dứt khoát:

> AppSheet migration đã xong → retire toàn bộ legacy identity.

Agent đã triển khai schema `039_retire_appsheet_identity`, giữ 302/302 Case và loại `legacy_case_ref`, `original_case_ref`, legacy mapping/index/trigger.

Theo tôi đây là **correction kiến trúc đúng**.

#### b. UI từng rời khỏi Approved KHUNG

Từ một KHUNG đã nghiệm thu, quá trình build feature tạo dần: - horizontal feature tabs - nested sidebar - nested headers - workspace trong workspace.

Đến mức Master Plan phải mở UI-R1 để reconcile lại AppShell.

Và hôm nay Vie lại phát hiện một phiên bản nhỏ của cùng vấn đề:

> `Case operations / Tạo hồ sơ, phân công và vòng đời`

đang trở thành một shell phụ dưới Case Summary.

Đề xuất **CASE-UX-R1 — Unified Case Summary & Operations** thực chất là tiếp tục sửa cùng root cause này:

**top-level capability thuộc sidebar; Case-specific action thuộc Case context.**

#### c. Infrastructure / Google governance đi quá xa so với giá trị product tại thời điểm đó

Phần D1/OAuth có rất nhiều: - preview - fingerprint - P1/P2/P3/P4 - exact authorization - scheduling - remediation.

Các control này không phải vô nghĩa — security là cần thiết.

Nhưng nhìn lại toàn bộ roadmap, có thời điểm chúng ta dành quá nhiều effort cho Google Cloud/OAuth trong khi: - Claims Bordereau chưa có - Case Summary chưa hoàn chỉnh - Claim Summary chưa build - Dashboard chưa xong - Timesheet/Fee Note chưa thành module operational hoàn chỉnh.

Đây là ví dụ rõ nhất của **correct engineering topic nhưng sai timing**.

#### d. Test harness/environment noise từng bị nhầm thành product failure

Python path cũ, LibreOffice path, concurrency và browser auth session từng gây nhiều vòng troubleshoot.

Sau đó mới xác định root cause là test harness portability chứ không phải business feature.

Harness được sửa thành: - explicit env - PATH - bundled fallback - sequential LibreOffice tests.

Từ đó regression trở lại ổn định.

Đây là technical debt thật, nhưng đáng lẽ nên phân biệt từ đầu:

> **environment failure ≠ product logic failure.**

### 2. Vậy hiện tại chúng ta đang đứng ở đâu?

Có hai lớp trạng thái phải phân biệt.

### Canonical GitHub `main`

Tài liệu canonical tôi đọc hiện vẫn ghi:

> **Priority 1 AppSheet operational migration accepted and closed; Priority 2 Claims Bordereau is next.**

README cũng ghi cùng trạng thái đó.

### Local/current work hôm nay

Trong phiên hiện tại, Agent đã làm thêm nhưng **chưa commit/push**: - Claims Bordereau implementation - table field selector expansion đang chỉnh - column resizing vẫn đang sửa - Case Summary dense spreadsheet view - inline editing - PATCH partial-field correction - Case Summary ↔ Bordereau shared editability - AppSheet legacy retirement schema `039` - proposed Case UX unification.

Vì vậy **current working product đã đi xa hơn canonical Git docs**.

Cho đến khi closure/commit/push, Git main vẫn chưa phản ánh đầy đủ trạng thái hôm nay.

### 3. Phần đã khá vững của LA-Page

Hiện tại tôi xem các foundation sau đã tương đối mạnh: - Approved KHUNG/AppShell - local authentication + 2FA - role/authorization foundation - Case creation/register - assignment/status/lifecycle - tasks/deadlines foundation - Field Survey - BBHT generation - LA Report structured editor - local AI proposal workflow - submission/review/approval/issue - document ingestion/LACDM foundation - Document Request - local file/document register - backup/restore foundation - 302 operational Cases - current canonical CaseRef - audit architecture - regression harness.

Nói cách khác: **LA-Page không còn là prototype sơ khai nữa**.

Nhưng tôi cũng chưa gọi nó là MVP, vì các gap còn lại chạm đúng operational journey mà Gate A yêu cầu.

### 4. MVP GAP — những gì còn thiếu để có thể nói “MVP candidate”

Tôi sẽ thu gọn thành **8 nhóm**, thay vì tiếp tục hàng chục Gate nhỏ.

|MVP area|Current situation|Gap còn lại|
|---|---|---|
|**1. Case Management UX**|backend foundation khá đầy đủ|hoàn thiện Case Summary, Case Detail, inline editing, bỏ nested Case Operations, professional desktop/mobile UX|
|**2. Claims Bordereau**|đang build|column sizing/resizing, complete selectable fields, inline editing, CSV/report consistency, acceptance|
|**3. Claim Summary**|có foundations/AI references nhưng chưa phải operational module hoàn chỉnh|build real Claim Summary workflow/table/calculation/review|
|**4. Documents + Drive**|local foundation PASS, OAuth/sandbox groundwork có|controlled production-like Drive lifecycle chưa hoàn tất/được mở|
|**5. Dashboard / My Work**|architecture đã định nghĩa|operational dashboard, workload, deadlines, next actions, management view|
|**6. Timesheet & Fee Note**|data/migration và một số capability có|user-facing complete Timesheet/Fee Note workflow chưa đóng|
|**7. Unified Approval / Notifications**|report approval đã có|cross-module Approval Inbox, deadlines/reminders/notification operationalization|
|**8. One end-to-end AI-assisted real workflow + pilot readiness**|local AI/report pieces có|nối Case → evidence → LA-P/AI → human review → output → audit thành một workflow thật, rồi limited pilot/monitoring/recovery|

Ngoài 8 nhóm đó còn một gap security riêng đã được Master Plan nhắc rõ: **Sole Administrator Recovery** vẫn chưa được giải quyết; UI-R1 không đóng gap này.

### 5. Nếu vẽ đường từ hôm nay tới MVP, tôi sẽ không quay lại roadmap kiểu cũ

Tôi nghĩ từ đây cần tránh mở thêm “Gate trong Gate”.

Đường ngắn nhất hợp lý là:

**Case UX hoàn thiện → Claims Bordereau đóng → Claim Summary → controlled Documents/Drive → Dashboard/My Work → Timesheet & Fee Note → unified Approval/Notifications → one AI-assisted end-to-end workflow → monitoring/recovery → limited pilot rehearsal → PO MVP acceptance.**

Đây cũng phù hợp hơn với Product Vision: người Loss Adjuster phải mở một Case và biết **case đang ở đâu, cần làm gì tiếp theo, evidence nào liên quan, có quyền làm gì và sản phẩm nào cần review**.

## Nếu bắt đầu lại, tôi sẽ làm khác điều gì?

Bài học đáng tái sử dụng nhất của LA-Page không nằm ở Next.js, SQLite, Google Drive hay một nhà cung cấp nhận dạng ký tự nào. Nó nằm ở cách phân quyền, cách giới hạn ngữ cảnh và kích thước của công việc giao cho AI Agent.

Tôi vẫn sẽ giữ một kế hoạch tổng thể. Nhưng trước mỗi phần việc, tôi muốn có một cam kết sản phẩm rất ngắn: mục tiêu là gì; nằm trong phạm vi nào; điều gì nằm ngoài phạm vi; quyết định nào của người chủ sản phẩm đã khóa; tiêu chí chấp nhận là gì; và khi nào phải dừng.

Người xây không cần mang hàng trăm dòng lịch sử dự án trong đầu để làm một thay đổi nhỏ. Ký ức của dự án và ngữ cảnh cần thiết để thực hiện một phần việc là hai thứ khác nhau. Lịch sử phải được giữ ở nơi bền vững; còn người thực hiện chỉ cần đủ thông tin để không vi phạm cam kết hiện tại.

Nếu KHUNG đã duyệt, tôi cần cài quy tắc khóa - để bắt Agent phải coi nó là một nguyên tắc cấu trúc bắt buộc. Một chức năng mới có thể bổ sung trạng thái, biểu mẫu, hành vi và độ hoàn thiện, nhưng không được tự ý tạo thêm một lớp KHUNG khác.

Tôi cũng sẽ sắp xếp công việc theo câu hỏi: “Sau phần này, người dùng làm được trọn vẹn việc gì mới?” thay vì: “Chúng ta vừa hoàn tất thêm hệ thống kỹ thuật nào?”. Mỗi phần việc cần tạo ra tiến bộ có thể nhìn thấy và sử dụng được, rồi dừng đúng lúc: hiểu yêu cầu, xây dựng, xem thử, kiểm tra, người chủ sản phẩm chấp nhận, dừng. Không có “tiện đây làm thêm”. Không mặc nhiên mở thêm năm đầu việc mới chỉ vì Agent phát hiện ra chúng.

Tôi vẫn muốn dự án dựa trên bằng chứng, nhưng không muốn nó bị cai trị bởi thủ tục. Thay đổi phá hủy cấu trúc dữ liệu, tác động lên Google Drive thật hoặc đưa ra kết luận chuyên môn rõ ràng là những việc cần kiểm soát mạnh và phải có con người xem lại. Khoảng cách giữa hai nút bấm thì không cần một hội đồng kiến trúc. Vị trí một nút không cần cả một quy trình quản trị. Một phần đã được chấp nhận không nên tự động bị mở lại nếu không có lỗi hoặc lý do sản phẩm thực sự.

Kiểm soát an toàn và kiểm soát quan liêu là hai việc khác nhau.

Và chính ở đây, ý tưởng tổ chức nhiều Agent theo vai trò bắt đầu có ý nghĩa với tôi. Không phải vì bốn Agent chắc chắn thông minh hơn một Agent, mà vì mỗi Agent có thể được trao ít quyền hơn và ít ngữ cảnh hơn.

Người chủ sản phẩm vẫn là người quyết định. Một Agent giữ cam kết sản phẩm hiểu lịch sử và khóa phạm vi. Một Agent xây dựng chỉ thực hiện phần việc đã được giao. Một Agent kiểm tra chỉ xác minh kết quả chứ không âm thầm sửa lại. Một Agent kiểm toán rủi ro chỉ xuất hiện khi có dấu hiệu đủ nghiêm trọng để cần thêm một lớp kiểm tra. Sau đó mọi thứ quay lại cho người chủ sản phẩm chấp nhận.

Giá trị không nằm ở “nhiều Agent hơn”.

Giá trị nằm ở **tách quyền hạn**.

Nếu phải thu gọn mô hình làm dự án sau LA-Page thành vài tài liệu bền vững, tôi sẽ chỉ giữ những thứ thật sự cần: một tài liệu xác định phương hướng sản phẩm, một bản thiết kế sản phẩm, một kế hoạch tổng thể, một tệp nguyên tắc bắt buộc, một bản bàn giao trạng thái hiện tại và một cam kết riêng cho từng phần việc. Vòng làm việc cũng nên ngắn tương ứng: hiểu ý định, khóa phạm vi, xây dựng, xem thử, kiểm tra, chấp nhận, lưu lại trạng thái rồi chuyển sang bước kế tiếp.

Không có chuyện “tiếp tục cải thiện” vô hạn.

Không tự mở rộng phạm vi chỉ vì AI nhìn thấy thêm cơ hội để làm mọi thứ phức tạp hơn.

## LA-Page đã tạo ra thứ gì ngoài chính LA-Page?

Phụ lục tôi viết ngày 5 tháng 8 kết lại bằng nhận xét rằng LA-P đã thành hình, đã tạo ra giá trị, vẫn mắc lỗi và vẫn đang được xây dựng. Một tháng sau, LA-Page khiến phần chưa giải quyết của câu ấy trở nên cụ thể hơn.

Vấn đề không còn chỉ là làm sao để Agent nhớ đúng một kỹ năng hay thực hiện đúng một quy trình. Vấn đề là làm sao biến tất cả những năng lực đó thành một sản phẩm mà người khác có thể sử dụng mà không phải học cách trở thành tôi trước đã.

LA-Page chưa trả lời xong câu hỏi đó. Bản thân dự án vẫn còn đang trên đường tới một phiên bản khả dụng tối thiểu. Nhưng nó đã tạo ra một thứ có thể sống lâu hơn nhiều chức năng riêng lẻ: một cách rõ ràng hơn để làm sản phẩm cùng AI Agent.

**Cam kết nhỏ → quyền hạn giới hạn → phần sản phẩm nhìn thấy được → bằng chứng → người chủ sản phẩm chấp nhận → dừng.**

Tôi bắt đầu LA-Page vì muốn LA-P bước ra khỏi môi trường của người đã xây nó. Trong quá trình ấy, tôi nhận ra mình cũng phải bước ra khỏi một thói quen của chính mình: tin rằng càng có nhiều năng lực, càng nhiều lớp kiểm soát, càng nhiều cổng kiểm tra và càng nhiều thứ được xây thì sản phẩm càng gần ngày hoàn thành.

Không nhất thiết như vậy.

Một sản phẩm tiến gần tới người dùng không phải khi sơ đồ kiến trúc của nó dài thêm, mà khi người dùng phải nghĩ ít hơn về hệ thống và có thể nghĩ nhiều hơn về công việc thật của mình.

Có lẽ đó mới là tiêu chuẩn tôi muốn mang sang những dự án sau này.

LA-P đã giúp tôi bắt đầu trả lời câu hỏi thứ nhất: **AI có thể làm được gì cho nghề của tôi?**

LA-Page buộc tôi phải học câu hỏi thứ hai: **làm thế nào để những gì AI làm được trở thành một phần tự nhiên, đáng tin và đủ giản dị trong công việc của con người?**'''

en = r'''On 5 August 2026, when I wrote the appendix on LA-P to close that version of LA-CONNECT, I tried to capture the system as clearly as I could at that point in time. LA-P already had skills, workflows, layers of instructions, data-processing tools, and a way of making sure that lessons learned from each correction did not simply disappear when a chat session ended. I had travelled far enough to believe that what I had built was no longer just a collection of isolated prompts and instructions.

A system can be extremely useful to the person who built it and still not yet be a real product for anyone else. I knew where the data lived, which instructions to call, which workflows had limits, when to look at the command line, when to go back through the change history, and where to start looking when an Agent behaved strangely. More of that knowledge still lived in my head than I wanted to admit. If a new user still needed me sitting beside them to explain installation, environment connections, where to find the right function, or how to handle a technical problem, then I had only moved my work into a more complicated system. I had not truly transferred it.

That was the concern that led me to start LA-Page.

## When LA-P Became LA-PAGE

From 22 August, LA-Page was defined as something quite specific: not a prettier interface placed in front of LA-P, and not a new copy of AppSheet. The goal was an independent web application for Loss Adjusting work, where a user could simply open a browser and move through a continuous working journey: sign in, create and manage a case, assign responsibility, conduct a field survey, request documents, read and organise evidence, prepare reports, use AI where appropriate, submit work for review and approval, preserve an audit trail, and continue working across desktop, tablet, or mobile.

Underneath, there could still be a database, Google Drive, dedicated processing programs, and selected capabilities from LA-P. But all of that needed to become progressively invisible to the practitioner.

I no longer wanted users to need to know what Git was, where the command line lived, what a skill was called, or how the data had once come from AppSheet. They only needed to know which loss case they were handling, where the case currently stood, what needed to happen next, which documents were still missing, what evidence mattered, and which decisions still had to remain the responsibility of a human being.

At the first product gate, three main user groups were defined: Loss Adjusters (LA), office support staff (Admin), and Senior/Manager-level users. The minimum viable product was also not defined as a demonstration with a large number of screens. It had to support a real working journey: sign-in, cases, assignment, documents, AI assistance, review and approval, auditability, and practical use across different devices. The next decisions then locked business scope, the case lifecycle, role-based permissions, and the data and storage architecture.

## From an Approved KHUNG to a Real Working Journey

The Product Blueprint gradually took shape around the main working areas: Dashboard, Case Management, Field Survey, Document Request, Documents, LA Report, Claim Summary, Timesheet, AI Workspace, Team, and Administration. One interface decision that I still believe was right was not to force the phone into becoming a miniature desktop. Mobile is better suited to capture, quick review, and communication; dense tables and heavier work belong on a larger screen.

Today is Sunday, 6 September. I asked my little AI colleague to prepare a summary report so I could temporarily record where this unfinished journey has reached — and so that I can come back and read it many times, allowing the lessons to sink in as I move further into my Developer journey. Most of what follows was written by AI. I have hardly edited it at all; I am leaving it more or less as it came out, in all its roughness (hihihi).

### 1. When the Builder Lost Its Way

I see **four major lessons**.

#### a. AppSheet gradually shifted from a migration source into a “legacy authority”

The original intention was correct:

> migrate data → LA-Page replaces AppSheet.

But during MIG-R1, historical incompleteness, legacy mappings, original references, and reconciliation state began to exert too much influence over the new operational design.

At one point, the logic was effectively becoming:

> historical data is null → do not allow the Case to be updated.

That reverses the purpose of the product.

The PO later corrected it to:

> a historically blank business field is valid and must be allowed to be completed.

And today the PO went one step further:

> AppSheet migration is complete → retire the entire legacy identity layer.

The Agent implemented schema `039_retire_appsheet_identity`, kept all 302/302 Cases, and removed `legacy_case_ref`, `original_case_ref`, legacy mappings, indexes, and triggers.

In my view, this is the **right architectural correction**.

#### b. The UI drifted away from the Approved KHUNG

Starting from a KHUNG that had already been accepted, feature development gradually produced: - horizontal feature tabs - nested sidebars - nested headers - workspace inside workspace.

It reached the point where the Master Plan had to open UI-R1 simply to reconcile the product back to the AppShell.

And today Vie found a smaller version of the same problem again:

> `Case operations / Create case, assignment and lifecycle`

was becoming a secondary shell underneath Case Summary.

The proposed **CASE-UX-R1 — Unified Case Summary & Operations** is really another correction of the same root cause:

**top-level capabilities belong in the sidebar; Case-specific actions belong inside the Case context.**

#### c. Infrastructure / Google governance went too far relative to product value at that point in time

The D1/OAuth work contained a great deal of: - preview - fingerprint - P1/P2/P3/P4 - exact authorisation - scheduling - remediation.

Those controls were not meaningless — security matters.

But looking back across the roadmap, there was a period when we spent too much effort on Google Cloud/OAuth while: - Claims Bordereau did not yet exist - Case Summary was still incomplete - Claim Summary had not been built - Dashboard was unfinished - Timesheet/Fee Note had not yet become complete operational modules.

This is the clearest example of a **correct engineering topic at the wrong time**.

#### d. Test harness/environment noise was sometimes mistaken for product failure

Old Python paths, LibreOffice paths, concurrency, and browser authentication sessions caused repeated troubleshooting loops.

Only later did we identify that the root cause was test-harness portability rather than the business feature itself.

The harness was then corrected through: - explicit environment configuration - PATH handling - bundled fallback - sequential LibreOffice tests.

Regression became stable again.

This was real technical debt, but it should have been classified correctly from the start:

> **environment failure ≠ product logic failure.**

### 2. So Where Are We Now?

There are two different layers of state that need to be separated.

### Canonical GitHub `main`

The canonical documentation I reviewed still says:

> **Priority 1 AppSheet operational migration accepted and closed; Priority 2 Claims Bordereau is next.**

The README says the same thing.

### Local/current work today

In the current session, the Agent has gone further but has **not yet committed/pushed**: - Claims Bordereau implementation - table field-selector expansion still being adjusted - column resizing still being fixed - dense spreadsheet-style Case Summary view - inline editing - PATCH partial-field correction - shared Case Summary ↔ Bordereau editability - AppSheet legacy-retirement schema `039` - proposed Case UX unification.

So the **current working product is already ahead of the canonical Git documentation**.

Until closure/commit/push, Git `main` does not yet fully reflect today's working state.

### 3. What Already Feels Quite Solid in LA-Page

At this point I consider the following foundations reasonably strong: - Approved KHUNG/AppShell - local authentication + 2FA - role/authorisation foundation - Case creation/register - assignment/status/lifecycle - tasks/deadlines foundation - Field Survey - BBHT generation - LA Report structured editor - local AI proposal workflow - submission/review/approval/issue - document ingestion/LACDM foundation - Document Request - local file/document register - backup/restore foundation - 302 operational Cases - current canonical CaseRef - audit architecture - regression harness.

In other words: **LA-Page is no longer an early prototype.**

But I still would not call it an MVP, because the remaining gaps sit directly inside the operational journey that Gate A was meant to support.

### 4. MVP GAP — What Is Still Missing Before We Can Call It an “MVP Candidate”

I would now reduce this to **eight groups**, rather than continuing to open dozens of smaller Gates.

|MVP area|Current situation|Remaining gap|
|---|---|---|
|**1. Case Management UX**|backend foundation is fairly complete|finish Case Summary, Case Detail, inline editing, remove nested Case Operations, professional desktop/mobile UX|
|**2. Claims Bordereau**|currently being built|column sizing/resizing, complete selectable fields, inline editing, CSV/report consistency, acceptance|
|**3. Claim Summary**|foundations/AI references exist but it is not yet a complete operational module|build a real Claim Summary workflow/table/calculation/review process|
|**4. Documents + Drive**|local foundation PASS, OAuth/sandbox groundwork exists|controlled production-like Drive lifecycle is not yet complete/open|
|**5. Dashboard / My Work**|architecture is defined|operational dashboard, workload, deadlines, next actions, management view|
|**6. Timesheet & Fee Note**|data/migration and some capabilities exist|complete user-facing Timesheet/Fee Note workflow is not yet closed|
|**7. Unified Approval / Notifications**|report approval already exists|cross-module Approval Inbox, deadlines/reminders/notification operationalisation|
|**8. One end-to-end AI-assisted real workflow + pilot readiness**|local AI/report components exist|connect Case → evidence → LA-P/AI → human review → output → audit as one real workflow, then limited pilot/monitoring/recovery|

Outside those eight groups, there is one separate security gap already called out in the Master Plan: **Sole Administrator Recovery** remains unresolved; UI-R1 did not close it.

### 5. If I Drew the Shortest Road from Today to MVP, I Would Not Return to the Old Roadmap Style

From here, I think we should avoid opening another round of “Gates inside Gates”.

The shortest sensible path is:

**finish Case UX → close Claims Bordereau → Claim Summary → controlled Documents/Drive → Dashboard/My Work → Timesheet & Fee Note → unified Approval/Notifications → one AI-assisted end-to-end workflow → monitoring/recovery → limited pilot rehearsal → PO MVP acceptance.**

That also fits the Product Vision better: a Loss Adjuster should be able to open a Case and immediately understand **where the case stands, what needs to happen next, which evidence matters, what they are authorised to do, and which output still requires review**.

## What Would I Do Differently If I Started Again?

The most reusable lesson from LA-Page is not really about Next.js, SQLite, Google Drive, or any OCR provider. It is about authority, context, and the size of the unit of work given to an AI Agent.

I would still keep a Master Plan. But before each increment I would want a very short Product Contract: what is the objective; what is in scope; what is out of scope; which Product Owner decisions are locked; what counts as acceptance; and when the Agent must stop.

The Builder does not need to carry hundreds of lines of project history in its head just to make one small change. Project memory and the context needed to perform a specific task are not the same thing. History should live somewhere durable; the person or Agent doing the work only needs enough information to avoid violating the current contract.

If the KHUNG has already been approved, I need to install a locking rule that forces the Agent to treat it as a mandatory structural invariant. A new feature may add states, forms, behaviour, and polish, but it must not quietly create another KHUNG of its own.

I would also order work around the question, “After this increment, what complete new task can the user actually perform?” rather than, “Which additional technical subsystem have we completed?” Each increment should create visible, usable progress and then stop at the right point: understand the request, build, preview, verify, PO acceptance, stop. No “while we are here”. No automatically opening five new work items simply because the Agent happened to notice them.

I still want the project to be evidence-first, but I do not want it to be governed by procedure for its own sake. Destructive schema changes, mutations against live Google Drive data, or clear professional conclusions deserve strong controls and human review. The spacing between two buttons does not need an architecture committee. The position of a button does not need an entire governance process. Something already accepted should not be automatically reopened unless there is a defect or a genuine product reason.

Safety control and bureaucratic control are not the same thing.

And this is where the idea of organising several Agents by role began to make sense to me. Not because four Agents are automatically more intelligent than one, but because each Agent can be given less authority and less context.

The Product Owner remains the decision-maker. One Agent keeps the Product Contract, understands the history, and locks the scope. One Builder Agent implements only the work that has been assigned. One Verifier Agent checks the result without quietly changing the code. One Risk Auditor appears only when a sufficiently serious trigger justifies another layer of review. Then everything returns to the Product Owner for acceptance.

The value is not in having “more Agents”.

The value is in **separating authority**.

If I had to reduce the post-LA-Page project model to a few durable documents, I would keep only what is really needed: one document defining product direction, one Product Blueprint, one Master Plan, one file containing mandatory invariants, one current-state Session Handoff, and one Contract for each increment. The working loop should be equally small: understand intent, lock scope, build, preview, verify, accept, record the state, then move to the next step.

There should be no indefinite “continue improving”.

And no automatic scope expansion simply because AI sees another opportunity to make the system more complicated.

## What Has LA-Page Produced Beyond LA-Page Itself?

The appendix I wrote on 5 August ended with the observation that LA-P had taken shape, had already created value, still made mistakes, and was still being built. A month later, LA-Page made the unresolved part of that sentence much more concrete.

The problem was no longer simply how to help an Agent remember the right skill or follow the right workflow. The problem was how to turn all of those capabilities into a product that another person could use without first having to learn how to become me.

LA-Page has not finished answering that question. The project itself is still on the road to a minimum viable product. But it has already produced something that may live longer than many individual features: a clearer way of building products with AI Agents.

**small contract → limited authority → visible product increment → evidence → Product Owner acceptance → stop.**

I started LA-Page because I wanted LA-P to move beyond the environment of the person who built it. In the process, I realised that I also had to move beyond one of my own habits: the belief that more capabilities, more control layers, more gates, and more things built must mean that the product is getting closer to completion.

Not necessarily.

A product moves closer to its users not when its architecture diagram becomes longer, but when users have to think less about the system and can think more about the real work they are there to do.

Perhaps that is the standard I want to carry into the projects that come next.

LA-P helped me begin answering the first question: **what can AI do for my profession?**

LA-Page is forcing me to learn the second: **how do we make what AI can do become a natural, trustworthy, and simple enough part of human work?**'''

html = BOOK.read_text(encoding='utf-8')
assert 'href="#phu-luc-la-page"' not in html, 'PL2 already present in TOC'
assert '"slug": "phu-luc-la-page"' not in html and '"slug":"phu-luc-la-page"' not in html, 'PL2 already present in data'

obj = {'slug':'phu-luc-la-page','number':'PL2','vi':{'part':'Phụ lục 2','label':'Phụ lục 2','title':'Từ LA-P đến LA-Page','markdown':vi},'en':{'part':'Appendix 2','label':'Appendix 2','title':'From LA-P to LA-Page','markdown':en}}
m = re.search(r'(<script id="chapter-data" type="application/json">)(.*?)(</script>)', html, flags=re.S)
assert m, 'chapter-data block not found'
raw = m.group(2)
parsed = json.loads(raw)
assert parsed[-1]['slug'] == 'phu-luc-lap', 'Unexpected final chapter; refusing to patch'
raw2 = raw.rstrip()
assert raw2.endswith(']')
raw2 = raw2[:-1] + ', ' + json.dumps(obj, ensure_ascii=False) + ']'
html = html[:m.start(2)] + raw2 + html[m.end(2):]
old_toc = '<div class="toc-group"><p class="toc-group-title">Phụ lục</p><a class="toc-link" href="#phu-luc-lap"><span class="toc-no">PL</span><span class="toc-title">LA-P ở thời điểm cuốn sách khép lại</span></a></div>'
new_toc = '<div class="toc-group"><p class="toc-group-title">Phụ lục</p><a class="toc-link" href="#phu-luc-lap"><span class="toc-no">PL</span><span class="toc-title">LA-P ở thời điểm cuốn sách khép lại</span></a><a class="toc-link" href="#phu-luc-la-page"><span class="toc-no">PL2</span><span class="toc-title">Từ LA-P đến LA-Page</span></a></div>'
assert html.count(old_toc) == 1
html = html.replace(old_toc, new_toc, 1)
for old,new in {
'Bản song ngữ · 12 chương + Phụ lục':'Bản song ngữ · 12 chương + 2 Phụ lục',
'2026.08.24-production-v6.1-editorial-ch01-10':'2026.09.06-production-v6.2-editorial',
'Bản song ngữ hoàn chỉnh · v6.1':'Bản song ngữ hoàn chỉnh · v6.2',
'v6.1 · Final · VI/EN':'v6.2 · Final · VI/EN'}.items():
    assert old in html, old
    html = html.replace(old,new)
m2 = re.search(r'<script id="chapter-data" type="application/json">(.*?)</script>', html, flags=re.S)
chapters = json.loads(m2.group(1))
assert chapters[-1]['slug']=='phu-luc-la-page'
assert html.count('href="#phu-luc-la-page"')==1
assert 'Bản song ngữ hoàn chỉnh · v6.2' in html
BOOK.write_text(html, encoding='utf-8')

catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
entry = next(x for x in catalog if x.get('id')=='la-connect')
assert entry['version']=='6.1'
entry['version']='6.2'; entry['updated']='2026-09-06'
entry['description']='Ấn bản song ngữ v6.2 của LA-CONNECT; bổ sung Phụ lục 2 — Từ LA-P đến LA-Page, ghi lại bước chuyển từ LA-P sang một ứng dụng web độc lập và những bài học Developer rút ra từ hành trình xây dựng cùng AI Agent.'
CATALOG.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('LA-CONNECT v6.2 patch prepared and validated.')

# 卒業計画: Exam Rank 06 + ft_transcendence（10/8〜10/20）

## 目標

**10/20 までに卒業する。** 残りは次の2つ。

1. **Exam Rank 06 に合格する。** **最目標は 10/13（受験①）**、第2目標は 10/20（受験②）、最後の保険は 10/24（受験③）。10/13 は合格を狙いつつ、落ちた場合に備えて出題の情報を必ず持ち帰る。
2. **ft_transcendence の評価を通す。** コードは完成済み。自分（amakino）が説明できるようにする。
   担当は **AI 対戦相手 + LLM（4点）**。教材は `ft_transcendence/Explanation/amakino_memo/`（説明文）と `ft_transcendence/roles/amakino.md`（担当コードの読む順番）。

### トラ戦の教材（3種類。使い分ける）

| 教材 | 使い方 |
|---|---|
| **章立ての説明文** `explanation/01〜13` | 「なぜそうなっているか」を順番に理解する。02・04〜07・09〜11 章のコード引用には `> 📍 ファイル:行` が付いているので、右側でそのファイルを開いて行に飛ぶ（`Ctrl+G`） |
| **ファイル別の1行ずつ解説** `files/`（目次 `FILES.md`） | 「この行は何？」を全行で確認する。1ファイル＝1つの md。**左に解説、右にソース**で読む |
| **読む順番の目次** `READING_ORDER.md` | どのファイルから読むか。読んだら ☐ を ☑ に。**全54ファイル（5,290行）を読み切ったかの記録**になる |

| 日付 | 予定 |
|---|---|
| 10/13（火）15:00 | Exam 受験① ← **最目標。ここで合格する** |
| 10/20（火）15:00 | Exam 受験② ← 第2目標（卒業期限の当日） |
| 10/24（土）11:00 / 15:00 | Exam 受験③ ← 最後の保険（卒業期限には間に合わない） |
| **未定** | **トラ戦の評価。日程が決まったら、この表に書く。** 評価の前日は「評価前日」メニュー（下）に差し替える |

## 方針

1. **目標は3段構え。最目標は 10/13（受験①）で合格すること。** 落ちたら 10/20（受験②）、それでも落ちたら 10/24（受験③。最後の保険）。受験の度に「出た問題」を `exam06/question/` に詳細に書き出し、次の受験の対策に使う。
2. **10/9〜10/12 の4日間は、全力で 10/13 に合わせる。** 予想問題の day1〜day4（グラフ・区間・バックトラッキング・DP）と、過去問（exam3〜5）の通しだけをやる。`leetcode/` の追加や、新しい型への寄り道はしない。
3. **1日の配分は Exam 約3時間 + トラ戦 約2時間。** 順番は「Exam のウォームアップ → 予想問題（最低ライン）→ トラ戦 → 余裕があれば追加」。追加は1問15〜20分を目安に、詰まったら答えを読んで次へ進む（`[NG]` に記録して翌日に解き直す）。
4. **トラ戦は 10/9 スタート（10/8 は進まなかったので、チェックを全部外してやり直す）。説明文は、10/16 までに担当範囲（1〜8章 + 12章）を読み終える。** 読む順番は「Web 基礎 → JS → ゲームのルール → `rooms.js` の担当部分 → AI の章（本命）」。10/13 は休み。10/13 に合格したら、10/14〜10/16 の Exam の時間を全部トラ戦に回し、12章を前倒しする。 10/17 以降は手を動かす練習（実演・その場修正・想定問答）だけにする。評価が 10/17 より前に決まったら、12章と `roles/amakino.md` を前倒しする。
5. **合格したら、その時点で Exam は終了する。** 10/13 で合格 → 10/14 以降の Exam は毎日30分の復習だけ（または何もしない）。10/20 で合格 → 10/21 以降は Exam なし。浮いた時間は全部トラ戦に回す。
6. 本番と同じ制約で解く: `sorted()` / `.sort()` / `set()` / `heapq` / `Counter` / `deque` は使わない（予想問題の各 `.py` に書いてある）。
7. 時間が足りない日は **「最低ライン」とトラ戦だけは必ず終わらせる。** 10/12・10/19・10/23（受験前日）と、受験当日は追加をやらない（早く寝る方が大事）。
8. **Exam のメインは `~/42cadet/42_python_exam/exam06/` の予想問題（day1〜day16、全47問）。** 過去問（`exam3` / `exam4` / `exam5` の `pra/`）は本番の出題形式そのものなので、10/12 と 10/19 に通しで解く。`leetcode/` の155問は、その日の予想問題が終わってからの「追加」に格下げする。
9. 10/6・10/7 の分で終わっていない問題は、10/18 の「弱点つぶし」に回す。

### Exam 予想問題（exam06）と日付の対応

dayN は **10/(8+N)** の日の問題に対応している（day1 = 10/9 … day16 = 10/24）。受験日（day5 = 10/13、day12 = 10/20、day16 = 10/24）はウォームアップ 1 問だけ。

| day | 日付 | テーマ | 問題 |
|---|---|---|---|
| day1 | 10/9（金） | グラフ / グリッド | signal_spread, task_order, network_delay |
| day2 | 10/10（土） | 区間 / ウィンドウ / 自作ソート | room_planner, shortest_cover, merge_ranges |
| day3 | 10/11（日） | バックトラッキング | queens_count, word_hunt, bracket_builder |
| day4 | 10/12（月） | DP ① | text_distance, coin_min, word_split |
| day5 | **10/13（火）受験①** | ウォームアップ | group_anagrams |
| day6 | 10/14（水） | 過去問の穴（暗黙グラフ BFS / スタック / Union-Find） | lock_opener, cool_days, redundant_link, hist_area |
| day7 | 10/15（木） | クラス設計 | prefix_dictionary, cache_keeper, pack_strings |
| day8 | 10/16（金） | DP ② | equal_split, coin_ways, decode_ways, paths_with_walls |
| day9 | 10/17（土） | ヒープ自作 / 頻度 | top_k_frequent, k_closest, min_heap, median_tracker |
| day10 | 10/18（日） | 木 | tree_levels, valid_search_tree, best_path_sum |
| day11 | 10/19（月） | Hard の模擬 | word_grid_search, alien_order, cheapest_flight |
| day12 | **10/20（火）受験②** | ウォームアップ | spiral_fill |
| day13 | 10/21（水） | 文字列 / 配列 | find_all_anagrams, rotate_square, longest_palindrome_sub, multiply_strings |
| day14 | 10/22（木） | グラフの総復習 | min_wire, swim_time, itinerary |
| day15 | 10/23（金） | 貪欲 / DP の総復習 | can_reach, min_jumps, gas_loop, longest_climb |
| day16 | **10/24（土）受験③** | ウォームアップ | longest_unique_run |

進め方: `dayN/*.txt` を読む → `*.py` に実装 → `python3 dayN/<file>.py` で全部 `[OK]` → 詰まったら 30分で打ち切って `[NG]` に記録（翌日、何も見ずに解き直す）。

## 毎日の進め方

**Exam（約3時間）**
1. ウォームアップ（20分）: B 群を制限時間つきで、何も見ずに。
2. メイン（2時間）: その日の `exam06/dayN/` の問題を自力で書き、`python3 exam06/dayN/<file>.py` で全ケース `[OK]` を確認する。目安: Hard 40分、Medium 25分。余裕があれば `leetcode/pra/` の追加分へ。
3. 見直し（30分）: 30分考えても解けなかった問題は、答えを写して理解し、翌日に何も見ずに解き直す。

**トラ戦（約2時間）**
1. 説明文の章を読む。**読むときは必ず VS Code で実際のファイルを開き、出てきた関数を Ctrl+F で探して見比べる。**
2. 読み終えたら、その章の要点を **何も見ずに3行で** 末尾の進捗メモに書く（書けなければ理解できていない）。
3. 分からない行は **`files/` の該当ファイルの解説**（`FILES.md` から探す）か `99-line-by-line.md`、分からない単語は `13-glossary.md` で引く。
4. 読み終えたファイルは `READING_ORDER.md` の ☐ を ☑ にする。

---

## Phase 1: 10/8〜10/13 — 受験①まで（Exam: 予想問題 day1〜4 / トラ戦: 10/9 スタートで土台を読む）

### 10/8（木）
- **Exam** — グラフ（lc417 の続き）
  - [ ] **lc417_pacific_atlantic_water_flow**（取り組み中。解けなくても 30 分で打ち切って答えを読む）
  - 残りは **10/9 の `exam06/day1`** に統合する（lc743 = day1 の network_delay、lc994 = day1 の signal_spread）。
- **トラ戦** — **やり直し: 10/8 は予定どおり進まなかったので、10/9 からスタートし直す**（10/8 のチェックは全て外し、内容は 10/9 以降に組み直した）

### 10/9（金）
- **Exam** — グラフ（グリッドと最短経路）
  - ウォームアップ(20分): lc189, lc796（B 群）
  - **予想問題 `exam06/day1/`**（メイン。全問が最低ライン）:
    - [ ] py_signal_spread（lc994 系。グリッド BFS）
    - [ ] py_task_order（トポロジカルソート。exam4 L3 / exam5 L2 の型）
    - [ ] py_network_delay（lc743 系。`heapq` なし）
  - 最低ライン: day1 の3問
  - 余裕があれば: lc286_walls_and_gates, lc200_number_of_islands, lc207_course_schedule
- **トラ戦** — 全体像と Web の基礎（**ここがスタート**）
  - [ ] `EXPLAINATION.md`（読む順番と約束）
  - [ ] 01-big-picture（30分）
  - [ ] 02-web-basics の 1〜6節（90分）。HTTP / Cookie / JWT / WebSocket を自分の言葉で言えるように。**2節の「ログイン1回をコードで追う」表を、右側のコードと見比べる**（`POST` は関数名ではなくラベル、走るのは `app.post(...)` に渡した関数）
  - [ ] `READING_ORDER.md` の **第1段階** のうち `files/server/src/index.js.md` → `auth.js.md`（残り: `validate.js.md` / `db.js.md` / `schema.prisma.md` / `api.js.md` / `Auth.jsx.md` は 10/10 以降に余裕があれば）
  - 最低ライン: 01 と 02 の 1〜6節、`index.js.md` と `auth.js.md`

### 10/10（土）
- **Exam** — 区間・ソート自作・スライディングウィンドウ
  - ウォームアップ(20分): lc023, lc239（exam4 の元ネタ）
  - **予想問題 `exam06/day2/`**（メイン。全問が最低ライン）:
    - [ ] py_room_planner（= lc253。exam5 L2 の型）
    - [ ] py_shortest_cover（= lc076）
    - [ ] py_merge_ranges（= lc056。`sorted` 禁止なので自作ソート）
  - 最低ライン: ソートの自作（バブル／マージ）を何も見ずに書く + day2 の3問
  - 余裕があれば: lc057_insert_interval, lc435_non_overlapping_intervals, lc003_longest_substring_without_repeating
- **トラ戦** — JavaScript（一番大事な章）
  - [ ] 03-javascript-basics（120分）。**13節「非同期 async / await」は2回読む**
  - [ ] 読み残した第1段階のファイル解説（`auth.js.md` の L90-L125 を、`async` / `await` を意識してもう一度）
  - 最低ライン: 03 の 5〜10節と 13節

### 10/11（日）
- **Exam** — バックトラッキング（本命）
  - ウォームアップ(20分): lc132, lc131（exam4 の元ネタ）
  - **予想問題 `exam06/day3/`**（メイン。全問が最低ライン）:
    - [ ] py_queens_count（= lc051）
    - [ ] py_word_hunt（= lc079。exam5 L3 の型）
    - [ ] py_bracket_builder（= lc022）
  - 最低ライン: day3 の3問
  - 余裕があれば: lc212_word_search_ii（Trie が必要。先に `day7/py_prefix_dictionary` をやってもよい）, lc046_permutations, lc078_subsets
- **トラ戦** — ゲームのルール
  - [ ] 05-game-rules（90分）。状態遷移図と `endPhase` を丁寧に
  - [ ] 04-server-foundation（ざっと30分。自分の担当外なので「何がどこにあるか」だけ）
  - [ ] `READING_ORDER.md` の **第2段階**: `files/server/src/roles.js.md`、`game.js.md`（`endPhase`・`settle`・`resolveNight`・`resolveVote`・`checkWinner` の行を右のコードと見比べる）
  - 最低ライン: 05

### 10/12（月）— 受験①の前日
- **Exam** — DP ① + 過去問の通し（受験①の前日。**新しい型には手を出さない**）
  - ウォームアップ(20分): exam3 の level1〜2 から3問
  - **予想問題 `exam06/day4/`**（全問が最低ライン）:
    - [ ] py_text_distance（= lc072）
    - [ ] py_coin_min（= lc322）
    - [ ] py_word_split（= lc139。最後のテストは素朴な再帰だと遅い → メモ化か DP）
  - **過去問の通し**（本番と同じ時間配分で、何も見ずに）:
    - [ ] `exam5/pra` の level2〜3 から1問ずつ
    - [ ] `exam4/pra` の level2〜3 から1問（palindrome_partitioner か sliding_window_maximium）
    - [ ] `[NG]` だった問題の解き直し
  - 追加はやらない。早めに寝る。
- **トラ戦**（1時間だけ）— リアルタイム通信（`rooms.js`）の担当に近い所だけ
  - [ ] 06-realtime-rooms の 1〜4節と 10節（**3節 `botView` と 10節 `hooks` は自分の担当と直結するので丁寧に**）
  - [ ] `files/server/src/rooms.js.md` の **L1-L182**（`publicState` / `privateState` / `botView`）と **L367-L463**（`hooks`）
  - 最低ライン: 06 の 3節と 10節
- 早めに寝る。

### 10/13（火）— 受験①（15:00）
- [ ] 午前: ウォームアップ（20分）。**`exam06/day5/py_group_anagrams`** を何も見ずに。あとは新しい問題をやらず、`exam5/pra` の level3 を眺めて頭を温める程度にする
- [ ] 試験（**最目標: ここで合格する**）
- [ ] **試験直後に、出た問題を可能な限り詳細に `exam06/question/` に書き出す**（制約、入出力例、レベル、詰まった箇所）
- トラ戦: なし（休む）

---

## Phase 2: 10/14〜10/19 — 受験②まで（Exam: 本番の出題を踏まえた補強 / トラ戦: 担当を仕上げて実演練習）

受験①で合格していたら、Exam は毎日30分の復習だけにし、浮いた時間を全部トラ戦に回す。

### 10/14（水）— 受験①の振り返り
- **Exam** — 受験①の振り返り + 過去問の穴埋め
  - **受験①の問題を何も見ずに解き直す**（最優先。`exam06/question/` に書き出したもの）
  - 落ちた原因を分類する（アルゴリズム不足／実装ミス／時間切れ／禁止 built-in の回避）
  - **予想問題 `exam06/day6/`**（過去問に出ていた型の穴埋め）:
    - [ ] py_lock_opener（暗黙グラフの BFS。exam5 の word_ladder の型）
    - [ ] py_cool_days（スタック。exam4 の sliding window maximum に近い）
    - [ ] py_redundant_link（Union-Find）
    - [ ] py_hist_area（スタック。Hard）
  - 最低ライン: 受験①の解き直し + day6 の lock_opener, cool_days
  - 受験①で合格していたら、Exam はここで終了。以降は毎日30分の復習だけにして、全時間をトラ戦に回す。
- **トラ戦** — AI の章（担当・1回目 前半）
  - [ ] 07-ai-bots-and-llm の 0〜2節（`bots.js` の判断）
  - [ ] `files/server/src/bots.js.md` を通して読む（157行）。`view` の表と、`voteTarget` の優先順位（L86-L117）を自分の言葉で言えるように
  - [ ] 06-realtime-rooms の残り（5〜9節。時間があれば）
  - 最低ライン: 07 の 0〜2節 + `bots.js.md`

### 10/15（木）
- **Exam** — クラス設計（Trie・LRU・直列化）
  - ウォームアップ(20分): lc020, lc021
  - **予想問題 `exam06/day7/`**（メイン。全問が最低ライン）:
    - [ ] py_prefix_dictionary（Trie）
    - [ ] py_cache_keeper（LRU キャッシュ。`OrderedDict` 禁止）
    - [ ] py_pack_strings（lc271 系。exam5 L1 の compress_decompress に近い）
  - 最低ライン: day7 の3問
- **トラ戦** — AI の章（担当・1回目 後半）
  - [ ] 07-ai-bots-and-llm の 3〜8節（`lines.js`、Bot が話す、`llm.js`、テスト）
  - [ ] ファイル別解説: `files/server/src/lines.js.md`（209行。正規表現は「何に当たるか」の日本語説明を読む）、`llm.js.md`（100行）、`rooms.js.md` の **L227-L365**（`botPrompt` / `botSpeak` / `say` / `drainSpeech` / `reactToClaim` / `botReply`）
  - 最低ライン: 07 を最後まで1回読み切る

### 10/16（金）
- **Exam** — DP ②
  - ウォームアップ(20分): lc349, lc242, lc392
  - **予想問題 `exam06/day8/`**（メイン。全問が最低ライン）:
    - [ ] py_equal_split（lc416）
    - [ ] py_coin_ways（lc518）
    - [ ] py_decode_ways（lc091）
    - [ ] py_paths_with_walls（lc063）
  - 最低ライン: day8 の4問
  - 余裕があれば: lc1143_longest_common_subsequence, lc300_longest_increasing_subsequence
- **トラ戦** — 担当コードを実物で読む + 全体をつなげる（**ここで説明文を読むのは終わり**）
  - [ ] `roles/amakino.md` の表の #1〜#15 を、実際のファイルを開いて読む（`botView`、`bots.js` 全体、`hooks.phase`、`lines.js`、`botPrompt` / `botSpeak`、`llm.js` の `takeSlot` / `readSse` / 15秒打ち切り、テスト）
  - [ ] `MISTAKE`、`caughtLying`、`botClaim`、`botDelay` を何も見ずに説明できるか確認。説明できなかった行は `files/server/src/bots.js.md` で確認
  - [ ] 08-trace-one-game（60分）。1ゲームの流れの中で、Bot と Gemini がどこで呼ばれるかを確認（各場面の末尾の「📍 コードの場所」の表を使う）
  - [ ] `files/server/src/logic.test.js.md` の Bot 関係のテスト（L209-L244、L289-L353）を読む
  - `READING_ORDER.md` の☑が、担当範囲（`bots.js`、`lines.js`、`llm.js`、`rooms.js`、`game.js`、`logic.test.js`）で全部ついているか確認する
  - 最低ライン: `roles/amakino.md` の #1〜#15 と 08章

### 10/17（土）
- **Exam** — ヒープ（`heapq` 禁止）と設計
  - ウォームアップ(20分): lc189, lc796, lc125
  - **予想問題 `exam06/day9/`**（メイン。全問が最低ライン）:
    - [ ] py_top_k_frequent（lc347）
    - [ ] py_k_closest（lc973）
    - [ ] py_min_heap（ヒープ自作。push / pop は O(log n)）
    - [ ] py_median_tracker（lc295。min_heap を使う）
  - 最低ライン: day9 の4問
- **トラ戦** — 評価対策（手を動かす）
  - [ ] 12-evaluation-prep を読む（4節の各問に「📍 今のコードの場所」が付いた。**探す練習は、これを見る前に**）
  - [ ] 余裕があれば `READING_ORDER.md` の第9・第10段階（`Dockerfile.md`、`docker-compose.yml.md`、`Makefile.md`、`e2e/app.test.js.md`）。評価者は起動方法やテストも聞く
  - [ ] `make` で起動し、`docs/ASSIGNMENTS.md` の「評価での実演」（Bot と遊ぶ → Bot に話しかける → 返事が少しずつ流れる → キーを外すと定型文に戻る）を1回通す
  - [ ] 12章 4節「その場で直す練習問題」の amakino の問題を、**答えを見ずに** 実際に直す → `cd server && npm test` → `git checkout -- ファイル名` で戻す

### 10/18（日）— 弱点つぶし
- **Exam** — 木（弱点つぶしの日）
  - ウォームアップ(20分): lc239, lc132, lc131
  - **予想問題 `exam06/day10/`**（メイン。全問が最低ライン）:
    - [ ] py_tree_levels（lc102）
    - [ ] py_valid_search_tree（lc098）
    - [ ] py_best_path_sum（lc124。Hard）
  - 最低ライン: day10 の3問 + 10/9〜10/17 の `[NG]` と、終わっていない問題の解き直し
  - 過去問（exam3〜5）に木は一度も出ていないので、day10 は優先度が低い。時間が足りなければ `[NG]` の解き直しを優先する。
- **トラ戦** — 想定問答と模擬評価
  - [ ] 07章末「amakino の想定問答」と 12章 3節を、**声に出して** 何も見ずに答える。詰まった問いだけ読み直す
  - [ ] 12章 4節の他の人の練習問題も2〜3問やる（評価者は担当外も聞いてくる）
  - [ ] できればチームの誰かに評価者役をしてもらい、10分の模擬評価

### 10/19（月）— 受験②の前日
- **Exam** — 受験②の前日: 総仕上げ（**新しい型には手を出さない**）
  - **予想問題 `exam06/day11/`**（Hard の模擬。時間を計る）:
    - [ ] py_word_grid_search（lc212。Trie）
    - [ ] py_alien_order（lc269。トポロジカルソート）
    - [ ] py_cheapest_flight（lc787）
  - [ ] 受験①の問題と、過去試験の level3（exam4 の package_dependency_resolver、exam5 の prism_detector / word_ladder）を、時間を計って通しで解く
  - [ ] `[NG]` が出た問題を解き直す
  - 最低ライン: 受験①の問題 + 過去試験 level3 の通し。day11 は余力で。
- **トラ戦**（30分だけ）
  - [ ] 想定問答で詰まった問いだけ確認
- 早めに寝る。

### 10/20（火）— 受験②（15:00）
- [ ] 午前: ウォームアップ（20分）。**`exam06/day12/py_spiral_fill`** + 受験①で苦戦した問題を1問だけ解き直す
- [ ] 試験（**第2目標: 10/13 で落ちていたら、ここで合格する**）
- [ ] 試験直後に、出た問題を `exam06/question/` に追記する

---

## トラ戦の評価前日メニュー（評価日が決まったら、その前日に差し替える）

Exam は最低ライン（ウォームアップ + 1問）だけにして、残りの時間を全部これに使う。

- [ ] `make` で起動 → 自分の実演を1回通す（Chrome の DevTools を開いて、Console にエラーが出ないこと）
- [ ] その場修正の練習問題を1問、答えを見ずに直す
- [ ] 想定問答を声に出して一周
- [ ] `docs/ASSIGNMENTS.md` の「評価前に必須」のチェックが全部ついているか確認（未コミットの変更が残っていないか）

---

## Phase 3: 10/21〜10/24 — 予備（受験②で落ちた場合の最後の保険）

卒業期限（10/20）には間に合わないが、**10/24（土）は最後のチャンス**。受験②で合格していたら、この Phase の Exam は不要（トラ戦に全時間を回す）。

- **10/21（水）**: 受験②の問題を何も見ずに解き直し、落ちた原因を分類する。そのあと `exam06/day13`（py_find_all_anagrams, py_rotate_square, py_longest_palindrome_sub, py_multiply_strings）。受験②で合格していたら Exam は終了。
- **10/22（木）**: `exam06/day14`（py_min_wire, py_swim_time, py_itinerary）。受験①②の問題で落としたものを必ず1問入れる。
- **10/23（金）**: `exam06/day15` の前半（py_can_reach, py_min_jumps）+ `[NG]` の解き直し。新しい型には手を出さず、早めに寝る。
- **10/24（土）**: 11:00 と 15:00 の2回（受験③）。
  - [ ] 朝: ウォームアップ（20分）。**`exam06/day16/py_longest_unique_run`**
  - [ ] 11:00 の試験（**最終目標: 遅くともここで合格**）。落ちた場合は、間の時間で出た問題を書き出して見直す
  - [ ] 15:00 の試験

---

## LeetCode 対象一覧（優先度別）

### A: 必ず解く（上の日次計画に書いた問題）
太字は難しい問題で、本命・有力として優先する。

### B: 過去試験の元ネタ（level1〜2 の再出題対策）
毎日のウォームアップで消化する。

- [ ] lc349_intersection_of_two_arrays（Exam 3 inter / Exam 4 list_intersection_finder）
- [ ] lc242_valid_anagram（Exam 3 anagram / string_permutation_checker）
- [ ] lc392_is_subsequence（Exam 3 hidenp）
- [ ] lc125_valid_palindrome（Exam 3 echo_validator）
- [ ] lc189_rotate_array（Exam 3 twist_sequence）
- [ ] lc796_rotate_string（Exam 4 array_rotation_detector）
- [ ] lc020_valid_parentheses（Exam 3 bracket_validator）
- [ ] lc021_merge_two_sorted_lists（Exam 3 shadow_merge）
- [ ] lc023_merge_k_sorted_lists（Exam 4 merge_sorted_list）
- [ ] lc239_sliding_window_maximum（Exam 4 sliding_window_maximium）
- [ ] lc132_palindrome_partitioning_ii（Exam 4 palindrome_partitioner）
- [ ] lc131_palindrome_partitioning（上の前段）

### C〜E: 全問制覇の追加分（113問）
元の計画で「時間が余ったら」「後回し」にしていた問題も含めて、残り全部を 10/8〜10/18 の各日の「追加」に、その日のテーマに合わせて割り振った。これで `leetcode/` の155問が全部、日次計画のどこかに入っている。

---

## 進捗メモ

### Exam

| 日付 | 完了した問題 | `[NG]` だった問題 | 気づき |
|---|---|---|---|
| | | | |

### トラ戦：ファイル別解説の進み具合

`READING_ORDER.md` の ☑ の数を書く（全54ファイル）。

| 日付 | ☑の数 | 今日読んだファイル | 詰まった行 |
|---|---|---|---|
| | | | |

### トラ戦（読んだ章の要点を、何も見ずに3行で）

| 日付 | 章 | 要点（3行） | 分からなかったこと |
|---|---|---|---|
| | | | |

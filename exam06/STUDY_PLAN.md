# 卒業計画: Exam Rank 06 + ft_transcendence（10/8〜10/20）

## 目標

**10/20 までに卒業する。** 残りは次の2つ。

1. **Exam Rank 06 に合格する。** 本命は 10/20、10/13 は受験①（合格も狙うが、出題の情報を集める回でもある）。
2. **ft_transcendence の評価を通す。** コードは完成済み。自分（amakino）が説明できるようにする。
   担当は **AI 対戦相手 + LLM（4点）**。教材は `ft_transcendence/Explanation/amakino_memo/`（説明文）と `ft_transcendence/roles/amakino.md`（担当コードの読む順番）。

| 日付 | 予定 |
|---|---|
| 10/13（火）15:00 | Exam 受験① |
| 10/20（火）15:00 | Exam 受験② ← ここで合格が目標 |
| 10/24（土）11:00 / 15:00 | Exam 予備（卒業期限には間に合わない。最後の保険） |
| **未定** | **トラ戦の評価。日程が決まったら、この表に書く。** 評価の前日は「評価前日」メニュー（下）に差し替える |

## 方針

1. **1日の配分は Exam 3時間 + トラ戦 2時間 + 追加問題 2〜3時間。** `leetcode/` の155問を 10/18 までに全部解く。順番は「Exam の最低ライン → トラ戦 → 追加」。追加は1問15〜20分を目安に、詰まったら答えを読んで次へ進む（解き直しは `[NG]` に書いて 10/18 以降へ）。
2. **トラ戦の説明文は、10/16 までに担当範囲（1〜8章 + 12章）を読み終える。** 10/17 以降は手を動かす練習（実演・その場修正・想定問答）だけにする。評価が 10/17 より前に決まったら、12章と `roles/amakino.md` を前倒しする。
3. **Exam は難しい問題を優先、ただし level1〜2 は落とさない。** 毎日最初の20分は B 群（過去試験の元ネタ）を何も見ずに解く。
4. 本番と同じ制約で解く: `sorted()` / `.sort()` / `set()` / `heapq` / `Counter` / `deque` は使わない。
5. 時間が足りない日は **「最低ライン」とトラ戦だけは必ず終わらせる。** 追加が残ったら翌日以降に持ち越す。10/12・10/19（受験前日）と 10/13 は追加をやらない（早く寝る方が大事）。
6. 10/6・10/7 の分で終わっていない問題は、10/18 の「弱点つぶし」に回す（今日から先の予定を崩さない）。

## 毎日の進め方

**Exam（約3時間）**
1. ウォームアップ（20分）: B 群を制限時間つきで、何も見ずに。
2. メイン（2時間）: `leetcode/pra/` に自力で書き、`python3 leetcode/pra/<file>.py` で全ケース `[OK]` を確認 → `leetcode/ans/` と見比べる。目安: Hard 40分、Medium 25分。
3. 見直し（30分）: 30分考えても解けなかった問題は、答えを写して理解し、翌日に何も見ずに解き直す。

**トラ戦（約2時間）**
1. 説明文の章を読む。**読むときは必ず VS Code で実際のファイルを開き、出てきた関数を Ctrl+F で探して見比べる。**
2. 読み終えたら、その章の要点を **何も見ずに3行で** 末尾の進捗メモに書く（書けなければ理解できていない）。
3. 分からない行は `99-line-by-line.md`、分からない単語は `13-glossary.md` で引く。

---

## Phase 1: 10/8〜10/13 — 受験①まで（Exam: 探索系の強化 / トラ戦: 土台を読む）

### 10/8（木）
- **Exam** — グラフ（グリッドと最短経路）
  - ウォームアップ: lc189, lc796
  - [ ] **lc417_pacific_atlantic_water_flow**
  - [ ] **lc743_network_delay_time**（`heapq` なし。配列を線形に走査する方式）
  - [ ] lc286_walls_and_gates
  - 最低ライン: lc417, lc743
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc130_surrounded_regions
    - [ ] lc994_rotting_oranges
    - [ ] lc133_clone_graph
    - [ ] lc207_course_schedule
    - [ ] lc261_graph_valid_tree
    - [ ] lc323_number_of_connected_components
    - [ ] lc200_number_of_islands
    - [ ] lc695_max_area_of_island
    - [ ] lc1584_min_cost_to_connect_all_points
    - [ ] lc787_cheapest_flights_within_k_stops
    - [ ] lc778_swim_in_rising_water
    - [ ] lc329_longest_increasing_path_in_a_matrix
    - [ ] lc332_reconstruct_itinerary
- **トラ戦** — 全体像と Web の基礎
  - [ ] `EXPLAINATION.md`（読む順番と約束）
  - [ ] 01-big-picture（30分）
  - [ ] 02-web-basics（90分）。HTTP / Cookie / JWT / WebSocket を自分の言葉で言えるように
  - 最低ライン: 01 と 02 の 1〜6節

### 10/9（金）
- **Exam** — 区間・ソート自作・スライディングウィンドウ
  - ウォームアップ: lc023, lc239（Exam 4 の元ネタ）
  - [ ] ソートの自作（バブル／マージ）を何も見ずに書く
  - [ ] lc253_meeting_rooms_ii
  - [ ] **lc076_minimum_window_substring**
  - [ ] lc056_merge_intervals
  - 最低ライン: ソート自作、lc253, lc076
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc057_insert_interval
    - [ ] lc435_non_overlapping_intervals
    - [ ] lc042_trapping_rain_water
    - [ ] lc252_meeting_rooms
    - [ ] lc003_longest_substring_without_repeating
    - [ ] lc424_longest_repeating_character_replacement
    - [ ] lc567_permutation_in_string
    - [ ] lc011_container_with_most_water
    - [ ] lc015_3sum
    - [ ] lc167_two_sum_ii
    - [ ] lc853_car_fleet
    - [ ] lc084_largest_rectangle_in_histogram
    - [ ] lc1851_minimum_interval_to_include_each_query
- **トラ戦** — JavaScript（一番大事な章）
  - [ ] 03-javascript-basics（120分）。**13節「非同期 async / await」は2回読む**
  - [ ] 02 の残り（7〜11節）
  - 最低ライン: 03 の 5〜10節と 13節

### 10/10（土）
- **Exam** — バックトラッキング（本命）
  - ウォームアップ: lc132, lc131（Exam 4 の元ネタ）
  - [ ] lc079_word_search
  - [ ] **lc051_n_queens**
  - [ ] **lc212_word_search_ii**（Trie が必要）
  - [ ] lc046_permutations / lc078_subsets（時間があれば）
  - 最低ライン: lc051, lc212
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc039_combination_sum
    - [ ] lc040_combination_sum_ii
    - [ ] lc022_generate_parentheses
    - [ ] lc017_letter_combinations_of_a_phone_number
    - [ ] lc090_subsets_ii
    - [ ] lc036_valid_sudoku
    - [ ] lc208_implement_trie_prefix_tree
    - [ ] lc211_design_add_and_search_words_data_structure
    - [ ] lc001_two_sum
    - [ ] lc217_contains_duplicate
    - [ ] lc128_longest_consecutive_sequence
    - [ ] lc238_product_of_array_except_self
    - [ ] lc347_top_k_frequent_elements
- **トラ戦** — サーバーの土台とゲームのルール
  - [ ] 04-server-foundation（ざっと60分。自分の担当外なので「何がどこにあるか」だけ）
  - [ ] 05-game-rules（90分）。状態遷移図と `endPhase` を丁寧に
  - 最低ライン: 05

### 10/11（日）
- **Exam** — DP ①（まだ出ていない系統。出る可能性が高い）
  - ウォームアップ: lc020, lc021
  - [ ] **lc072_edit_distance**
  - [ ] **lc139_word_break**
  - [ ] **lc322_coin_change**
  - [ ] lc1143_longest_common_subsequence
  - 最低ライン: lc072, lc139, lc322
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc300_longest_increasing_subsequence
    - [ ] lc062_unique_paths
    - [ ] lc070_climbing_stairs
    - [ ] lc746_min_cost_climbing_stairs
    - [ ] lc198_house_robber
    - [ ] lc213_house_robber_ii
    - [ ] lc121_best_time_to_buy_and_sell_stock
    - [ ] lc053_maximum_subarray
    - [ ] lc152_maximum_product_subarray
    - [ ] lc647_palindromic_substrings
    - [ ] lc005_longest_palindromic_substring
    - [ ] lc097_interleaving_string
    - [ ] lc115_distinct_subsequences
- **トラ戦** — リアルタイム通信（`rooms.js`）
  - [ ] 06-realtime-rooms（150分）。**3節 `botView` と 10節 `hooks` は自分の担当と直結するので丁寧に**
  - 最低ライン: 06 の 1〜4節と 10節

### 10/12（月）— 受験①の前日
- **Exam** — 行列・文字列の確認と模擬試験
  - ウォームアップ: Exam 3/4 の level1〜2 を3問選んで解く
  - [ ] lc048_rotate_image / lc054_spiral_matrix / lc049_group_anagrams
  - [ ] 本番と同じ時間配分で、`exam5/pra` の level2〜3 から1問ずつ
  - [ ] `[NG]` だった問題の解き直し
  - 新しい問題には手を出さない。
- **トラ戦**（1時間だけ）— AI の章の前半
  - [ ] 07-ai-bots-and-llm の 0〜2節（`bots.js` の判断）
- 早めに寝る。

### 10/13（火）— 受験①（15:00）
- [ ] 午前: ウォームアップ（Exam 5 の level2 を1問）
- [ ] 試験
- [ ] **試験直後に、出た問題を可能な限り詳細に `exam06/question/` に書き出す**（制約、入出力例、レベル、詰まった箇所）
- トラ戦: なし（休む）

---

## Phase 2: 10/14〜10/19 — 受験②まで（Exam: 本番の出題を踏まえた補強 / トラ戦: 担当を仕上げて実演練習）

受験①で合格していたら、Exam は毎日30分の復習だけにし、浮いた時間を全部トラ戦に回す。

### 10/14（水）— 受験①の振り返り
- **Exam**
  - [ ] 受験①の問題を、何も見ずに解き直す
  - [ ] 落ちた原因を分類する（アルゴリズム不足／実装ミス／時間切れ／禁止 built-in の回避）
  - [ ] 原因に合う問題を `leetcode/` から選び、10/15〜10/17 の問題と入れ替える
  - 追加（数学・ビット。どれも短いので速度練習として）:
    - [ ] lc007_reverse_integer
    - [ ] lc268_missing_number
    - [ ] lc136_single_number
    - [ ] lc190_reverse_bits
    - [ ] lc191_number_of_1_bits
    - [ ] lc371_sum_of_two_integers
    - [ ] lc202_happy_number
    - [ ] lc066_plus_one
    - [ ] lc338_counting_bits
    - [ ] lc043_multiply_strings
    - [ ] lc050_powx_n
- **トラ戦** — AI の章（担当・1回目）
  - [ ] 07-ai-bots-and-llm の 3〜8節（`lines.js`、Bot が話す、`llm.js`、テスト）
  - 最低ライン: 07 を最後まで1回読み切る

### 10/15（木）
- **Exam** — DP ②
  - ウォームアップ: lc349, lc242, lc392
  - [ ] **lc416_partition_equal_subset_sum**
  - [ ] **lc518_coin_change_ii**
  - [ ] lc494_target_sum
  - [ ] lc091_decode_ways
  - 最低ライン: lc416, lc518
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc309_best_time_to_buy_and_sell_stock_with_cooldown
    - [ ] lc055_jump_game
    - [ ] lc045_jump_game_ii
    - [ ] lc134_gas_station
    - [ ] lc073_set_matrix_zeroes
    - [ ] lc704_binary_search
    - [ ] lc033_search_in_rotated_sorted_array
    - [ ] lc153_find_minimum_in_rotated_sorted_array
    - [ ] lc074_search_a_2d_matrix
    - [ ] lc875_koko_eating_bananas
    - [ ] lc004_median_of_two_sorted_arrays
    - [ ] lc010_regular_expression_matching
    - [ ] lc312_burst_balloons
- **トラ戦** — 担当コードを実物で読む（07章・2回目）
  - [ ] `roles/amakino.md` の表の #1〜#7 を、実際のファイルを開いて読む（`botView`、`bots.js` 全体、`hooks.phase`、人狼 Bot が合わせる処理）
  - [ ] `MISTAKE`、`caughtLying`、`botClaim`、`botDelay` を何も見ずに説明できるか確認

### 10/16（金）
- **Exam** — 設計問題とヒープ（`heapq` 禁止）
  - ウォームアップ: lc189, lc796, lc125
  - [ ] 配列ベースのヒープを自作する（push / pop）
  - [ ] **lc146_lru_cache**
  - [ ] **lc295_find_median_from_data_stream**
  - 最低ライン: ヒープ自作、lc146
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc215_kth_largest_element_in_an_array
    - [ ] lc973_k_closest_points_to_origin
    - [ ] lc155_min_stack
    - [ ] lc703_kth_largest_element_in_a_stream
    - [ ] lc1046_last_stone_weight
    - [ ] lc981_time_based_key_value_store
    - [ ] lc621_task_scheduler
    - [ ] lc846_hand_of_straights
    - [ ] lc1899_merge_triplets_to_form_target_triplet
    - [ ] lc678_valid_parenthesis_string
    - [ ] lc763_partition_labels
    - [ ] lc355_design_twitter
    - [ ] lc2013_detect_squares
- **トラ戦** — 担当コードの残りと、全体をつなげる
  - [ ] `roles/amakino.md` の #8〜#15（`lines.js`、`botPrompt` / `botSpeak`、`llm.js` の `takeSlot` / `readSse` / 15秒打ち切り、テスト）
  - [ ] 08-trace-one-game（60分）。1ゲームの流れの中で、Bot と Gemini がどこで呼ばれるかを確認
  - **ここで説明文を読むのは終わり。**

### 10/17（土）
- **Exam** — グラフとバックトラッキングの再演
  - ウォームアップ: lc020, lc021, lc023
  - [ ] lc684_redundant_connection（Union-Find）
  - [ ] lc051_n_queens / lc212_word_search_ii を何も見ずに書き直す
  - [ ] lc127_word_ladder / lc269_alien_dictionary を何も見ずに書き直す
  - [ ] lc210_course_schedule_ii を何も見ずに書き直す（Exam 4 の level3 の元ネタ）
  - 最低ライン: 再演の4問
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc104_maximum_depth_of_binary_tree
    - [ ] lc102_binary_tree_level_order_traversal
    - [ ] lc226_invert_binary_tree
    - [ ] lc098_validate_binary_search_tree
    - [ ] lc206_reverse_linked_list
    - [ ] lc141_linked_list_cycle
    - [ ] lc143_reorder_list
    - [ ] lc025_reverse_nodes_in_k_group
    - [ ] lc019_remove_nth_node_from_end_of_list
    - [ ] lc002_add_two_numbers
    - [ ] lc138_copy_list_with_random_pointer
    - [ ] lc287_find_the_duplicate_number
    - [ ] lc271_encode_and_decode_strings
- **トラ戦** — 評価対策（手を動かす）
  - [ ] 12-evaluation-prep を読む
  - [ ] `make` で起動し、`docs/ASSIGNMENTS.md` の「評価での実演」（Bot と遊ぶ → Bot に話しかける → 返事が少しずつ流れる → キーを外すと定型文に戻る）を1回通す
  - [ ] 12章 4節「その場で直す練習問題」の amakino の問題を、**答えを見ずに** 実際に直す → `cd server && npm test` → `git checkout -- ファイル名` で戻す

### 10/18（日）— 弱点つぶし
- **Exam**
  - ウォームアップ: lc239, lc132, lc131
  - [ ] 10/6〜10/17 の `[NG]` と、10/6・10/7 で終わっていない問題を解き直す
  - [ ] lc739_daily_temperatures / lc150_evaluate_reverse_polish_notation（時間があれば）
  - 最低ライン: `[NG]` の解き直し
  - 追加（全問制覇。最低ラインとトラ戦が終わってから）:
    - [ ] lc100_same_tree
    - [ ] lc110_balanced_binary_tree
    - [ ] lc543_diameter_of_binary_tree
    - [ ] lc572_subtree_of_another_tree
    - [ ] lc230_kth_smallest_element_in_a_bst
    - [ ] lc235_lowest_common_ancestor_of_a_bst
    - [ ] lc199_binary_tree_right_side_view
    - [ ] lc1448_count_good_nodes_in_binary_tree
    - [ ] lc105_construct_binary_tree_from_preorder_and_inorder
    - [ ] lc124_binary_tree_maximum_path_sum
    - [ ] lc297_serialize_and_deserialize_binary_tree
- **トラ戦** — 想定問答と模擬評価
  - [ ] 07章末「amakino の想定問答」と 12章 3節を、**声に出して** 何も見ずに答える。詰まった問いだけ読み直す
  - [ ] 12章 4節の他の人の練習問題も2〜3問やる（評価者は担当外も聞いてくる）
  - [ ] できればチームの誰かに評価者役をしてもらい、10分の模擬評価

### 10/19（月）— 受験②の前日
- **Exam** — 総仕上げ
  - [ ] 受験①の問題と、過去試験の level3（Exam 4 の package_dependency_resolver、Exam 5 の prism_detector / word_ladder）を、時間を計って通しで解く
  - [ ] `[NG]` が出た問題を解き直す
  - 新しい問題には手を出さない。
- **トラ戦**（30分だけ）
  - [ ] 想定問答で詰まった問いだけ確認
- 早めに寝る。

### 10/20（火）— 受験②（15:00）
- [ ] 午前: 受験①で苦戦した問題を1問だけ解き直す
- [ ] 試験
- [ ] 試験直後に、出た問題を `exam06/question/` に追記する

---

## トラ戦の評価前日メニュー（評価日が決まったら、その前日に差し替える）

Exam は最低ライン（ウォームアップ + 1問）だけにして、残りの時間を全部これに使う。

- [ ] `make` で起動 → 自分の実演を1回通す（Chrome の DevTools を開いて、Console にエラーが出ないこと）
- [ ] その場修正の練習問題を1問、答えを見ずに直す
- [ ] 想定問答を声に出して一周
- [ ] `docs/ASSIGNMENTS.md` の「評価前に必須」のチェックが全部ついているか確認（未コミットの変更が残っていないか）

---

## Phase 3: 10/21〜10/24 — 予備（受験②で落ちた場合）

卒業期限（10/20）には間に合わないが、最後の保険として残す。

- **10/21（水）**: 受験②の問題を何も見ずに解き直し、落ちた原因を分類する。
- **10/22（木）**: 原因ごとに補強する（アルゴリズム不足なら同系統を3〜5問。実装ミスなら受験①②の問題をもう一度）。
- **10/23（金）**: 受験①②の問題と Exam 5 を通しで解き直す。早めに寝る。
- **10/24（土）**: 11:00 と 15:00 の2回。11:00 で落ちた場合は、間の時間で問題を書き出して見直す。

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

### トラ戦（読んだ章の要点を、何も見ずに3行で）

| 日付 | 章 | 要点（3行） | 分からなかったこと |
|---|---|---|---|
| | | | |

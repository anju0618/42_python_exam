# Exam Rank 06 学習計画（10/6〜10/24）

## 目標とスケジュール

**目標: 10/20 までに合格する。** 10/24 の2回は予備。

| 日付 | 試験 |
|---|---|
| 10/13（火）15:00 | 受験① |
| 10/20（火）15:00 | 受験② ← ここで合格が目標 |
| 10/24（土）11:00 | 予備③ |
| 10/24（土）15:00 | 予備④ |

## 方針

1. **難しい問題を優先する。** 過去の level3 は Course Schedule II / Word Search / Word Ladder（Medium〜Hard のグラフ探索・バックトラッキング）だった。Exam 6 の level3 も同系統か、DP が来ると予想している。
2. **ただし level1〜2 は落とさない。** 試験は level1→2→3 と進むので、ここでのミスが致命的になる。毎日の最初に30分、過去試験の元ネタ（B 群）を速度確認として解く。
3. 本番と同じ制約で解く: `sorted()` / `.sort()` / `set()` / `heapq` / `Counter` / `deque` は使わない。
4. 1日4時間前後を想定。足りない日は「最低ライン」だけは必ず終わらせる。
5. **10/13 の受験①は情報収集の機会でもある。** 受験後すぐに、覚えている問題文を `exam06/question/` に書き出す。これが 10/20 の最大の対策になる。
6. 出題予想は過去の傾向からの推測で、確実ではない。受験①の結果を見て 10/14 に修正する。

## 毎日の進め方

1. **ウォームアップ（30分）**: B 群の問題を制限時間つきで、何も見ずに解く。
2. **メイン（2.5〜3時間）**: 難しい問題を `leetcode/pra/` に自力で書く。`python3 leetcode/pra/<file>.py` で全ケース `[OK]` を確認し、`leetcode/ans/` と見比べる。
3. **見直し（30分）**: 30分考えても解けなかった問題は、答えを写して理解し、**翌日のウォームアップの前に何も見ずに解き直す**。
4. 進捗メモ（末尾）に `[NG]` だった問題と気づきを書く。

目安: Hard 級は1問40分、Medium 級は1問25分。

---

## Phase 1: 10/6〜10/12 — 受験①に向けて（探索系の強化）

### 10/6（火）— 今日は軽め: 現状確認とグリッド
- ウォームアップ: lc349, lc242
- [ ] `exam5/pra/` の level2〜3（graph_cycle_detector, island_matrix_counter, prism_detector, word_ladder）を何も見ずに解き直す
- [ ] lc130_surrounded_regions
- [ ] lc994_rotting_oranges
- 最低ライン: exam5 の4問の解き直し

### 10/7（水）— グラフ ①（Word Ladder と依存解決の発展）
- ウォームアップ: lc392, lc125
- [ ] lc127_word_ladder（何も見ずに書けること）
- [ ] lc210_course_schedule_ii
- [ ] **lc269_alien_dictionary**（本命）
- [ ] lc207_course_schedule
- 最低ライン: lc269, lc210

### 10/8（木）— グラフ ②（グリッドと最短経路）
- ウォームアップ: lc189, lc796
- [ ] **lc417_pacific_atlantic_water_flow**
- [ ] lc286_walls_and_gates
- [ ] **lc743_network_delay_time**（`heapq` なし。配列を線形に走査する方式で書く）
- [ ] lc133_clone_graph
- 最低ライン: lc417, lc743

### 10/9（金）— 区間・ソート自作・スライディングウィンドウ
- ウォームアップ: lc023, lc239（Exam 4 の元ネタ）
- [ ] ソートの自作（バブル／マージ）を何も見ずに書く
- [ ] lc253_meeting_rooms_ii
- [ ] lc056_merge_intervals
- [ ] lc057_insert_interval
- [ ] lc435_non_overlapping_intervals
- [ ] **lc076_minimum_window_substring**
- 最低ライン: ソート自作、lc253, lc076

### 10/10（土）— バックトラッキング（本命）
- ウォームアップ: lc132, lc131（Exam 4 の元ネタ）
- [ ] lc079_word_search（exam5 の prism_detector と同系統）
- [ ] **lc051_n_queens**（本命）
- [ ] **lc212_word_search_ii**（本命。Trie が必要）
- [ ] lc046_permutations
- [ ] lc078_subsets
- 最低ライン: lc051, lc212

### 10/11（日）— DP ①（まだ出ていない系統。出る可能性が高い）
- ウォームアップ: lc020, lc021
- [ ] **lc072_edit_distance**
- [ ] **lc139_word_break**
- [ ] **lc322_coin_change**
- [ ] **lc1143_longest_common_subsequence**
- [ ] lc300_longest_increasing_subsequence
- 最低ライン: lc072, lc139, lc322

### 10/12（月）— 受験①の前日: 行列・文字列の確認と模擬試験
- ウォームアップ: Exam 3/4 の level1〜2 を3問選んで解く
- [ ] lc048_rotate_image
- [ ] lc073_set_matrix_zeroes
- [ ] lc054_spiral_matrix
- [ ] lc049_group_anagrams
- [ ] 本番と同じ時間配分で、`exam5/pra` の level2〜3 から1問ずつ
- [ ] `[NG]` だった問題の解き直し
- 新しい問題には手を出さない。早めに寝る。

### 10/13（火）— 受験①（15:00）
- [ ] 午前: ウォームアップ（Exam 5 の level2 を1問）
- [ ] 試験
- [ ] **試験直後に、出た問題を可能な限り詳細に `exam06/question/` に書き出す**（制約、入出力例、レベル、自分が詰まった箇所）

---

## Phase 2: 10/14〜10/19 — 受験②に向けて（本番の出題を踏まえた補強）

### 10/14（水）— 受験①の振り返り
- [ ] 受験①の問題を、何も見ずに解き直す
- [ ] 落ちた原因を分類する（アルゴリズム不足／実装ミス／時間切れ／禁止 built-in の回避）
- [ ] 原因に合う問題を `leetcode/` から選び、以下の日程の問題と入れ替える
- 受験①で合格していた場合は、ここで学習を終えて復習のみにする。

### 10/15（木）— DP ②
- ウォームアップ: lc349, lc242, lc392（元ネタの再確認）
- [ ] **lc416_partition_equal_subset_sum**
- [ ] **lc518_coin_change_ii**
- [ ] **lc494_target_sum**
- [ ] lc091_decode_ways
- [ ] lc062_unique_paths
- [ ] lc042_trapping_rain_water
- 最低ライン: lc416, lc518

### 10/16（金）— 設計問題とヒープ（`heapq` 禁止）
- ウォームアップ: lc189, lc796, lc125
- [ ] 配列ベースのヒープを自作する（push / pop）
- [ ] **lc146_lru_cache**
- [ ] **lc295_find_median_from_data_stream**
- [ ] lc215_kth_largest_element_in_an_array
- [ ] lc973_k_closest_points_to_origin
- [ ] lc155_min_stack
- 最低ライン: lc146, lc295

### 10/17（土）— グラフとバックトラッキングの再演
- ウォームアップ: lc020, lc021, lc023
- [ ] lc684_redundant_connection（Union-Find）
- [ ] lc261_graph_valid_tree
- [ ] lc323_number_of_connected_components
- [ ] lc051_n_queens / lc212_word_search_ii を何も見ずに書き直す
- [ ] lc127_word_ladder / lc269_alien_dictionary を何も見ずに書き直す
- 最低ライン: 再演の4問

### 10/18（日）— 弱点つぶしと周辺ジャンル
- ウォームアップ: lc239, lc132, lc131
- [ ] 10/6〜10/17 の `[NG]` を解き直す
- [ ] lc739_daily_temperatures
- [ ] lc150_evaluate_reverse_polish_notation
- [ ] lc271_encode_and_decode_strings（exam5 の compress_decompress と同系統）
- [ ] 木の基本: lc104 / lc102 / lc226 / lc098
- 最低ライン: `[NG]` の解き直し

### 10/19（月）— 受験②の前日: 総仕上げ
- [ ] 受験①の問題と、過去試験の level3 全部（Exam 4 の package_dependency_resolver、Exam 5 の prism_detector / word_ladder）を、時間を計って通しで解く
- [ ] `[NG]` が出た問題を解き直す
- 新しい問題には手を出さない。早めに寝る。

### 10/20（火）— 受験②（15:00）
- [ ] 午前: 受験①で苦戦した問題を1問だけ解き直す
- [ ] 試験
- [ ] 試験直後に、出た問題を `exam06/question/` に追記する

---

## Phase 3: 10/21〜10/24 — 予備（受験②で落ちた場合）

- **10/21（水）**: 受験②の問題を何も見ずに解き直し、落ちた原因を分類する。
- **10/22（木）**: 原因ごとに補強する（アルゴリズム不足なら、D 群から同系統を3〜5問。実装ミスなら受験①②の問題をもう一度）。
- **10/23（金）**: 受験①②の問題と Exam 5 を通しで解き直す。早めに寝る。
- **10/24（土）**: 11:00 と 15:00 の2回。11:00 で落ちた場合は、間の時間で問題を書き出して見直す。

---

## LeetCode 対象一覧（優先度別）

### A: 必ず解く（上の日次計画に書いた問題）
太字は難しい問題で、本命・有力として優先する。受験②までに全部終える。

### B: 過去試験の元ネタ（level1〜2 の再出題対策）
Exam 3/4 の level1〜2 は、同じ発想が別の名前で再登場した実績がある。毎日のウォームアップで消化する。

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

### C: 時間が余ったら解く（頻出の基本）
受験①の後、余り時間に回す。

- [ ] lc001 / lc217 / lc053 / lc121 / lc167 / lc015 / lc011 / lc003
- [ ] lc347 / lc238 / lc128（ハッシュ・配列）
- [ ] lc704 / lc033 / lc153 / lc875（二分探索）
- [ ] lc019 / lc141 / lc002（連結リスト）
- [ ] lc1046（ヒープ）

### D: 後回し（出る可能性が低いと判断）
Exam 3〜5 の傾向になく、実装も重い。受験②で落ちた場合のみ検討する。

lc004 / lc010 / lc084 / lc097 / lc115 / lc124 / lc208 / lc211 / lc297 / lc312 / lc329 / lc332 / lc355 / lc787 / lc778 / lc1851 / lc2013 ほか

---

## 進捗メモ

| 日付 | 完了した問題 | `[NG]` だった問題 | 気づき |
|---|---|---|---|
| | | | |

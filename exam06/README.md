# exam06 予想問題（全47問）

dayN は **10/(8+N)** の日の問題（day1 = 10/9 … day16 = 10/24）。各問題は `.txt`（問題文）と `.py`（空の関数 + テスト）のセット。
日ごとの詳しい計画は `STUDY_PLAN.md`。

| day | 日付 | テーマ | 問題 |
|---|---|---|---|
| day1 | 10/9 | グラフ / グリッド | signal_spread, task_order, network_delay |
| day2 | 10/10 | 区間 / ウィンドウ / 自作ソート | room_planner, shortest_cover, merge_ranges |
| day3 | 10/11 | バックトラッキング | queens_count, word_hunt, bracket_builder |
| day4 | 10/12 | DP ① | text_distance, coin_min, word_split |
| day5 | 10/13 受験① | ウォームアップ | group_anagrams |
| day6 | 10/14 | 過去問の穴 | lock_opener, cool_days, redundant_link, hist_area |
| day7 | 10/15 | クラス設計 | prefix_dictionary, cache_keeper, pack_strings |
| day8 | 10/16 | DP ② | equal_split, coin_ways, decode_ways, paths_with_walls |
| day9 | 10/17 | ヒープ自作 / 頻度 | top_k_frequent, k_closest, min_heap, median_tracker |
| day10 | 10/18 | 木 | tree_levels, valid_search_tree, best_path_sum |
| day11 | 10/19 | Hard の模擬 | word_grid_search, alien_order, cheapest_flight |
| day12 | 10/20 受験② | ウォームアップ | spiral_fill |
| day13 | 10/21 | 文字列 / 配列 | find_all_anagrams, rotate_square, longest_palindrome_sub, multiply_strings |
| day14 | 10/22 | グラフの総復習 | min_wire, swim_time, itinerary |
| day15 | 10/23 | 貪欲 / DP の総復習 | can_reach, min_jumps, gas_loop, longest_climb |
| day16 | 10/24 受験③ | ウォームアップ | longest_unique_run |

使い方: `.txt` を読む → `.py` に実装 → `python3 day1/py_task_order.py` で全部 `[OK]` を確認。
制約: `sorted()` / `.sort()` / `set()` / `heapq` / `Counter` / `deque` は使わない。

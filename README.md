# 42_python_exam

Practice problems for the 42 School Python curriculum exams (Exam Rank 03 / 04 / 05).

[English](#english) | [日本語](#日本語)

---

## English

### Contents

| Directory | Contents |
|---|---|
| `exam3/` | Exam Rank 03, level1–level6, 14 problems |
| `exam4/` | Exam Rank 04, level1–level3, 7 problems |
| `exam5/` | Exam Rank 05, level1–level3, 7 problems |
| `leetcode/` | LeetCode problems the exam problems are based on + NeetCode 150 (155 problems) |
| `leetcode_normal/ans/` | Alternative, easier-to-read solutions for `leetcode/` |
| `STUDY_PLAN.md` | Daily study plan (Japanese) |
| `_template.py` | Template for adding a new problem |

Each source directory has three subdirectories:

- `question/` — problem statement
- `pra/` — practice stub (function body is empty, test cases included)
- `ans/` — solution

Solutions in `ans/` do not use `sorted()`, `.sort()`, `set()`, `heapq`, `Counter`, or `deque`.

### Usage

1. Read the problem in `question/`.
2. Implement the function in `pra/`.
3. Run it and check that every case prints `[OK]`.
4. Compare with `ans/`.

```sh
python3 exam5/pra/level1/py_spiral_matrix.py
```

To reset the practice files and start over, discard your changes with git. This can be repeated any number of times.

```sh
git restore .                # reset everything
git restore exam5/pra/       # reset only exam5 practice files
```

Note: `git restore .` discards all uncommitted changes in the repository.

### Problems

LeetCode column: the LeetCode problem the exam problem is likely based on (`-` = none found).

#### Exam Rank 03

| Level | Problem | LeetCode |
|---|---|---|
| 1 | cryptic_sorter | - |
| 1 | inter | 349. Intersection of Two Arrays |
| 2 | echo_validator | 125. Valid Palindrome |
| 2 | mirror_matrix | - |
| 3 | hidenp | 392. Is Subsequence |
| 3 | number_base_converter | - |
| 3 | pattern_tracker | - |
| 4 | anagram | 242. Valid Anagram |
| 4 | shadow_merge | 21. Merge Two Sorted Lists |
| 4 | string_permutation_checker | 242. Valid Anagram |
| 5 | string_sculptor | - |
| 5 | twist_sequence | 189. Rotate Array |
| 6 | bracket_validator | 20. Valid Parentheses |
| 6 | whisper_cipher | - |

#### Exam Rank 04

| Level | Problem | LeetCode |
|---|---|---|
| 1 | array_rotation_detector | 796. Rotate String |
| 1 | constellation_mapper | - |
| 1 | list_intersection_finder | 349. Intersection of Two Arrays |
| 2 | merge_sorted_list | 23. Merge k Sorted Lists |
| 2 | palindrome_partitioner | 132. Palindrome Partitioning II |
| 2 | sliding_window_maximium | 239. Sliding Window Maximum |
| 3 | package_dependency_resolver | 210. Course Schedule II |

#### Exam Rank 05

| Level | Problem | LeetCode |
|---|---|---|
| 1 | compress_decompress | - |
| 1 | spiral_matrix | 54. Spiral Matrix |
| 2 | graph_cycle_detector | 207. Course Schedule |
| 2 | island_matrix_counter | 200. Number of Islands |
| 2 | schedule_meetings | 253. Meeting Rooms II |
| 3 | prism_detector | 79. Word Search |
| 3 | word_ladder | 127. Word Ladder |

---

## 日本語

### 中身

| ディレクトリ | 内容 |
|---|---|
| `exam3/` | Exam Rank 03、level1〜level6、14問 |
| `exam4/` | Exam Rank 04、level1〜level3、7問 |
| `exam5/` | Exam Rank 05、level1〜level3、7問 |
| `leetcode/` | exam問題の元ネタのLeetCode問題 + NeetCode 150（計155問） |
| `leetcode_normal/ans/` | `leetcode/`の読みやすさ重視の別解 |
| `STUDY_PLAN.md` | 日次の学習計画 |
| `_template.py` | 問題追加用テンプレート |

各ディレクトリの下は3つに分かれている。

- `question/` — 問題文
- `pra/` — 練習用（関数の中身は空、テストケース付き）
- `ans/` — 解答

`ans/`の解答は`sorted()`・`.sort()`・`set()`・`heapq`・`Counter`・`deque`を使っていない。

### 使い方

1. `question/`で問題を読む
2. `pra/`の関数を実装する
3. 実行して全ケース`[OK]`になることを確認する
4. `ans/`と見比べる

```sh
python3 exam5/pra/level1/py_spiral_matrix.py
```

練習ファイルはgitで元に戻せる。何度でもリセットしてやり直せる。

```sh
git restore .                # 全部リセット
git restore exam5/pra/       # exam5の練習ファイルだけリセット
```

注意: `git restore .`はリポジトリ内のコミットしていない変更をすべて破棄する。

### 問題一覧

LeetCode列: 元ネタと思われるLeetCode問題（`-` = 該当なし）。

#### Exam Rank 03

| レベル | 問題 | LeetCode |
|---|---|---|
| 1 | cryptic_sorter | - |
| 1 | inter | 349. Intersection of Two Arrays |
| 2 | echo_validator | 125. Valid Palindrome |
| 2 | mirror_matrix | - |
| 3 | hidenp | 392. Is Subsequence |
| 3 | number_base_converter | - |
| 3 | pattern_tracker | - |
| 4 | anagram | 242. Valid Anagram |
| 4 | shadow_merge | 21. Merge Two Sorted Lists |
| 4 | string_permutation_checker | 242. Valid Anagram |
| 5 | string_sculptor | - |
| 5 | twist_sequence | 189. Rotate Array |
| 6 | bracket_validator | 20. Valid Parentheses |
| 6 | whisper_cipher | - |

#### Exam Rank 04

| レベル | 問題 | LeetCode |
|---|---|---|
| 1 | array_rotation_detector | 796. Rotate String |
| 1 | constellation_mapper | - |
| 1 | list_intersection_finder | 349. Intersection of Two Arrays |
| 2 | merge_sorted_list | 23. Merge k Sorted Lists |
| 2 | palindrome_partitioner | 132. Palindrome Partitioning II |
| 2 | sliding_window_maximium | 239. Sliding Window Maximum |
| 3 | package_dependency_resolver | 210. Course Schedule II |

#### Exam Rank 05

| レベル | 問題 | LeetCode |
|---|---|---|
| 1 | compress_decompress | - |
| 1 | spiral_matrix | 54. Spiral Matrix |
| 2 | graph_cycle_detector | 207. Course Schedule |
| 2 | island_matrix_counter | 200. Number of Islands |
| 2 | schedule_meetings | 253. Meeting Rooms II |
| 3 | prism_detector | 79. Word Search |
| 3 | word_ladder | 127. Word Ladder |

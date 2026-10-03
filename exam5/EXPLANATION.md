# exam5 解説

`ans/` の模範解答に基づく解説です。問題の順番は level1 → level2 → level3 です。

| # | 問題 | レベル | 主なアルゴリズム | 計算量 |
|---|------|--------|------------------|--------|
| 1 | py_compress_decompress | 1 | 連続文字のラン長圧縮/展開 | O(n) |
| 2 | py_spiral_matrix | 1 | 4つの境界を縮める渦巻き生成 | O(n²) |
| 3 | py_graph_cycle_detector | 2 | 3状態 DFS による有向閉路検出 | O(V+E) |
| 4 | py_island_matrix_counter | 2 | グリッド DFS (連結成分の数え上げ) | O(R·C) |
| 5 | py_schedule_meetings | 2 | ソート + 貪欲な部屋割り当て | O(n log n 〜 n²) |
| 6 | py_prism_detector | 3 | 8方向の総当たり探索 | O(R·C·8·L) |
| 7 | py_word_ladder | 3 | BFS による最短経路 | O(N²·L) |

---

## 1. py_compress_decompress (level1)

### 考え方
- **compress**: 「今の文字」と「1つ前の文字」を比べながら左から1回走査する。同じなら `count` を増やし、違えば直前の文字の run が終わったので書き出す。
- **decompress**: 文字を1つ読み、その直後に続く数字を全部読み取って(複数桁対応)回数にする。数字がなければ 1 回。

### 実装のポイント
```python
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result.append(s[i - 1])
        if count > 1:            # 1回だけの文字には数字を付けない
            result.append(str(count))
        count = 1
result.append(s[-1])             # ループ後、最後の run が未出力なので出す
```
- ループ中に書き出されるのは「1つ前の run」なので、**最後の run はループの外で必ず追加**する必要がある。ここを忘れるのが典型的なバグ。
- 空文字列は `s[-1]` で落ちるため、先頭で `if not s: return ""` と弾く。
- decompress は `while s[i].isdigit()` で数字を連結して `int(digits)` に変換する。`"a12"` → 12 個の `a` になる。

### トレース: `compress("aabcccccaaa")`
| i | s[i] | 動作 | result | count |
|---|------|------|--------|-------|
| 1 | a | 同じ | | 2 |
| 2 | b | 違う → `a`,`2` 出力 | a2 | 1 |
| 3 | c | 違う → `b` 出力 (count=1) | a2b | 1 |
| 4〜7 | c | 同じ | | 5 |
| 8 | a | 違う → `c`,`5` 出力 | a2bc5 | 1 |
| 9〜10 | a | 同じ | | 3 |
| 終了 | | 最後の `a`,`3` 出力 | a2bc5a3 | |

### 計算量
時間 O(n)、空間 O(n)。

### 落とし穴
- 入力の元の文字列に数字が含まれると decompress が曖昧になる(この問題では想定外)。
- `result += ...` の文字列連結より、リストに貯めて `"".join` する方が効率的。

---

## 2. py_spiral_matrix (level1)

### 考え方
外周から内側へ向かって、**上辺 → 右辺 → 下辺 → 左辺**の順に番号を埋める。埋め終わった辺の分だけ境界 (`top`, `right`, `bottom`, `left`) を内側に縮め、境界が交差したら終了する。

### 実装のポイント
```python
while top <= bottom and left <= right:
    for col in range(left, right + 1):      # 上辺: 左→右
        matrix[top][col] = num; num += 1
    top += 1
    for row in range(top, bottom + 1):      # 右辺: 上→下
        matrix[row][right] = num; num += 1
    right -= 1
    if top <= bottom:                       # 下辺: 右→左
        for col in range(right, left - 1, -1): ...
        bottom -= 1
    if left <= right:                       # 左辺: 下→上
        for row in range(bottom, top - 1, -1): ...
        left += 1
```
- 下辺と左辺の手前の `if` が重要。n が奇数のとき最後は中心の1マスだけが残る。ガードがないと、上辺で埋めたセルを下辺で**二重に埋めてしまう**。
- 各辺を処理するたびに対応する境界を1つ縮めるので、次の辺の範囲が自動的に正しくなる。

### トレース: n = 3
| 手順 | 埋めるセル | 数字 |
|------|-----------|------|
| 上辺 | (0,0)(0,1)(0,2) | 1,2,3 |
| 右辺 | (1,2)(2,2) | 4,5 |
| 下辺 | (2,1)(2,0) | 6,7 |
| 左辺 | (1,0) | 8 |
| 2周目 上辺 | (1,1) | 9 |

結果: `[[1,2,3],[8,9,4],[7,6,5]]`

### 計算量
時間 O(n²)、空間 O(n²)(出力サイズ)。

### 落とし穴
- n = 1 のとき: 上辺で埋めた後 `top > bottom` となり、`if top <= bottom` のガードで下辺をスキップできる。
- 「4方向に進みながら壁にぶつかったら曲がる」方式でも解けるが、境界縮小方式の方が単純。

---

## 3. py_graph_cycle_detector (level2)

### 考え方
有向グラフの閉路は **DFS 中に、いま辿っている経路上のノードへ戻ってきたら**見つかる。そのため各ノードに3つの状態を持たせる。

| 状態 | 意味 |
|------|------|
| 未訪問 (`state` にない) | まだ見ていない |
| `"visiting"` | 現在の DFS 経路の途中(スタック上) |
| `"done"` | そこから先を全部調べ終わり、閉路なしと確定 |

`"visiting"` のノードにもう一度到達したら閉路。`"done"` のノードに到達しても閉路ではない(すでに調べ済みなので探索を打ち切れる)。

### 実装のポイント
```python
def dfs(node):
    if state.get(node) == "visiting": return True   # 経路上に戻った = 閉路
    if state.get(node) == "done":     return False  # 調査済み
    state[node] = "visiting"
    for neighbor in graph.get(node, []):
        if dfs(neighbor): return True
    state[node] = "done"
    return False

for node in graph:                 # 非連結成分すべてを起点にする
    if node not in state and dfs(node): return True
```
- 外側の `for node in graph` が、**複数の非連結成分**への対応になっている。
- `graph.get(node, [])` で、キーとして現れない(辞書に載っていない)隣接ノードも安全に扱える。
- 空グラフは `for` が回らず `False` になる。冒頭の `if not graph` は明示的な早期リターン。

### なぜ visited(2状態)ではだめか
無向グラフなら「訪問済み = 閉路」の判定でよいが、有向グラフでは `A→B, A→C, B→C` のように、**別経路から訪問済みのノードに着いても閉路ではない**。そのため「今の経路上か」を区別する3状態が必要。

### 計算量
時間 O(V+E)、空間 O(V)(再帰スタック込み)。

### 落とし穴
- 自己ループ `{0: [0]}` は、`0` が `"visiting"` のまま自分に戻るので `True` になる。
- 再帰が深いと Python の再帰上限(既定 1000)に当たる可能性がある。試験の規模では問題にならない。

---

## 4. py_island_matrix_counter (level2)

### 考え方
行列を走査し、**未訪問の `"1"` を見つけたら島が1つ増える**。その島全体を DFS で訪問済みにして、同じ島を二度数えないようにする。

### 実装のポイント
```python
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "1" and not visited[r][c]:
            count += 1       # 新しい島の発見
            dfs(r, c)        # 島全体を visited にする
```
```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols: return   # 範囲外
    if visited[r][c] or matrix[r][c] != "1":     return   # 訪問済み or 水
    visited[r][c] = True
    dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)    # 上下左右のみ
```
- 斜めには進まない(4方向のみ)ので、斜めだけで接するセルは別の島になる。
- 入力の行列を書き換えず、別の `visited` 配列を使っている。問題文では書き換えも許可されている(`"1"` を `"0"` にすれば `visited` は不要)。
- `not matrix or not matrix[0]` で、行なし・列なしのどちらも 0 を返す。

### トレース (例2)
```
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
- (0,0) で1つ目 → 左上の 2x2 を全訪問
- (2,2) で2つ目 → 単独
- (3,3) で3つ目 → (3,4) まで訪問
- 合計 **3**

### 計算量
時間 O(R·C)(各セルは高々1回訪問)、空間 O(R·C)。

### 落とし穴
- 要素は整数ではなく文字列 `"1"`/`"0"`。`== 1` と比べると常に偽になる。
- 範囲チェックを `visited` の参照より**先に**書くこと。逆だと負のインデックスが Python では末尾要素を指してしまい、バグになる。

---

## 5. py_schedule_meetings (level2)

### 考え方
1. 会議を**開始時刻でソート**する。
2. ソート済みの会議を順に見て、既存の部屋のうち「**最後の会議の終了時刻 ≤ この会議の開始時刻**」となる最初の部屋に入れる。
3. どの部屋にも入らなければ新しい部屋を作る。

部屋の数がそのまま最小の必要会議室数になる(開始順に貪欲に割り当てる区間グラフ彩色と同じ構造)。

### 実装のポイント
```python
for i in range(1, len(ordered)):         # 挿入ソート(手書きの安定ソート)
    key = ordered[i]
    j = i - 1
    while j >= 0 and ordered[j][0] > key[0]:
        ordered[j + 1] = ordered[j]; j -= 1
    ordered[j + 1] = key
```
```python
for room in rooms:
    if room[-1][1] <= start:     # 終了 == 開始 は重ならない扱い
        room.append(meeting); assigned = True; break
if not assigned:
    rooms.append([meeting])
```
- 比較は `<=`。会議 `(5,10)` と `(10,15)` は同じ部屋に入れる(終了と開始が同時刻なら重複しない)。
- 挿入ソートは**安定**なので、開始時刻が同じ会議の順序は入力順のまま保たれる。出力例と一致させるために重要。
- `list(intervals)` でコピーしてからソートし、呼び出し元の入力を変更しない。
- 空入力は `(0, [])`。

### トレース (例1): `[(0,30), (5,10), (15,20)]`
| 会議 | 判定 | rooms |
|------|------|-------|
| (0,30) | 部屋なし → 新規 | `[[(0,30)]]` |
| (5,10) | 部屋1の終了30 > 5 → 入らない → 新規 | `[[(0,30)], [(5,10)]]` |
| (15,20) | 部屋1: 30 > 15 ✗、部屋2: 10 ≤ 15 ✓ | `[[(0,30)], [(5,10),(15,20)]]` |

結果: `(2, [[(0,30)], [(5,10),(15,20)]])`

### 計算量
- ソート: 挿入ソートなので最悪 O(n²)(組み込み `sorted` なら O(n log n))
- 割り当て: 部屋数を m として O(n·m)

### 落とし穴・別解
- 部屋数だけでよければ、最小ヒープで終了時刻を管理する LeetCode 253 の定石 (O(n log n)) がある。
- この問題は「どの部屋に入れるか」まで出力に含むため、各部屋の最後の会議を直接見る方式にしている。出力の形(部屋の順序、部屋内の順序)が採点対象なので、「最初に空いている部屋」という選び方も仕様の一部である。

---

## 6. py_prism_detector (level3)

### 考え方
グリッドの**全セルを起点**に、**8方向すべて**へ、パターンの長さ分だけ文字を比較する。全文字が一致したら `(x, y, 方向コード)` を結果に追加する。

### 実装のポイント
```python
DIRECTIONS = [(1,0,"H"), (-1,0,"H-"), (0,1,"V"), (0,-1,"V-"),
              (1,1,"D1"), (-1,-1,"D1-"), (-1,1,"D2"), (1,-1,"D2-")]
```
`(dx, dy)` で、**dx は列(x)方向、dy は行(y)方向**の増分。
```python
for y in range(rows):
    for x in range(cols):
        for dx, dy, code in DIRECTIONS:
            match = True
            for i in range(plen):
                nx, ny = x + dx*i, y + dy*i
                if ny < 0 or ny >= rows or nx < 0 or nx >= cols: match = False; break
                if grid[ny][nx] != pattern[i]:                   match = False; break
            if match: result.append((x, y, code))
```
- 出力の `x` は**列**、`y` は**行**。`grid[y][x]` でアクセスする点に注意(行列の `[row][col]` と順序が逆に見える)。
- 範囲外に出たら即不一致にして打ち切る。
- 走査順(y 外側 → x → 方向リストの順)が出力順になる。例では同じ起点で `H` が `V` より先に出る。方向リストの順序を変えると出力順が変わる。

### トレース (例1): `["CAT","A..","T.."]`, `"CAT"`
- 起点 (0,0) = `C`
  - `H` (右): `C,A,T` ✓
  - `V` (下): `C,A,T` ✓
  - その他は範囲外または不一致
- 他のセルは `C` ではないので起点にならない

結果: `[(0,0,"H"), (0,0,"V")]`

### 計算量
時間 O(R·C·8·L)(L = パターン長)、空間は出力を除いて O(1)。

### 落とし穴
- `V` は下向き `(0,1)`(y は下に向かって増える)。
- `D2` は問題文の説明では「右上」だが、ベクトル `(-1,1)` を `(dx,dy)` として使うと実際に進むのは**左下**で、説明と実際の向きが食い違っている。`D2-` も同様。採点は問題文の「ベクトル → コード」の対応表どおりに行われるので、**表のベクトルとコードをそのまま写す**こと。向きの説明に合わせて直してはいけない。
- 1文字のパターンだと、全方向が同じセルで一致するため8個の結果が出る(仕様どおり)。
- `cols = len(grid[0])` は全行が同じ長さであることが前提。

---

## 7. py_word_ladder (level3)

### 考え方
「単語 = ノード、1文字だけ違う単語同士 = 辺」とみなしたグラフで、`start` から `end` への**最短経路の頂点数**を求める問題。重みなしグラフの最短経路は **BFS** が最適。

### 実装のポイント
```python
if end not in sentence: return 0          # 到達不能な終点は即座に 0

visited = {start: True}
queue = [(start, 1)]                       # (単語, ここまでの語数)
idx = 0
while idx < len(queue):
    word, length = queue[idx]; idx += 1    # list を使った疑似 deque (pop(0) を避ける)
    if word == end: return length
    for candidate in sentence:
        if candidate in visited: continue
        diff = 0
        for a, b in zip(word, candidate):  # 1文字差の判定
            if a != b:
                diff += 1
                if diff > 1: break
        if diff == 1:
            visited[candidate] = True      # キューに入れる時点で訪問済みにする
            queue.append((candidate, length + 1))
return 0
```
- 長さは **語数**(`start` と `end` を含む)なので、初期値は 1。
- `visited` は**キューに入れるとき**に更新する。取り出すときに更新すると同じ単語が何度もキューに入る。
- `diff == 1` を要求するので、同一単語(差 0)は遷移にならない。
- キューの先頭は `idx` を進めて取り出している。`list.pop(0)` は O(n) なので避けている。

### トレース (例1): `hit → cog`
```
hit(1) → hot(2) → dot(3), lot(3) → dog(4), log(4) → cog(5)
```
結果 **5**。例2では `cog` が `sentence` にないので即 `0`。

### 計算量
時間 O(N²·L)(N = 単語数、L = 単語長。各単語について全候補と比較)、空間 O(N)。

### 落とし穴・別解
- `start` が `sentence` に含まれなくてもよい(そこからの最初の一歩は `sentence` の単語へ)。
- 単語数が多い場合は、`h*t` のような**ワイルドカード辞書**を作って隣接を O(N·L) で求める方式が速い(LeetCode 127 の標準解)。
- 全単語が同じ長さである前提で `zip` を使っている。長さが違うと `zip` は短い方に合わせてしまう。

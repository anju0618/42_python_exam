# exam5 暗記用まとめ

`ans/` の模範解答がベース。問題順は level1 → level2 → level3。
計算量などの余談は省き、**覚えるべきこと**だけに絞っている。

| # | 問題 | レベル | 覚えるキーワード |
|---|------|--------|------------------|
| 1 | py_compress_decompress | 1 | ラン長圧縮: 比較しながら1回走査 |
| 2 | py_spiral_matrix | 1 | 境界を縮める渦巻き |
| 3 | py_graph_cycle_detector | 2 | DFSで「今の道」に戻ったら閉路 |
| 4 | py_island_matrix_counter | 2 | グリッドDFSで陸を"0"に塗りつぶす |
| 5 | py_schedule_meetings | 2 | ソート＋貪欲な部屋割り当て |
| 6 | py_prism_detector | 3 | 全セル×8方向の総当たり |
| 7 | py_word_ladder | 3 | BFSで最短経路(語数) |

---

## 1. py_compress_decompress (level1)

**暗記ポイント**: 「今の文字」と「1つ前の文字」を比べながら左から1回だけ走査する。違いが出た瞬間に「1つ前の run」を書き出す。

### compress の型
```python
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result.append(s[i - 1])
        if count > 1:            # 1回だけの文字には数字を付けない
            result.append(str(count))
        count = 1
result.append(s[-1])             # ★ループの外で最後のrunを必ず出す
```
- **最重要**: ループ中に出力されるのは常に「1つ前の run」。だから**最後の run はループの外で追加**しないと消える。これが典型的なバグ。
- 空文字列は `s[-1]` で落ちるので、先頭で `if not s: return ""`。

### decompress の型
- 文字を1つ読む → 直後の数字を `while s[i].isdigit()` で全部つなげて `int()` → 回数にする。数字がなければ1回。

### 覚えるトレース: `compress("aabcccccaaa")` → `"a2bc5a3"`
- a,a → count2 → bで違う→a2出力
- b → count1 → cで違う→b出力(数字なし)
- c×5 → count5 → aで違う→c5出力
- a×3 → ループ終了 → 最後にa3を追加

### 落とし穴
- 元の文字列に数字が入っているとdecompressが曖昧になる(この問題では想定外)。
- 文字列連結の繰り返しでなく、リストに貯めて最後に `"".join`。

---

## 2. py_spiral_matrix (level1)

**暗記ポイント**: 外側から内側へ、**上辺→右辺→下辺→左辺**の順に埋める。1辺埋めたらその境界を1つ縮める。

### 型
```python
while top <= bottom and left <= right:
    for col in range(left, right + 1):       # 上辺: 左→右
        matrix[top][col] = num; num += 1
    top += 1
    for row in range(top, bottom + 1):       # 右辺: 上→下
        matrix[row][right] = num; num += 1
    right -= 1
    if top <= bottom:                        # ★下辺を埋める前にガード
        for col in range(right, left - 1, -1): ...
        bottom -= 1
    if left <= right:                        # ★左辺を埋める前にガード
        for row in range(bottom, top - 1, -1): ...
        left += 1
```
- **最重要**: 下辺・左辺の手前の `if` ガードを忘れない。n が奇数だと中心1マスが残るタイミングがあり、ガードがないと上辺で埋めたセルを下辺で二重に埋める。

### 覚えるトレース: n=3 → `[[1,2,3],[8,9,4],[7,6,5]]`
上辺(1,2,3)→右辺(4,5)→下辺(6,7)→左辺(8)→中心(9)

### 落とし穴
- n=1 のときは上辺を埋めた直後に `top > bottom` となり、ガードで下辺以降をスキップできる(これで正しく動く)。

---

## 3. py_graph_cycle_detector (level2)

**暗記ポイント**: 有向グラフの閉路検出は「訪問済みか」ではなく「**今たどっている道の上にいるか**」で判定する。道に入るときに `visiting` に入れ、戻るときに消す。

### 型
```python
visiting = {}                      # 今の道に乗っているノード(set()禁止なのでdict)

def dfs(node):
    if node in visiting: return True       # 今の道に戻ってきた=閉路
    visiting[node] = True                  # 道に入る
    for n in graph.get(node, []):
        if dfs(n): return True
    del visiting[node]                     # ★戻るときに道から消す
    return False

for node in graph:                 # ★非連結成分すべてを起点にする
    if dfs(node): return True
return False
```
- **最重要**: 戻るときの `del visiting[node]` を忘れない。消さないと `A→B, A→C, B→C` のように別の道から同じノードに着いただけで閉路と誤判定する。
- `graph.get(node, [])` で辞書にないノードも安全に処理。
- 外側の `for node in graph` で非連結成分すべてをカバー。空のグラフはループが回らず `False`。

### 覚えるトレース: `{0: [1], 1: [2], 2: [0]}`
`dfs(0)` 道={0} → `dfs(1)` 道={0,1} → `dfs(2)` 道={0,1,2} → `dfs(0)`: 0は道にいる → **True**

### 落とし穴
- 自己ループ `{0: [0]}` は `0` が道に乗ったまま自分に戻るので `True`。
- 調べ終わったノードを覚えないので、同じノードを何度も調べ直す。分岐が多い大きなグラフでは遅くなる(普通のテスト規模なら問題ない)。

---

## 4. py_island_matrix_counter (level2)

**暗記ポイント**: `"1"` を見つけたら島が1つ増える。その島全体をDFSで `"0"`(水)に塗りつぶして二重カウントを防ぐ。`visited` は使わない(問題文で行列の書き換えが許可されている)。

### 型
```python
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == "1":
            count += 1       # 新しい島の発見
            dfs(r, c)        # 島全体を"0"に塗る

def dfs(r, c):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]): return   # ★範囲外チェックを先に
    if matrix[r][c] != "1": return                                         # 水 or 塗り済み
    matrix[r][c] = "0"
    dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)    # 上下左右のみ(斜めなし)
```
- **最重要**: 範囲チェックを `matrix[r][c]` 参照より**先に**書く。逆だと負のインデックスがPythonでは末尾要素を指してバグになる。
- 空の行列 `[]` は外側のループが回らないので、そのまま `0`。
- 斜めには進まない(4方向のみ)。斜めだけで接するセルは別の島。
- 要素は文字列 `"1"`/`"0"`。`== 1` と比べると常に偽になるので注意。

### 覚えるトレース
```
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
(0,0)で1つ目(左上2x2) → (2,2)で2つ目(単独) → (3,3)で3つ目((3,4)含む) → **合計3**

---

## 5. py_schedule_meetings (level2)

**暗記ポイント**: 1) **開始時刻でソート** 2) 順に見て「最後の会議の終了時刻 ≤ この会議の開始時刻」になる**最初の部屋**に入れる 3) どこにも入らなければ新しい部屋を作る。

### 型
```python
for room in rooms:
    if room[-1][1] <= start:     # 終了==開始は重ならない扱い(★ <= )
        room.append(meeting); assigned = True; break
if not assigned:
    rooms.append([meeting])
```
- **最重要**: 比較は `<=`。会議 `(5,10)` と `(10,15)` は同じ部屋に入れてよい。
- ソートは安定でないといけない(開始時刻が同じ会議は入力順を保つ)。挿入ソートは安定。
- 元の入力リストは変更しない(コピーしてからソート)。
- 空入力は `(0, [])`。

### 覚えるトレース: `[(0,30), (5,10), (15,20)]`
- (0,30) → 部屋なし → 新規: `[[(0,30)]]`
- (5,10) → 部屋1終了30>5 → 新規: `[[(0,30)],[(5,10)]]`
- (15,20) → 部屋1:30>15✗、部屋2:10≤15✓ → `[[(0,30)],[(5,10),(15,20)]]`
- 結果: `(2, [[(0,30)], [(5,10),(15,20)]])`

### 落とし穴
- 「どの部屋に入れるか」は仕様の一部。「最初に空いている部屋」を選ぶ順序も採点対象。

---

## 6. py_prism_detector (level3)

**暗記ポイント**: グリッドの**全セルを起点**に、**8方向すべて**へパターンの長さ分だけ文字を比較。全部一致したら `(x, y, 方向コード)` を記録。

### 方向の定義(そのまま暗記する)
```python
DIRECTIONS = [(1,0,"H"), (-1,0,"H-"), (0,1,"V"), (0,-1,"V-"),
              (1,1,"D1"), (-1,-1,"D1-"), (-1,1,"D2"), (1,-1,"D2-")]
```
- `(dx, dy)`: **dx=列(x)方向、dy=行(y)方向**の増分。
- `V` は下向き `(0,1)`(yは下に向かって増える)。
- **最重要**: `D2` は問題文の説明では「右上」だが、ベクトル `(-1,1)` を実際に使うと進むのは左下。説明と実際の向きが食い違っていても、**表のベクトルとコードをそのまま写す**(向きの説明に合わせて直してはいけない)。

### 型
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
- 出力の `x` は列、`y` は行。アクセスは `grid[y][x]`(行列の `[row][col]` と順序が逆に見える点に注意)。
- 走査順(y→x→方向リストの順)がそのまま出力順になる。

### 覚えるトレース: `["CAT","A..","T.."]`, パターン`"CAT"`
起点(0,0)=`C` → H(右):C,A,T✓ / V(下):C,A,T✓ → 結果 `[(0,0,"H"), (0,0,"V")]`

### 落とし穴
- 1文字パターンは全方向が同じセルで一致するので8個出る(仕様どおり)。
- `cols = len(grid[0])` は全行が同じ長さである前提。

---

## 7. py_word_ladder (level3)

**暗記ポイント**: 「単語=ノード、1文字だけ違う単語同士=辺」のグラフで最短経路を求める → 重みなし最短経路は**BFS**。

### 型
```python
if end not in sentence: return 0          # 到達不能な終点は即座に0

visited = {start: True}
queue = [(start, 1)]                       # (単語, ここまでの語数)
for word, length in queue:                 # ★ループ中にappendした要素も順に回ってくる
    if word == end: return length
    for cand in sentence:
        if cand in visited: continue
        diff = 0
        for i in range(len(word)):         # 違う文字の数を最後まで数える
            if word[i] != cand[i]:
                diff += 1
        if diff == 1:
            visited[cand] = True           # ★キューに入れる時点でvisited更新
            queue.append((cand, length + 1))
return 0
```
- **最重要**: 先頭の `if end not in sentence: return 0` は消さない。消すと `start == end` で `end` が `sentence` にないときに `1` を返してしまう。
- **最重要**: 長さは「語数」(startとendを含む)なので初期値は1。
- **最重要**: `visited` は**キューに入れる時**に更新する。取り出す時に更新すると同じ単語が何度も入ってしまう。
- `diff == 1` のみ遷移可(同一単語=diff0は遷移にならない)。

### 覚えるトレース: `hit → cog`
`hit(1) → hot(2) → dot(3), lot(3) → dog(4), log(4) → cog(5)` → 結果 **5**
(例2: `cog` が `sentence` にない → 即 `0`)

### 落とし穴
- `start` は `sentence` に含まれなくてもよい。
- 全単語が同じ長さである前提で `word[i]`/`cand[i]` のインデックス比較をしている(長さが違う単語が混ざると `IndexError` になりうる)。

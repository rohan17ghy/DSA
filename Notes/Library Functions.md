## 1. Core Collection Data Types

Python has four built-in collection types with distinct characteristics:

|Collection|Ordered|Changeable|Duplicates|Notes|
|:--|:--|:--|:--|:--|
|**List**|Yes|Yes|Yes|General purpose dynamic array.|
|**Tuple**|Yes|No|Yes|Immutable sequence.|
|**Set**|No|No*|No|Stores ==unique values==; unindexed.|
|**Dictionary**|Yes**|Yes|No|Key-value pairs; no duplicate keys.|

_*Sets are unchangeable but you can add/remove items. **Dictionaries are ordered as of Python 3.7+._

---

## 2. Lists & Iterables

### Basic Operations

- ==String.IsNullOrEmpty()== equivalent: `if not my_string:`.
- **Copying**: `arr.copy()` creates a shallow copy.
- **Removing Elements**:
    - `arr.remove(val)`: Removes the ==first occurrence== of `val`.
    - `arr.pop(index)`: Removes and returns element at `index` (default last).
- **Utility Functions**: `sum(arr)`, `max(arr)`, `arr.index(val)`, `arr.reverse()`.

### itertools.groupby()

Groups ==consecutive== elements based on a key.

```
import itertools
nums =
# Groups: 1:, 2:, 3:, 2:
for key, group in itertools.groupby(nums):
    print(key, list(group))
```

> **Pro Tip**: To group _all_ occurrences of a value regardless of position, you must ==sort the list first==.

---

## 3. Strings

### Key Methods & Comparisons

- **Reversing**: `s[::-1]`.
- **Case**: `s.swapcase()`, `s.isupper()`, `s.islower()`.
- **Checks**: `s.isalnum()`, `s.isalpha()`, `s.isnumeric()`.
- **Trimming**: `s.strip()`, `s.lstrip()`, `s.rstrip()` (removes specific characters from ends).
- **Comparison**:
    - `==` compares ==values==.
    - `is` compares ==memory identity== (id).
    - ==String Pool==: Small strings with the same value often share the same `id()` to save memory.

### Complexity Note

Comparing two dictionaries where keys are characters is ==O(26) (constant time)== rather than O(n), which is useful for frequency-based string problems.

---

## 4. Sets & Tuples

### Sets

- `a.add(val)`: Adds an element.
- `a.discard(val)`: Removes element; ==does NOT raise error== if missing.
- `a.remove(val)`: Removes element; ==raises KeyError== if missing.

### Tuples

- Accessed by index: `a`.
- Attempting to change a value results in a `TypeError`.

---

## 5. Sorting & Mapping

### map(function, iterable)

Applies a function to every item in an iterable.

```
numbers = (1, 2, 3)
result = map(lambda x: x * 2, numbers) #
```

### Advanced Sorting

- **Stability**: Python uses ==Timsort==, which is **stable** (preserves relative order of elements with equal keys).
- **Key-based Sorting**:
    
    ```
    # Sort 2D list: 2nd element DESC, then 1st element DESC
    tasks = [,,,,]
    tasks.sort(key=lambda x: (-x, -x))
    ```
    
- **Custom Comparator**: Use `functools.cmp_to_key` for complex logic.

---

## 6. Heaps (Priority Queues)

Python's `heapq` module implements a ==Min-Heap==.

### Common Operations

- `heapq.heapify(list)`: Transforms list into a heap in-place (O(N)).
- `heapq.heappush(heap, item)`: Adds item (O(log N)).
- `heapq.heappop(heap)`: Removes smallest item (O(log N)).
- `heapq.heappushpop()`: Push then pop; more efficient than separate calls.
- `heapq.heapreplace()`: Pop then push.

### Heap with Tuples

When storing tuples, the heap sorts by the ==first element==, then the second, and so on.

```
# Useful for priority queues with tie-breakers
minHeap = []
heapq.heappush(minHeap, (priority, task_id))
```

---

## 7. Advanced Collections

### collections.deque

A double-ended queue providing ==O(1) appends and pops== from both ends.

- Methods: `append()`, `appendleft()`, `pop()`, `popleft()`, `extend()`, `extendleft()`.

### collections.Counter

A dictionary subclass for counting hashable objects.

- Missing keys return ==0== instead of an error.
- Supports math operations: `+`, `-`, and logical comparisons `>`, `==`.
- `c.most_common(n)`: Returns the `n` most frequent elements.
- **Dictionaries/Counters** use `del` (raises error) and `pop` (silent if a default is provided).

### collections.defaultdict

Automatically initializes a value for a missing key using a ==factory function== (e.g., `int`, `list`).
Counter acts like a defaultdict i.e. if key doesn't exist than it returns 0

### sortedcontainers (External Library)

- **SortedList**: Maintains sorted order during insertion. Supports `bisect_left`/`right` and `pop(index)`.
- **SortedDict**: Maintains sorted order of keys.

---

## 8. Logic & Binary

### Binary Operations

- `val.bit_count()`: Returns the number of ==set bits== (1s) in the binary representation.

### Bisect Module

Binary search for sorted lists:

- `bisect_left(arr, x)`: Index to insert `x` while maintaining order; if `x` exists, insert to the ==left==.
- `bisect_right(arr, x)`: Same, but insert to the ==right==.

### Comparison Dunder Methods

To make custom objects comparable, implement:

- `__lt__`: Less than (`<`)
- `__gt__`: Greater than (`>`)
- `__eq__`: Equality (`==`). Note: default `__eq__` checks ==object identity== (memory address).

---

## 9. Math & Miscellaneous

### Negative Division Fix

Python's `//` operator performs floor division, which can be unintuitive with negative numbers (e.g., `6 // -132` is `-1`). **Corrected Logic for Truncated Division (like C++/Java)**:

```python
def truncated_div(a, b):
    sign = -1 if (a < 0) ^ (b < 0) else 1
    return sign * (abs(a) // abs(b))
```

### Regular Expressions (`re`)

- `re.findall(pattern, string)`: Returns all non-overlapping matches.
- Example: `re.findall("[+-]?\d+", "19/4-6/4")` extracts numbers with signs.

### Enumerator

- `enumerate(iterable)`: Returns pairs of `(index, element)`.
- Can be manually iterated using `next(enmtr)`.

---

## Visual Summary: Memory & Comparison

```
graph TD
    A[Object Comparison] --> B{== Operator}
    B --> C[Checks Value Equality]
    A --> D{is Operator}
    D --> E[Checks Memory ID]

    subgraph Strings
    F[String Pool] --> G[Identical literals share same ID]
    end
```

---

## Additional Reference: Complexity Table

| Operation       | List     | Deque    | SortedList |
| :-------------- | :------- | :------- | :--------- |
| Append          | O(1)*    | O(1)     | O(log N)   |
| Pop Left        | ==O(N)== | ==O(1)== | O(log N)   |
| Pop Right       | O(1)     | O(1)     | O(log N)   |
| Access by Index | O(1)     | O(N)     | O(log N)   |


\*Average case amortized O(1).
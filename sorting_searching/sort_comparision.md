# **Sorting Algorithms Comparison Table**

## **Overview Comparison**

| Feature | **Insertion Sort** | **Quick Sort** | **Merge Sort** | **Heap Sort** |
|---------|-------------------|----------------|----------------|---------------|
| **Best Case** | O(n) | O(n log n) | O(n log n) | O(n log n) |
| **Average Case** | O(n²) | O(n log n) | O(n log n) | O(n log n) |
| **Worst Case** | O(n²) | **O(n²)** ⚠️ | O(n log n) | O(n log n) |
| **Space Complexity** | O(1) | O(log n) | **O(n)** | O(1) |
| **Stable?** | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| **In-Place?** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Adaptive?** | ✅ Yes | ❌ No | ❌ No | ❌ No |

---

## **Detailed Comparison**

| Aspect | **Insertion Sort** | **Quick Sort** | **Merge Sort** | **Heap Sort** |
|--------|-------------------|----------------|----------------|---------------|
| **Algorithm Type** | Simple comparison | Divide & conquer | Divide & conquer | Comparison + heap |
| **How it works** | Build sorted array one element at a time | Pick pivot, partition, recurse | Split in half, sort, merge | Build heap, extract max repeatedly |
| **Recursion** | No (iterative) | Yes | Yes | No (can be iterative) |
| **Cache Performance** | ⭐⭐⭐ Excellent | ⭐⭐⭐ Excellent | ⭐⭐ Good | ⭐ Poor (random access) |
| **Practical Speed** | Slow for large n | **Fastest** for most data | Good, predictable | Slower than Quick/Merge |
| **Predictability** | Varies (O(n) to O(n²)) | Varies (O(n log n) to O(n²)) | **Always O(n log n)** ✅ | **Always O(n log n)** ✅ |

---

## **Strengths & Weaknesses**

| Algorithm | **Strengths** ✅ | **Weaknesses** ❌ |
|-----------|------------------|-------------------|
| **Insertion Sort** | • Simple to implement<br>• Fast for small arrays (n < 10)<br>• O(n) when nearly sorted<br>• Stable<br>• In-place<br>• Adaptive | • O(n²) for large arrays<br>• Very slow for random data<br>• Not practical for big datasets |
| **Quick Sort** | • **Fastest average case**<br>• In-place (low memory)<br>• Good cache locality<br>• Widely used in practice | • **O(n²) worst case**<br>• Unstable<br>• Not adaptive<br>• Bad for already sorted data<br>• Poor pivot = poor performance |
| **Merge Sort** | • **Guaranteed O(n log n)**<br>• Stable<br>• Predictable performance<br>• Great for linked lists<br>• Good for external sorting | • Requires O(n) extra space<br>• Not in-place<br>• Slower than Quick Sort in practice<br>• Not adaptive |
| **Heap Sort** | • **Guaranteed O(n log n)**<br>• In-place (O(1) space)<br>• No worst case like Quick Sort<br>• No recursion needed | • Unstable<br>• Poor cache performance<br>• Slower than Quick/Merge in practice<br>• Not adaptive<br>• Complex to implement |

---

## **Performance on Different Data**

| Data Pattern | **Insertion** | **Quick Sort** | **Merge Sort** | **Heap Sort** |
|--------------|---------------|----------------|----------------|---------------|
| **Random data** | O(n²) 🐌 | **O(n log n)** 🚀 | O(n log n) ⚡ | O(n log n) ⚡ |
| **Already sorted** | **O(n)** 🚀 | O(n²) 🐌 | O(n log n) ⚡ | O(n log n) ⚡ |
| **Reverse sorted** | O(n²) 🐌 | O(n²) 🐌 | O(n log n) ⚡ | O(n log n) ⚡ |
| **Nearly sorted** | **O(n)** 🚀 | O(n log n) ⚡ | O(n log n) ⚡ | O(n log n) ⚡ |
| **Many duplicates** | O(n²) 🐌 | O(n²) 🐌 | O(n log n) ⚡ | O(n log n) ⚡ |
| **Small arrays (n<20)** | **Fastest** 🚀 | Slower ⚡ | Slower ⚡ | Slower ⚡ |

---

## **Use Cases**

| Scenario | **Best Choice** | **Why?** |
|----------|----------------|----------|
| **Small arrays (< 10-20 elements)** | **Insertion Sort** | Simplest, lowest overhead |
| **General-purpose sorting** | **Quick Sort** | Fastest average case, widely used |
| **Need guaranteed O(n log n)** | **Merge Sort** or **Heap Sort** | No worst-case O(n²) |
| **Need stable sort** | **Merge Sort** | Only stable O(n log n) option here |
| **Limited memory (in-place required)** | **Quick Sort** or **Heap Sort** | Both O(1) or O(log n) space |
| **Nearly sorted data** | **Insertion Sort** | O(n) when adaptive kicks in |
| **Linked lists** | **Merge Sort** | Can be done with O(1) space |
| **External sorting (disk)** | **Merge Sort** | Sequential access pattern |
| **Need worst-case guarantee + in-place** | **Heap Sort** | O(n log n) + O(1) space |

---

## **Real-World Usage**

| Language/System | **Algorithm Used** |
|-----------------|-------------------|
| **C++ std::sort** | Introsort (Quick + Heap + Insertion) |
| **Python sorted()** | Timsort (Merge + Insertion) |
| **Java Arrays.sort()** | Dual-Pivot Quick Sort (primitives)<br>Timsort (objects) |
| **JavaScript Array.sort()** | Timsort (V8 engine) |
| **Go sort.Sort()** | pdqsort (Pattern-defeating Quick Sort) |
| **Rust sort()** | Timsort or pdqsort |

**Key insight:** Modern languages use **hybrid algorithms** that combine the best features! 🎯

---

## **Visual Summary**

```
Speed (average case):
Quick Sort > Merge Sort > Heap Sort >> Insertion Sort

Memory efficiency:
Insertion/Heap Sort > Quick Sort >> Merge Sort

Reliability (worst case):
Merge/Heap Sort > Quick Sort >> Insertion Sort

Simplicity:
Insertion Sort >> Heap Sort > Quick Sort ≈ Merge Sort

Stability:
Insertion Sort ✅  Merge Sort ✅  Quick Sort ❌  Heap Sort ❌
```

---

## **The Winner? It Depends!**

- 🥇 **Overall champion:** Quick Sort (with optimizations)
- 🥈 **Most reliable:** Merge Sort (guaranteed performance + stable)
- 🥉 **Best space efficiency:** Heap Sort (in-place + guaranteed)
- 🏅 **Best for small data:** Insertion Sort (simplest + fastest for tiny arrays)

**In practice:** Use **hybrid algorithms** like Introsort or Timsort that combine multiple approaches! 🚀
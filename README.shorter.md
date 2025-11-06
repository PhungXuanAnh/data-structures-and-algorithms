# Array

## Sort
* [Compare sort algorithms](sorting_searching/sort_comparision.md)
* [Insertion sort]()
* [Quick sort](https://colab.research.google.com/github/PhungXuanAnh/data-structures-and-algorithms/blob/master/sorting_searching/quick_sort/quick_sort_solution.ipynb)
* [Merge sort](https://colab.research.google.com/github/PhungXuanAnh/data-structures-and-algorithms/blob/master/sorting_searching/merge_sort/merge_sort_solution.ipynb)

## Hybrid sort

Real-world note: Most modern programming languages use hybrid algorithms like:

- **C++:** Introsort (Quick + Heap + Insertion)
- **Python/Java:** Timsort (Insertion + Merge)
- **Go:** pdqsort (Pattern-defeating Quick Sort with Insertion + Heap)
- **Rust:** pdqsort or Timsort depending on type

**So Which Hybrid is "Best"?** It depends on your priorities:

| Priority | Best Hybrid | Why |
|----------|-------------|-----|
| **Minimize memory** | Introsort (Quick+Heap+Insertion) | All in-place |
| **Stability needed** | Timsort (Insertion+Merge) | Merge Sort is stable |
| **General arrays** | Introsort | Fastest in practice |
| **Real-world data** | Timsort | Exploits patterns |
| **Parallel processing** | Quick+Parallel Merge | Utilizes multiple cores |

* [Introsort (Quick+Heap+Insertion)]()
* [Timsort (Insertion+Merge)]()

## Search
* [Linear search]()
* [Binary search]()

# Linked List

* [Implement linked list]()

# Stack

* [Implement stack]()

# Queue

* [Implement queue]()

# Hash table

* []()

# Trees

* [Implement tree]()
* [Implement binary tree]()
* [Binary Search Trees]()
* []()

# Graph

* []()
* [Shortest path]()
* [Shortest path: Dijkstra's Algorithm]()
* [Shortest path: Bellman-Ford Algorithm]()


# Reference:

* [5 steps to approach an DA question in a interview](https://www.hiredintech.com/algorithms/algorithm-design-canvas/what-is-the-canvas/)
* [origin repostory](https://github.com/donnemartin/interactive-coding-challenges?tab=readme-ov-file)
* [This repository contains many good things/documents](https://github.com/jwasham/coding-interview-university)
* [system design](https://github.com/donnemartin/system-design-primer)
* [design pattern](https://github.com/PhungXuanAnh/python-patterns)
* https://www.w3schools.com/dsa

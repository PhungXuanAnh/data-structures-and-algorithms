# -*- coding: utf-8 -*-
"""
    Quick sort

    Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element 
    and partitioning the array around it such that: Left side of pivot contains all the elements that are less than the pivot
    element Right side contains all elements greater than the pivot.

    Ý tưởng:
    1. chọn 1 giá trị làm chốt (thường là điểm đầu hoặc cuối của list cho dễ duyệt)
    2. duyệt list không tính phần tử chốt, chuyển số lớn hơn chốt sang trái, nhỏ hơn chốt sang phải
    3. chuyển xong thì đưa chốt vào giữa, ta được 2 list bên phải và bên trái chốt,lúc này chốt cố
định vị trí
    4. tiếp tục các bước trên với 2 list con và làm tiếp đến khi nào 2 list chỉ còn 1 phần tử là xong

    Ví dụ cho ý tưởng trên:
    1. danh sách: 3, 1, 2, chọn 2 làm chốt
    2. duyệt danh sách ta thấy 3 > 2 và 1 < 2 ==> di chuyển 3 sang phải, di chuyển 1 sang trái,
       tức là đổi vị trí 2 sô, lúc này ta được danh sách là 1, 3, 2
    3. đưa 2 vào giữa ta được danh sách 1, 2, 3
    4. 2 list con không kể chốt là: 1 và 3. Chỉ còn 1 phần tử, lúc này ta đã sắp xếp xong.
    
"""


def partition(alist, left, right):
    'Bước 1: Chọn phần tử chốt là phần tử có chỉ mục cao nhất(phần tử ở cuối danh sách)'
    pivot = alist[right]

    'Bước 2: Khai báo hai biến để trỏ tới bên trái và bên phải của danh sách, ngoại trừ phần tử chốt'
    left_p = left
    right_p = right - 1

    'Bước 3: Bắt đầu duyệt danh sách'
    while True:

        '''
        Bước 4: Duyệt từ bên trái
                Khi giá trị tại biến bên trái là nhỏ hơn phần tử chốt
                Hoặc con trỏ bên trái nhỏ hơn con trỏ bên phải 
                Thì di chuyển sang phải
        '''
        while left_p <= right_p and alist[left_p] <= pivot:
            left_p = left_p + 1

        '''
        Bước 5: Duyệt từ bên phải
                Khi giá trị biến bên phải lớn hơn phần tử chốt
                Hoặc con trỏ bên phải lớn hơn con trỏ bên trái
                Thì di chuyển sang trái
        '''
        while right_p >= left_p and alist[right_p] >= pivot:
            right_p = right_p - 1

        '''
        Bước 6.1: Khi không thỏa mãn bước 4, bước 5, thì
                  Nếu con trỏ bên trái lớn hơn hoặc bằng con trỏ bên trái,
                  Nghĩa là ta đã duyệt xong các giá trị. Thoát vòng lặp
        '''
        if left_p >= right_p:
            break

            '''
            Bước 6.2: Nếu không thì ta đã tìm được 2 giá trị thỏa mãn như sau:
                    Giá trị bên trái lớn hơn phần tử chốt
                    Giá trị bên phải nhỏ hơn phần tử chốt
                    Tráo đổi 2 giá trị này và tiếp tục duyệt 
            '''
        else:
            alist[left_p], alist[right_p] = alist[right_p], alist[left_p]

    '''
    Bước 7: Khi đã duyệt xong danh sách
            Tráo đổi vị trí con trỏ trái với vị trí phần tử chốt
            Lúc này phần tử chốt đã có vị trí cố định
            Đồng thời vị trí này chia danh sách làm 2 phần
            Trả về vị trí này để xác định 2 danh sách con cho bước đệ qui tiếp theo
    '''
    alist[left_p], alist[right] = alist[right], alist[left_p]

    return left_p


def quick_sort_helper(alist, left, right):
    '''
    Bước 1: Nếu con trỏ bên trái lớn hơn hoặc bằng bên phải
            Nghĩa là lúc này dãy chỉ còn 1 phần tử, đã được sắp xếp
            Thoát quá trình đệ quy
    '''
    if left >= right:
        return

    '''
    Bước 2: Nếu không thì tiếp tục chọn phần tử chốt và
            chuyển các phần tử lớn hơn chốt sang phải,
            chuyển các phần tử nhỏ hơn chốt sang trái
    '''
    split_point = partition(alist, left, right)

    '''
    Bước 3: Dùng phần tử chốt, chia danh sách làm 2 phần không chứa phần tử chốt 
            Tiếp tục sắp xếp đệ qui 2 danh sách này
    '''
    quick_sort_helper(alist, left, split_point - 1)
    quick_sort_helper(alist, split_point + 1, right)


def quickSort(alist):
    '''
    Giải thuật quick sort cần đầu vào là danh sách, và điểm đầu và điểm cuối danh sách
    '''
    quick_sort_helper(alist, 0, len(alist) - 1)


if __name__ == '__main__':
    alist = [3, 4, 2, 1, 8, 6, 9, 0, 5, 7]
    quickSort(alist)
    print(alist)

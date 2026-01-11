class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node: return 0
        return node.height

    def get_balance(self, node):
        if not node: return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # --- HÀM XOAY PHẢI (Right Rotation) ---
    # Áp dụng quy tắc: "Con ngoài giữ nguyên, Con giữa đổi cha"
    def right_rotate(self, old_parent):
        print(f"   [Xoay Phải] tại nút {old_parent.key}")
        
        new_parent = old_parent.left      # Con trái lên làm cha mới
        middle_child = new_parent.right   # Nhánh phải của con trái (Con Giữa)

        # Thực hiện xoay
        new_parent.right = old_parent     # Cha cũ xuống làm con phải của cha mới
        old_parent.left = middle_child    # Con giữa đổi sang làm con trái của cha cũ

        # Cập nhật chiều cao (Cập nhật old_parent trước vì nó thấp hơn)
        old_parent.height = 1 + max(self.get_height(old_parent.left), self.get_height(old_parent.right))
        new_parent.height = 1 + max(self.get_height(new_parent.left), self.get_height(new_parent.right))

        return new_parent

    # --- HÀM XOAY TRÁI (Left Rotation) ---
    def left_rotate(self, old_parent):
        print(f"   [Xoay Trái] tại nút {old_parent.key}")

        new_parent = old_parent.right     # Con phải lên làm cha mới
        middle_child = new_parent.left    # Nhánh trái của con phải (Con Giữa)

        # Thực hiện xoay
        new_parent.left = old_parent      # Cha cũ xuống làm con trái của cha mới
        old_parent.right = middle_child   # Con giữa đổi sang làm con phải của cha cũ

        # Cập nhật chiều cao
        old_parent.height = 1 + max(self.get_height(old_parent.left), self.get_height(old_parent.right))
        new_parent.height = 1 + max(self.get_height(new_parent.left), self.get_height(new_parent.right))

        return new_parent

    # --- HÀM INSERT ---
    # Đổi tên 'root' thành 'node' cho chuẩn ngữ nghĩa (nút hiện tại đang xét)
    def insert(self, node, key):
        # 1. Chèn bình thường (BST Insert)
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Cập nhật chiều cao
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. Tính hệ số cân bằng
        balance = self.get_balance(node)

        # 4. Xử lý 4 trường hợp mất cân bằng
        # Ta nhóm lại: Kiểm tra Lệch Trái trước, rồi đến Lệch Phải
        
        # === NHÓM LỆCH TRÁI (LEFT HEAVY) ===
        if balance > 1:
            # Case 1: Left - Left (Lệch Trái - Trái)
            # Mô tả: Nút mới (10) nằm bên TRÁI của con trái (20)
            #
            #       30 (Mất CB)           20
            #      /                     /  \
            #    20      ====>         10    30
            #   /
            # 10
            if key < node.left.key:
                return self.right_rotate(node)

            # Case 2: Left - Right (Lệch Trái - Phải)
            # Mô tả: Nút mới (20) nằm bên PHẢI của con trái (10)
            #
            #       30 (Mất CB)           30                20
            #      /                     /                /    \
            #    10      ====>         20     ====>     10      30
            #      \                  /
            #       20              10
            #    (Xoay Trái 10)      (Xoay Phải 30)
            if key > node.left.key:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        # === NHÓM LỆCH PHẢI (RIGHT HEAVY) ===
        if balance < -1:
            # Case 3: Right - Right (Lệch Phải - Phải)
            # Mô tả: Nút mới (30) nằm bên PHẢI của con phải (20)
            #
            #    10 (Mất CB)              20
            #      \                     /  \
            #       20     ====>       10    30
            #         \
            #          30
            if key > node.right.key:
                return self.left_rotate(node)

            # Case 4: Right - Left (Lệch Phải - Trái) -> (Trường hợp bạn hỏi ban đầu)
            # Mô tả: Nút mới (20) nằm bên TRÁI của con phải (30)
            #
            #    10 (Mất CB)              10                 20
            #      \                        \              /    \
            #       30     ====>             20   ====>  10      30
            #      /                           \
            #    20                             30
            #    (Xoay Phải 30)            (Xoay Trái 10)
            if key < node.right.key:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node
    
    # =================================== delete node ===================================
    # --- HELPER: Tìm node có giá trị nhỏ nhất (dùng cho thế mạng) ---
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --- HÀM XÓA (DELETE) ---
    def delete(self, node, key):
        # BƯỚC 1: Xóa theo quy tắc BST chuẩn
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Tìm thấy node cần xóa!
            
            # Trường hợp 1 & 2: Node có 1 con hoặc không có con
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Trường hợp 3: Node có 2 con
            # Tìm node thế mạng (nhỏ nhất bên nhánh phải - Successor)
            temp = self.get_min_value_node(node.right)
            
            # Copy giá trị của node thế mạng vào node hiện tại
            node.key = temp.key
            
            # Xóa node thế mạng cũ đi
            node.right = self.delete(node.right, temp.key)

        # Nếu cây chỉ có 1 node và vừa bị xóa thì trả về None
        if node is None:
            return node

        # BƯỚC 2: Cập nhật chiều cao nút hiện tại
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # BƯỚC 3: Kiểm tra cân bằng
        balance = self.get_balance(node)

        # BƯỚC 4: Xử lý 4 trường hợp mất cân bằng
        # Lưu ý: Logic phát hiện Case ở đây khác với Insert một chút.
        # Ta dựa vào Balance Factor của node CON thay vì so sánh key.

        # Case 1: Left Heavy (Lệch Trái)
        if balance > 1:
            # Kiểm tra con trái xem nó lệch đường nào?
            # get_balance(node.left) >= 0: Nghĩa là nhánh trái của con trái nặng hơn hoặc bằng
            # -> Trường hợp Left-Left
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            # get_balance(node.left) < 0: Nghĩa là nhánh phải của con trái nặng hơn
            # -> Trường hợp Left-Right
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        # Case 2: Right Heavy (Lệch Phải)
        if balance < -1:
            # Kiểm tra con phải xem nó lệch đường nào?
            # get_balance(node.right) <= 0: Nghĩa là nhánh phải của con phải nặng hơn hoặc bằng
            # -> Trường hợp Right-Right
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            # get_balance(node.right) > 0: Nghĩa là nhánh trái của con phải nặng hơn
            # -> Trường hợp Right-Left
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

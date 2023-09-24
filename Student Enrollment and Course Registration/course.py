import datetime

class AVLNode:
    def __init__(self, course_code,start_time, end_time,enrolled_students=None):
        self.course_code = course_code
        self.enrolled_students = enrolled_students or []
        self.start_time=start_time
        self.end_time=end_time
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
        self.conflicting_courses={}
        

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def insert(self, course_code,  start_time,end_time):
        self.root = self._insert(self.root, course_code, start_time,end_time)
        self.conflicting_courses[course_code]=[]

        for course_id in self.conflicting_courses.keys():
            if course_id == course_code:
                continue
            course=self.search(course_id)
            if (course.start_time<= start_time and start_time<=course.end_time) or (course.start_time<= end_time and start_time<=course.end_time):
                self.conflicting_courses[course_id].append(course_code)  
                self.conflicting_courses[course_code].append(course_id)         


    def _insert(self, node, course_code,start_time,end_time):
        if node is None:
            return AVLNode(course_code,start_time, end_time )

        if course_code < node.course_code:
            node.left = self._insert(node.left, course_code, start_time,end_time)
        elif course_code > node.course_code:
            node.right = self._insert(node.right, course_code, start_time,end_time)
        else:
            # Course with the same code already exists, handle it as needed.
            return node

                    

        self._update_height(node)

        balance = self._balance_factor(node)

        # Left Heavy
        if balance > 1:
            if course_code < node.left.course_code:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # Right Heavy
        if balance < -1:
            if course_code > node.right.course_code:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def delete(self, course_code):
        self.root = self._delete(self.root, course_code)

    def _delete(self, node, course_code):
        if node is None:
            return node

        if course_code < node.course_code:
            node.left = self._delete(node.left, course_code)
        elif course_code > node.course_code:
            node.right = self._delete(node.right, course_code)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.course_code = temp.course_code
            node.right = self._delete(node.right, temp.course_code)

        self._update_height(node)

        balance = self._balance_factor(node)

        # Left Heavy
        if balance > 1:
            if self._balance_factor(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # Right Heavy
        if balance < -1:
            if self._balance_factor(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, course_code):
        return self._search(self.root, course_code)

    def _search(self, node, course_code):
        if node is None or node.course_code == course_code:
            return node
        if node.course_code < course_code:
            return self._search(node.right, course_code)
        return self._search(node.left, course_code)
    

    #Code to generate Student roster 
    def print_roster(self,course_code):
        roster=self.search(course_code)
        print("------ROSTER-------")   
        print(f"Course Code: {roster.course_code}")
        print(f"Start Time: {roster.start_time}")
        print(f"End Time: {roster.end_time}")
        print("Enrolled Students:", roster.enrolled_students)
        print("-------------------",end="\n\n")   

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            # result.append([node.course_code, node.start_time,node.end_time,node.enrolled_students])
            print(f"Course Code: {node.course_code}")
            print(f"Start Time: {node.start_time}")
            print(f"End Time: {node.end_time}")
            print("Enrolled Students:", node.enrolled_students)
            print("Height:", node.height)
            print("-------------------",end="\n\n")            
            self._inorder_traversal(node.right, result)
            

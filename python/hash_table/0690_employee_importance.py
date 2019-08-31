# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, _id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        es = {}
        for emp in employees:
            es[emp.id] = (emp.importance, emp.subordinates,)
        stack = [es[_id]]
        importance = 0
        while stack:
            imp, subordinates = stack.pop()
            importance += imp
            for sid in subordinates:
                stack.append(es[sid])
        return importance


def test_get_importance():
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])

    assert 11 == Solution().getImportance([e1, e2, e3], 1)

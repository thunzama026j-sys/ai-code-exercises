import unittest
from datetime import datetime, timedelta
from use_cases.code_comprehension_001.python.TaskManager.models import Task, TaskPriority, TaskStatus

class TestTaskModel(unittest.TestCase):

    def test_task_priority_enum(self):
        self.assertEqual(TaskPriority.LOW.name, 'LOW')
        self.assertEqual(TaskPriority.MEDIUM.name, 'MEDIUM')
        self.assertEqual(TaskPriority.HIGH.name, 'HIGH')

    def test_task_status_enum(self):
        self.assertEqual(TaskStatus.PENDING.name, 'PENDING')
        self.assertEqual(TaskStatus.IN_PROGRESS.name, 'IN_PROGRESS')
        self.assertEqual(TaskStatus.COMPLETED.name, 'COMPLETED')

    def test_task_initialization(self):
        task = Task(name='Test Task', priority=TaskPriority.LOW, status=TaskStatus.PENDING, due_date=datetime(2026, 5, 1))
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.priority, TaskPriority.LOW)
        self.assertEqual(task.status, TaskStatus.PENDING)
        self.assertEqual(task.due_date, datetime(2026, 5, 1))

    def test_task_update_method(self):
        task = Task(name='Test Task', priority=TaskPriority.LOW, status=TaskStatus.PENDING, due_date=datetime(2026, 5, 1))
        task.update(name='Updated Task', priority=TaskPriority.HIGH, status=TaskStatus.IN_PROGRESS)
        self.assertEqual(task.name, 'Updated Task')
        self.assertEqual(task.priority, TaskPriority.HIGH)
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)

    def test_mark_as_done_method(self):
        task = Task(name='Test Task', priority=TaskPriority.LOW, status=TaskStatus.PENDING, due_date=datetime(2026, 5, 1))
        task.mark_as_done()
        self.assertEqual(task.status, TaskStatus.COMPLETED)

    def test_is_overdue_method(self):
        task = Task(name='Overdue Task', priority=TaskPriority.LOW, status=TaskStatus.PENDING, due_date=datetime(2026, 4, 1))
        self.assertTrue(task.is_overdue())
        task.due_date = datetime(2026, 5, 1)
        self.assertFalse(task.is_overdue())

if __name__ == '__main__':
    unittest.main()
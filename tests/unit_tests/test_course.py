from django.test import TestCase

from Scheduler.models import Course


class CourseCreationTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            courseID='CS361',
            name='Introduction to Software Engineering',
            semester='F',
            year=2022
        )
        self.assertEqual(course.courseID, 'CS361')
        self.assertEqual(course.name, 'Introduction to Software Engineering')
        self.assertEqual(course.semester, 'F')
        self.assertEqual(course.year, 2022)


class CourseDeletionTests(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            courseID='CS361',
            name='Introduction to Software Engineering',
            semester='F',
            year=2022
        )

    def test_course_deletion_success(self):
        self.course.delete()
        self.assertEqual(Course.objects.count(), 0, msg='Course was not deleted')

    def test_course_deletion_success_by_id(self):
        Course.objects.filter(courseID='CS361').delete()
        self.assertEqual(Course.objects.count(), 0, msg='Course was not deleted')

    def test_course_deletion_failure_by_id(self):
        Course.objects.filter(courseID='CS362').delete()
        self.assertEqual(Course.objects.count(), 1, msg='Course was deleted')


class CourseUpdateTests(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            courseID='CS361',
            name='Introduction to Software Engineering',
            semester='F',
            year=2022
        )

    def test_course_update_success_id(self):
        self.course.courseID = 'CS362'
        self.course.save()
        self.assertEqual(self.course.courseID, 'CS362', msg='Course ID was not updated')

    def test_course_update_success_name(self):
        self.course.name = 'Introduction to Software Engineering II'
        self.course.save()
        self.assertEqual(self.course.name, 'Introduction to Software Engineering II',
                         msg='Course name was not updated')

    def test_course_update_success_semester(self):
        self.course.semester = 'S'
        self.course.save()
        self.assertEqual(self.course.semester, 'S', msg='Course semester was not updated')

    def test_course_update_success_year(self):
        self.course.year = 2023
        self.course.save()
        self.assertEqual(self.course.year, 2023, msg='Course year was not updated')

    def test_course_update_failure_id(self):
        self.course.courseID = ''
        self.course.save()
        self.assertEqual(self.course.courseID, 'CS361', msg='Course ID was updated')
        self.course.courseID = None
        self.course.save()
        self.assertEqual(self.course.courseID, 'CS361', msg='Course ID was updated')

    def test_course_update_failure_name(self):
        self.course.name = ''
        self.course.save()
        self.assertEqual(self.course.name, 'Introduction to Software Engineering',
                         msg='Course name was updated')
        self.course.name = None
        self.course.save()
        self.assertEqual(self.course.name, 'Introduction to Software Engineering',
                         msg='Course name was updated')

    def test_course_update_failure_semester(self):
        self.course.semester = ''
        self.course.save()
        self.assertEqual(self.course.semester, 'F', msg='Course semester was updated')
        self.course.semester = None
        self.course.save()
        self.assertEqual(self.course.semester, 'F', msg='Course semester was updated')

    def test_course_update_failure_year(self):
        self.course.year = ''
        self.course.save()
        self.assertEqual(self.course.year, 2022, msg='Course year was updated')
        self.course.year = None
        self.course.save()
        self.assertEqual(self.course.year, 2022, msg='Course year was updated')

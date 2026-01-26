import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'eduplanners.settings'
import django
django.setup()

from core.models import Semester, ClassSection, SystemConfiguration

print('=== SEMESTERS ===')
for s in Semester.objects.select_related('department').all():
    print(f'  S{s.number} - Dept: {s.department.code}')

print()
print('=== CLASSES (ClassSection) ===')
classes = ClassSection.objects.select_related('semester__department').all()
if classes.exists():
    for c in classes:
        print(f'  {c.name} - S{c.semester.number} ({c.semester.department.code})')
else:
    print('  No classes found!')

print()
print('=== SYSTEM CONFIG ===')
config = SystemConfiguration.objects.first()
if config:
    print(f'  Active Semester Type: {config.active_semester_type}')
    print(f'  Academic Year: {config.academic_year}')
else:
    print('  No config found!')

# Check specifically for ODD semester classes
print()
print('=== CLASSES IN ODD SEMESTERS (1,3,5,7) ===')
odd_classes = ClassSection.objects.filter(semester__number__in=[1, 3, 5, 7])
if odd_classes.exists():
    for c in odd_classes.select_related('semester__department'):
        print(f'  {c.name} - S{c.semester.number} ({c.semester.department.code})')
else:
    print('  No classes in ODD semesters!')

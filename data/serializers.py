from multiprocessing import Event
from rest_framework import serializers

from .models import (
    Department,
    Major,
    Minor,
    Student,
    Professor,
    AdminAssistant,
    Course,
    HighImpactExperience,
    Event
)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = [
            "name"
        ]


class MajorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Major
        fields = [
            "name",
            "subject"
        ]


class MinorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Minor
        fields = [
            "name",
            "subject"
        ]


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    #could be CharField(read_only=True)
    #DOES USER NEED A SERIALIZER WITH username ??
    class Meta:
        model = Student
        fields = [
            "user",
            "major",
            "minor",
            "schoolyear"
        ]


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Professor
        fields = [
            "user",
            "department",
            "degree_desc"
        ]


class AdminAssistantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdminAssistant
        fields = [
            "user",
            "department"
        ]


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = [
            "crn",
            "title",
            "desc_text",
            "course_num",
            "subject",
            "instructor",
            "credit_hours"
        ]


class HighImpactExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HighImpactExperience
        fields = [
            "name",
            "RTX_name",
            "Freshman_desc",
            "Sophomore_desc",
            "Junior_desc",
            "Senior_desc",
            "creation_date"
            # ,
            # "area"
        ]


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = ["__all__"]

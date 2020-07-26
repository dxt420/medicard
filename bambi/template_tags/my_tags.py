from django import template
from  bambi.models import *
register = template.Library()


     

# @register.simple_tag
# def timer(sss):
#     s = float(sss)
#     hours, remainder = divmod(s, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
#     return duration

@register.simple_tag(takes_context=True)
def getDisplayName(context):
    request = context['request']
    name = Agent.objects.get(email=request.user.email)
    return name

# @register.simple_tag
# def getLessonVideoUrl(courseID,chapterID,lessonID):
#     lesson = db.child("chapters").child(courseID).child(chapterID).child("lessons").child(lessonID).get()
#     return lesson.val()["video_url"]

# @register.simple_tag
# def getLessonDuration(courseID,chapterID,lessonID):
#     lesson = db.child("chapters").child(courseID).child(chapterID).child("lessons").child(lessonID).get()
#     s = float(lesson.val()["duration"])
#     hours, remainder = divmod(s, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
#     return duration
   


# @register.simple_tag
# def readableTime(strr):
#     datetime_object = datetime.strptime(strr, '%c')
#     return datetime_object.strftime("%A %B %d %Y  at %I:%M %p")


# @register.simple_tag
# def getAvatar(username):
#     user = UserSocialAuth.objects.get(user=username)
  
#     if user.provider == "google-oauth2":
#         return user.extra_data["picture"]
#     elif user.provider == "facebook":
#         return user.extra_data["picture"].data.url
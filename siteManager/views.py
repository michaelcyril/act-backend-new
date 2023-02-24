from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def PostEventView(request):
    print(request.data)
    try:
        title = request.data['title']
        description = request.data['description']
        day = request.data['day']
        time = request.data['time']
        event = Event.objects.create(title=title, description=description, date=day, time=time)
        print("reached here")

        event.save()
        message = {"save": True}
        return Response(message)
    except:
        try:
            title = request.data['title']
            description = request.data['description']

            event = Event.objects.create(title=title, description=description)

            event.save()
            message = {"save": True}
            return Response(message)
        except:
            message = {"save": False}
            return Response(message)


# {
#     "title": "hey its title",
#     "description": "hey demo",
#     "day": "10-03-2023",
#     "time": "12:11",
#     "files": [{"file":"111111101101100"}, {"file":"111101010101"}]
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def PostNewsView(request):
    try:
        title = request.data['title']
        description = request.data['description']

        new = New.objects.create(title=title, description=description)

        new.save()
        myData = New.objects.values('id').all()
        mySavedData = [entry for entry in myData]
        if len(mySavedData) > 1:
            e_id = []
            for i in range(0, len(mySavedData) - 1):
                id = mySavedData[i]['id']
                e_id.append(id)
            last_a_id = max(e_id)

        elif len(mySavedData) == 1:
            last_a_id = mySavedData[0]['id']

        else:
            return Response({"message": "Insert asset"})

        myNews = New.objects.get(id=last_a_id)

        for myfile in request.data['files']:
            file = myfile['file']
            FileToSave = NewFile.objects.create(file=file, new_id=myNews)
            FileToSave.save()
        message = {"message": "successful saved"}
        return Response(message)
    except:
        message = {"message": "fail to save"}
        return Response(message)


# {
#     "title": "hey its title",
#     "description": "hey demo",
#     "created_at": "12:11:76",
#     "files": [{"file":"111111101101100"}, {"file":"111101010101"}]
# }


@api_view(["GET"])
@permission_classes([AllowAny])
def GetEventsView(request):
    try:
        events = Event.objects.values('id', 'title', 'description', 'date', 'time', 'created_at').all()
    # data = [entry for entry in events]
    # d = []
    # for i in data:
    #     event = Event.objects.get(id=i['id'])
    #     files = EventFile.objects.values('file').filter(event_id=event)
    #     myev = {
    #         'id': i['id'],
    #         'title': i['title'],
    #         'description': i['description'],
    #         'date': i['date'],
    #         'time': i['time'],
    #         'created_at': i['created_at'],
    #         'files': files
    #     }
    #     d.append(myev)
    except:
        events = []
    return Response(events)


@api_view(["GET"])
@permission_classes([AllowAny])
def GetNewsView(request):
    news = New.objects.values('id', 'title', 'description', 'created_at').all()
    data = [entry for entry in news]
    d = []
    for i in data:
        new = New.objects.get(id=i['id'])
        files = NewFile.objects.values('file').filter(new_id=new)
        mynew = {
            'id': i['id'],
            'title': i['title'],
            'description': i['description'],
            'date': i['created_at'],
            'files': files
        }
        d.append(mynew)

    return Response(d)


@api_view(["POST"])
@permission_classes([AllowAny])
def ContactUs(request):
    try:
        # Set up the SMTP server
        s_email = request.data['email']
        s_name = request.data['name']
        s_message = request.data['message']
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "michaelcyril71@gmail.com"
        smtp_password = "hcojkefeoctysmso"
        smtp_sender = s_email
        smtp_recipient = "michaelcyril71@gmail.com"

        # Create a message object
        message = MIMEMultipart()
        message['From'] = smtp_sender
        message['To'] = smtp_recipient
        message['Subject'] = 'EMAIL FROM CONTACT US.'

        # Add a text message to the email
        text = "SENDER MESSAGE" + "\n" + s_message + '\n \n \n' + "SENDER INFORMATION" + "\n" + "Username: " + s_name + "\n" + "Email: " + s_email
        message.attach(MIMEText(text))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_sender, smtp_recipient, message.as_string())

        print()
        return Response({'message': "Email sent successfully!"})
    except:
        return Response({'message': "Authentication failed"})

# {
#     "email": "erickshayo306@gmail.com",
#     "name": "shayo",
#     "message": "some demo"
# }


@api_view(["GET"])
@permission_classes([AllowAny])
def SingleEventView(request, id):
    event = Event.objects.values('id', 'title', 'description', 'date', 'time', 'created_at').get(id=id)
    # ev = Event.objects.get(id=id)
    # files = EventFile.objects.values('file').filter(event_id=ev)
    myev = {
        'id': event['id'],
        'title': event['title'],
        'description': event['description'],
        'date': event['date'],
        'time': event['time'],
        'created_at': event['created_at'],
        # 'files': files
    }
    return Response(myev)


@api_view(['GET'])
@permission_classes([AllowAny])
def DeleteEvent(request, id):
    # print(id)
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({'message': 'Detail not found'})

    event.delete()
    return Response({'delete': True})

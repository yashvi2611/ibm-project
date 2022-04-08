from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
import subprocess
from .forms import UserRegistrationForm
from django.contrib.auth import login

import boto3
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import threading
import time


queue_url = "https://sqs.ap-south-1.amazonaws.com/997165460744/IBM-project-sqs"

def getAuthenticateEmail(email):
	sqs = boto3.client('sqs',region_name='ap-south-1')
	
	# Send message to SQS queue
	response = sqs.send_message(
		QueueUrl=queue_url,
		DelaySeconds=10,
		MessageAttributes={
			'email': {
				'DataType': 'String',
				'StringValue': email
			},
			'is_secret': {
				'DataType': 'String',
				'StringValue': "no"
			}					
		},
		MessageBody=(
			'sgnons'
		)
	)
	print("\n\n\n\n\n")
	print(response['MessageId'])


def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			getAuthenticateEmail(request.POST['email'])
			user = form.save()
			login(request, user)
			
			return redirect("detection")
	form = UserRegistrationForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})    




# Create your views here.
#shree ganeshay namah
#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
is_detecting = True
stop_process = False
def StartDetecting(n):
    # Load model
    global stop_process,is_detecting
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()

        # Make detections 
        results = model(frame)

        cv2.imshow('YOLO', np.squeeze(results.render()))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("\n\n its stopping \n\n\n")
            is_detecting = True
            break

        print(stop_process)
        if stop_process:
            break	
    cap.release()
    cv2.destroyAllWindows()


def detection(request):
    global stop_process,is_detecting
    
    if request.method == "GET":
        stop_process = False
        #StartDetecting(10)
        #request.session['msg']=""
        return render(request=request, template_name="setWAF.html",context={  })	
    t1 = None
    if request.method == "POST":
        # t1 = threading.Thread(target=StartDetecting, args=(10,))  
        # t1.start()
        # t1.join()
        StartDetecting(10)
        print("process is started 1st time \n\n\n\n")


        return redirect(detection)














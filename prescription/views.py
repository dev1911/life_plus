from utils import prescription
from django.shortcuts import render,redirect
from .models import Prescriptions
from . import forms
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract
from django.http import HttpResponse
# Create your views here.
	
def record_list(request):
	trial = prescription.Prescription()
	prescriptions = trial.record_list(request)
	return render(request,'prescription/prescription_list.html',{'prescriptions':prescriptions})

def upload(request):
	trial = prescription.Prescription()
	form = trial.upload(request)
	if form == True:
		return redirect('prescription:list')
	else:
		return render(request,'prescription/prescription_upload.html',{'form':form})

def delete(request,pk):
	trial = prescription.Prescription()
	trial.delete_record(request,pk)
	return redirect('prescription:list')

def ocr(request,pk):
	trial = prescription.Prescription()
	ocr_instance = trial.ocr(request,pk)
	prescriptions = ocr_instance[1]
	text = ocr_instance[0]
	return render(request,'prescription/prescription_ocr.html',{'prescriptions':prescriptions,'text':text})
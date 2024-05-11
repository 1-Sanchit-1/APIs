from rest_framework.views import APIView
from rest_framework.response import Response
from  .models import CropData
from rest_framework import permissions
from .serializers import CropDataSerializer
from rest_framework import status
import joblib
from .apps import *

class Prediction(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Crop_data items for given requested user
        '''
        Crop_data = CropData.objects.all()
        serializer = CropDataSerializer(Crop_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Crop_data with given  data
        '''
        Nitrogen= request.data.get('nitrogen')
        Phosphorus=request.data.get('phosphorus')
        Potassium=request.data.get('potassium')
        Temperature=request.data.get('temperature')
        Humidity=request.data.get('humidity')
        Ph=request.data.get('ph')
        Rainfall=request.data.get('rainfall')
      
        values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
        output = ""
        if Ph>0 and Ph<=14 :
            model_path = '/home/sanchit/San/vscode/Django/API/API_demo/api_demo/ml/crop_app'  
            model = joblib.load(model_path)
            arr = [values]
            acc = model.predict(arr)
            for value in acc:
                output += value
   
        data = {
             
            'nitrogen': request.data.get('nitrogen'),
            'phosphorus':request.data.get('phosphorus'),
            'potassium':request.data.get('potassium'),
            'temperature':request.data.get('temperature'),
            'humidity':request.data.get('humidity'),
            'ph':request.data.get('ph'),
            'rainfall':request.data.get('rainfall'),
            'result':output,
        }
        serializer = CropDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, *args, **kwargs):
        '''
        Delete the CropData with given id
        '''
        crop_data_id =request.data.get('id') 
        print(crop_data_id)
        try:
            crop_data = CropData.objects.get(id=crop_data_id)
        except CropData.DoesNotExist:
            return Response({'error': 'CropData not found'}, status=status.HTTP_404_NOT_FOUND)

        crop_data.delete()

        return Response({'message': 'CropData deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        

from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status, generics
from plugD.models import Project as my_project
from plugD.serilizers import ProjectSerializer
import math
from datetime import datetime





class ProjectView(APIView):
    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            projects = my_project.objects.get(pk=pk)
            serializer = ProjectSerializer(projects)
            return Response(serializer.data)
        else:
            projects = my_project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            project = my_project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            project = my_project.objects.get(pk=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            project = my_project.objects.all()
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)






# class Project(generics.GenericAPIView):
#     serializer_class = ProjectSerializer
#     queryset = my_project.objects.all()


#     def get(self, request):
#         page_num = int(request.GET.get("page", 1))
#         limit_num = int(request.GET.get("limit", 10))
#         start_num = (page_num - 1) * limit_num
#         end_num = limit_num * page_num
#         search_param = request.GET.get("searhc")
#         projects = my_project.objects.all()
#         total_projects = projects.count
        

#         if search_param:
#             projects = projects.filter(title_icontains=search_param)
#         serializer = self.serializer_class(projects[start_num:end_num], many=True)
#         return Response({
#             "status": "Success",
#             # "total": total_projects,
#             # "page": page_num,
#             # "last_page": math.ceil(page_num / limit_num),
#             "projects": serializer.data
#         })



#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": {'project': serializer.data}}, status=status.HTTP_201_CREATED)
        
#         else:
#             return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# class ProjectDetail(generics.GenericAPIView):
#     queryset = my_project.objects.all()
#     serializer_class = ProjectSerializer

#     def get_project(self, pk):
#         try:
#             return my_project.objects.get(pk=pk)

#         except:
#             return None

    
#     def get(self, request, pk):
#         project = self.get_project(pk=pk)

#         if project == None:
#             return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(project)
#         return Response({"status": "success", "data": {"project": serializer.data}})


#     def patch(self, request, pk):
#         project = self.get_project(pk)
#         if project == None:
#             return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(project, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.validated_data['updatedAt'] = datetime.now()
#             serializer.save()
#             return Response({"status": "success", "data": {"project": serializer.data}})
#         return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
#     def delete(self, request, pk):
#         project = self.get_project(pk)
#         if project == None:
#             return Response({"status": "fail", "message": f"Project with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         project.__delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
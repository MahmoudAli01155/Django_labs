# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Publisher
from .serlializers import PublisherSerializer
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by name': '/?publisher=name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/publisher/pk/delete'
	}
	return Response(api_urls)

@api_view(['POST'])
def add_items(request):
	item = PublisherSerializer(data=request.data)

	# validating for already existing data
	if Publisher.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
	# checking for the parameters from the URL
	if request.query_params:
		items = Publisher.objects.filter(**request.query_params.dict())
	else:
		items = Publisher.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = PublisherSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
	item = Publisher.objects.get(pk=pk)
	data = PublisherSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(Publisher, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)

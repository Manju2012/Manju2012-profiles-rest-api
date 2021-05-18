from rest_framework.views import APIView
from rest_framework.response import Response


class HellowApiView(APIView):
    """Test API View """

    def get(self, request, format=None):
        """returns a list of APIview features"""

        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you most control over apps logic ',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

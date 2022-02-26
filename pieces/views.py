from pieces.models import Color, Piece
from pieces.serializers import PieceSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class PieceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing pieces.
    """
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

    def list(self, request, *args, **kwargs):
        """
        A function that receives name or color as a url parameter and return a list of piece id

        color: string
        name: string
        """
        try:
            queryset = self.queryset

            name = request.GET.get('name')
            color = request.GET.get('color')

            if name:
                queryset = queryset.filter(name=name.lower())
            if color:
                queryset = queryset.filter(color__name=color.lower())

            if not name and not color:
                return Response({'status': 402, 'message': 'Please, insert any piece name or color to get the id'})

            if not queryset.first():
                message = '''Please, insert any of these name: Bishop, King, Queen, Pawn, Tower. Or any of these 
                colors: Black or White '''

                return Response({'status': 402, 'message': message})

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)

            return Response({'status': 500, 'message': 'Something went wrong'})

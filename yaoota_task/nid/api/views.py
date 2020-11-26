from rest_framework.response import Response
from rest_framework.views import APIView

from yaoota_task.nid.api.serializers import NationalIdSerializer
from yaoota_task.nid.api import utils


class NationalIdCheckApi(APIView):
    serializer_class = NationalIdSerializer

    def post(self, request):
        # serialization
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # data extraction
        id_number = serializer.data.get("id_number")
        id_data = utils.extract_id_data(id_number)
        millennium = id_data.get("millennium")
        year = id_data.get("year")
        full_year = f"19{year}" if millennium == "2" else f"20{year}"
        month = id_data.get("month")
        day = id_data.get("day")
        birth_governorate = id_data.get("birth_governorate")
        gender = id_data.get("gender")

        resp_data = {
            "status": "Valid",
            "info": {
                "birth_date": f"{day}-{month}-{full_year}",  # DD-MM-YYYY
                "birth_governorate": utils.governorates.get(birth_governorate),
                "gender": "Female" if int(gender) % 2 == 0 else "Male",
            },
        }

        return Response(resp_data)

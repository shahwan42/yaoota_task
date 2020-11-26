from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from yaoota_task.nid.api import utils


class NationalIdSerializer(serializers.Serializer):
    id_number = serializers.CharField(max_length=14, min_length=14)

    def validate_id_number(self, value):
        if not value.isdigit():
            raise ValidationError("Digits only")
        utils.validate_id_data(utils.extract_id_data(value))
        return value
